#in this we are making one new function,
#  save_data_helper(),and adding the try catch in data_load method
import json



def load_data():
    try:
        with open('youtube.txt','r') as file:
            #using r to read the file if it's exit, it not then we are using exception 
            #in this to handle error 
            return json.load(file)
        #using json.load, to load our data of our file
    except FileNotFoundError:
        return []

    #making function to save the data
def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)
    #using dump method to write the data, in this we writing the data of videos inside the file

        

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
            
