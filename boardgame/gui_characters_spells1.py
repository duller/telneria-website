import streamlit as st
import random

# --- CLASSES ---
class Spell:
    def __init__(self, name, mana, effect):
        self.name = name
        self.mana = mana
        self.effect = effect
        # Frequency logic: 3 for 1 mana, 2 for 2-3 mana, 1 for 4+ mana
        if self.mana == 1:
            self.frequency = 3
        elif 2 <= self.mana <= 3:
            self.frequency = 2
        else:
            self.frequency = 1

class Character:
    def __init__(self, name, f, v, i, vo, caps, schools):
        self.name = name
        self.base_stats = {"Force": f, "Vigueur": v, "Intellect": i, "Volonté": vo}
        self.capacities = caps
        self.allowed_schools = schools

# --- DATABASE: SPELLS ---
all_schools = {
    "Sort d'arcane": [
        Spell("Boule de feu", 1, "Inflige 2 dégâts de feu."),
        Spell("Lévitation", 1, "Hors combat: mouv. +1. Combat: pioche 1 sort."),
        Spell("Doigt de givre", 2, "2 dégâts givre. Seuil de toucher monstre +1."),
        Spell("Contrôle des lames", 2, "Relance des dés +6 pour la phase."),
        Spell("Altération de réalité", 3, "Remplace 6 dés par dégâts d'arcane."),
        Spell("Météore", 3, "Inflige 5 dégâts de feu."),
        Spell("Trait de givrefeu", 4, "4 dégâts de feu et 2 de givre."),
        Spell("Glyphe réfléchissante", 4, "Renvoie 4 dégâts d'arcane par attaque."),
        Spell("Téléportation", 5, "Téléportation (hors combat) ou pioche 3 sorts (combat)."),
        Spell("Blizzard éternel", 6, "6 dégâts de givre à chaque monstre par phase.")
    ],
    "Sort de sacré": [
        Spell("Bouclier de protection", 1, "Armure +1."),
        Spell("Châtiment", 1, "1 dégât sacré. Soigne 1 PV."),
        Spell("Infusion sacrée", 2, "Attaque physique +1 dégât sacré."),
        Spell("Purification", 2, "Armure +1. Soigne 2 PV."),
        Spell("Fontaine sacrée", 3, "Stats du groupe +2."),
        Spell("Pénitence", 3, "3 dégâts sacrés. Soigne 3 PV."),
        Spell("Bouclier divin", 4, "Armure +4."),
        Spell("Barrière angélique", 4, "Prochaine mise hors de combat: +1 PV / +2 Armure."),
        Spell("Intervention lumineuse", 5, "Full Soin PV/Mana/Sorts. +3 armure."),
        Spell("Immunité divine", 6, "Insensible cette phase. +4 armure.")
    ],
    "Sort de chaos": [
        Spell("Trait d'ombre", 1, "2 dégâts de chaos."),
        Spell("Débilitation", 1, "Seuil de toucher monstre +1."),
        Spell("Toucher de faiblesse", 2, "Force monstre -2."),
        Spell("Agonie", 2, "2 dégâts de chaos par phase."),
        Spell("Drain d'âme", 3, "Force monstre -2 / Force joueur +2."),
        Spell("Flétrissement", 3, "Vigueur monstre -3."),
        Spell("Armure nécrotique", 4, "Armure +1. Dégâts subis boostent la Force."),
        Spell("Nuage toxique", 4, "Force/Vigueur monstres -4."),
        Spell("Hypnose", 5, "Force monstre -5 et 5 dégâts."),
        Spell("Domination funeste", 6, "Force et Vigueur monstre -6.")
    ],
    "Sort de nature": [
        Spell("Toucher de la nature", 1, "Force +1 et soigne 2 PV."),
        Spell("Appel de la nature", 1, "Attaques subies boostent Force de 2."),
        Spell("Trait de foudre", 2, "3 dégâts nature et Force +2."),
        Spell("Sauvagerie", 2, "Force +2."),
        Spell("Précision féline", 3, "Seuil de toucher -1."),
        Spell("Endurance farouche", 3, "Vigueur +5."),
        Spell("Croissance sauvage", 4, "Force +5."),
        Spell("Sarments épineux", 4, "4 dégâts aux monstres qui attaquent."),
        Spell("Tempête", 5, "Expulse monstres et 5 dégâts."),
        Spell("Invocation sylvaine", 6, "Force et Vigueur +6.")
    ]
}

