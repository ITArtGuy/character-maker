"""Flask web app for Character Maker.

Serves the character generator UI and a small JSON API backed by
generator.py / data.py. Saved characters persist to characters.json
next to this file so the gallery survives restarts.
"""

import json # import json for reading/writing the gallery file
import uuid # import uuid for generating unique IDs for saved characters
from datetime import datetime, timezone
from pathlib import Path # import Path for file path manipulations

from flask import Flask, jsonify, render_template, request # type: ignore

import data
import generator

BASE_DIR = Path(__file__).resolve().parent
GALLERY_FILE = BASE_DIR / 'characters.json'

app = Flask(__name__)


def _load_gallery():
    if not GALLERY_FILE.exists():
        return []
    with GALLERY_FILE.open('r', encoding='utf-8') as f:
        return json.load(f)


def _save_gallery(characters):
    with GALLERY_FILE.open('w', encoding='utf-8') as f:
        json.dump(characters, f, indent=2)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/options')
def api_options():
    """Everything the frontend needs to build the form dynamically."""
    species_options = {}
    for species, config in data.SPECIES_DATA.items():
        species_options[species] = {
            'races': config['races'],
            'age_categories': list(config['age_range'].keys()),
            'height_categories': list(config['height_range'].keys()),
        }
    return jsonify({
        'species': data.SPECIES,
        'genders': data.GENDERS,
        'species_options': species_options,
    })


@app.route('/api/generate', methods=['POST'])
def api_generate():
    options = request.get_json(silent=True) or {}
    try:
        character = generator.generate_character(options)
    except generator.CharacterGenerationError as exc:
        return jsonify({'error': str(exc)}), 400
    return jsonify(character)


@app.route('/api/gallery', methods=['GET'])
def api_gallery_list():
    return jsonify(_load_gallery())


@app.route('/api/gallery', methods=['POST'])
def api_gallery_save():
    character = request.get_json(silent=True)
    if not character or not isinstance(character, dict):
        return jsonify({'error': 'A character object is required.'}), 400

    gallery = _load_gallery()
    saved = dict(character)
    saved['id'] = uuid.uuid4().hex
    saved['saved_at'] = datetime.now(timezone.utc).isoformat()
    gallery.insert(0, saved)
    _save_gallery(gallery)
    return jsonify(saved), 201


@app.route('/api/gallery/<character_id>', methods=['DELETE'])
def api_gallery_delete(character_id):
    gallery = _load_gallery()
    remaining = [c for c in gallery if c.get('id') != character_id]
    if len(remaining) == len(gallery):
        return jsonify({'error': 'Character not found.'}), 404
    _save_gallery(remaining)
    return '', 204


if __name__ == '__main__':
    app.run(debug=True, port=5000)
