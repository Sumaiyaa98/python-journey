#in this we are making extra function, which are lodad_data and main function

def load_data():
    pass

def list_all_videos(videos):
     pass

def add_video(video):
     pass

def update_video(videos):
     pass

def delete_video(videos):
     pass

def main():
    videos = load_data()
    #to get data or to load data from the file

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
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
            #works as a default option
                print('Invalid Choice')


#for calling function if someone will calls it
if __name__ == "__main__":
    main()
            