# --- DATABASE: CHARACTERS (Updated from new PDF) ---
characters = [
    Character("Varelias Druide", 2, 3, 3, 4, [
        "Peut lancer des sorts de nature et de sacré.",
        "Au début du combat, se transforme dans la forme de son choix :",
        "◦ Cerf : ajoute [niveau] à sa Vigueur.",
        "◦ Ours : ajoute [niveau] à sa Force.",
        "◦ Hibou : régénère tous ses points de mana, pioche jusqu’à un sort, effet des sorts de nature augmentés de 1."
    ], ["Sort de nature", "Sort de sacré"]),

    Character("Orc Guerrier", 5, 5, 1, 1, [
        "Commence le jeu avec une épée courte et une targe en bois.",
        "Ne peut pas lancer de sorts.",
        "Peut porter deux armes à deux mains.",
        "Les armes ajoutent le double de la Force indiquée.",
        "Enrage, devient insensible au charme et à l’assommement, et ajoute [volonté] à sa force Force quand le guerrier :",
        "◦ subit des dégâts.",
        "◦ retrouve ses esprits après avoir été charmé ou assommé par un monstre."
    ], []),

    Character("Murvien Thermolige", 1, 2, 5, 4, [
        "Peut lancer tout type de sort.",
        "Peut se défausser d’un sort qui n’ est pas de givrefeu pour dupliquer un sort de givrefeu. (Les sorts d’ arcane sont de givrefeu ou temporels).",
        "Les effets des sorts de givrefeu sont augmentés de 1.",
        "Peut porter autant d’armes que ses quatres bras lui permettent."
    ], ["Sort d'arcane", "Sort de sacré", "Sort de chaos", "Sort de nature"]),

    Character("Djinn Roublard", 3, 3, 3, 3, [
        "Commence avec deux épées courtes.",
        "Peut lancer des sorts d’arcane. (Les sorts d’ arcane sont de givrefeu ou temporels).",
        "Gain de pièces d’ or augmenté de [volonté] à la fin d’un évènement.",
        "Peut relancer [intellect] dés par phase, dont ceux des ennemis.",
        "Peut payer une pièce d’or pour :",
        "◦ gagner un point de caractéristique au choix en montant de niveau.",
        "◦ piocher jusqu’à un sort supplémentaire au début du tour.",
        "◦ remettre un sort lancé dans sa main.",
        "◦ ajouter 1 à son Intellect pour la phase."
    ], ["Sort d'arcane"]),

    Character("Elfe Clerc", 1, 2, 4, 5, [
        "Peut lancer des sorts de sacré et de chaos.",
        "Effet des sorts de sacré augmentés de 1.",
        "À chaque lancer de sort de sacré :",
        "◦ gagne 1 d’armure.",
        "◦ inflige 1 dégât de sacré à un monstre.",
        "Chaque attaque de monstre inflige en retour un nombre de dégâts égal à l’armure de l’elfe.",
        "Lorsque l’elfe soigne des points de vie, elle inflige autant de dégâts de sacré.",
        "Les dégâts de sacré sont doublés contre les goules, fantômes et démons."
    ], ["Sort de sacré", "Sort de chaos"]),

    Character("Chepteg Chaman", 3, 4, 3, 2, [
        "Peut lancer des sorts de nature et d’arcane.",
        "Peut éviter le combat dans la neige.",
        "À chaque lancer de sort de nature, il lance 1d6 et bénéficie de (chaque effet s’ ajoute à l’ effet inférieur) :",
        "◦ 1 : gagne 1 de Force pour le combat.",
        "◦ 2 : gagne 1 de Vigueur pour le combat.",
        "◦ 3 : inflige 1 dégât de nature.",
        "◦ 4 : regagne le mana dépensé.",
        "◦ 5 : pioche un sort.",
        "◦ 6 : peut échanger un sort."
    ], ["Sort de nature", "Sort d'arcane"]),

    Character("Dragonide Sombregarde", 4, 4, 1, 3, [
        "Commence avec une épée courte.",
        "Peut lancer des sorts de chaos.",
        "Le déplacement en montagne ne compte pas dans la limite du tour.",
        "Lorsqu’il attaque, le sombregarde peut infuser au choix son arme :",
        "◦ Frappe sanguinaire : regagne [niveau] points de vie à la fin de la phase.",
        "◦ Frappe morbide : réduit la Vigueur du monstre de [niveau].",
        "◦ Frappe démoniaque : réduit la Force du monstre de [niveau].",
        "◦ Frappe spectrale : ignore l’armure du monstre et inflige des dégâts de chaos à la place des dégâts physiques."
    ], ["Sort de chaos"]),

    Character("Centaure Rôdeuse", 3, 4, 2, 3, [
        "Commence le jeu avec un gambison.",
        "Peut lancer des sorts de nature.",
        "Peut se déplacer de 5 régions par tour.",
        "Bénéficie d’une première phase de combat supplémentaire au début du combat pendant laquelle :",
        "◦ seule la centaure peut agir.",
        "◦ elle ajoute [niveau] à sa Force.",
        "◦ son seuil de toucher est réduit de 1.",
        "Peut fuir le combat à chaque fin de phase sans lancer de dé."
    ], ["Sort de nature"]),

    Character("Humain Démoniste", 2, 2, 4, 4, [
        "Peut lancer des sorts de chaos et d’arcane.",
        "À chaque lancer de sort de chaos, en fonction du coût en mana du sort :",
        "◦ 1-2 : un diablotin apparaît et réduit la Vigueur d’un monstre de 1.",
        "◦ 3-4 : une succube apparaît et réduit la Force d’un monstre de 2.",
        "◦ 5-6 : un molosse chaotique apparaît et inflige 3 de dégâts à un monstre."
    ], ["Sort de chaos", "Sort d'arcane"]),

    Character("Satyre Nécromant", 1, 3, 4, 4, [
        "Peut lancer des sorts de chaos et de nature.",
        "Lorsqu’il vainc un monstre, il peut le réanimer pour ajouter [niveau] Force lors du prochain combat.",
        "À chaque lancer de sort de chaos, réduit la Force et la Vigueur d’un monstre de 1."
    ], ["Sort de chaos", "Sort de nature"]),

    Character("Nain Paladin", 4, 4, 3, 1, [
        "Commence le jeu avec un gambison, un capuchon, une épée courte et une targe en bois.",
        "Peut lancer des sorts de sacré.",
        "À chaque lancer de sort de sacré, gagne autant de Force que de points de mana dépensés.",
        "Lorsque le paladin soigne des points de vie, il augmente sa Force d’autant pour le combat.",
        "Lors de son attaque normale, ajoute son armure à sa Force.",
        "Double sa Force quand il attaque une goule, un fantôme, ou un démon."
    ], ["Sort de sacré"]),

    Character("Minotaure Chronosage", 2, 3, 5, 2, [
        "Peut lancer des sorts d’arcane et de sacré. (Les sorts d’ arcane sont de givrefeu ou temporels).",
        "Peut choisir parmi deux sorts de plus en piochant des sorts d’arcane.",
        "À chaque lancer de sort temporel, il lance 1d6, ajoute le nombre de sorts dans sa main, et bénéficie de (chaque effet s’ ajoute à l’ effet inférieur) :",
        "◦ 1-3 : ajoute [vigueur] à sa Force.",
        "◦ 4-6 : le sort revient dans la main.",
        "◦ 7-9 : le sort est dupliqué.",
        "◦ 10+ : ajoute [volonté] à sa Force."
    ], ["Sort d'arcane", "Sort de sacré"]),
]

