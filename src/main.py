"""
Command line runner for the Music Recommender Simulation.
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded {len(songs)} songs.\n")

    profiles = [
        {
            "name": "High-Energy Pop",
            "prefs": {"genre": "pop", "mood": "happy", "energy": 0.9}
        },
        {
            "name": "Chill Lofi",
            "prefs": {"genre": "lofi", "mood": "chill", "energy": 0.35, "likes_acoustic": True}
        },
        {
            "name": "Deep Intense Rock",
            "prefs": {"genre": "rock", "mood": "intense", "energy": 0.95}
        },
        {
            "name": "Edge Case: High Energy but Sad",
            "prefs": {"genre": "ambient", "mood": "sad", "energy": 0.9}
        },
    ]

    for profile in profiles:
        print("=" * 50)
        print(f"Profile: {profile['name']}")
        print(f"Preferences: {profile['prefs']}\n")
        recommendations = recommend_songs(profile["prefs"], songs, k=5)
        for i, (song, score, explanation) in enumerate(recommendations, start=1):
            print(f"  #{i} {song['title']} by {song['artist']}")
            print(f"      Score : {score}")
            print(f"      Why   : {explanation}")
        print()


if __name__ == "__main__":
    main()