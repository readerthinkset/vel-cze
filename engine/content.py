"""AI phrase generation with permanent no-repeat history."""

from __future__ import annotations

import json
import random
import time
from datetime import datetime

import requests

import config
from config import CATEGORIES, CATEGORIES_NATIVE, HISTORY_DIR, MAX_RECENT_CATEGORIES

PHRASE_HISTORY_FILE = HISTORY_DIR / "all_generated_phrases.json"
RECENT_CATEGORIES_FILE = HISTORY_DIR / "recent_categories.json"

PHRASE_KEY = config.LANGUAGE["history_key"]
LANGUAGE_NAME = config.LANGUAGE["name"]
NATIVE_NAME = config.LANGUAGE["native_name"]

# ==== FALLBACK PHRASES START ====
FALLBACK_PHRASES = [
    {"english": "Hello, nice to meet you.", "native": "Dobrý den, těší mě.", "transliteration": "Dobry den, teshi me."},
    {"english": "Thank you very much.", "native": "Děkuji mnohokrát.", "transliteration": "Dekuji mnohokrat."},
    {"english": "Good morning, have a great day.", "native": "Dobré ráno, přeji krásný den.", "transliteration": "Dobre rano, preji krasny den."},
    {"english": "I love learning new languages.", "native": "Miluji učení se novým jazykům.", "transliteration": "Miluji uceni se novym jazykum."},
    {"english": "Never give up on your dreams.", "native": "Nikdy se nevzdávejte svých snů.", "transliteration": "Nikdy se nevzdavejte svych snu."},
    {"english": "Every day is a fresh start.", "native": "Každý den je nový začátek.", "transliteration": "Kazdy den je novy zacatek."},
    {"english": "Believe in yourself always.", "native": "Vždy věřte v sebe.", "transliteration": "Vzdy verte v sebe."},
    {"english": "Small steps lead to big changes.", "native": "Malé kroky vedou k velkým změnám.", "transliteration": "Male kroky vedou k velkym zmenam."},
    {"english": "You are stronger than you think.", "native": "Jste silnější, než si myslíte.", "transliteration": "Jste silnejsi, nez si myslite."},
    {"english": "Happiness is a choice, choose it.", "native": "Štěstí je volba, zvolte si ho.", "transliteration": "Stesti je volba, zvolte si ho."},
    {"english": "What time is it please.", "native": "Kolik je hodin, prosím?", "transliteration": "Kolik je hodin, prosim?"},
    {"english": "Where is the train station.", "native": "Kde je nádraží?", "transliteration": "Kde je nadrazi?"},
    {"english": "How much does this cost.", "native": "Kolik to stojí?", "transliteration": "Kolik to stoji?"},
    {"english": "Can you help me please.", "native": "Můžete mi prosím pomoci?", "transliteration": "Muzete mi prosim pomoci?"},
    {"english": "I would like a coffee please.", "native": "Dal bych si kávu, prosím.", "transliteration": "Dal bych si kavu, prosim."},
    {"english": "The food is delicious today.", "native": "Jídlo je dnes vynikající.", "transliteration": "Jidlo je dnes vynikajici."},
    {"english": "Have a wonderful weekend.", "native": "Přeji Vám krásný víkend.", "transliteration": "Preji Vam krasny vikend."},
    {"english": "Take care of yourself.", "native": "Pečujte o sebe.", "transliteration": "Pecujte o sebe."},
    {"english": "See you tomorrow my friend.", "native": "Uvidíme se zítra, příteli.", "transliteration": "Uvidime se zitra, príteli."},
    {"english": "The weather is beautiful outside.", "native": "Venku je krásné počasí.", "transliteration": "Venku je krasne pocasi."},
    {"english": "I am very happy today.", "native": "Dnes mám velkou radost.", "transliteration": "Dnes mam velkou radost."},
    {"english": "Learning a language opens new doors.", "native": "Učení jazyků otevírá nové dveře.", "transliteration": "Uceni jazyku otevira nove dvere."},
    {"english": "Keep practicing every single day.", "native": "Procvičujte se každý den.", "transliteration": "Procvičujte se kazdy den."},
    {"english": "You can achieve anything you want.", "native": "Můžete dosáhnout čehokoli, co si přejete.", "transliteration": "Muzete dosahnout cehokoli, co si prejete."},
    {"english": "Rest when you are tired.", "native": "Odpočívejte, když jste unavení.", "transliteration": "Odpočívejte, kdyz jste unaveni."},
    {"english": "Focus on the positive things.", "native": "Soustřeďte se na pozitivní věci.", "transliteration": "Soustřeďte se na pozitivní věci."},
    {"english": "Learn from your mistakes.", "native": "Učte se ze svých chyb.", "transliteration": "Učte se ze svých chyb."},
    {"english": "Trust the process completely.", "native": "Plně důvěřujte procesu.", "transliteration": "Plně důvěřujte procesu."},
    {"english": "Breathe deeply and stay calm.", "native": "Zhluboka se nadechněte a zůstaňte klidní.", "transliteration": "Zhluboka se nadechněte a zůstaňte klidní."},
    {"english": "Enjoy the little moments in life.", "native": "Užívejte si malé okamžiky v životě.", "transliteration": "Užívejte si malé okamžiky v životě."},
    {"english": "Smile more, worry less.", "native": "Více se usmívejte, méně se obávejte.", "transliteration": "Více se usmívejte, méně se obávejte."},
    {"english": "Be kind to everyone you meet.", "native": "Buďte laskaví ke všem, které potkáte.", "transliteration": "Buďte laskaví ke všem, které potkáte."},
    {"english": "Help others without expecting anything back.", "native": "Pomáhejte druhým bez očekávání něčeho zpět.", "transliteration": "Pomáhejte druhým bez očekávání něčeho zpět."},
    {"english": "Forgive yourself and move forward.", "native": "Odpusťte si a jděte dál.", "transliteration": "Odpusťte si a jděte dál."},
    {"english": "Stay strong in difficult times.", "native": "Zůstaňte silní v těžkých časech.", "transliteration": "Zůstaňte silní v těžkých časech."},
    {"english": "Every moment is a new beginning.", "native": "Každý okamžik je nový začátek.", "transliteration": "Každý okamžik je nový začátek."},
    {"english": "Listen to your heart always.", "native": "Vždy poslouchejte své srdce.", "transliteration": "Vždy poslouchejte své srdce."},
    {"english": "Do what makes you happy.", "native": "Dělejte to, co vás dělá šťastnými.", "transliteration": "Dělejte to, co vás dělá šťastnými."},
    {"english": "Your potential is unlimited.", "native": "Váš potenciál je neomezený.", "transliteration": "Váš potenciál je neomezený."},
    {"english": "Be brave and take risks.", "native": "Buďte odvážní a podstupujte rizika.", "transliteration": "Buďte odvážní a podstupujte rizika."},
    {"english": "Celebrate your progress every day.", "native": "Oslavujte svůj pokrok každý den.", "transliteration": "Oslavujte svůj pokrok každý den."},
    {"english": "Surround yourself with good people.", "native": "Obklopte se dobrými lidmi.", "transliteration": "Obklopte se dobrými lidmi."},
    {"english": "Read books and grow your mind.", "native": "Čtěte knihy a rozšiřujte svou mysl.", "transliteration": "Čtěte knihy a rozšiřujte svou mysl."},
    {"english": "Travel and discover new places.", "native": "Cestujte a objevujte nová místa.", "transliteration": "Cestujte a objevujte nová místa."},
    {"english": "Appreciate what you already have.", "native": "Oceňte to, co už máte.", "transliteration": "Oceňte to, co už máte."},
    {"english": "Dance like nobody is watching.", "native": "Tancujte, jako by se nikdo nedíval.", "transliteration": "Tancujte, jako by se nikdo nedíval."},
    {"english": "Sing from your heart out loud.", "native": "Zpívejte z celého srdce nahlas.", "transliteration": "Zpívejte z celého srdce nahlas."},
    {"english": "Plant seeds of kindness everywhere.", "native": "Zasévejte semínka laskavosti všude.", "transliteration": "Zasévejte semínka laskavosti všude."},
    {"english": "Let go of what you cannot control.", "native": "Pusťte to, co nemůžete ovládat.", "transliteration": "Pusťte to, co nemůžete ovládat."},
    {"english": "Be present in the here and now.", "native": "Buďte přítomni v tady a teď.", "transliteration": "Buďte přítomni v tady a teď."},
]
# ==== FALLBACK PHRASES END ====