# --- STREAMLIT UI ---
st.set_page_config(page_title="RPG Character Manager", page_icon="⚔️", layout="wide")

st.title("⚔️ RPG Character & Spell Manager")

with st.sidebar:
    st.header("🛡️ Personnage")
    char_names = [c.name for c in characters]
    selected_name = st.selectbox("Choisir un Héros", char_names)
    char = next(c for c in characters if c.name == selected_name)
    
    level = st.select_slider("Niveau du personnage", options=range(1, 7), value=1)
    bonus_points_total = (level - 1) * 2
    
    st.divider()
    st.subheader(f"📈 Points bonus: {bonus_points_total}")
    
    # Stat distribution logic
    bonus_stats = {}
    current_spent = 0
    for stat in ["Force", "Vigueur", "Intellect", "Volonté"]:
        remaining = bonus_points_total - current_spent
        val = st.number_input(f"+ {stat}", min_value=0, max_value=bonus_points_total, value=0, key=f"bonus_{stat}")
        bonus_stats[stat] = val
        current_spent += val
        
    if current_spent > bonus_points_total:
        st.error(f"Attention! Vous avez utilisé {current_spent}/{bonus_points_total} points.")
    elif bonus_points_total > 0 and current_spent < bonus_points_total:
        st.warning(f"Il vous reste {bonus_points_total - current_spent} points à distribuer.")
    elif bonus_points_total > 0:
        st.success("Tous les points sont répartis !")

    st.divider()
    if char.allowed_schools:
        chosen_school = st.selectbox("École de Magie", char.allowed_schools)
        draw_count = st.number_input("Nombre de sorts", 1, 10, 1)
        draw_btn = st.button("🔮 Tirer les sorts")
    else:
        st.warning("Aucune magie disponible.")
        draw_btn = False

