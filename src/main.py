"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded {len(songs)} songs.\n")

    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}
    print(f"Profile: {user_prefs}\n")

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("Top recommendations:\n")
    for i, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"  #{i} {song['title']} by {song['artist']}")
        print(f"      Score : {score}")
        print(f"      Why   : {explanation}")
        print()


if __name__ == "__main__":
    main()
