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
        if len(grades) > 0:
            average = sum(list(map(lambda x: int(x), grades)))/len(grades)
        else:
            average = 0
        print(f"[{i}]" + " "*(15-len(i)) + "({:.2f}) ".format(average) + " ".join(grades))


def delete_subject():
    while True:
        subject_name = input("[Enter the name of the Subject you want to delete]: ")
        if subject_name == "q":
            break
        c.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='{}'".format(subject_name))
        if c.fetchone()[0] == 1:
            while True:
                warning = input("[Are you sure you want to delete {}? (y/n)]: ".format(subject_name))
                if warning == "y":
                    c.execute("DROP TABLE {}".format(subject_name))
                    conn.commit()
                    print(f"[{subject_name} deleted]")
                    break
                elif warning == "n":
                    break
                else:
                    print("[Invalid input]")
            break
        else:
            print("[This Subject does not exist]")


def delete_grade():
    while True:
        subject_name = input("[Enter the name of the Subject]: ")
        if subject_name == "q":
            break
        c.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='{}'".format(subject_name))
        if c.fetchone()[0] == 1:
            c.execute("SELECT rowid, * FROM {}".format(subject_name))
            grades = c.fetchall()
            while True:
                for i in grades:
                    print(f"[{i[0]}] {i[1]}")
                grade_id = input("[Enter the [id] of the grade you want to delete]: ")
                try:
                    c.execute(f"SELECT * FROM {subject_name} WHERE rowid={grade_id}")
                    grade = "".join(c.fetchone())
                    while True:
                        warning = input(f"[Are you sure you want to delete {grade} from {subject_name}? (y/n)]: ")
                        if warning == "y":
                            c.execute(f"DELETE from {subject_name} WHERE rowid={grade_id}")
                            conn.commit()
                            print(f"[{grade} deleted from {subject_name}]")
                            break
                        elif warning == "n":
                            break
                        else:
                            print("[Invalid input]")
                    break
                except:
                    print("[Invalid input]")
            break
        else:
            print(f"[{subject_name} does not exist]")
            
