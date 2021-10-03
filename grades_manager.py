import sqlite3

conn = sqlite3.connect("My_Grades.db")
c = conn.cursor()


def add_subject():
    while True:
        subject_name = input("[Enter the name of the new Subject]: ")
        try:
            c.execute("CREATE TABLE {} (grade, date)".format(subject_name))
            conn.commit()
            break
        except:
            print("[This subject already exists or you enter invalid name]")