import streamlit as st
import random

# --- CLASSES ---
class Spell:
    def __init__(self, name, mana, effect):
        self.name = name
        self.mana = mana
        self.effect = effect
        # Fréquence basée sur le coût en mana
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

# --- DATABASE: SPELLS (Exact Verbatim Text from sorts.pdf) ---
all_schools = {
    "Sort d'arcane": [
        Spell("Boule de feu", 1, "Inflige 1 dégât de feu."),
        Spell("Lévitation", 1, "Hors combat: mouvement augmenté de 1 et permet d'éviter le combat. Combat: permet de piocher un sort."),
        Spell("Contrôle des lames", 1, "Augmente la relance des dés totale des joueurs de 6 pour la phase."),
        Spell("Doigt de givre", 2, "Inflige 1 dégât de givre. Augmente le seuil de toucher d'un monstre de 1 pour la phase."),
        Spell("Altération de réalité", 2, "Remplace jusqu'à 6 dés par autant de dégâts d'arcane."),
        Spell("Trait de givrefeu", 3, "Inflige 2 dégâts de feu et 1 dégât de givre."),
        Spell("Météore", 2, "Inflige 2 dégâts de feu."),
        Spell("Glyphe réfléchissante", 3, "Chaque attaque de monstre inflige en retour 3 dégâts d'arcane."),
        Spell("Téléportation", 4, "Hors combat: téléporte un monstre ou joueur sur une région du même continent. Combat: permet de piocher trois sorts."),
        Spell("Blizzard éternel", 4, "Chaque phase, inflige 4 dégâts de givre à chaque monstre.")
    ],
    "Sort de sacré": [
        Spell("Bouclier de protection", 1, "Augmente l'armure de 1 pour le combat."),
        Spell("Châtiment", 1, "Inflige 1 dégât de sacré. Soigne jusqu'à 1 point de vie, immédiatement ou à la prochaine phase."),
        Spell("Infusion sacrée", 1, "Chaque attaque physique de joueur inflige 1 dégât de sacré supplémentaire."),
        Spell("Purification", 2, "Augmente l'armure de 1 pour le combat. Soigne jusqu'à 2 point de vie, immédiatement ou à la prochaine phase."),
        Spell("Fontaine sacrée", 2, "Augmente Force, Vigueur, Intellect et Volonté du groupe de 1 pour le combat."),
        Spell("Pénitence", 2, "Inflige 2 dégâts de sacré. Soigne jusqu'à 2 points de vie, immédiatement ou à la prochaine phase."),
        Spell("Bouclier divin", 3, "Augmente l'armure de 3 pour le combat."),
        Spell("Barrière angélique", 3, "Augmente l'armure de 2 pour le combat. La prochaine mise hors de combat soigne 1 point de vie et augmente l'armure de 1 pour le combat."),
        Spell("Intervention lumineuse", 4, "Soigne tous les points de vie, regagne tous les points de mana et sorts."),
        Spell("Immunité divine", 4, "Augmente l'armure de 2 pour le combat. Hors combat: permet de traverser les régions occupées pour le tour. Combat: Augmente l'armure de 6 pour le combat.")
    ],
    "Sort de chaos": [
        Spell("Trait d'ombre", 1, "Inflige 1 dégât de chaos."),
        Spell("Agonie", 2, "Inflige 1 dégât de chaos par phase. Augmente de 1 à chaque phase."),
        Spell("Toucher de faiblesse", 1, "Réduit la Force d'un monstre de 2 pour le combat."),
        Spell("Débilitation", 1, "Augmente le seuil de toucher d'un monstre de 1 pour le combat."),
        Spell("Drain d'âme", 2, "Réduit la Force d'un monstre de 2 pour le combat. Augmente votre Force de 2 pour le combat."),
        Spell("Flétrissement", 2, "Réduit la Vigueur d'un monstre de 2 pour le combat."),
        Spell("Armure nécrotique", 3, "Augmente l'armure de 1. Chaque attaque de monstre augmente votre Force de 4 pour le combat."),
        Spell("Nuage toxique", 3, "Réduit la Force et la Vigueur de chaque monstre de 2 pour le combat."),
        Spell("Hypnose", 4, "Réduit la Force d'un monstre de 5 pour le combat et inflige 5 dégâts de chaos."),
        Spell("Domination funeste", 4, "Chaque monstre attaque avec une Force réduite de 3 et s'inflige 3 dégât de chaos. Réduit la Force et la Vigueur d'un monstre de 3 pour le combat.")
    ],
    "Sort de nature": [
        Spell("Toucher de la nature", 1, "Augmente la Vigueur d'un joueur de 1 pour le combat."),
        Spell("Précision féline", 1, "Réduit le seuil de toucher des dés d'un joueur de 1 pour le combat."),
        Spell("Sauvagerie", 1, "Augmente la Force d'un joueur de 2 pour le combat."),
        Spell("Trait de foudre", 2, "Inflige 1 dégât de nature et augmente la Force d'un joueur de 2 pour le combat."),
        Spell("Appel de la nature", 2, "Chaque attaque de monstre augmente la Force d'un joueur de 4 pour le combat."),
        Spell("Endurance farouche", 2, "Augmente la Vigueur d'un joueur de 4 pour le combat."),
        Spell("Croissance sauvage", 3, "Augmente la Force d'un joueur de 4 pour le combat."),
        Spell("Sarments épineux", 3, "Inflige 3 dégâts de nature à chaque monstre qui utilise une capacité ou qui attaque."),
        Spell("Tempête", 4, "Expulse les monstres du combat et inflige 4 dégâts de nature."),
        Spell("Invocation sylvaine", 4, "Augmente la Force et la Vigueur de chaque joueur de 5 pour le combat.")
    ]
}

