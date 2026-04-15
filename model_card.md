# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

GrooveGuide 1.0



## 2. Intended Use  

GrooveGuide tries to figure out which songs in a catalog best match what a user is in the mood for. You give it a genre, a mood, and an energy level, and it scores every song against those preferences and returns the top five. It doesn't learn from feedback or change over time,  it just runs the same scoring logic every time.



---

## 3. How the Model Works  

The catalog has 10 songs with features like genre, mood, energy, valence, danceability, and acousticness. It covers genres like pop, lofi, rock, jazz, ambient, and synthwave, and moods like happy, chill, intense, and relaxed. The main gap is diversity,  everything in the catalog is Western popular music, so users who prefer hip-hop, classical, country, or music from outside the English-speaking world won't get good results.




---

## 4. Data  

The system goes through every song and adds up points based on how well it matches the user. A genre match is worth the most, a mood match is worth a bit less, and energy gets a sliding score based on how close the song's energy is to what the user wants. The song with the highest total score gets recommended first. It's basically a checklist with point values, no machine learning, just weighted math.



---

## 5. Strengths  

The biggest issue is that the system never admits it doesn't know. Every song scores above zero no matter what, so it always returns five results even when none of them are actually a good fit. Genre matching is also all-or-nothing — pop and indie pop are treated as completely unrelated even though they'd sit next to each other on any real playlist. And because the catalog is so small, some songs win just because they're the only representative of their genre, not because they're genuinely a good match.


---

## 6. Limitations and Bias 

The system has three main biases. Genre matching is all-or-nothing, so "indie pop" and "pop" are treated as completely different even though they're closely related. The small 10-song catalog means some genres have only one representative, so it wins by default rather than true fit. Finally, every song scores above zero even with no matches, so the system always returns results even when none are actually good.

---

## 7. Evaluation  

Four profiles were tested: High-Energy Pop, Chill Lofi, Deep Intense Rock, and a deliberately broken edge case with conflicting preferences. The first three worked well and returned intuitive results. The edge case was the most interesting — someone who wanted sad ambient music at high energy got back Storm Runner and Gym Hero, because the catalog had nothing that actually fit and the system just picked the least-wrong options without flagging that anything was off.


---

## 8. Future Work  

The most useful next step would be teaching the system that genres can be related — right now pop and indie pop are strangers, which loses a lot of good matches. I'd also add a way for the system to just say "I don't have anything good for you" instead of always returning five results no matter what. Beyond that, the catalog needs to grow a lot, especially outside Western music, because right now a huge portion of what people actually listen to doesn't exist in this system at all.

## 9. Personal Reflection  

 I went in thinking the algorithm was the hard part. It wasn't — the catalog was. No scoring logic can recommend a song that isn't there. The other thing that surprised me was how the system looked equally confident whether it was right or completely wrong. The edge case profile got terrible results presented in the exact same clean format as the good ones. That made me think differently about how much I trust recommendations from real apps.