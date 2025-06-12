#in this we make functions and choices for the user to select


def list_all_videos(videos):
     pass

def add_video(video):
     pass

def update_video(videos):
     pass

def delete_video(videos):
     pass

while True:
     print("\n Youtube Manager | choose an option ")
     print("1. List all youtube videos ")
     print("2. Add a youtube video ")
     print("3. Update a youtube video details ")
     print("4. Delete a youtube video ")
     print("5. Exit the app ")
     choice = input("Enter your choice:")
     #match is like a switch statment in python, use for choices
     match choice:
          case '1':
               list_all_videos(videos)
          case '2':
               add_video(video)
          case '3':
               update_video(videos)
          case '4':
               delete_video(videos)
          case '5':
               break
          case _:
          #works as a default option
               print('Invalid Choice')
          