# --- DATABASE: CHARACTERS ---
characters = [
    Character("Varelias Druide", 1, 2, 3, 2, [
        "Peut lancer des sorts de nature et de sacré.",
        "Au début du combat, se transforme dans la forme de son choix :",
        "◦ Cerf : ajoute [niveau] à sa Vigueur.",
        "◦ Ours : ajoute [niveau] à sa Force.",
        "◦ Hibou : régénère tous ses points de mana. pioche jusqu'à un sort. effet des sorts de nature augmentés de 1."
    ], ["Sort de nature", "Sort de sacré"]),

    Character("Orc Guerrier", 3, 3, 1, 1, [
        "Commence le jeu avec une épée courte et une targe en bois.",
        "Ne peut pas lancer de sorts.",
        "Peut porter deux armes à deux mains.",
        "Les armes ajoutent le double de la Force indiquée.",
        "Enrage, devient insensible au charme et à l'assommement, et ajoute [volonté] à sa force Force quand le guerrier :",
        "◦ subit des dégâts.",
        "◦ retrouve ses esprits après avoir été charmé ou assommé par un monstre."
    ], []),

    Character("Murvien Thermolige", 1, 2, 2, 3, [
        "Peut lancer tout type de sort.",
        "Peut se défausser d'un sort qui n'est pas de givrefeu pour dupliquer un sort de givrefeu. (Les sorts d'arcane sont de givrefeu ou temporels).",
        "Les effets des sorts de givrefeu sont augmentés de 1.",
        "Peut porter autant d'armes que ses quatres bras lui permettent."
    ], ["Sort d'arcane", "Sort de sacré", "Sort de chaos", "Sort de nature"]),

    Character("Djinn Roublard", 2, 2, 2, 2, [
        "Commence avec deux épées courtes.",
        "Peut lancer des sorts d'arcane. (Les sorts d'arcane sont de givrefeu ou temporels).",
        "Gain de pièces d'or augmenté de [volonté] à la fin d'un évènement.",
        "Peut relancer [intellect] dés par phase, dont ceux des ennemis.",
        "Peut payer une pièce d'or pour :",
        "◦ gagner un point de caractéristique au choix en montant de niveau.",
        "◦ piocher jusqu'à un sort supplémentaire au début du tour.",
        "◦ remettre un sort lancé dans sa main.",
        "◦ ajouter 1 à son Intellect pour la phase."
    ], ["Sort d'arcane"]),

    Character("Elfe Clerc", 1, 2, 3, 2, [
        "Peut lancer des sorts de sacré et de chaos.",
        "Effet des sorts de sacré augmentés de 1.",
        "À chaque lancer de sort de sacré, inflige 1 dégât de sacré à un monstre.",
        "Chaque dégât réduit par un point d'armure de l'elfe se dissipe et inflige autant de dégâts de sacré à un monstre.",
        "Les soins effectifs des sorts de sacré de l'elfe infligent à un monstre autant de dégâts de sacré.",
        "Les dégâts de sacré de l'elfe sont doublés contre les morts-vivants et démons."
    ], ["Sort de sacré", "Sort de chaos"]),

    Character("Chepteg Chaman", 1, 2, 3, 2, [
        "Peut lancer des sorts de nature et d'arcane.",
        "Peut éviter le combat dans la neige.",
        "À chaque lancer de sort de nature, il lance 1d6 et bénéficie de (chaque effet s'ajoute à l'effet inférieur) :",
        "◦ 1-2 : gagne 1 de Force pour le combat.",
        "◦ 3-4 : gagne 1 de Vigueur pour le combat.",
        "◦ 5-6 : inflige 1 dégât de nature et pioche un sort."
    ], ["Sort de nature", "Sort d'arcane"]),

    Character("Dragonide Sombregarde", 3, 3, 1, 1, [
        "Commence avec une épée courte.",
        "Peut lancer des sorts de chaos.",
        "Le déplacement en montagne ne compte pas dans la limite du tour.",
        "Lorsqu'il attaque, le sombregarde peut infuser au choix son arme :",
        "◦ Frappe sanguinaire : regagne [niveau] points de vie à la fin de la phase.",
        "◦ Frappe morbide : réduit la Vigueur du monstre de [niveau].",
        "◦ Frappe démoniaque : réduit la Force du monstre de [niveau].",
        "◦ Frappe spectrale : ignore l'armure du monstre et inflige des dégâts de chaos à la place des dégâts physiques."
    ], ["Sort de chaos"]),

    Character("Centaure Rôdeuse", 2, 2, 2, 2, [
        "Commence le jeu avec un gambison.",
        "Peut lancer des sorts de nature.",
        "Peut se déplacer de 5 régions par tour.",
        "Bénéficie d'une première phase de combat supplémentaire au début du combat pendant laquelle :",
        "◦ seule la centaure peut agir.",
        "◦ elle ajoute [niveau] à sa Force.",
        "◦ son seuil de toucher est réduit de 1.",
        "Peut fuir le combat à chaque fin de phase sans lancer de dé."
    ], ["Sort de nature"]),

    Character("Humain Démoniste", 1, 2, 2, 3, [
        "Peut lancer des sorts de chaos et d'arcane.",
        "À chaque lancer de sort de chaos, le démoniste invoque un démon en fonction du coût en mana du sort :",
        "◦ 1 : succube impie : réduit la Force d'un monstre de 1.",
        "◦ 2 : diablotin ravageur : inflige 1 dégât de chaos.",
        "◦ 3 : molosse chaotique : réduit la Vigueur d'un monstre de 1.",
        "◦ 4 : dévoreur infernal : inflige 2 dégâts de chaos."
    ], ["Sort de chaos", "Sort d'arcane"]),

    Character("Satyre Nécromant", 1, 2, 2, 3, [
        "Peut lancer des sorts de chaos et de nature.",
        "Lorsqu'il vainc un monstre, il peut le réanimer pour ajouter [niveau] Force lors du prochain combat.",
        "À chaque lancer de sort de chaos, réduit la Force et la Vigueur d'un monstre de 1."
    ], ["Sort de chaos", "Sort de nature"]),

    Character("Nain Paladin", 3, 3, 1, 1, [
        "Commence le jeu avec un gambison, un capuchon, une épée courte et une targe en bois.",
        "Peut lancer des sorts de sacré.",
        "À chaque lancer de sort de sacré, gagne autant de Force que de points de mana dépensés.",
        "Les soins effectifs des sorts de sacré du paladin augmentent son armure d'autant.",
        "Lors de son attaque normale, ajoute son armure à sa Force.",
        "Les dégâts physiques du paladin sont doublés contre les morts-vivants et démons."
    ], ["Sort de sacré"]),

    Character("Minotaure Chronosage", 1, 2, 2, 3, [
        "Peut lancer des sorts d'arcane et de sacré. (Les sorts d'arcane sont de givrefeu ou temporels).",
        "Peut choisir parmi deux sorts de plus en piochant des sorts d'arcane.",
        "À chaque lancer de sort temporel, il lance 1d6, ajoute le nombre de sorts dans sa main, et bénéficie de (chaque effet s'ajoute à l'effet inférieur) :",
        "◦ 1-3 : ajoute [vigueur] à sa Force.",
        "◦ 4-6 : le sort revient dans la main.",
        "◦ 7-9 : le sort est dupliqué.",
        "◦ 10+ : ajoute [volonté] à sa Force."
    ], ["Sort d'arcane", "Sort de sacré"])
]


