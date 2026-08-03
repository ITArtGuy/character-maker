let optionsData = null;
let currentCharacter = null;

const speciesSelect = document.getElementById('species');
const raceSelect = document.getElementById('race');
const genderSelect = document.getElementById('gender');
const ageCategorySelect = document.getElementById('age_category');
const ageValueInput = document.getElementById('age_value');
const heightCategorySelect = document.getElementById('height_category');
const heightValueInput = document.getElementById('height_value');
const nameValueInput = document.getElementById('name_value');
const includeAppearance = document.getElementById('include_appearance');
const includePersonality = document.getElementById('include_personality');
const appearanceOptions = document.getElementById('appearance-options');
const appearanceManualFields = document.getElementById('appearance-manual-fields');
const personalityOptions = document.getElementById('personality-options');
const personalityManualFields = document.getElementById('personality-manual-fields');
const hairColorInput = document.getElementById('hair_color');
const eyeColorInput = document.getElementById('eye_color');
const skinToneInput = document.getElementById('skin_tone');
const buildInput = document.getElementById('build');
const personalityTraitInput = document.getElementById('personality_trait');
const quirkInput = document.getElementById('quirk');

const form = document.getElementById('generate-form');
const resultEmpty = document.getElementById('result-empty');
const resultCard = document.getElementById('result-card');
const resultActions = document.getElementById('result-actions');
const saveBtn = document.getElementById('save-btn');
const regenerateBtn = document.getElementById('regenerate-btn');

const galleryEmpty = document.getElementById('gallery-empty');
const galleryList = document.getElementById('gallery-list');

function fillSelect(select, values, { includeRandom = true } = {}) {
  select.innerHTML = '';
  if (includeRandom) {
    const opt = document.createElement('option');
    opt.value = 'random';
    opt.textContent = 'Random';
    select.appendChild(opt);
  }
  for (const value of values) {
    const opt = document.createElement('option');
    opt.value = value;
    opt.textContent = value;
    select.appendChild(opt);
  }
}

function refreshDependentFields() {
  const species = speciesSelect.value;
  const config = optionsData.species_options[species];

  if (!config) {
    // "Random" species selected: race/age/height categories are pooled across all species.
    fillSelect(raceSelect, []);
    fillSelect(ageCategorySelect, ['Minor', 'Adult', 'Elderly']);
    fillSelect(heightCategorySelect, ['Short', 'Average', 'Tall']);
    return;
  }

  fillSelect(raceSelect, config.races);
  fillSelect(ageCategorySelect, config.age_categories);
  fillSelect(heightCategorySelect, config.height_categories);
}

function setupModeToggle(radioName, targets, onValue = 'exact') {
  const radios = document.querySelectorAll(`input[name="${radioName}"]`);
  radios.forEach((radio) => {
    radio.addEventListener('change', () => {
      const isOn = document.querySelector(`input[name="${radioName}"]:checked`).value === onValue;
      targets.forEach(({ exact, random }) => {
        exact.classList.toggle('hidden', !isOn);
        if (random) random.classList.toggle('hidden', isOn);
      });
    });
  });
}

function setupIncludeToggle(checkbox, optionsContainer) {
  checkbox.addEventListener('change', () => {
    optionsContainer.classList.toggle('hidden', !checkbox.checked);
  });
}

async function loadOptions() {
  const res = await fetch('/api/options');
  optionsData = await res.json();
  fillSelect(speciesSelect, optionsData.species);
  fillSelect(genderSelect, optionsData.genders);
  refreshDependentFields();
}

function buildRequestOptions() {
  const ageMode = document.querySelector('input[name="age_mode"]:checked').value;
  const heightMode = document.querySelector('input[name="height_mode"]:checked').value;
  const nameMode = document.querySelector('input[name="name_mode"]:checked').value;
  const appearanceMode = document.querySelector('input[name="appearance_mode"]:checked').value;
  const personalityMode = document.querySelector('input[name="personality_mode"]:checked').value;

  return {
    species: speciesSelect.value,
    race: raceSelect.value || 'random',
    gender: genderSelect.value,
    age_mode: ageMode,
    age_category: ageCategorySelect.value,
    age_value: ageValueInput.value,
    height_mode: heightMode,
    height_category: heightCategorySelect.value,
    height_value: heightValueInput.value,
    name_mode: nameMode,
    name_value: nameValueInput.value,
    include_appearance: includeAppearance.checked,
    hair_color: appearanceMode === 'manual' ? hairColorInput.value : '',
    eye_color: appearanceMode === 'manual' ? eyeColorInput.value : '',
    skin_tone: appearanceMode === 'manual' ? skinToneInput.value : '',
    build: appearanceMode === 'manual' ? buildInput.value : '',
    include_personality: includePersonality.checked,
    personality_trait: personalityMode === 'manual' ? personalityTraitInput.value : '',
    quirk: personalityMode === 'manual' ? quirkInput.value : '',
  };
}

