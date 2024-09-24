import os
from pyrogram import Client
from pyrogram.errors import PeerIdInvalid

# Replace these with your own API ID and API Hash
api_id = 1111
api_hash = '---'

# Folder where the voice messages will be saved
download_folder = r'File/Path'

# Initialize Pyrogram client
app = Client("my_account", api_id=api_id, api_hash=api_hash)

# Ensure the download folder exists
if not os.path.exists(download_folder):
    os.makedirs(download_folder)

# Function to download voice messages from a private channel
def download_voice_messages(channel_username):
    
    try:
        # Fetch all messages in the channel
        messages = app.get_chat_history(channel_username)

        # Collect voice messages into a list
        voice_messages = [message for message in messages if message.voice]

        # Sort the collected voice messages by date
        voice_messages.sort(key=lambda msg: msg.date)

        # Download the voice messages
        for message in voice_messages:
            sent_time = message.date.strftime("%Y-%m-%d_%H-%M-%S")
            file_name = f"{message.id}_{sent_time}.ogg"
            file_path = os.path.join(download_folder, file_name)

            if os.path.exists(file_path):
                print(f"File {file_name} already exists. Skipping...")
                continue  # Skip if the file already exists

            print(f"Downloading {file_name}...")
            app.download_media(message, file_name=file_path)

        print("All voice messages have been downloaded in chronological order.")
    except PeerIdInvalid:
        print("Error: Invalid Peer ID. Make sure the channel is accessible and that you have joined it.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main function to run the voice message download
if __name__ == "__main__":
    # Start the client session
    app.start()
    
    try:
        # Enter the channel username or ID
        channel_username = 111111
        
        # Attempt to download messages
        download_voice_messages(channel_username)
    finally:
        # Stop the client session when done
        app.stop()
