import sqlite3

conn = sqlite3.connect('youtube_video.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
               )

''')

def list_videos():
    cursor.execute("SELECT * FROM video")
    for row in cursor.fetchall():
        print(row)


def add_video(name,time):
    cursor.execute("INSERT INTO videos (name,time) VALUES (?, ?)" (name,time))
    cursor.commit()
    

def update_video():
    pass

def delete_video():
    pass


def main():
    while True:
        print("\nYoutube Manager App with DB")
        print("1. List Videos")
        print("2. Add Videos")
        print("3. Delete Videos")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            add_video(name,time)
        elif choice == '3':
            video_ID =input("Enter video ID to update: ")
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            update_video(video_ID,name,time)
        elif choice == '4':
            video_ID =input("Enter video ID to delete: ")
            delete_video(video_ID)
        elif choice == '5':
            break
        else:
            print("Invalid Choice")

    conn.close()

if __name__ == "__main__":
    main()