function renderCharacterCard(container, character) {
  const traits = [
    ['Species', character.species],
    ['Race', character.race],
    ['Gender', character.gender],
    ['Age', character.age],
    ['Height', character.height],
  ];

  if (character.hair_color) {
    traits.push(['Hair', character.hair_color], ['Eyes', character.eye_color],
      ['Skin', character.skin_tone], ['Build', character.build]);
  }

  const traitHtml = traits.map(([label, value]) => `
    <div class="trait"><strong>${label}</strong>${value}</div>
  `).join('');

  const quirkHtml = character.personality_trait
    ? `<div class="quirk-line"><strong>${character.personality_trait}.</strong> ${character.quirk}</div>`
    : '';

  container.innerHTML = `
    <h3>${character.name}</h3>
    <p class="subtitle">${character.race} ${character.species} &middot; ${character.gender}</p>
    <div class="trait-grid">${traitHtml}</div>
    ${quirkHtml}
  `;
}

function renderGallery(characters) {
  galleryList.innerHTML = '';
  galleryEmpty.classList.toggle('hidden', characters.length > 0);

  for (const character of characters) {
    const card = document.createElement('div');
    card.className = 'gallery-card';
    card.innerHTML = `
      <button class="delete-btn" title="Remove">&times;</button>
      <h4>${character.name}</h4>
      <p>${character.race} ${character.species} &middot; ${character.gender}</p>
      <p>${character.age} yrs &middot; ${character.height}</p>
      ${character.hair_color ? `<p>${character.hair_color} hair, ${character.eye_color} eyes</p>` : ''}
      ${character.personality_trait ? `<p><em>${character.personality_trait}</em></p>` : ''}
    `;
    card.querySelector('.delete-btn').addEventListener('click', () => deleteFromGallery(character.id));
    galleryList.appendChild(card);
  }
}

async function loadGallery() {
  const res = await fetch('/api/gallery');
  const characters = await res.json();
  renderGallery(characters);
}

async function deleteFromGallery(id) {
  await fetch(`/api/gallery/${id}`, { method: 'DELETE' });
  loadGallery();
}

async function generateCharacter() {
  const res = await fetch('/api/generate', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(buildRequestOptions()),
  });

  if (!res.ok) {
    const err = await res.json().catch(() => ({ error: 'Something went wrong.' }));
    alert(err.error || 'Something went wrong.');
    return;
  }

  currentCharacter = await res.json();
  resultEmpty.classList.add('hidden');
  resultCard.classList.remove('hidden');
  resultActions.classList.remove('hidden');
  renderCharacterCard(resultCard, currentCharacter);
}

form.addEventListener('submit', (event) => {
  event.preventDefault();
  generateCharacter();
});

regenerateBtn.addEventListener('click', generateCharacter);

saveBtn.addEventListener('click', async () => {
  if (!currentCharacter) return;
  await fetch('/api/gallery', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(currentCharacter),
  });
  loadGallery();
});

speciesSelect.addEventListener('change', refreshDependentFields);

setupModeToggle('age_mode', [{ exact: ageValueInput, random: ageCategorySelect }]);
setupModeToggle('height_mode', [{ exact: heightValueInput, random: heightCategorySelect }]);
setupModeToggle('name_mode', [{ exact: nameValueInput }]);
setupModeToggle('appearance_mode', [{ exact: appearanceManualFields }], 'manual');
setupModeToggle('personality_mode', [{ exact: personalityManualFields }], 'manual');
setupIncludeToggle(includeAppearance, appearanceOptions);
setupIncludeToggle(includePersonality, personalityOptions);

(async function init() {
  await loadOptions();
  await loadGallery();
})();