# --- STREAMLIT UI ---
st.set_page_config(page_title="RPG Manager", page_icon="⚔️", layout="wide")
st.title("⚔️ RPG Character & Spell Manager")

# Sidebar for character selection and leveling
with st.sidebar:
    st.header("🛡️ Configuration du Héros")
    char_names = [c.name for c in characters]
    selected_name = st.selectbox("Choisir un Héros", char_names)
    char = next(c for c in characters if c.name == selected_name)
    
    level = st.select_slider("Niveau du personnage", options=range(1, 7), value=1)
    bonus_points_total = (level - 1) * 2
    
    st.divider()
    st.subheader(f"📈 Points bonus disponibles: {bonus_points_total}")
    
    bonus_stats = {}
    current_spent = 0
    for stat in ["Force", "Vigueur", "Intellect", "Volonté"]:
        val = st.number_input(f"+ {stat}", min_value=0, max_value=bonus_points_total, value=0, key=f"bonus_{stat}")
        bonus_stats[stat] = val
        current_spent += val
        
    if current_spent > bonus_points_total:
        st.error(f"Points excédentaires ! ({current_spent}/{bonus_points_total})")

    st.divider()
    if char.allowed_schools:
        chosen_school = st.selectbox("École de Magie", char.allowed_schools)
        draw_count = st.number_input("Nombre de sorts à tirer", 1, 10, 1)
        draw_btn = st.button("🔮 Tirer les sorts")
    else:
        st.warning("Ce héros n'utilise pas de magie.")
        draw_btn = False