def _load_json(path, default):
    if path.exists():
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            pass
    return default


def _save_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def load_phrase_history():
    data = _load_json(PHRASE_HISTORY_FILE, {"phrases": [], "last_updated": None})
    data.setdefault("phrases", [])
    return data


def save_phrase_history(data):
    data["last_updated"] = datetime.now().isoformat()
    _save_json(PHRASE_HISTORY_FILE, data)


def is_phrase_used(english):
    english_lower = english.lower().strip()
    for p in load_phrase_history()["phrases"]:
        if p.get("english", "").lower().strip() == english_lower:
            return True
    return False


def _history_native(p):
    for key in (PHRASE_KEY, "vietnamese", "native", "translation", "target"):
        value = p.get(key)
        if value:
            return str(value)
    return ""


def add_phrases_to_history(phrases, category):
    history = load_phrase_history()
    for phrase in phrases:
        history["phrases"].append({
            "english": phrase["english"],
            PHRASE_KEY: phrase["native"],
            "transliteration": phrase.get("transliteration", ""),
            "category": category,
            "generated_at": datetime.now().isoformat(),
        })
    save_phrase_history(history)
    print(f"[content] Saved {len(phrases)} phrases (history total: {len(history['phrases'])})")


def get_available_category():
    data = _load_json(RECENT_CATEGORIES_FILE, {"recent_categories": [], "last_updated": None})
    recent = data.get("recent_categories", [])
    available = [c for c in CATEGORIES if c not in recent]
    if not available:
        recent = recent[-5:]
        available = [c for c in CATEGORIES if c not in recent]
        print("[rotation] Reset recent categories")
    selected = random.choice(available)
    recent.append(selected)
    data["recent_categories"] = recent[-MAX_RECENT_CATEGORIES:]
    data["last_updated"] = datetime.now().isoformat()
    _save_json(RECENT_CATEGORIES_FILE, data)
    print(f"[rotation] Category: {selected} ({len(available)} available)")
    return selected


