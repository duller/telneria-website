import streamlit as st
import random

st.set_page_config(page_title="RPG Game Master Tool", layout="wide", initial_sidebar_state="expanded")

class GameElement:
    def __init__(self, name, description, category=""):
        self.name = name
        self.description = description
        self.category = category

class Event(GameElement):
    def __init__(self, region, name, effect):
        super().__init__(name, effect, category=region)

class Spell(GameElement):
    def __init__(self, name, mana, effect, school=""):
        super().__init__(name, effect, category=school)
        self.mana = mana
        if self.mana <= 3:
            self.frequency = 2
        else:
            self.frequency = 1

class Character:
    def __init__(self, name, f, v, i, vo, caps, schools):
        self.name = name
        self.base_stats = {"Force": f, "Vigueur": v, "Intellect": i, "Volonté": vo}
        self.capacities = caps
        self.allowed_schools = schools


COMPONENTS = [
    GameElement("Fiole", "Ingrédient requis pour : Panoplia Atheria, Shal Nevidimosti, Zvaig Asara."),
    GameElement("Hellébore", "Ingrédient requis pour : Stafur Hugrunar, Shal Nevidimosti, Zvaig Asara."),
    GameElement("Mithril", "Ingrédient requis pour : Sciath Nemeton, Gladius Stellaris, Panoplia Atheria."),
    GameElement("Glyphe", "Ingrédient requis pour : Sciath Nemeton, Gladius Stellaris, Stafur Hugrunar."),
    GameElement("Poudre magique", "Ingrédient requis pour : Sciath Nemeton, Stafur Hugrunar, Shal Nevidimosti."),
    GameElement("Pierre incandescente", "Ingrédient requis pour : Gladius Stellaris, Panoplia Atheria, Zvaig Asara."),
    GameElement("Potion de soins", "Peut être utilisé pour régénérer [niveau] points de vie pendant la première étape d'une phase de combat. Ingrédient requis pour : Zvaig Asara."),
    GameElement("Potion de mana", "Peut être utilisé pour régénérer [niveau] points de mana pendant la première étape d'une phase de combat. Ingrédient requis pour : Zvaig Asara."),
    GameElement("Trèfle à quatre feuilles", "Peut être échangé pour n'importe quel autre composant d'artefact chez un artisan.")
]

EQUIPMENT = [
    GameElement("Hache naine", "Arme (2 mains) - Prérequis: 6 Force - Coût: 10 PO - Effet: Augmente la Force de 4."),
    GameElement("Épée elfique", "Arme (2 mains) - Prérequis: 6 Force - Coût: 10 PO - Effet: Augmente la Force de 4 et la Vigueur de 1."),
    GameElement("Épée courte", "Arme (1 main) - Prérequis: 2 Force - Coût: 6 PO - Effet: Augmente la Force de 1."),
    GameElement("Targe en bois", "Arme (1 main) - Prérequis: 2 Force - Coût: 6 PO - Effet: Augmente l'armure de 1."),
    GameElement("Hache orque", "Arme (1 main) - Prérequis: 6 Force - Coût: 8 PO - Effet: Augmente la Force de 2."),
    GameElement("Bouclier renforcé", "Arme (1 main) - Prérequis: 6 Force - Coût: 8 PO - Effet: Augmente l'armure de 2."),
    GameElement("Plastron draconique", "Armure (Corps) - Prérequis: 6 Force - Coût: 10 PO - Effet: Augmente la Vigueur de 2."),
    GameElement("Heaume forgé", "Armure (Tête) - Prérequis: 6 Force - Coût: 8 PO - Effet: Augmente la Vigueur de 2."),
    GameElement("Gambison", "Armure (Corps) - Prérequis: - - Coût: 6 PO - Effet: Augmente la Vigueur de 1."),
    GameElement("Capuchon", "Armure (Tête) - Prérequis: - - Coût: 6 PO - Effet: Augmente la Vigueur de 1."),
    GameElement("Robe cérémonielle", "Armure (Corps) - Prérequis: 4 Intellect - Coût: 10 PO - Effet: Augmente la Volonté de 1."),
    GameElement("Toge à entrelacts", "Armure (Corps) - Prérequis: 4 Intellect - Coût: 10 PO - Effet: Augmente l'Intellect de 1."),
    GameElement("Bâton enchanté", "Arme (2 mains) - Prérequis: 4 Intellect - Coût: 10 PO - Effet: Augmente l'Intellect de 1 et la Volonté de 1."),
    GameElement("Baguette magique", "Arme (1 main) - Prérequis: 4 Intellect - Coût: 8 PO - Effet: Augmente l'Intellect de 1."),
    GameElement("Gemme talismanique", "Arme (1 main) - Prérequis: 4 Intellect - Coût: 8 PO - Effet: Augmente la Volonté de 1.")
]

RELICS = [
    GameElement("Hache enchantée", "Arme magique - 1 main - Effet: Ajoute 2 de Force et 1 de Vigueur."),
    GameElement("Tiare de sagacité", "Armure magique - Tête - Effet: Ajoute 1 de Volonté et 1 d'Intellect."),
    GameElement("Casque maudit", "Armure magique - Tête - Effet: Ajoute 4 de Force et réduit la Vigueur de 1."),
    GameElement("Coupe de vitalité", "Bijou - Effet: Votre force et votre vigueur ne peuvent pas être réduites."),
    GameElement("Bottes de marchevent", "Armure magique - Corps - Effet: Augmente le déplacement de 1."),
    GameElement("Orbe de divination", "Bijou - Effet: Vous pouvez piocher une carte évènement de remplacement une fois par tour."),
    GameElement("Gemme des arcanes", "Bijou - Effet: Réduit le coût en mana de vos sorts de 1. (Le coût minimum d'un sort est 1)."),
    GameElement("Clé squelette", "Bijou - Effet: Débloque des passages secrets vous permettant de vous déplacer directement d'une ville à une autre."),
    GameElement("Anneau du chaos", "Bijou - Effet: Vous pouvez toujours agir même après avoir échoué un jet de caractéristique.")
]

