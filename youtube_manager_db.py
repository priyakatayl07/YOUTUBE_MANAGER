import sqlite3

conn=sqlite3.connect("youtube_videos.db")
cursor= conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS VIDEOS(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL)
''')

def main():
    pass
def list_videos():
    cursor.execute("SELECT *from videos")
    print("\n"+"*"*50)
    for row in cursor.fetchall():
        print(row)
    print("\n"+"*"*50)


def add_video(name,time):
    cursor.execute("INSERT INTO videos(name,time) VALUES(?,?)",(name,time))
    conn.commit()

def update_video(video_id,new_name,new_time):
    cursor.execute("UPDATE videos SET name=?,time=? WHERE id=?",(new_name,new_time,video_id))
    conn.commit()

def delete_video(video_id):
    cursor.execute(" DELETE from videos where id=?",(video_id,))
    conn.commit()

def main():
    while True:
        print("\nYouTube Manager | Choose an option:")
        print("1. List favorite videos")
        print("2. Add a YouTube video")
        print("3. Update a YouTube video details")
        print("4. Delete a YouTube video")
        print("5. Exit the app")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name=input("enter the video name:")
            time=input("enter the video time:")
            add_video(name,time)
        elif choice == '3':
            video_id=input("enter video id to update:")
            name=input("enter the video name:")
            time=input("enter the video time:")
            update_video(video_id,name,time)
        elif choice == '4':
            video_id=input("enter video id to delete:")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice")

    conn.close()

if __name__== "__main__":
    main()