def _normalize_phrase(item):
    if not isinstance(item, dict):
        return None
    english = str(item.get("english", "")).strip()
    native = str(
        item.get(PHRASE_KEY)
        or item.get("native")
        or item.get("vietnamese")
        or item.get("translation")
        or ""
    ).strip()
    translit = str(item.get("transliteration") or item.get("romanization") or item.get("romaji") or "").strip()
    if not english or not native:
        return None
    if len(english.split()) > 16:
        return None
    if "/" in native or "|" in native:
        native = native.split("/")[0].split("|")[0].strip()
    return {
        "english": english.replace("  ", " ").strip(),
        "native": native.strip(),
        "transliteration": translit.strip().strip("[]"),
    }


def _history_keys(history):
    used_en = set()
    used_nat = set()
    for p in history.get("phrases", []):
        en = str(p.get("english", "")).lower().strip()
        nat = _history_native(p).lower().strip()
        if en:
            used_en.add(en)
        if nat:
            used_nat.add(nat)
    return used_en, used_nat


def generate_phrases(category_english: str, num_phrases: int = 5) -> list:
    category_native = CATEGORIES_NATIVE[category_english]
    history = load_phrase_history()
    used_en, used_nat = _history_keys(history)
    recent_english = [
        p["english"] for p in history["phrases"] if p.get("category") == category_english
    ][-30:]

    models = [config.AI_MODEL]
    if "gemini-fast" not in models:
        models.append("gemini-fast")

    if config.POLLINATIONS_API_KEY:
        for attempt in range(5):
            model = models[0] if attempt < 3 else models[-1]
            try:
                phrases = _request_phrases(category_english, category_native, recent_english, num_phrases, attempt, model)
                unique = []
                for item in phrases:
                    p = _normalize_phrase(item)
                    if not p:
                        continue
                    key_en = p["english"].lower().strip()
                    key_nat = p["native"].lower().strip()
                    if key_en in used_en or key_nat in used_nat:
                        continue
                    if any(key_en == u["english"].lower().strip() for u in unique):
                        continue
                    used_en.add(key_en)
                    used_nat.add(key_nat)
                    unique.append(p)
                    if len(unique) >= num_phrases:
                        break
                if len(unique) >= num_phrases:
                    add_phrases_to_history(unique[:num_phrases], category_english)
                    return unique[:num_phrases]
                print(f"[content] Attempt {attempt + 1}: only {len(unique)} fresh phrases (need {num_phrases})")
            except Exception as exc:  # noqa: BLE001 - network boundary
                print(f"[content] Attempt {attempt + 1} failed ({model}): {exc}")
            time.sleep(1.5 * (attempt + 1))
    else:
        print("[content] No POLLINATIONS_API_KEY, using fallback phrases")

    fresh_fallback = []
    for p in FALLBACK_PHRASES:
        if p["english"].lower().strip() in used_en or p["native"].lower().strip() in used_nat:
            continue
        fresh_fallback.append(p)
    if not fresh_fallback:
        raise RuntimeError("Phrase API unavailable and no unused fallback phrases left; refusing to reuse phrases")
    chosen = fresh_fallback[:num_phrases]
    if len(chosen) < num_phrases:
        print(f"[content] Only {len(chosen)} fresh fallback phrases; building a shorter lesson")
    add_phrases_to_history(chosen, category_english)
    return chosen