SPELLS_BY_SCHOOL = {
    "Sort d'arcane": [
        Spell("Boule de feu", 1, "Inflige 1 dégât de feu.", "Sort d'arcane"),
        Spell("Lévitation", 1, "Hors combat: mouvement augmenté de 1 et permet d'éviter le combat. Combat: permet de piocher un sort.", "Sort d'arcane"),
        Spell("Contrôle des lames", 1, "Augmente la relance des dés totale des joueurs de 6 pour la phase.", "Sort d'arcane"),
        Spell("Doigt de givre", 2, "Inflige 1 dégât de givre. Augmente le seuil de toucher d'un monstre de 1 pour la phase.", "Sort d'arcane"),
        Spell("Altération de réalité", 2, "Remplace jusqu'à 6 dés par autant de dégâts d'arcane.", "Sort d'arcane"),
        Spell("Trait de givrefeu", 3, "Inflige 2 dégâts de feu et 1 dégât de givre.", "Sort d'arcane"),
        Spell("Météore", 2, "Inflige 2 dégâts de feu.", "Sort d'arcane"),
        Spell("Glyphe réfléchissante", 3, "Chaque attaque de monstre inflige en retour 3 dégâts d'arcane.", "Sort d'arcane"),
        Spell("Téléportation", 4, "Hors combat: téléporte un monstre ou joueur sur une région du même continent. Combat: permet de piocher trois sorts.", "Sort d'arcane"),
        Spell("Blizzard éternel", 4, "Chaque phase, inflige 4 dégâts de givre à chaque monstre.", "Sort d'arcane")
    ],
    "Sort de sacré": [
        Spell("Bouclier de protection", 1, "Augmente l'armure de 1 pour le combat.", "Sort de sacré"),
        Spell("Châtiment", 1, "Inflige 1 dégât de sacré. Soigne jusqu'à 1 point de vie, immédiatement ou à la prochaine phase.", "Sort de sacré"),
        Spell("Infusion sacrée", 1, "Chaque attaque physique de joueur inflige 1 dégât de sacré supplémentaire.", "Sort de sacré"),
        Spell("Purification", 2, "Augmente l'armure de 1 pour le combat. Soigne jusqu'à 2 point de vie, immédiatement ou à la prochaine phase.", "Sort de sacré"),
        Spell("Fontaine sacrée", 2, "Augmente Force, Vigueur, Intellect et Volonté du groupe de 1 pour le combat.", "Sort de sacré"),
        Spell("Pénitence", 2, "Inflige 2 dégâts de sacré. Soigne jusqu'à 2 points de vie, immédiatement ou à la prochaine phase.", "Sort de sacré"),
        Spell("Bouclier divin", 3, "Augmente l'armure de 3 pour le combat.", "Sort de sacré"),
        Spell("Barrière angélique", 3, "Augmente l'armure de 2 pour le combat. La prochaine mise hors de combat soigne 1 point de vie et augmente l'armure de 1 pour le combat.", "Sort de sacré"),
        Spell("Intervention lumineuse", 4, "Soigne tous les points de vie, regagne tous les points de mana et sorts.", "Sort de sacré"),
        Spell("Immunité divine", 4, "Augmente l'armure de 2 pour le combat. Hors combat: permet de traverser les régions occupées pour le tour. Combat: Augmente l'armure de 6 pour le combat.", "Sort de sacré")
    ],
    "Sort de chaos": [
        Spell("Trait d'ombre", 1, "Inflige 1 dégât de chaos.", "Sort de chaos"),
        Spell("Agonie", 2, "Inflige 1 dégât de chaos par phase. Augmente de 1 à chaque phase.", "Sort de chaos"),
        Spell("Toucher de faiblesse", 1, "Réduit la Force d'un monstre de 2 pour le combat.", "Sort de chaos"),
        Spell("Débilitation", 1, "Augmente le seuil de toucher d'un monstre de 1 pour le combat.", "Sort de chaos"),
        Spell("Drain d'âme", 2, "Réduit la Force d'un monstre de 2 pour le combat. Augmente votre Force de 2 pour le combat.", "Sort de chaos"),
        Spell("Flétrissement", 2, "Réduit la Vigueur d'un monstre de 2 pour le combat.", "Sort de chaos"),
        Spell("Armure nécrotique", 3, "Augmente l'armure de 1. Chaque attaque de monstre augmente votre Force de 4 pour le combat.", "Sort de chaos"),
        Spell("Nuage toxique", 3, "Réduit la Force et la Vigueur de chaque monstre de 2 pour le combat.", "Sort de chaos"),
        Spell("Hypnose", 4, "Réduit la Force d'un monstre de 5 pour le combat et inflige 5 dégâts de chaos.", "Sort de chaos"),
        Spell("Domination funeste", 4, "Chaque monstre attaque avec une Force réduite de 3 et s'inflige 3 dégât de chaos. Réduit la Force et la Vigueur d'un monstre de 3 pour le combat.", "Sort de chaos")
    ],
    "Sort de nature": [
        Spell("Toucher de la nature", 1, "Augmente la Vigueur d'un joueur de 1 pour le combat.", "Sort de nature"),
        Spell("Précision féline", 1, "Réduit le seuil de toucher des dés d'un joueur de 1 pour le combat.", "Sort de nature"),
        Spell("Sauvagerie", 1, "Augmente la Force d'un joueur de 2 pour le combat.", "Sort de nature"),
        Spell("Trait de foudre", 2, "Inflige 1 dégât de nature et augmente la Force d'un joueur de 2 pour le combat.", "Sort de nature"),
        Spell("Appel de la nature", 2, "Chaque attaque de monstre augmente la Force d'un joueur de 4 pour le combat.", "Sort de nature"),
        Spell("Endurance farouche", 2, "Augmente la Vigueur d'un joueur de 4 pour le combat.", "Sort de nature"),
        Spell("Croissance sauvage", 3, "Augmente la Force d'un joueur de 4 pour le combat.", "Sort de nature"),
        Spell("Sarments épineux", 3, "Inflige 3 dégâts de nature à chaque monstre qui utilise une capacité ou qui attaque.", "Sort de nature"),
        Spell("Tempête", 4, "Expulse les monstres du combat et inflige 4 dégâts de nature.", "Sort de nature"),
        Spell("Invocation sylvaine", 4, "Augmente la Force et la Vigueur de chaque joueur de 5 pour le combat.", "Sort de nature")
    ]
}