# Main Layout
col_info, col_spells = st.columns([1, 1])

with col_info:
    st.header(f"Fiche de {char.name} (Niv. {level})")
    
    # Attributes with bonus points added
    st.subheader("📊 Caractéristiques")
    for stat, base_val in char.base_stats.items():
        total_val = base_val + bonus_stats[stat]
        st.write(f"**{stat}**: {total_val} (Base {base_val} + {bonus_stats[stat]})")
        st.progress(min(total_val / 15, 1.0))

    st.subheader("📜 Capacités Spéciales")
    for cap in char.capacities:
        # Dynamic replacement for placeholders like [niveau]
        display_cap = cap.replace("[niveau]", str(level))
        display_cap = display_cap.replace("[volonté]", str(char.base_stats["Volonté"] + bonus_stats["Volonté"]))
        display_cap = display_cap.replace("[intellect]", str(char.base_stats["Intellect"] + bonus_stats["Intellect"]))
        st.markdown(f"- {display_cap}")

with col_spells:
    if draw_btn and current_spent <= bonus_points_total:
        st.header(f"✨ Sorts de {chosen_school}")
        
        # Weighted draw based on new frequency logic
        pool = []
        for s in all_schools[chosen_school]:
            pool.extend([s] * s.frequency)
            
        if not pool:
            st.error("Aucun sort disponible pour cette école.")
        else:
            results = random.sample(pool, k=min(draw_count, len(pool)))
            
            for s in results:
                with st.expander(f"**{s.name}** ({s.mana} Mana)", expanded=True):
                    st.write(s.effect)
                    # Display frequency for info
                    freq_label = "Fréquente (3)" if s.frequency == 3 else "Moyenne (2)" if s.frequency == 2 else "Rare (1)"
                    st.caption(f"Fréquence dans le deck : {freq_label}")
    elif draw_btn:
        st.warning("Veuillez corriger la distribution de vos points bonus avant de tirer des sorts.")