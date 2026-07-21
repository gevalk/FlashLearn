import sqlite3
import json

db_path = input("Pad naar collection.anki2: ").strip().strip('"')

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("SELECT flds FROM notes")

rows = cursor.fetchall()

print(f"Aantal kaarten gevonden: {len(rows)}")

for row in rows[:10]:
   flashcards = []

for row in rows:
    velden = row[0].split("\x1f")

    vraag = velden[0]
    antwoord = velden[1]

    flashcards.append({
        "question": vraag,
        "answer": antwoord
    })

with open("flashcards.json", "w", encoding="utf-8") as f:
    json.dump(flashcards, f, indent=4, ensure_ascii=False)

conn.close()