EVENTS = {
    "Champ": [
        Event("Champ", "Mendiant insistant", "Un mendiant vous réclame une pièce d'or. Si vous l'honorez, il vous procure un objet. Sinon, vous pouvez l'achever pour lui voler son objet et perdre 1 de chaque caractéristique lors du prochain combat."),
        Event("Champ", "Filon sans fin", "Vous trouvez une pièce d'or sur un filon magique. Vous pouvez reposer la pièce et lancer un dé. Si vous faites 4 ou plus, vous gagnez deux pièces. Vous pouvez continuer avec deux pièces pour en gagner quatre."),
        Event("Champ", "Fontaine de puissance", "Vous découvrez une fontaine de puissance à l'orée des arbres. Ajoutez 1 de Force ou 1 d'Intellect lors de votre prochain combat."),
        Event("Champ", "Tome abandonné", "Vous trouvez un livre magique. Vous l'ouvrez, lancez un dé. 1: une pièce d'or 2: deux pièces d'or. 3: un composant. 4: un objet. 5: une grenouille. 6: un brigand."),
        Event("Champ", "Torrent de grenouille", "Une grenouille trop téméraire s'est installée dans les réserves d'eau de la ville voisine. Vous devez la vaincre."),
        Event("Champ", "Pluie de grenouille", "Une grenouille patauge effrontément dans la mare proche du village. Vous devez la vaincre."),
        Event("Champ", "Chevalier itinérant", "Un chevalier de la lumière vous propose son aide. Ajoutez 2 de Force lors de votre prochain combat. Vous pouvez le poignarder dans le dos pour lui voler son destrier, et ajouter 2 de Vigueur à la place."),
        Event("Champ", "Attaque de grand chemin", "Un brigand attaque les routes passantes de la région. Vous devez le vaincre."),
        Event("Champ", "Embuscade subite", "Un brigand rôde entre les chaumières mal éclairées. Vous devez le vaincre.")
    ],
    "Bosquet": [
        Event("Bosquet", "Chaudron douteux", "Vous trempez vos lèvres dans un chaudron fumant. Lancez un dé pour déterminer votre prochain combat. 1: -1 Vigueur 2: -1 Force. 3: -1 Intellect. 4: +1 Intellect. 5: +1 Force. 6: +1 Vigueur."),
        Event("Bosquet", "Fontaine de jouvence", "Vous découvrez une fontaine de jouvence dans une clairière. Ajoutez 1 de Vigueur lors de votre prochain combat. Ajoutez 1 de Vigueur de plus si vous possédez une potion."),
        Event("Bosquet", "Invasion gnolle", "Un gnoll vandalise les celliers du village voisin. Vous devez le vaincre."),
        Event("Bosquet", "Surprise gnolle", "Un gnoll espiègle rend la vie des paysans locaux misérable. Vous devez le vaincre."),
        Event("Bosquet", "Éclosion grouillante", "Une araignée tisse sa toile entre les branches des chênes larmoyants. Vous devez la vaincre."),
        Event("Bosquet", "Prolifération venimeuse", "Une araignée cliquette au pied des arbustes verdoyants. Vous devez la vaincre.")
    ],
    "Colline": [
        Event("Colline", "Cloches retentissantes", "Les cloches de l'abbaye vous font rejeter la violence. Si vous échouez un jet de Volonté de 8, vous perdez 1 de chaque caractéristique lors de votre prochain combat."),
        Event("Colline", "Gîte accueillant", "Une abbesse vous dévisage. - Si vous possédez un sort de chaos, elle vous attaque. - Si vous possédez un sort de sacré, elle vous offre un composant. - Sinon, elle vous ignore."),
        Event("Colline", "Abbaye reculée", "L'abbesse vous enjoint de faire un don de deux pièces d'or. Si vous refusez, vous devez réussir un jet d'Intellect de 8 pour l'empêcher de vous attaquer.")
    ],
    "Plaine": [
        Event("Plaine", "Épidémie de peste", "Une épidémie de peste ravage la région. Si vous échouez un jet de Vigueur de 10, vous perdez 1 de chaque caractéristique lors de votre prochain combat."),
        Event("Plaine", "Conseil des mages", "Vous participez à une épreuve de magie. Lancez un dé. 1: une naga vous attaque. 2: une goule vous attaque. 3: une pièce d'or. 4: un composant. 5: un objet. 6: échangez un sort."),
        Event("Plaine", "Trésor enfoui", "Vous découvrez l'emplacement d'un trésor maudit. Si vous échouez un jet de Volonté de 8, vous succombez à la tentation, et une naga vous attaque."),
        Event("Plaine", "Châtelet imposant", "Un malentendu conduit à votre emprisonnement. Si vous échouez un jet de Force de 10 pour forcer la porte, vous devez combattre une goule qui bloque la sortie."),
        Event("Plaine", "Noblesse elfique", "Une princesse vous invite et vous pose des questions historiques. Si vous échouez un jet d'Intellect de 10, elle s'offusque et vous expulse vers Aremorica, le port de Middenardh."),
        Event("Plaine", "Arrivée ondoyante", "Une naga attaque les nautes chargeant les barques des ports fluviaux. Vous devez la vaincre."),
        Event("Plaine", "Débarquement sinueux", "Une naga se faufile discrètement entre les rivières des villes marchandes. Vous devez la vaincre."),
        Event("Plaine", "Profanation des tombes", "Une goule putride erre sans but aux abords des villages paisibles. Vous devez la vaincre."),
        Event("Plaine", "Exhumation morbide", "Les activités obscures des occupants du temple voisin ont animé une goule du cimetière local. Vous devez la vaincre.")
    ],
    "Foret": [
        Event("Foret", "Soif de sang", "Un garou lucide vous supplie de le laisser boire votre sang. - Si vous acceptez, perdez 1 de Vigueur et gagnez 1 de Volonté lors de votre prochain combat. - Si vous refusez, il vous attaque."),
        Event("Foret", "Anachorète mystique", "Un anachorète vous observe. - Si vous possédez un sort d'arcane, il vous donne deux objets. - Si vous possédez un sort de nature, il vous téléporte en Aremorica. - Sinon, il disparaît subitement."),
        Event("Foret", "Arbre facétieux", "Vous découvrez un arbre magique. - Si vous possédez un sort de nature, il vous donne deux objets. - Si vous possédez un sort d'arcane, il fait apparaître un fantôme. - Sinon, il se moque de vous."),
        Event("Foret", "Maison champignon", "Vous découvrez dans une clairière une maison fort appétissante. Si vous échouez un jet de Volonté de 10, vous vous remplissez la panse, et perdez 1 de Force et 1 de Vigueur lors de votre prochain combat."),
        Event("Foret", "Cohorte spectrale", "Un fantôme effraie les voyageurs les plus couards aux abords de la forêt. Vous devez le vaincre."),
        Event("Foret", "Apparition fantomatique", "Le fantôme d'un pendu accusé injustement hante les villages isolés de la montagne. Vous devez le vaincre."),
        Event("Foret", "Sorcière isolée", "Une sorcière vous attire à elle. - Si vous possédez un sort de chaos, elle vous donne deux objets. - Si vous possédez un sort de sacré elle invoque un garou. - Sinon, elle vous agrandit le nez."),
        Event("Foret", "Transformation bestiale", "Un forgeron coriace s'est fait mordre par un loup et erre maintenant sous forme de garou. Vous devez le vaincre."),
        Event("Foret", "Pleine lune", "Vous entendez un hurlement issu des profondeurs de la forêt. Un garou est en train de se transformer. Vous devez le vaincre.")
    ],
    "Montagne": [
        Event("Montagne", "Portail magique", "Un hibours rôde autour d'un portail magique. Il peut être convaincu de ne pas combattre avec un jet de Volonté de 15. Une fois l'hibours vaincu ou convaincu, vous pouvez vous téléporter où vous voulez."),
        Event("Montagne", "Tremblement de terre", "Vous devez réussir un jet de Vigueur de 12 pour résister au tremblement de terre. Si vous échouez, un ogre profite de votre déséquilibre pour vous attaquer."),
        Event("Montagne", "Maraudeur brutal", "Un ogre maraudeur surgit d'une grotte et vous réclame 10 pièces d'or. Si vous refusez de payer, il vous attaque."),
        Event("Montagne", "Filon de gemmes", "Vous trouvez un filon enchanté. Vous arrachez une gemme. Lancez un dé pour déterminer ce qui vous attend. 1: une liche. 2: un hibours. 3: un ogre. 4: un composant. 5: une pièce d'or. 6: un objet."),
        Event("Montagne", "Porte secrète", "Une porte vous bloque le passage. Vous pouvez la franchir avec un jet de Force de 15. Si vous échouez, une liche est attirée par le bruit, et vous attaque."),
        Event("Montagne", "Grotte hantée", "Une liche s'est installée dans une grotte voisine. Elle réclame trois composants lors de votre passage, à défaut de quoi elle émerge de son repaire et vous attaque."),
        Event("Montagne", "Force brute", "Un ogre déchaîné sème le chaos dans la région. Vous devez le vaincre."),
        Event("Montagne", "Hibernation contrariée", "Un hibours grogneur émerge de sa profonde hibernation. Vous devez le vaincre."),
        Event("Montagne", "Nécrose squelettique", "Une liche imbue de magie nécrotique imprègne l'atmosphère environnante. Vous devez la vaincre.")
    ],
    "Neige": [
        Event("Neige", "Abondance de gemmes", "Vous découvrez une grotte remplie de pierres précieuses. Vous pouvez y ajouter 20 pièces d'or. Si vous vous abstenez ou tentez de prendre une gemme, un dragon vous attaque. (Neige - 2 joueurs)"),
        Event("Neige", "Gargouille gigantesque", "Une gigantesque gargouille de pierre semble se métamorphoser, il faut la détruire prestement. Si aucun joueur ne réussit un jet de Force de 18, un dragon vous attaque. (Neige - 2 joueurs)"),
        Event("Neige", "Puissance draconique", "Vous entrez dans le domaine d'un dragon affamé. Il pousse un hurlement déchirant, déploie ses ailes et vous attaque. (Neige - 2 joueurs)")
    ],
    "Désert": [
        Event("Désert", "Djinn maléfique", "Un djinn maléfique vous barre le passage. Il vous réclame 6 composants. Si vous ne l'honorez pas, il se dissipe dans un nuage de fumée, puis un démon vous attaque. (Désert - 2 joueurs)"),
        Event("Désert", "Tour d'onyx", "Une tour en onyx est érigée au milieu du désert, troublant votre vision. Si chaque joueur réussit un jet d'Intellect de 14, vous pouvez traverser le désert sain et sauf. Sinon, un démon vous attaque. (Désert - 2 joueurs)"),
        Event("Désert", "Rictus démoniaque", "Vous entrez dans le domaine d'un démon déchaîné. Il s'embrase, enflamme son épée, et vous attaque. (Désert - 2 joueurs)")
    ],
    "Marais": [
        Event("Marais", "Regard funeste", "Vous sentez un regard peser sur vous, vos jambes ne vous obéissent plus. Si chaque joueur réussit un jet de Volonté de 14, vous pouvez traverser le marais sain et sauf. Sinon une vampiresse vous attaque. (Marais - 2 joueurs)"),
        Event("Marais", "Chevalier maudit", "Un chevalier maudit vous barre le passage. Il vous réclame 6 objets. Si vous ne l'honorez pas, son cheval squelettique hennit violemment, puis une vampiresse vous attaque. (Marais - 2 joueurs)"),
        Event("Marais", "Malveillance vampirique", "Vous entrez dans le domaine d'une vampiresse assoiffée de sang. Elle vous tance un instant, puis vous attaque. (Marais - 2 joueurs)")
    ]
}

