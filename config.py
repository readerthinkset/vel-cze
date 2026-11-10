"""VELOCITY CZECH - language pack, brand and motion design constants."""

import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

OUTPUT_DIR = BASE_DIR / "output"
LESSONS_DIR = OUTPUT_DIR / "lessons"
HISTORY_DIR = OUTPUT_DIR / "history"
SCENE_DIR = BASE_DIR / "scene"

VIDEO_WIDTH = 1080
VIDEO_HEIGHT = 1920
FPS = 30

# ---------------------------------------------------------------- brand

BRAND = "VELOCITY CZECH"
BRAND_LOCKUP_TOP = "VELOCITY"
BRAND_LOCKUP_BOTTOM = "CZECH"
HANDLE = "@velocityczech"
MASCOT_NAME = "Velo"

# ==== LANGUAGE PACK START ====
LANGUAGE = {
    "code": "cs",
    "name": "Czech",
    "native_name": "Čeština",
    "history_key": "czech",
    "english_voice": "en-US-AvaNeural",
    "english_fallback_voice": "en-US-GuyNeural",
    "native_voice": "cs-CZ-AntoninNeural",
    "native_fallback_voice": "cs-CZ-VlastaNeural",
    "native_engine": "edge",
    "native_lang_code": "cs",
    "english_rate": "-2%",
    "native_rate": "-6%",
    "english_pitch": "+0Hz",
    "native_pitch": "+0Hz",
    "native_label": "ČEŠTINA",
    "translit_label": "SAY IT LIKE",
    "greeting": "Ahoj!",
    "encouragement": "Výborně!",
    "rtl": False,
    "char_tiles": False,
    "script_font": "",
}
# ==== LANGUAGE PACK END ====

AI_MODEL = os.getenv("AI_MODEL", "gemini-fast")
POLLINATIONS_API_KEY = os.getenv("POLLINATIONS_API_KEY", "")

# ---------------------------------------------------------------- timing (seconds)

INTRO_DURATION = 4.0
OUTRO_DURATION = 5.2
EN_CARD_IN = 0.55
GAP_EN_NATIVE = 0.5
NATIVE_CARD_LEAD = 0.35
GAP_BEFORE_REPEAT = 0.8
TAIL_HOLD = 1.4
MAX_REEL_DURATION = 88.0

# ---------------------------------------------------------------- palette

INK = "#3C3C3C"
MUTED = "#8A8A8A"
CREAM = "#FFF8E7"
GREEN = "#58CC02"
GREEN_DARK = "#46A302"
GREEN_DEEP = "#3D8F00"
BLUE = "#1CB0F6"
PURPLE = "#A560E8"
ORANGE = "#FF7A00"
RED = "#FF4B4B"
YELLOW = "#F5A700"
TEAL = "#00A889"
PINK = "#E056A0"

PALETTE = [GREEN, BLUE, PURPLE, ORANGE, RED, YELLOW, TEAL, PINK]

# ---------------------------------------------------------------- categories
# (english, native, icon, accent)

