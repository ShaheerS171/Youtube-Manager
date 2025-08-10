import sqlite3

conn = sqlite3.connect('Youtube_manager.db')

cursor = conn.cursor()

cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS videos (
              id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               duration TEXT NOT NULL
      )
 ''')

def list_of_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(f"ID: {row[0]}, Name: {row[1]}, Duration: {row[2]}")

def add_vedio(name, duration):
    cursor.execute("INSERT INTO videos (name, duration) VALUES (?, ?)", (name, duration))
    conn.commit()
    print("Video added successfully.")

def update_vedio(video_id, new_name, new_duration):
    cursor.execute("UPDATE videos SET name = ?, duration = ? WHERE id = ?",(new_name, new_duration, video_id))
    conn.commit()

def delete_videos(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    conn.commit()
    print("Video deleted successfully.")

def main():
     while True:
      print("\n Youtube Manager. Please select an option:")
      print("1. List all youtube  vedio")
      print("2. Add a favourite vedio")
      print("3. Update a youtube vedio details")
      print("4. Delete a youtube vedio")
      print("5. Exit")
      choice = input("Enter your choice: ")

      match choice: # This case is like the switch in C or Java
          case '1':
              list_of_videos()
          case '2':
               name = input("Enter the name of the video: ")
               duration = input("Enter the duration of the video: ")
               add_vedio(name, duration)
          case '3':
              video_id = input("Enter the ID of the video to update: ")
              new_name = input("Enter the new name of the video: ")
              new_duration = input("Enter the new duration of the video: ")
              update_vedio(video_id, new_name, new_duration)
          case '4':
              video_id = input("Enter the ID of the video to delete: ")
              delete_videos(video_id)
          case '5':
                break
          case _: # Default case if no match found
              print("Invalid choice. Please try again.")

     conn.close()

if __name__ == "__main__":
    main()