MONSTERS = {
    "Champ": [
        {"Monstre": "Grenouille", "Région": "Champs", "Nombre de joueurs": "1", "Force": "2", "Vigueur": "3", "Capacités": "Duplication de chaque grenouille au début du tour dans une région adjacente inoccupée."},
        {"Monstre": "Brigand", "Région": "Champs", "Nombre de joueurs": "1", "Force": "2", "Vigueur": "3", "Capacités": "Peut être convaincu de ne pas combattre en le payant 1 pièce d’or."}
    ],
    "Bosquet": [
        {"Monstre": "Araignée", "Région": "Bosquet", "Nombre de joueurs": "1", "Force": "3", "Vigueur": "4", "Capacités": "Relance 3 de ses dés. Les joueurs ne peuvent pas fuir."},
        {"Monstre": "Gnoll", "Région": "Bosquet", "Nombre de joueurs": "1", "Force": "3", "Vigueur": "4", "Capacités": "Perd 1 de Force à chaque fin de phase."}
    ],
    "Colline": [
        {"Monstre": "Abbesse", "Région": "Colline", "Nombre de joueurs": "1", "Force": "4", "Vigueur": "6", "Capacités": "Au début de chaque phase, submerge un joueur au hasard de magie du Sacré et lui inflige 1 de dégât."}
    ],
    "Plaine": [
        {"Monstre": "Naga", "Région": "Plaine", "Nombre de joueurs": "1", "Force": "4", "Vigueur": "6", "Capacités": "Au début du combat, un joueur au hasard doit réussir un jet de Volonté (8) sinon il ne peut agir pendant cette phase."},
        {"Monstre": "Goule", "Région": "Plaine", "Nombre de joueurs": "1", "Force": "4", "Vigueur": "6", "Capacités": "Les joueurs perdent 1 de Vigueur pour le combat."}
    ],
    "Forêt": [
        {"Monstre": "Fantôme", "Région": "Forêt", "Nombre de joueurs": "1", "Force": "5", "Vigueur": "8", "Capacités": "Le jet requis pour le toucher est augmenté à 5."},
        {"Monstre": "Garou", "Région": "Forêt", "Nombre de joueurs": "1", "Force": "5", "Vigueur": "8", "Capacités": "Gagne 1 de Force et perd 1 de Vigueur à chaque fin de phase."}
    ],
    "Montagne": [
        {"Monstre": "Hibours", "Région": "Montagne", "Nombre de joueurs": "1", "Force": "6", "Vigueur": "10", "Capacités": "Hiberne pendant la première phase. Enrage au début de la deuxième phase et double sa Force."},
        {"Monstre": "Ogre", "Région": "Montagne", "Nombre de joueurs": "1", "Force": "6", "Vigueur": "10", "Capacités": "Le jet requis pour le toucher est réduit à 3."},
        {"Monstre": "Liche", "Région": "Montagne", "Nombre de joueurs": "1", "Force": "6", "Vigueur": "10", "Capacités": "Au début du combat, chaque joueur doit réussir un jet d’Intellect (10) sinon il ne peut agir pendant cette phase."}
    ],
    "Marais": [
        {"Monstre": "Vampiresse", "Région": "Marais", "Nombre de joueurs": "2", "Force": "10", "Vigueur": "30", "Capacités": "À chaque fin de phase, elle gagne 1 de Force et de Vigueur et tous les joueurs perdent 1 de chaque caractéristique."}
    ],
    "Neige": [
        {"Monstre": "Dragon", "Région": "Neige", "Nombre de joueurs": "2", "Force": "10", "Vigueur": "30", "Capacités": "Les joueurs ne peuvent pas agir pendant la première phase du combat."}
    ],
    "Désert": [
        {"Monstre": "Démon", "Région": "Désert", "Nombre de joueurs": "2", "Force": "10", "Vigueur": "30", "Capacités": "Au début du combat, chaque joueur doit réussir un jet de Force (12) sinon il ne peut agir pendant cette phase."}
    ],
    "Temple": [
        {"Monstre": "Manifestation", "Région": "Temple", "Nombre de joueurs": "2", "Force": "30", "Vigueur": "40", "Capacités": "Au début de chaque phase, submerge un joueur au hasard de magie du Telnas et lui inflige 5 de dégâts."}
    ],
    "Provebor": [
        {"Monstre": "Nitriel, Seigneuresse du Telnas", "Région": "Provebor", "Nombre de joueurs": "4", "Force": "15", "Vigueur": "60", "Capacités": "Au début de chaque phase, submerge deux joueurs au hasard de magie du Telnas et leur inflige 5 de dégâts."},
    ]
}

