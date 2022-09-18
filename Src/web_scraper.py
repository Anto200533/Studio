# ***********************************************************************************************************
# Summary: Read all the scripts and stores into one file
#
# Requirements: Python Verison 3.7
#
# Author : Anto
# ***********************************************************************************************************

from bs4 import BeautifulSoup
import movielist
import requests

# ***********************************************************************************************************
#
#   This function selects lists from movielist, multiple lists can be combined into one script.txt by running this file multiple times.
#
# ***********************************************************************************************************


def select_list():
    try:
        print("Enter the movie genre:")
        genre = input().lower()
        chosen_genre = getattr(movielist, genre)
        print(chosen_genre)
        return chosen_genre
    except Exception as e:
        raise Exception(str(e))

# ***********************************************************************************************************
#
#   This function scrapes the Imsdb script database for the movies in the list & outputs just the script
#
# ***********************************************************************************************************


def get_script(chosen_genre):
    try:
        for i in range(len(chosen_genre)):
            api_request = requests.get(
                'https://imsdb.com/scripts/{}.html'.format(chosen_genre[i])).text
            soup = BeautifulSoup(api_request, 'lxml')
            script = soup.find('pre')
            output = script.text
        return output
    except Exception as e:
        raise Exception(str(e))

# ***********************************************************************************************************
#
#   This function appends all the scripts and store it in the scripts.txt file
#
# ***********************************************************************************************************


def store_scripts(file):
    try:
        with open('scripts.txt', 'a', encoding='utf-8') as f:
            f.write(file)
    except Exception as e:
        raise Exception(str(e))


# ***********************************************************************************************************
#
#   Move this to main.py later
#
# ***********************************************************************************************************

genretype = select_list()
data = get_script(genretype)
combined_data = store_scripts(data)
