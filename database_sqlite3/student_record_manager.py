import sqlite3

conn = sqlite3.connect("student_record.db")
cursur = conn.cursor()

cursur.execute('''
    CREATE TABLE IF NOT EXISTS students (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               age INTEGER NOT NULL
              
            
    )
''')


def show_st_record():
    cursur.execute("SELECT * FROM students")
    for row in cursur.fetchall():
        print(row)

    
def add_st_record(name,age):
    cursur.execute("INSERT INTO students (name, age) VALUES (?, ?)", (name, age))
    conn.commit()


def update_st_record(student_id,name,age):
    cursur.execute("UPDATE students SET name = ?, age = ? WHERE id = ?", (name, age, student_id))
    conn.commit()

def delete_st_record(student_id):
    cursur.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()

def main():
    while(True):
        print("STUDENT RECORD MANAGER | CHOOSE AN OPTION")
        print("1-View All Students Record")
        print("2-Add Student Record")
        print("3-Update Student's Info")
        print("4-Delete Student Record")
        print("5-Exit")
        choice = input("Enter your choice: ")
        match(choice):
            case '1':
                show_st_record()
            case '2':
                name = input("Enter student name: ")
                while(True):
                    try:
                        age = int(input("Enter student age: "))
                        break
                    except ValueError:
                        print("Enter correct age,(DIGITS ONLY)")
                
                add_st_record(name,age)
            case '3':
                student_id = input("Enter student ID to update: ")
                name = input("Enter the student name: ")
                while(True):
                    try:
                        age = int(input("Enter student age: "))
                        break
                    except ValueError:
                        print("Enter correct age,(DIGITS ONLY)")
                
                update_st_record(student_id,name,age)
            case '4':
                student_id = input("Enter student ID to delete: ")
                delete_st_record(student_id)
            case '5':
                break
            case _:
                print("Invalid Choice")

    conn.close()

if __name__ == "__main__":
    main()