characters = [
    Character("Varelias Druide", 1, 2, 3, 2, [
        "Peut lancer des sorts de nature et de sacré.",
        "Le déplacement en forêt ne compte pas dans la limite du tour.",
        "Au début du combat, se transforme dans la forme de son choix :",
        "◦ Cerf : ajoute [niveau] à sa Vigueur.",
        "◦ Ours : ajoute [niveau] à sa Force.",
        "◦ Hibou : ajoute 1 à son Intellect, ajoute 1 à sa Volonté, pioche un sort de nature, et le coût de mana des sorts de nature est réduit de 1 (minimum 1)."
    ], ["Sort de nature", "Sort de sacré"]),

    Character("Orc Guerrier", 3, 3, 1, 1, [
        "Commence le jeu avec une épée courte et une targe en bois.",
        "Ne peut pas lancer de sorts.",
        "Peut porter deux armes à deux mains.",
        "Les armes ajoutent le double de la Force indiquée.",
        "Enrage et ajoute [volonté] à sa Force quand le guerrier :",
        "◦ subit des dégâts.",
        "◦ retrouve ses esprits après avoir échoué un jet d'Intellect ou de Volonté."
    ], []),

    Character("Murvien Thermolige", 1, 2, 2, 3, [
        "Peut lancer tout type de sort.",
        "Ne peut pas avoir en même temps des sorts de sacré et de chaos, ou de nature et d'arcane.",
        "Le déplacement en région portuaire ne compte pas dans la limite du tour.",
        "Peut se défausser d'un sort qui n'est pas de givrefeu pour dupliquer un sort de givrefeu. (Les sorts d'arcane sont de givrefeu ou temporels).",
        "À chaque lancer de sort de givrefeu, inflige 1 dégât de feu ou de givre.",
        "Peut porter autant d'armes que ses quatre bras lui permettent."
    ], ["Sort d'arcane", "Sort de sacré", "Sort de chaos", "Sort de nature"]),

    Character("Djinn Roublard", 2, 2, 2, 2, [
        "Commence avec deux épées courtes.",
        "Peut lancer des sorts d'arcane. (Les sorts d'arcane sont de givrefeu ou temporels).",
        "Gain de pièces d'or augmenté de [volonté] à la fin d'un évènement.",
        "Peut relancer [intellect] dés par phase, dont ceux des ennemis.",
        "Peut payer une pièce d'or pour :",
        "◦ gagner un point de caractéristique au choix en montant de niveau.",
        "◦ remettre un sort lancé dans sa main.",
        "◦ ajouter 1 à son Intellect pour la phase."
    ], ["Sort d'arcane"]),

    Character("Elfe Clerc", 1, 2, 3, 2, [
        "Peut lancer des sorts de sacré ou de chaos.",
        "Lorsqu'elle pioche son premier sort de chaos, elle augmente toutes ses caractéristiques de 1, se défausse de ses sorts de sacré, et ne peut plus en piocher.",
        "À chaque lancer de sort de sacré, inflige 1 dégât de sacré à un monstre.",
        "Chaque dégât réduit par un point d'armure de l'elfe inflige autant de dégâts de sacré à un monstre.",
        "Quand elle regagne des points de vie grâce à un sort, l'elfe inflige autant de dégâts de sacré à un monstre."
    ], ["Sort de sacré", "Sort de chaos"]),

    Character("Chepteg Chaman", 1, 2, 3, 2, [
        "Peut lancer des sorts de nature ou d'arcane.",
        "Lorsqu'il pioche son premier sort d'arcane, il augmente toutes ses caractéristiques de 1, se défausse de ses sorts de nature, et ne peut plus en piocher.",
        "Peut éviter le combat dans la neige.",
        "À chaque lancer de sort de nature, il jette 1d6 et gagne pour la phase (effets cumulatifs) :",
        "◦ 1-2 : ajoute 2 à sa Force.",
        "◦ 3-4 : ajoute 2 à sa Vigueur.",
        "◦ 5-6 : inflige 1 dégât de nature et pioche un sort."
    ], ["Sort de nature", "Sort d'arcane"]),

    Character("Dragonide Sombregarde", 3, 3, 1, 1, [
        "Commence avec une épée courte.",
        "Peut lancer des sorts de chaos.",
        "Le déplacement en montagne ne compte pas dans la limite du tour.",
        "Lorsqu'il attaque, peut infuser son arme :",
        "◦ Frappe sanguinaire : regagne [niveau] points de vie à la fin de la phase.",
        "◦ Frappe morbide : réduit la Vigueur du monstre de [niveau].",
        "◦ Frappe démoniaque : réduit la Force du monstre de [niveau].",
        "◦ Frappe spectrale : ignore l'armure et inflige des dégâts de chaos."
    ], ["Sort de chaos"]),

    Character("Centaure Rôdeuse", 2, 2, 2, 2, [
        "Commence le jeu avec un gambison.",
        "Peut lancer des sorts de nature.",
        "Peut se déplacer de 5 régions par tour.",
        "Bénéficie d'une phase de combat supplémentaire initiale où :",
        "◦ seule la centaure agit.",
        "◦ elle ajoute [niveau] à sa Force.",
        "◦ son seuil de toucher est réduit de 1.",
        "Peut fuir le combat à chaque fin de phase sans lancer de dé."
    ], ["Sort de nature"]),

    Character("Humain Démoniste", 1, 2, 2, 3, [
        "Peut lancer des sorts de chaos et d'arcane.",
        "À chaque lancer de sort de chaos, invoque un démon selon le coût en mana :",
        "◦ 1 : succube impie (réduit la Force d'un monstre de 2).",
        "◦ 2 : diablotin ravageur (réduit la Vigueur d'un monstre de 2).",
        "◦ 3 : molosse chaotique (inflige 3 dégâts de chaos).",
        "◦ 4 : dévoreur infernal (inflige 4 dégâts de chaos)."
    ], ["Sort de chaos", "Sort d'arcane"]),

    Character("Satyre Nécromant", 1, 2, 2, 3, [
        "Peut lancer des sorts de chaos et de nature.",
        "Lorsqu'un monstre meurt, il est réanimé en zombie (+[niveau] Force et +[niveau] Vigueur au prochain combat ; un seul actif).",
        "Ajoute une dose d'ichor à sa flasque nécrotique lors d'un meurtre ou d'un sort de chaos.",
        "La flasque (max 6 doses) peut être vidée pour infliger autant de dégâts de chaos."
    ], ["Sort de chaos", "Sort de nature"]),

    Character("Nain Paladin", 3, 3, 1, 1, [
        "Commence avec gambison, capuchon, épée courte et targe en bois.",
        "Peut lancer des sorts de sacré.",
        "Quand il perd des points de vie, augmente sa Force d'autant pour le combat.",
        "Quand il regagne des points de vie par un sort, augmente son armure d'autant pour le combat.",
        "Lors de son attaque normale, ajoute son armure à sa Force pour la phase."
    ], ["Sort de sacré"]),

    Character("Minotaure Chronosage", 1, 2, 2, 3, [
        "Peut lancer des sorts d'arcane et de sacré.",
        "Peut choisir parmi deux sorts de plus en piochant des sorts d'arcane.",
        "Après le premier sort temporel par phase, lance 1d6 + sorts en main pour des bonus (cumulatifs) :",
        "◦ 1-2 : le sort revient dans la main.",
        "◦ 3-4 : ajoute [vigueur] à sa Force.",
        "◦ 5-6 : ajoute [intellect] à sa Force.",
        "◦ 7+ : ajoute [volonté] à sa Force."
    ], ["Sort d'arcane", "Sort de sacré"])
]


