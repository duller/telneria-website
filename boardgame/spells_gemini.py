import random

class Spell:
    def __init__(self, name, mana, effect):
        self.name = name
        self.mana = mana
        self.effect = effect
        # Frequency: 2 for 1-4 mana, 1 for 5-6 mana
        self.frequency = 2 if 1 <= mana <= 4 else 1

    def __repr__(self):
        return f"{self.name} ({self.mana} mana): {self.effect}"

# Spell lists extracted from the document
arcane_spells = [
    Spell("Boule de feu", 1, "Inflige 2 dégâts de feu."),
    Spell("Lévitation", 1, "Hors combat: mouvement augmenté de 1. Combat: piochez un sort."),
    Spell("Contrôle des lames", 2, "Augmente la relance des dés total des joueurs de 6."),
    Spell("Doigt de givre", 2, "Inflige 2 dégâts de givre. Augmente le seuil de toucher du monstre de 1."),
    Spell("Altération de réalité", 3, "Remplace jusqu'à 6 dés par autant de dégâts d'arcane."),
    Spell("Météore", 3, "Inflige 5 dégâts de feu."),
    Spell("Trait de givrefeu", 4, "Inflige 4 dégâts de feu et 2 dégâts de givre."),
    Spell("Glyphe réfléchissante", 4, "Chaque attaque de monstre inflige en retour 4 dégâts d'arcane."),
    Spell("Téléportation", 5, "Téléportation (hors combat) ou piocher trois sorts (combat)."),
    Spell("Blizzard éternel", 6, "Chaque phase, inflige 6 dégâts de givre à chaque monstre.")
]

sacred_spells = [
    Spell("Bouclier de protection", 1, "Augmente l'armure de 1 pour le combat."),
    Spell("Châtiment", 1, "Inflige 1 dégât de sacré. Soigne jusqu'à 1 point de vie."),
    Spell("Purification", 2, "Effet de purification (général)."),
    Spell("Infusion sacrée", 2, "Chaque attaque physique inflige 1 dégât de sacré supplémentaire."),
    Spell("Pénitence", 3, "Inflige 3 dégâts de sacré. Soigne jusqu'à 3 points de vie."),
    Spell("Fontaine sacrée", 3, "Augmente l'armure de 1, soigne 2 PV, et booste les stats du groupe."),
    Spell("Bouclier divin", 4, "Augmente l'armure de 4 pour le combat."),
    Spell("Barrière angélique", 4, "La prochaine mise hors de combat soigne 1 PV et booste l'armure."),
    Spell("Intervention lumineuse", 5, "Soigne tous les PV, mana et sorts. +3 armure."),
    Spell("Immunité divine", 6, "Joueur insensible pour la phase. +4 armure.")
]

chaos_spells = [
    Spell("Trait d'ombre", 1, "Inflige 2 dégâts de chaos."),
    Spell("Débilitation", 1, "Augmente le seuil de toucher d'un monstre de 1."),
    Spell("Toucher de faiblesse", 2, "Réduit la Force d'un monstre de 2."),
    Spell("Agonie", 2, "Inflige 2 dégâts de chaos par phase."),
    Spell("Drain d'âme", 3, "Réduit la Force du monstre de 2 et augmente celle du joueur de 2."),
    Spell("Flétrissement", 3, "Réduit la Vigueur d'un monstre de 3."),
    Spell("Armure nécrotique", 4, "Augmente l'armure de 1. Attaques monstres augmentent votre Force."),
    Spell("Nuage toxique", 4, "Réduit Force et Vigueur de chaque monstre de 4."),
    Spell("Hypnose", 5, "Réduit la Force du monstre de 5 par attaque et inflige 5 dégâts."),
    Spell("Domination funeste", 6, "Réduit la Force et la Vigueur d'un monstre de 6.")
]

nature_spells = [
    Spell("Toucher de la nature", 1, "Augmente la Force de 1 et soigne 2 PV."),
    Spell("Appel de la nature", 1, "Chaque attaque de monstre augmente la Force des joueurs de 2."),
    Spell("Trait de foudre", 2, "Inflige 3 dégâts de nature et augmente la Force de 2."),
    Spell("Sauvagerie", 2, "Augmente la Force d'un joueur de 2."),
    Spell("Précision féline", 3, "Réduit le seuil de toucher des dés de 1."),
    Spell("Endurance farouche", 3, "Augmente la Vigueur d'un joueur de 5."),
    Spell("Croissance sauvage", 4, "Augmente la Force d'un joueur de 5."),
    Spell("Sarments épineux", 4, "Inflige 4 dégâts aux monstres qui attaquent ou utilisent des capacités."),
    Spell("Tempête", 5, "Expulse les monstres d'une région et inflige 5 dégâts."),
    Spell("Invocation sylvaine", 6, "Augmente la Force et la Vigueur d'un joueur de 6.")
]

schools = {
    "1": ("Sort d'arcane", arcane_spells),
    "2": ("Sort de sacré", sacred_spells),
    "3": ("Sort de chaos", chaos_spells),
    "4": ("Sort de nature", nature_spells)
}

def draw_spells():
    print("--- Sélection de Sort ---")
    print("1: Sort d'arcane\n2: Sort de sacré\n3: Sort de chaos\n4: Sort de nature")
    choice = input("Choisissez une école de magie (1-4): ")

    if choice not in schools:
        print("Choix invalide.")
        return

    school_name, spell_list = schools[choice]
    
    try:
        count = int(input("Combien de sorts voulez-vous tirer ? "))
    except ValueError:
        print("Veuillez entrer un nombre valide.")
        return

    # Create a weighted list based on spell frequency
    weighted_pool = []
    for spell in spell_list:
        weighted_pool.extend([spell] * spell.frequency)

    # Pick the spells
    if count > len(weighted_pool):
        print(f"Demande trop élevée. Il n'y a que {len(spell_list)} sorts différents disponibles.")
        count = len(spell_list)

    # Using random.sample on the weighted pool might pick the same spell twice if frequency > 1
    # To ensure distinct spells (if desired), we pick from the unique list using weights
    selected = random.choices(
        spell_list, 
        weights=[s.frequency for s in spell_list], 
        k=count
    )

    print(f"\n--- Sorts tirés pour l'école {school_name} ---")
    for i, spell in enumerate(selected, 1):
        print(f"{i}. {spell}")

if __name__ == "__main__":
    draw_spells()
