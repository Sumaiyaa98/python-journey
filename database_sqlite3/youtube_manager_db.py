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

if __name__ == "__main__":
    main()