if 'inventory' not in st.session_state:
    st.session_state.inventory = {"Composants": [], "Équipement": [], "Reliques": [], "Sorts": []}
if 'current_event' not in st.session_state:
    st.session_state.current_event = None
if 'current_monster' not in st.session_state:
    st.session_state.current_monster = None

def safe_rerun():
    if hasattr(st, "experimental_rerun") and callable(getattr(st, "experimental_rerun")):
        try:
            st.experimental_rerun()
        except Exception:
            return
    else:
        return

def add_item(source_list, key):
    if not source_list:
        st.toast("Source vide", icon="⚠️")
        return
    item = random.choice(source_list)
    st.session_state.inventory[key].append(item)
    st.toast(f"Ajouté : {item.name}", icon="🎒")

def draw_event(region_name):
    if region_name not in EVENTS or not EVENTS[region_name]:
        st.toast("Aucun événement disponible pour cette région.", icon="⚠️")
        return
    ev = random.choice(EVENTS[region_name])
    st.session_state.current_event = ev
    # Also pick a monster for the region if available
    monsters = MONSTERS.get(region_name, [])
    st.session_state.current_monster = random.choice(monsters) if monsters else None

def draw_spell_from_school(school_name):
    spells = SPELLS_BY_SCHOOL.get(school_name, [])
    if not spells:
        st.toast("Aucun sort disponible pour cette école.", icon="⚠️")
        return None
    # Weighted draw based on frequency
    pool = []
    for s in spells:
        pool.extend([s] * s.frequency)
    s = random.choice(pool) if pool else random.choice(spells)
    st.session_state.inventory["Sorts"].append(s)
    return s