# ==== CATEGORY TABLE START ====
CATEGORY_TABLE = [
    ("Greetings", "Pozdravy", "hand", "#1CB0F6"),
    ("Basic Phrases", "Základní Fráze", "chat", "#58CC02"),
    ("Common Expressions", "Běžné Výrazy", "chat", "#1CB0F6"),
    ("Travel", "Cestování", "plane", "#1CB0F6"),
    ("Restaurant", "Restaurace", "fork", "#FF7A00"),
    ("Shopping", "Nakupování", "bag", "#E056A0"),
    ("Emergency", "Nouzové Situace", "siren", "#FF4B4B"),
    ("Family Terms", "Rodinné Výrazy", "heart", "#E056A0"),
    ("Numbers", "Čísla", "hash", "#A560E8"),
    ("Time", "Čas", "clock", "#00A889"),
    ("Motivation", "Motivace", "rocket", "#A560E8"),
    ("Love", "Láska", "heart", "#FF4B4B"),
    ("Success", "Úspěch", "trophy", "#F5A700"),
    ("Wisdom", "Moudrost", "book", "#A560E8"),
    ("Happiness", "Štěstí", "smile", "#F5A700"),
    ("Self Improvement", "Sebezdokonalování", "leaf", "#58CC02"),
    ("Gratitude", "Vděčnost", "heart", "#FF7A00"),
    ("Friendship", "Přátelství", "users", "#00A889"),
    ("Hope", "Naděje", "sun", "#FF7A00"),
    ("Creativity", "Kreativita", "palette", "#E056A0"),
    ("Inner Peace", "Vnitřní Klid", "lotus", "#00A889"),
    ("Confidence", "Sebedůvěra", "shield", "#1CB0F6"),
    ("Perseverance", "Vytrvalost", "mountain", "#FF7A00"),
    ("Inspiration", "Inspirace", "sparkles", "#A560E8"),
    ("Positive Life", "Pozitivní Život", "sun", "#58CC02"),
    ("Courage", "Odvaha", "shield", "#FF4B4B"),
    ("Kindness", "Laskavost", "heart", "#E056A0"),
    ("Patience", "Trpělivost", "hourglass", "#00A889"),
    ("Forgiveness", "Odpuštění", "hands", "#FF7A00"),
    ("Strength", "Síla", "dumbbell", "#FF4B4B"),
    ("Joy", "Radost", "smile", "#F5A700"),
    ("Balance", "Rovnováha", "scale", "#00A889"),
    ("Growth", "Růst", "sprout", "#58CC02"),
    ("Purpose", "Smysl", "target", "#A560E8"),
    ("Mindfulness", "Všímavost", "lotus", "#00A889"),
    ("Daily Routine", "Denní rutina", "calendar", "#1CB0F6"),
    ("Weather", "Počasí", "cloud", "#1CB0F6"),
    ("Feelings", "Pocity", "smile", "#E056A0"),
    ("Food", "Jídlo", "fork", "#FF7A00"),
    ("Health", "Zdraví", "heart", "#58CC02"),
    ("Work", "Práce", "briefcase", "#1CB0F6"),
    ("Technology", "Technologie", "chip", "#A560E8"),
    ("Nature", "Příroda", "leaf", "#58CC02"),
    ("Animals", "Zvířata", "paw", "#FF7A00"),
    ("Colors", "Barvy", "palette", "#E056A0"),
    ("Directions", "Směry", "compass", "#1CB0F6"),
    ("Body Parts", "Části těla", "hand", "#00A889"),
    ("Clothes", "Oblečení", "shirt", "#E056A0"),
    ("Music", "Hudba", "music", "#A560E8"),
    ("Sports", "Sport", "ball", "#FF7A00"),
    ("Holidays", "Svátky", "gift", "#FF4B4B"),
    ("Education", "Vzdělávání", "book", "#1CB0F6"),
    ("Culture", "Kultura", "globe", "#00A889"),
    ("Finance", "Finance", "coin", "#58CC02"),
    ("Relationships", "Vztahy", "users", "#E056A0"),
]
# ==== CATEGORY TABLE END ====

CATEGORIES = [c[0] for c in CATEGORY_TABLE]
CATEGORIES_NATIVE = {c[0]: c[1] for c in CATEGORY_TABLE}
CATEGORY_META = {c[0]: {"native": c[1], "icon": c[2], "accent": c[3]} for c in CATEGORY_TABLE}
MAX_RECENT_CATEGORIES = 25

# ==== HASHTAGS START ====
HASHTAGS = [
    "#learnczech",
    "#czechlessons",
    "#czechforbeginners",
    "#languagelearning",
    "#czechvocabulary",
    "#velocityczech",
    "#dailyczech",
    "#czech",
    "#learnlanguages",
    "#speakczech",
    "#bilingual",
    "#languagetips",
]
# ==== HASHTAGS END ====
