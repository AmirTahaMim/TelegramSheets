import os
from pyrogram import Client

api_id = 111111
api_hash = '-'
phone_number = '-'

download_folder = rf'--'
app = Client("my_account", api_id=api_id, api_hash=api_hash)

if not os.path.exists(download_folder):
    os.makedirs(download_folder)

def download_media(channel_username):
    with app:
        for message in app.get_chat_history(channel_username):
            if message.audio or message.voice:
                file_name = message.audio.file_name if message.audio else message.voice.file_unique_id

                file_path = os.path.join(download_folder, file_name)

                if os.path.exists(file_path):
                    print(f"File {file_name} already exists. Skipping...")
                    continue  
                print(f"Downloading {file_name}...")
                app.download_media(message, file_name=file_path)

        print("All files have been downloaded.")

if __name__ == "__main__":
    channel_username = input("Enter the channel username or ID: ")
    download_media(channel_username)