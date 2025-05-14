import sqlite3

conn = sqlite3.connect('homework16b.db')
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS Students")
cur.execute("""
    CREATE TABLE Students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        grade INTEGER
    )
""")

students = [
    (1, 'Vasilisa', 85),
    (2, 'Will', 92),
    (3, 'Oleg', 78)
]
cur.executemany("INSERT INTO Students VALUES (?, ?, ?)", students)
conn.commit()

print("Students with grade >= 80:")
cur.execute("SELECT * FROM Students WHERE grade >= ?", (80,))
for row in cur.fetchall():
    print(row)

conn.close()