# --- INTERFACE UTILISATEUR ---

with st.sidebar:
    st.title("🧙 Gestion du Héros")
    
    char_names = [c.name for c in characters]
    
    # 1. Inline Selectbox for Character Selection
    # Using vertical_alignment="center" (requires Streamlit >= 1.38) to keep text aligned with the input box
    col1, col2 = st.columns([1, 1], vertical_alignment="center")
    col1.write("Choisir un Héros")
    selected_name = col2.selectbox("Choisir un Héros", char_names, label_visibility="collapsed")
    
    char = next(c for c in characters if c.name == selected_name)

    # Sliders usually look better on their own line, so we leave it as is
    level = st.select_slider("Niveau du personnage", options=range(1, 7), value=1)
    bonus_points_total = (level - 1) * 2

    st.divider()
    st.subheader(f"📈 Points bonus disponibles: {bonus_points_total}")

    bonus_stats = {}
    current_spent = 0
    for stat in ["Force", "Vigueur", "Intellect", "Volonté"]:
        # 2. Inline Number Inputs for Stats
        col1, col2 = st.columns([1, 1], vertical_alignment="center")
        col1.write(f"+ {stat}")
        val = col2.number_input(
            f"+ {stat}", 
            min_value=0, 
            max_value=bonus_points_total, 
            value=0, 
            key=f"bonus_{stat}", 
            label_visibility="collapsed"
        )
        bonus_stats[stat] = val
        current_spent += val

    if current_spent > bonus_points_total:
        st.error(f"Points excédentaires ! ({current_spent}/{bonus_points_total})")

    st.divider()
    if char.allowed_schools:
        # 3. Inline Selectbox for Magic School
        col1, col2 = st.columns([1, 1], vertical_alignment="center")
        col1.write("École de Magie")
        chosen_school = col2.selectbox("École de Magie", char.allowed_schools, label_visibility="collapsed")
        
        # 4. Inline Number Input for Spell Count
        col1, col2 = st.columns([1, 1], vertical_alignment="center")
        col1.write("Nombre de sorts")
        draw_count = col2.number_input("Nombre de sorts à tirer", 1, 10, 1, label_visibility="collapsed")
        
        # When pressing the button, add the drawn spells to the right inventory ("Sorts")
        if st.button("🔮 Tirer les sorts"):
            for _ in range(draw_count):
                s = draw_spell_from_school(chosen_school)
                if s:
                    st.toast(f"Sort acquis : {s.name}", icon="✨")
    else:
        st.warning("Ce héros n'utilise pas de magie.")

    st.divider()
    st.subheader("🎲 Tirages Aléatoires")
    if st.button("💎 Piocher Composant", use_container_width=True): add_item(COMPONENTS, "Composants")
    if st.button("⚔️ Piocher Équipement", use_container_width=True): add_item(EQUIPMENT, "Équipement")
    if st.button("👑 Piocher Relique", use_container_width=True): add_item(RELICS, "Reliques")

    st.divider()
    st.subheader("🗺️ Exploration")
    
    # Text and selectbox on the same line
    col1, col2 = st.columns([1, 1], vertical_alignment="center")
    col1.write("Choisir la région")
    reg = col2.selectbox("Choisir la région", list(EVENTS.keys()), label_visibility="collapsed")
    
    # Button below
    if st.button("🎴 Tirer Événement", use_container_width=True):
        draw_event(reg)

