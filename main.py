import grades_manager

print("[Welcome to your grade manager]\n")

while True:
    print("[view/add subject/add grade/delete subject/delete grade]")
    print("[If you want to quit or go back type 'q']")
    task = input("[Enter what you want to do]: ")
    print()
    if task == "view":
        grades_manager.view_grades()
    elif task == "add subject":
        grades_manager.add_subject()
    elif task == "add grade":
        grades_manager.add_grade()
    elif task == "delete subject":
        grades_manager.delete_subject()
    elif task == "delete grade":
        grades_manager.delete_grade()
    elif task == "q":
        break
    else:
        print("[Invalid input]")
    print()

grades_manager.conn.close()