# Main Display Area
col_info, col_spells = st.columns([1, 1])

with col_info:
    st.header(f"{char.name} (Niveau {level})")
    
    st.subheader("📊 Caractéristiques Finales")
    for stat, base_val in char.base_stats.items():
        total_val = base_val + bonus_stats[stat]
        st.write(f"**{stat}**: {total_val} (Base {base_val} + {bonus_stats[stat]} bonus)")
        st.progress(min(total_val / 15, 1.0))

    st.subheader("📜 Capacités Spéciales")
    for cap in char.capacities:
        # Replacement dynamique des variables
        display_cap = cap.replace("[niveau]", str(level))
        display_cap = display_cap.replace("[volonté]", str(char.base_stats["Volonté"] + bonus_stats["Volonté"]))
        display_cap = display_cap.replace("[vigueur]", str(char.base_stats["Vigueur"] + bonus_stats["Vigueur"]))
        display_cap = display_cap.replace("[intellect]", str(char.base_stats["Intellect"] + bonus_stats["Intellect"]))
        st.markdown(f"- {display_cap}")

with col_spells:
    if draw_btn and current_spent <= bonus_points_total:
        st.header(f"✨ Grimoire : {chosen_school}")
        
        # Tirage pondéré
        pool = []
        for s in all_schools[chosen_school]:
            pool.extend([s] * s.frequency)
            
        results = random.sample(pool, k=min(draw_count, len(pool)))
        results.sort(key=lambda spell: spell.mana)
        
        for s in results:
            with st.expander(f"**{s.name}** — Coût: {s.mana} Mana", expanded=True):
                st.write(s.effect)
                freq_text = "Rare" if s.frequency == 1 else "Commune" if s.frequency == 3 else "Peu commune"
                st.caption(f"Disponibilité : {freq_text}")