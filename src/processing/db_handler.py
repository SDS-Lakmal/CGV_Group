import sqlite3

def save_attendance(student_id, status):
    # Save result to database
    conn = sqlite3.connect('attendance.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS records (id TEXT, status TEXT)')
    cursor.execute('INSERT INTO records VALUES (?, ?)', (student_id, status))
    conn.commit()
    conn.close()