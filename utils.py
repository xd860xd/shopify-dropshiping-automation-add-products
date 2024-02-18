import os
import requests
import shutil

COLORS = {
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "magenta": "\033[95m",
    "cyan": "\033[96m",
    "white": "\033[97m",
    "black": "\033[30m",
    "default": "\033[39m",
    "light_red": "\033[31m",
    "light_green": "\033[32m",
    "light_yellow": "\033[33m",
    "light_blue": "\033[34m",
    "light_magenta": "\033[35m",
    "light_cyan": "\033[36m",
    "light_white": "\033[37m",
    "light_black": "\033[90m",
    "light_default": "\033[39m",
    "end": "\033[0m"

}

def download_files(urls, directory):
    # Create directory if it doesn't exist
    directory = os.path.join("outputs", directory)
    print(COLORS["light_blue"] + "Downloading files from" + COLORS["end"], urls, COLORS["light_blue"] + "to" + COLORS["end"], directory)

    if not os.path.exists(directory):
        os.makedirs(directory)

    aux = 0
    for url in urls:
        aux += 1
        # Extract filename from URL
        name = url.split('/')[-1].split('.')[0] + str(aux) + ".jpg"
        filename = os.path.join(directory, name)
        
        print(COLORS["light_blue"] + "Downloading file from" + COLORS["end"], url,"\n" ,  COLORS["light_blue"] + "to" + COLORS["end"], filename)
        # Send a GET request to the URL
        correct_image = url.replace(".jpg_80x80", "")
        response = requests.get(correct_image)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Open the file in binary write mode and write the content from the response
            with open(filename, 'wb') as file:
                file.write(response.content)
            print(COLORS["light_green"] + "File downloaded successfully:" + COLORS["end"], filename)

        else:
            print(COLORS["light_red"] + "Failed to download file from" + COLORS["end"], url, COLORS["light_red"] + ". Status code:" + COLORS["end"], response.status_code)