def _request_phrases(category_english, category_native, recent_english, num_phrases, attempt, model=None):
    avoid = ""
    if recent_english:
        avoid = "\nDo NOT reuse any of these phrases:\n" + "\n".join(f"- {p}" for p in recent_english)

    prompt = f"""Create {num_phrases * 6} unique {category_english} phrases for English speakers learning {LANGUAGE_NAME}.
{avoid}

Rules:
1. Keep every phrase short and natural (4-11 words in English).
2. Use natural commas for TTS breathing pauses.
3. Each phrase must be speakable in 2-4 seconds.
4. Write clean {LANGUAGE_NAME} in {NATIVE_NAME} with correct accents and orthography. One translation only, no slashes.
5. Transliteration is a friendly Roman-script pronunciation guide for English speakers (not IPA).
6. Vary the sentence patterns and emotions. No duplicates.
7. Phrases must feel like real everyday language, not textbook filler.

Return ONLY a JSON array:
[{{"english": "...", "native": "...", "transliteration": "..."}}]"""

    response = requests.post(
        "https://gen.pollinations.ai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {config.POLLINATIONS_API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": model or config.AI_MODEL,
            "messages": [
                {"role": "system", "content": f"You are a {LANGUAGE_NAME} teacher creating short, natural, varied bilingual phrases. Reply with JSON only."},
                {"role": "user", "content": prompt},
            ],
            "temperature": min(0.95 + attempt * 0.02, 1.0),
        },
        timeout=90,
    )
    response.raise_for_status()
    content = response.json()["choices"][0]["message"]["content"].strip()

    if "```json" in content:
        content = content.split("```json", 1)[1].split("```", 1)[0].strip()
    elif "```" in content:
        content = content.split("```", 1)[1].split("```", 1)[0].strip()

    start = content.find("[")
    end = content.rfind("]")
    if start >= 0 and end > start:
        content = content[start:end + 1]

    data = json.loads(content)
    if not isinstance(data, list):
        raise ValueError("AI did not return a JSON array")
    return data
