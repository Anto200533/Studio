#***********************************************************************************************************
# Summary: Read all the scripts and stores into one file
#          
# Requirements: Python Verison 3.7
#
# Author : Anto 
#***********************************************************************************************************

from bs4 import BeautifulSoup
from movielist import movie_name
import requests

#TODO: Add a way selecting different genres for the script.txt dataset

#***********************************************************************************************************
#   
#   This function scrapes the Imsdb script database for the movies in the list & outputs just the script 
#
#***********************************************************************************************************

def get_script(): 
    try: 
        for i in range(len(movie_name)):
            api_request = requests.get('https://imsdb.com/scripts/{}.html'.format(movie_name[i])).text
            soup = BeautifulSoup(api_request, 'lxml')
            script = soup.find('pre')
            output = script.text
            return output
    except Exception as e: 
        raise Exception(str(e))

#***********************************************************************************************************
#   
#   This function appends all the scripts and store it in the scripts.txt file 
#TODO: Fix the path to where script.txt file is created 
#***********************************************************************************************************


def store_scripts(file):
    try:
        with open('scripts.txt', 'a') as f:
            f.write(file)          
    except Exception as e: 
        raise Exception(str(e))


#***********************************************************************************************************
#   
#   Move this to main.py later 
#
#***********************************************************************************************************

data = get_script()
combined_data = store_scripts(data)

