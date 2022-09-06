# ***********************************************************************************************************
# Summary: Read all the scripts and stores into one file
#
# Requirements: Python Verison 3.7
#
# Author : Anto
# ***********************************************************************************************************

from bs4 import BeautifulSoup
from movielist import movie_name
import requests

# TODO: Add a way selecting different genres for the script.txt dataset

# ***********************************************************************************************************
#
#   This function scrapes the Imsdb script database for the movies in the list & outputs just the script
#
# ***********************************************************************************************************


def get_script():
    try:
        for i in range(len(movie_name)):
            api_request = requests.get(
                'https://imsdb.com/scripts/{}.html'.format(movie_name[i])).text
            soup = BeautifulSoup(api_request, 'lxml')
            script = soup.find('pre')
            output = script.text
<<<<<<< HEAD
        return output
=======
            return output
>>>>>>> f723c76 (modified:   Src/web_scraper.py)
    except Exception as e:
        raise Exception(str(e))

# ***********************************************************************************************************
#
#   This function appends all the scripts and store it in the scripts.txt file
<<<<<<< HEAD
#
=======
# TODO: Fix the path to where script.txt file is created
>>>>>>> f723c76 (modified:   Src/web_scraper.py)
# ***********************************************************************************************************


def store_scripts(file):
    try:
<<<<<<< HEAD
        with open('Src/scripts.txt', 'a', encoding='utf-8') as f:
=======
        with open('scripts.txt', 'a', encoding='utf-8') as f:
>>>>>>> f723c76 (modified:   Src/web_scraper.py)
            f.write(file)
    except Exception as e:
        raise Exception(str(e))


# ***********************************************************************************************************
<<<<<<< HEAD
#
#   Move this to main.py later
#
=======
#
#   Move this to main.py later
#
>>>>>>> f723c76 (modified:   Src/web_scraper.py)
# ***********************************************************************************************************

data = get_script()
combined_data = store_scripts(data)