# Main Page
st.title(f"Table de Jeu : {selected_name}")

col_left, col_right = st.columns([2, 1])

with col_left:
    # Event area: show name and description on the same line
    if st.session_state.current_event:
        ev = st.session_state.current_event
        st.error(f"📍 ÉVÉNEMENT EN COURS : {ev.category.upper()}")
        # Single-line event title + description
        st.write(f"**{ev.name}** — {ev.description}")
        # If a monster was selected for this event, display its key attributes on single lines
        monster = st.session_state.current_monster
        if monster:
            st.write(f"**Monstre**: {monster['Monstre']}  —  **Région**: {monster['Région']}  —  **Joueurs**: {monster['Nombre de joueurs']}")
            st.write(f"**Force**: {monster['Force']}  —  **Vigueur**: {monster['Vigueur']}  —  **Capacités**: {monster['Capacités']}")
        if st.button("✅ Résoudre l'événement"):
            st.session_state.current_event = None
            st.session_state.current_monster = None
            safe_rerun()
    else:
        st.info("Aucun événement actif. Utilisez la barre latérale pour explorer le monde.")

    st.divider()

    # Character info and leveling display with single-line stat + progress
    st.header(f"🛡️ {char.name} (Niveau {level})")
    st.subheader("📊 Caractéristiques Finales")
    for stat, base_val in char.base_stats.items():
        total_val = base_val + bonus_stats.get(stat, 0)
        st.write(f"**{stat}**: {total_val} (Base {base_val} + {bonus_stats.get(stat,0)} bonus)")
        st.progress(min(total_val / 15, 1.0))

    st.subheader("📜 Capacités Spéciales")
    for cap in char.capacities:
        display_cap = cap.replace("[niveau]", str(level))
        display_cap = display_cap.replace("[volonté]", str(char.base_stats["Volonté"] + bonus_stats.get("Volonté", 0)))
        display_cap = display_cap.replace("[vigueur]", str(char.base_stats["Vigueur"] + bonus_stats.get("Vigueur", 0)))
        display_cap = display_cap.replace("[intellect]", str(char.base_stats["Intellect"] + bonus_stats.get("Intellect", 0)))
        # show each capacity on a single line
        st.write(f"- {display_cap}")

    st.divider()

    # Note: drawn spells are no longer shown here; they are added to the right inventory.

with col_right:
    # Inventory: components, equipment, relics, and drawn spells ("Sorts")
    st.header("🎒 Sac à dos")
    for category, items in st.session_state.inventory.items():
        st.subheader(f"--- {category} ---")
        if not items:
            st.caption("Vide")
        else:
            for idx, item in enumerate(items):
                # item is GameElement or Spell
                name = getattr(item, "name", str(item))
                desc = getattr(item, "description", "")
                # show name and short description on the same line in the expander title
                with st.expander(f"{name} — {desc}", expanded=False):
                    # inside the expander keep the full description and a delete button
                    st.write(desc)
                    if st.button("🗑️ Supprimer", key=f"del_{category}_{idx}"):
                        st.session_state.inventory[category].pop(idx)
                        safe_rerun()

st.markdown("---")
st.caption("Le grimoire du Telnas - François Ripp - telneria.eu - 2026")
