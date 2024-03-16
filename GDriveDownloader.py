import os
import io
import hashlib
import tkinter as tk
from tkinter import simpledialog
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Initialize drive as None with the correct capitalization
drive = None

def request_secret_information():
    # Create a new Tkinter root window
    root = tk.Tk()
    # Hide the root window
    root.withdraw()

    # Request the secret information from the user
    secret = simpledialog.askstring("Enter Secret", "Please enter your secret information:", show='*')
    
    # Print or use the secret information
    print("The secret information is:", secret)

    # Don't forget to destroy the root window
    root.destroy()

def request_secret_information():
    # Create a new Tkinter root window
    root = tk.Tk()
    # Hide the root window
    root.withdraw()

    # Request the secret information from the user
    secret = simpledialog.askstring("Enter Secret", "Please enter your secret information:", show='*')
    
    # Print or use the secret information
    print("The secret information is:", secret)

    # Don't forget to destroy the root window
    root.destroy()
    


def login():
    global drive
    secrets_path = input("Enter the path to your client_secrets.json file: ").strip()
    if not os.path.isfile(secrets_path):
        print("The specified client_secrets.json file does not exist. Please check the path and try again.")
        return False
    
    gauth = GoogleAuth()
    gauth.settings['client_config_file'] = secrets_path
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)
    return True

if login():
    print("Login successful.")
else:
    print("Login failed.")
# Call login to authenticate and initialize the global 'drive' object
login()

def list_files(folder_id='root'):
    """Lists files in a specified Google Drive folder."""
    global drive
    file_list = drive.ListFile({'q': f"'{folder_id}' in parents and trashed=false"}).GetList()
    for file in file_list:
        print(f'File Name: {file["title"]}')

def download_file(file_id, output_path):
    """Downloads a file from Google Drive."""
    global drive
    file = drive.CreateFile({'id': file_id})
    file.GetContentFile(output_path)

# Example usage
list_files()  # Assuming drive is authenticated
download_file('your_file_id_here', '/path/to/save/file.iso')
