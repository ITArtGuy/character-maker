"""Static data for the Character Maker app.

Holds species definitions (races, age ranges, height ranges, name file
mapping) plus appearance and personality option pools used by generator.py.
"""

GENDERS = ['Male', 'Female']

SPECIES = ['Human', 'Elf', 'Dwarf', 'Demon']

# ---------------------------------------------------------------------------
# Human
# ---------------------------------------------------------------------------
HUMAN_RACES = [
    'Black-American', 'White-American', 'Asian-American', 'Hispanic-American', 'Native American',
    'Pacific Islander', 'Middle Eastern', 'Japanese', 'Chinese', 'Korean', 'Indian', 'Filipino',
    'Vietnamese', 'German', 'French', 'Italian', 'British', 'Irish', 'Russian', 'Polish',
    'Scandinavian', 'African', 'Caribbean', 'Latin American', 'Egyptian', 'Arab', 'Persian',
    'Turkish', 'Jewish', 'Greek',
]
HUMAN_AGE_RANGE = {
    'Minor': (0, 17),
    'Adult': (18, 64),
    'Elderly': (65, 120),
}
HUMAN_HEIGHT_RANGE = {
    'Short': (40, 59),
    'Average': (60, 72),
    'Tall': (73, 96),
}

# ---------------------------------------------------------------------------
# Elf
# ---------------------------------------------------------------------------
ELF_RACES = ['High Elf', 'Wood Elf', 'Dark Elf']
ELF_AGE_RANGE = {
    'Minor': (0, 100),
    'Adult': (101, 500),
    'Elderly': (501, 1000),
}
ELF_HEIGHT_RANGE = {
    'Short': (36, 59),
    'Average': (60, 72),
    'Tall': (73, 128),
}

# ---------------------------------------------------------------------------
# Dwarf
# ---------------------------------------------------------------------------
DWARF_RACES = ['Mountain Dwarf', 'Hill Dwarf', 'Duergar']
DWARF_AGE_RANGE = {
    'Minor': (0, 100),
    'Adult': (101, 500),
    'Elderly': (501, 1000),
}
DWARF_HEIGHT_RANGE = {
    'Short': (32, 39),
    'Average': (40, 47),
    'Tall': (48, 56),
}

# ---------------------------------------------------------------------------
# Demon
# ---------------------------------------------------------------------------
DEMON_RACES = ['Balor', 'Incubus', 'Succubus']
DEMON_AGE_RANGE = {
    'Minor': (0, 100),
    'Adult': (101, 500),
    'Elderly': (501, 1000),
}
DEMON_HEIGHT_RANGE = {
    'Short': (36, 59),
    'Average': (60, 72),
    'Tall': (73, 128),
}

# ---------------------------------------------------------------------------
# Per-species config: races, ranges, and where to find name lists.
# ---------------------------------------------------------------------------
SPECIES_DATA = {
    'Human': {
        'races': HUMAN_RACES,
        'age_range': HUMAN_AGE_RANGE,
        'height_range': HUMAN_HEIGHT_RANGE,
        'name_files': {
            'Male': 'male_human_names.txt',
            'Female': 'female_human_names.txt',
            'surname': 'human_surnames.txt',
        },
    },
    'Elf': {
        'races': ELF_RACES,
        'age_range': ELF_AGE_RANGE,
        'height_range': ELF_HEIGHT_RANGE,
        'name_files': {
            'Male': 'male_elf_names.txt',
            'Female': 'female_elf_names.txt',
            'surname': 'elf_surnames.txt',
        },
    },
    'Dwarf': {
        'races': DWARF_RACES,
        'age_range': DWARF_AGE_RANGE,
        'height_range': DWARF_HEIGHT_RANGE,
        'name_files': {
            'Male': 'male_dwarf_names.txt',
            'Female': 'female_dwarf_names.txt',
            'surname': 'dwarf_surnames.txt',
        },
    },
    'Demon': {
        'races': DEMON_RACES,
        'age_range': DEMON_AGE_RANGE,
        'height_range': DEMON_HEIGHT_RANGE,
        'name_files': {
            'Male': 'male_demon_names.txt',
            'Female': 'female_demon_names.txt',
            'surname': 'demon_surnames.txt',
        },
    },
}

