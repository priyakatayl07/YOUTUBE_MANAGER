import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            test=json.load(file)
            print(type(test))
            return test
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    if not videos:
        print("No videos found.")
        return
    print("\n"+"*"*50)

    for index, video in enumerate(videos, start=1):
        print(f"{index}. Name: {video['name']}, Time: {video['time']}")
    print("\n"+"*"*50)

def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index=int(input("enter the video number to update :"))
    if 1<=index<=len(videos):
        name=input("enter the new video name:")
        time=input("enter the new video time:")
        videos[index-1]={'name':name,'time':time}
        save_data_helper(videos)
    else:
        print("invalid index selected")    

def delete_video(videos):
    list_all_videos(videos)
    index=int(input ("enter the video number to be deleted :"))

    if 1<=index<=len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("invalid video index selected")    
def main():
    videos = load_data()
    while True:
        print("\nYouTube Manager | Choose an option:")
        print("1. List favorite videos")
        print("2. Add a YouTube video")
        print("3. Update a YouTube video details")
        print("4. Delete a YouTube video")
        print("5. Exit the app")
        choice = input("Enter your choice: ")
        print(videos)  

        if choice == '1':
            list_all_videos(videos)
        elif choice == '2':
            add_video(videos)
        elif choice == '3':
            update_video(videos)
        elif choice == '4':
            delete_video(videos)
        elif choice == '5':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
