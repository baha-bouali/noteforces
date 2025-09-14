# noteforces/noteforces/services/notes_service.py

from noteforces.database import get_connection


def add_note(tag, rating, ideas, time_spent):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO notes (tags, rating, ideas, time_spent)
        VALUES (?, ?, ?, ?)
    """, (tag, rating, ideas, time_spent))

    conn.commit()
    conn.close()


def search_note(by_tag=None, by_rating=None):
    conn = get_connection()
    cur = conn.cursor()

    query = "SELECT * FROM notes WHERE 1=1"
    params = []

    if by_tag:
        query += " AND tags LIKE ?"
        params.append(f"%{by_tag}%")
    if by_rating:
        query += " AND rating >= ?"
        params.append(by_rating)

    query += " ORDER BY created_at DESC"
    cur.execute(query, params)

    rows = cur.fetchall()
    conn.close()
    return rows
