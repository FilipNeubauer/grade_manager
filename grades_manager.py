import sqlite3

conn = sqlite3.connect("My_Grades.db")
c = conn.cursor()


def add_subject():
    while True:
        subject_name = input("[Enter the name of the new Subject]: ")
        try:
            c.execute("CREATE TABLE {} (grade text)".format(subject_name))
            conn.commit()
            break
        except:
            print("[This subject already exists or you enter invalid name]")


def add_grade():
    while True:
        subject_name = input("[Enter the name of the Subject]: ")
        c.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='{}'".format(subject_name))
        if c.fetchone()[0] == 1:
            grade = input("[Enter the grade]: ")
            try:
                float(grade)
                c.execute("INSERT INTO {} VALUES (?)".format(subject_name), grade)
                conn.commit()
                break
            except:
                print("[Invalid grade]")
                break
        print("[Invalid Subject]")


def view_grades():
    c.execute("SELECT name FROM sqlite_master WHERE type='table'")
    subjects = list(map(lambda x: "".join(x), c.fetchall()))
    for i in subjects:
        c.execute("SELECT * FROM {}".format(i))
        grades = list(map(lambda x: "".join(x), c.fetchall()))
        average = sum(list(map(lambda x: int(x), grades)))/len(grades)
        print(f"[{i}]" + " "*(15-len(i)) + "({:.2f}) ".format(average) + " ".join(grades))