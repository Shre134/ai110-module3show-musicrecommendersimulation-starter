import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """Represents a song and its attributes."""
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """Represents a user's taste preferences."""
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """OOP implementation of the recommendation logic."""
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Return the top-k Song objects for this user."""
        song_dicts = [{k: getattr(s, k) for k in s.__dataclass_fields__} for s in self.songs]
        prefs = {
            "genre": user.favorite_genre,
            "mood": user.favorite_mood,
            "energy": user.target_energy,
            "likes_acoustic": user.likes_acoustic,
        }
        results = recommend_songs(prefs, song_dicts, k=k)
        title_map = {s.title: s for s in self.songs}
        return [title_map[r[0]["title"]] for r in results]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Return a plain-language explanation for why this song was recommended."""
        prefs = {
            "genre": user.favorite_genre,
            "mood": user.favorite_mood,
            "energy": user.target_energy,
            "likes_acoustic": user.likes_acoustic,
        }
        song_dict = {k: getattr(song, k) for k in song.__dataclass_fields__}
        _, reasons = score_song(prefs, song_dict)
        return "; ".join(reasons) if reasons else "No strong match found."


def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file and return a list of dicts with typed values."""
    songs = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            songs.append({
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": float(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            })
    return songs


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score a single song against user preferences and return (score, reasons)."""
    score = 0.0
    reasons = []

    if song["genre"].lower() == user_prefs.get("genre", "").lower():
        score += 2.0
        reasons.append("genre match (+2.0)")

    if song["mood"].lower() == user_prefs.get("mood", "").lower():
        score += 1.5
        reasons.append("mood match (+1.5)")

    user_energy = float(user_prefs.get("energy", 0.5))
    energy_score = round(1.0 - abs(user_energy - song["energy"]), 3)
    score += energy_score
    reasons.append(f"energy proximity (+{energy_score})")

    if user_prefs.get("likes_acoustic"):
        if song["acousticness"] >= 0.6:
            score += 0.5
            reasons.append("acoustic match (+0.5)")
    else:
        if song["acousticness"] <= 0.3:
            score += 0.3
            reasons.append("produced sound match (+0.3)")

    return round(score, 3), reasons


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Score all songs, sort by score descending, and return the top k results."""
    scored = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        scored.append((song, score, "; ".join(reasons)))
    scored.sort(key=lambda x: -x[1])
    return scored[:k]