# ---------------------------------------------------------------------------
# Appearance traits, for quick visual reference when drawing.
# ---------------------------------------------------------------------------
HAIR_COLORS = {
    'Human': ['Black', 'Dark Brown', 'Brown', 'Light Brown', 'Auburn', 'Red', 'Strawberry Blonde',
               'Blonde', 'Platinum Blonde', 'Gray', 'Silver', 'White'],
    'Elf': ['Black', 'Silver', 'Platinum Blonde', 'White', 'Brown', 'Auburn', 'Moonlight Blue',
             'Forest Green', 'Violet', 'Copper'],
    'Dwarf': ['Black', 'Brown', 'Red', 'Auburn', 'Iron Gray', 'Gray', 'White'],
    'Demon': ['Black', 'Blood Red', 'Charcoal', 'Ash Gray', 'Crimson', 'Obsidian', 'White',
               'Violet', 'Midnight Blue'],
}

EYE_COLORS = {
    'Human': ['Brown', 'Hazel', 'Green', 'Blue', 'Gray', 'Amber'],
    'Elf': ['Green', 'Blue', 'Violet', 'Silver', 'Gold', 'Gray', 'Emerald'],
    'Dwarf': ['Brown', 'Black', 'Gray', 'Hazel', 'Deep Blue'],
    'Demon': ['Red', 'Black', 'Amber', 'Violet', 'Yellow', 'Crimson', 'Void Black'],
}

SKIN_TONES = {
    'Human': ['Fair', 'Light', 'Medium', 'Olive', 'Tan', 'Bronze', 'Brown', 'Dark Brown', 'Deep'],
    'Elf': ['Porcelain', 'Fair', 'Sun-Kissed', 'Golden', 'Deep Brown', 'Moon-Pale'],
    'Dwarf': ['Ruddy', 'Weathered Tan', 'Stone Gray', 'Deep Brown', 'Ashen'],
    'Demon': ['Ashen Gray', 'Charcoal Black', 'Crimson Red', 'Deep Violet', 'Sulfur Yellow', 'Obsidian'],
}

BUILDS = [
    'Slim', 'Lean', 'Athletic', 'Average', 'Stocky', 'Muscular', 'Heavyset',
    'Broad-Shouldered', 'Petite', 'Wiry',
]

# ---------------------------------------------------------------------------
# Personality traits and quirks, for quick character flavor.
# ---------------------------------------------------------------------------
PERSONALITY_TRAITS = [
    'Brave', 'Cautious', 'Cheerful', 'Cynical', 'Stoic', 'Reckless', 'Curious', 'Loyal',
    'Ambitious', 'Gentle', 'Fierce', 'Witty', 'Grumpy', 'Compassionate', 'Arrogant', 'Shy',
    'Bold', 'Calculating', 'Optimistic', 'Pessimistic', 'Mischievous', 'Honorable', 'Ruthless',
    'Kind', 'Aloof', 'Charming', 'Stubborn', 'Naive', 'Wise', 'Impulsive',
]

QUIRKS = [
    'Always carries a lucky trinket.',
    'Talks to animals as if they understand.',
    "Can't resist a bet or wager.",
    'Hums an old tune when nervous.',
    'Collects buttons from everyone they meet.',
    'Terrified of deep water.',
    'Never removes their gloves in public.',
    "Sketches strangers' faces on scrap paper.",
    "Refuses to eat anything green.",
    'Sleeps with one eye open.',
    "Keeps a running list of everyone who's wronged them.",
    'Speaks to their weapon like an old friend.',
    'Superstitious about the number thirteen.',
    "Can't walk past a mirror without checking their reflection.",
    'Chews on a twig or toothpick constantly.',
    'Insists on naming every mount, pet, or tool they own.',
    'Cracks their knuckles before any confrontation.',
    'Keeps a diary written in a private code.',
    "Has a habit of finishing others' sentences.",
    'Never sits with their back to a door.',
    'Hoards receipts and ticket stubs for no reason.',
    'Whistles when concentrating.',
    'Distrusts anyone who is too polite.',
    'Names their weapons but forgets people\'s names.',
    'Always sits closest to the exit.',
    'Flinches at loud applause.',
    'Overexplains simple decisions.',
    'Collects maps of places never visited.',
    'Taps out rhythms on any nearby surface.',
    'Refuses to travel without a specific object for luck.',
]
