import streamlit as st
import random

# --- DATA STRUCTURE ---
class Spell:
    def __init__(self, name, mana, effect):
        self.name = name
        self.mana = mana
        self.effect = effect
        if mana == 1:
            self.frequency = 3
        elif mana == 2 or mana == 3:
            self.frequency = 2
        else:
            self.frequency = 1

# --- DATABASE (Same as before) ---
arcane_spells = [
    Spell("Boule de feu", 1, "Inflige 2 dégâts de feu."),
    Spell("Lévitation", 1, "Hors combat: mouvement +1. Combat: piochez un sort."),
    Spell("Contrôle des lames", 2, "Augmente la relance des dés de 6."),
    Spell("Doigt de givre", 2, "2 dégâts de givre. Seuil de toucher monstre +1."),
    Spell("Altération de réalité", 3, "Remplace 6 dés par dégâts d'arcane."),
    Spell("Météore", 3, "Inflige 5 dégâts de feu."),
    Spell("Trait de givrefeu", 4, "4 dégâts de feu et 2 dégâts de givre."),
    Spell("Glyphe réfléchissante", 4, "Renvoie 4 dégâts d'arcane par attaque."),
    Spell("Téléportation", 5, "Téléportation (hors combat) ou pioche 3 sorts (combat)."),
    Spell("Blizzard éternel", 6, "Inflige 6 dégâts de givre à chaque monstre par phase.")
]

sacred_spells = [
    Spell("Bouclier de protection", 1, "Armure +1."),
    Spell("Châtiment", 1, "1 dégât sacré. Soigne 1 PV."),
    Spell("Purification", 2, "Effet de purification."),
    Spell("Infusion sacrée", 2, "Attaque physique +1 dégât sacré."),
    Spell("Pénitence", 3, "3 dégâts sacrés. Soigne 3 PV."),
    Spell("Fontaine sacrée", 3, "Armure +1, Soigne 2 PV, Boost stats groupe."),
    Spell("Bouclier divin", 4, "Armure +4."),
    Spell("Barrière angélique", 4, "Si hors combat: Soigne 1 PV et boost armure."),
    Spell("Intervention lumineuse", 5, "Soigne tous les PV/Mana/Sorts. +3 armure."),
    Spell("Immunité divine", 6, "Insensible pour la phase. +4 armure.")
]

chaos_spells = [
    Spell("Trait d'ombre", 1, "2 dégâts de chaos."),
    Spell("Débilitation", 1, "Seuil de toucher monstre +1."),
    Spell("Toucher de faiblesse", 2, "Force monstre -2."),
    Spell("Agonie", 2, "2 dégâts de chaos par phase."),
    Spell("Drain d'âme", 3, "Force monstre -2 / Force joueur +2."),
    Spell("Flétrissement", 3, "Vigueur monstre -3."),
    Spell("Armure nécrotique", 4, "Armure +1. Attaques monstres boostent votre Force."),
    Spell("Nuage toxique", 4, "Force/Vigueur monstres -4."),
    Spell("Hypnose", 5, "Force monstre -5 et 5 dégâts."),
    Spell("Domination funeste", 6, "Force et Vigueur monstre -6.")
]

nature_spells = [
    Spell("Toucher de la nature", 1, "Force +1 et soigne 2 PV."),
    Spell("Appel de la nature", 1, "Chaque attaque augmente Force de 2."),
    Spell("Trait de foudre", 2, "3 dégâts nature et Force +2."),
    Spell("Sauvagerie", 2, "Force +2."),
    Spell("Précision féline", 3, "Seuil de toucher -1."),
    Spell("Endurance farouche", 3, "Vigueur +5."),
    Spell("Croissance sauvage", 4, "Force +5."),
    Spell("Sarments épineux", 4, "4 dégâts aux monstres qui attaquent."),
    Spell("Tempête", 5, "Expulse monstres et inflige 5 dégâts."),
    Spell("Invocation sylvaine", 6, "Force et Vigueur +6.")
]

schools = {
    "Sort d'arcane": arcane_spells,
    "Sort de sacré": sacred_spells,
    "Sort de chaos": chaos_spells,
    "Sort de nature": nature_spells
}

# --- STREAMLIT GUI ---
st.set_page_config(page_title="Magic Spell Randomizer", page_icon="🪄")

st.title("🪄 Magic Spell Randomizer")
st.write("Sélectionnez votre école de magie et le nombre de sorts à tirer.")

# Sidebar for inputs
with st.sidebar:
    st.header("Paramètres")
    school_choice = st.selectbox("École de Magie", list(schools.keys()))
    num_spells = st.number_input("Nombre de sorts", min_value=1, max_value=10, value=1)
    draw_button = st.button("Tirer les sorts")

if draw_button:
    selected_school_list = schools[school_choice]
    
    # Create the weighted pool based on rules
    weighted_pool = []
    for spell in selected_school_list:
        weighted_pool.extend([spell] * spell.frequency)
    
    # Pick the spells (allowing for frequency weighting)
    # random.sample is used to ensure we don't pick the EXACT same instance twice
    # but the frequency increases the odds of it appearing in the pool.
    results = random.sample(weighted_pool, k=min(num_spells, len(weighted_pool)))

    st.subheader(f"Résultats pour: {school_choice}")
    
    for i, spell in enumerate(results, 1):
        with st.expander(f"{i}. {spell.name} ({spell.mana} Mana)"):
            st.write(f"**Effet:** {spell.effect}")
            st.caption(f"Fréquence dans le deck: {spell.frequency}")