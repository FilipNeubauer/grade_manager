import sqlite3

conn = sqlite3.connect("My_Grades.db")
c = conn.cursor()


def add_subject():
    subject_name = input("[Enter the name of the new Subject]: ")
    c.execute("CREATE TABLE {} (grade, date)".format(subject_name))
    conn.commit()