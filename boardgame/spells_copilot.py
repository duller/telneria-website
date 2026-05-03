import random

# -----------------------------
# Spell class
# -----------------------------
class Spell:
    def __init__(self, name, mana, effect):
        self.name = name
        self.mana = mana
        self.effect = effect
        # Frequency rule: 1–4 mana → 2 copies, 5–6 mana → 1 copy
        self.frequency = 2 if 1 <= mana <= 4 else 1

    def __repr__(self):
        return f"{self.name} ({self.mana} mana): {self.effect}"


# -----------------------------
# Spell lists by school
# -----------------------------

arcane_spells = [
    Spell("Boule de feu", 1, "Inflige 2 dégâts de feu."),
    Spell("Lévitation", 1, "Mouvement +1 hors combat, évite le combat. En combat : pioche 1 sort."),
    Spell("Doigt de givre", 2, "Inflige 2 dégâts de givre. Augmente le seuil de toucher du monstre de 1."),
    Spell("Contrôle des lames", 2, "Augmente la relance totale des dés des joueurs de 6."),
    Spell("Altération de réalité", 3, "Remplace jusqu'à 6 dés par autant de dégâts d'arcane."),
    Spell("Météore", 3, "Inflige 5 dégâts de feu."),
    Spell("Trait de givrefeu", 4, "Inflige 4 dégâts de feu et 2 dégâts de givre."),
    Spell("Glyphe réfléchissante", 4, "Chaque attaque de monstre inflige en retour 4 dégâts d'arcane."),
    Spell("Téléportation", 5, "Téléporte un monstre/joueur. En combat : pioche 3 sorts."),
    Spell("Blizzard éternel", 6, "Inflige 6 dégâts de givre à chaque monstre chaque phase.")
]

holy_spells = [
    Spell("Bouclier de protection", 1, "Augmente l'armure de 1 pour le combat."),
    Spell("Châtiment", 1, "Inflige 1 dégât de sacré et soigne 1 PV."),
    Spell("Infusion sacrée", 2, "Chaque attaque physique inflige 1 dégât de sacré supplémentaire."),
    Spell("Purification", 2, "Armure +1 et soigne 2 PV."),
    Spell("Fontaine sacrée", 3, "Augmente toutes les caractéristiques du groupe de 2."),
    Spell("Pénitence", 3, "Inflige 3 dégâts de sacré et soigne 3 PV."),
    Spell("Bouclier divin", 4, "Augmente l'armure de 4."),
    Spell("Barrière angélique", 4, "Prochaine mise hors combat : soigne 1 PV et armure +2."),
    Spell("Intervention lumineuse", 5, "Soigne tous les PV, rend tout le mana, armure +3."),
    Spell("Immunité divine", 6, "Rend un joueur insensible à tout, armure +4.")
]

chaos_spells = [
    Spell("Trait d'ombre", 1, "Inflige 2 dégâts de chaos."),
    Spell("Débilitation", 1, "Augmente le seuil de toucher d'un monstre de 1."),
    Spell("Toucher de faiblesse", 2, "Réduit la Force d'un monstre de 2."),
    Spell("Agonie", 2, "Inflige 2 dégâts de chaos par phase."),
    Spell("Drain d'âme", 3, "Force -2 au monstre, Force +2 au joueur."),
    Spell("Flétrissement", 3, "Réduit la Vigueur d'un monstre de 3."),
    Spell("Armure nécrotique", 4, "Armure +1. Chaque attaque de monstre augmente la Force de 4."),
    Spell("Nuage toxique", 4, "Force et Vigueur -4 pour chaque monstre."),
    Spell("Hypnose", 5, "Chaque attaque d'un monstre réduit sa Force de 5 et inflige 5 dégâts."),
    Spell("Domination funeste", 6, "Force et Vigueur -6 d'un monstre.")
]

nature_spells = [
    Spell("Toucher de la nature", 1, "Force +1 pour un joueur."),
    Spell("Appel de la nature", 1, "Soigne 2 PV."),
    Spell("Sauvagerie", 2, "Force +2 pour un joueur."),
    Spell("Trait de foudre", 2, "Inflige 3 dégâts et Force +2."),
    Spell("Précision féline", 3, "Réduit le seuil de toucher d'un joueur de 1."),
    Spell("Endurance farouche", 3, "Vigueur +5."),
    Spell("Croissance sauvage", 4, "Force +5."),
    Spell("Sarments épineux", 4, "Inflige 4 dégâts à chaque monstre qui attaque ou utilise une capacité."),
    Spell("Tempête", 5, "Expulse les monstres et inflige 5 dégâts à chacun."),
    Spell("Invocation sylvaine", 6, "Force +6 et Vigueur +6.")
]


# -----------------------------
# Spell school dictionary
# -----------------------------
schools = {
    "arcane": arcane_spells,
    "sacré": holy_spells,
    "chaos": chaos_spells,
    "nature": nature_spells
}


# -----------------------------
# Random selection function
# -----------------------------
def pick_spells(school_name, count):
    spells = schools[school_name.lower()]
    weighted_pool = []

    for spell in spells:
        weighted_pool.extend([spell] * spell.frequency)

    return random.sample(weighted_pool, count)


# -----------------------------
# User interaction
# -----------------------------
def main():
    print("Écoles de magie disponibles : arcane, sacré, chaos, nature")
    school = input("Choisissez une école : ").strip().lower()

    if school not in schools:
        print("École inconnue.")
        return

    try:
        n = int(input("Combien de sorts voulez-vous tirer ? "))
    except ValueError:
        print("Veuillez entrer un nombre valide.")
        return

    selected = pick_spells(school, n)

    print("\n--- Sorts sélectionnés ---")
    for s in selected:
        print(f"- {s.name} ({s.mana} mana) : {s.effect}")


if __name__ == "__main__":
    main()
