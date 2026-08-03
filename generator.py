"""Non-interactive character generation logic.

Refactored from the original character_maker.py CLI script: same underlying
rules (species -> race/gender/age/height/name), but every choice is driven
by an `options` dict instead of input() prompts, so it can be called from a
web request. Also adds appearance and personality generation, and fills in
Dwarf/Demon (which were incomplete/stubbed in the original CLI script).
"""

import random
from pathlib import Path

import data

BASE_DIR = Path(__file__).resolve().parent


class CharacterGenerationError(ValueError):
    """Raised when the supplied options can't produce a valid character."""


def _load_names(filename):
    path = BASE_DIR / filename
    with path.open('r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]


def _pick_species(options):
    species = options.get('species', 'random')
    if species == 'random':
        return random.choice(data.SPECIES)
    if species not in data.SPECIES_DATA:
        raise CharacterGenerationError(f'Unknown species: {species}')
    return species


def _pick_race(options, species_config):
    race = options.get('race', 'random')
    if race == 'random' or not race:
        return random.choice(species_config['races'])
    return race


def _pick_gender(options):
    gender = options.get('gender', 'random')
    if gender == 'random' or not gender:
        return random.choice(data.GENDERS)
    if gender not in data.GENDERS:
        raise CharacterGenerationError(f'Unknown gender: {gender}')
    return gender


def _pick_age(options, species_config):
    age_mode = options.get('age_mode', 'random')
    if age_mode == 'exact':
        try:
            return int(options['age_value'])
        except (KeyError, TypeError, ValueError):
            raise CharacterGenerationError('age_value must be an integer when age_mode is exact')

    age_range = species_config['age_range']
    category = options.get('age_category', 'random')
    if category == 'random' or not category:
        category = random.choice(list(age_range.keys()))
    if category not in age_range:
        raise CharacterGenerationError(f'Unknown age category: {category}')
    low, high = age_range[category]
    return random.randint(low, high)


def _pick_height(options, species_config):
    height_mode = options.get('height_mode', 'random')
    if height_mode == 'exact':
        try:
            return int(options['height_value'])
        except (KeyError, TypeError, ValueError):
            raise CharacterGenerationError('height_value must be an integer (inches) when height_mode is exact')

    height_range = species_config['height_range']
    category = options.get('height_category', 'random')
    if category == 'random' or not category:
        category = random.choice(list(height_range.keys()))
    if category not in height_range:
        raise CharacterGenerationError(f'Unknown height category: {category}')
    low, high = height_range[category]
    return random.randint(low, high)


def _pick_name(options, species_config, gender):
    name_mode = options.get('name_mode', 'random')
    if name_mode == 'exact':
        name_value = options.get('name_value', '').strip()
        if not name_value:
            raise CharacterGenerationError('name_value must be provided when name_mode is exact')
        return name_value

    name_files = species_config['name_files']
    first_name_file = name_files.get(gender)
    if first_name_file is None:
        # Fall back to whichever first-name list exists for a non-binary gender choice.
        first_name_file = next(iter(name_files.values()))
    first_names = _load_names(first_name_file)
    surnames = _load_names(name_files['surname'])
    return f'{random.choice(first_names)} {random.choice(surnames)}'


def _manual_or_random(manual_value, choices):
    if manual_value and str(manual_value).strip():
        return str(manual_value).strip()
    return random.choice(choices)


def height_to_feet_inches(height_in_inches):
    feet = height_in_inches // 12
    inches = height_in_inches % 12
    return f'{feet} feet {inches} inches'


def generate_character(options=None):
    """Generate a single character from an options dict.

    Any field left out (or set to 'random') is randomized. Recognized keys:
    species, race, gender, age_mode/age_category/age_value,
    height_mode/height_category/height_value, name_mode/name_value,
    include_appearance, include_personality.
    """
    options = options or {}

    species = _pick_species(options)
    species_config = data.SPECIES_DATA[species]

    race = _pick_race(options, species_config)
    gender = _pick_gender(options)
    age = _pick_age(options, species_config)
    height_inches = _pick_height(options, species_config)
    name = _pick_name(options, species_config, gender)

    character = {
        'species': species,
        'race': race,
        'gender': gender,
        'age': age,
        'height_inches': height_inches,
        'height': height_to_feet_inches(height_inches),
        'name': name,
    }

    if options.get('include_appearance', True):
        character['hair_color'] = _manual_or_random(options.get('hair_color'), data.HAIR_COLORS[species])
        character['eye_color'] = _manual_or_random(options.get('eye_color'), data.EYE_COLORS[species])
        character['skin_tone'] = _manual_or_random(options.get('skin_tone'), data.SKIN_TONES[species])
        character['build'] = _manual_or_random(options.get('build'), data.BUILDS)

    if options.get('include_personality', True):
        character['personality_trait'] = _manual_or_random(options.get('personality_trait'), data.PERSONALITY_TRAITS)
        character['quirk'] = _manual_or_random(options.get('quirk'), data.QUIRKS)

    return character
