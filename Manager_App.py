import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file) 
    except FileNotFoundError:
        return []

def data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)

 
def list_all_videos(videos):
    print("\n", "_"*50, "\n")
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']}")
    print("\n", "_"*50)

def add_video(videos):
    name = input("\nEnter video name: ")
    time = input("Enter video time: ")
    videos.append({'name': name, 'time': time})
    data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the number of the video to be updated: "))
    if 1 <= index <= len(videos):
        name = input("Enter new name of the video: ")
        time = input("Enter new time of the video: ")
        videos[index-1] = {'name': name, 'time': time}
        data_helper(videos)
    else:
        print("Invalid index number!")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the number of the video to be deleted: "))
    if 1 <= index <= len(videos):
        del videos[index-1]
        print("\nVideo number", index, "is deleted")
        data_helper(videos)
    else:
        print("Invalid index number!")
    

def main():
    videos = load_data()
    while True:
        print("\nYoutube Manager App")
        print("1: List all youtube videos")
        print("2: Add a youtube video")
        print("3: Update a youtube video")
        print("4. Delete a youtube video")
        print("5: Exit the app!")
        choice = input("Choose a number: ")
        

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
                print("Invalid choice!")


if __name__ == "__main__":
    main()