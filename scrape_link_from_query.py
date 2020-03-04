from bs4 import BeautifulSoup
import urllib.request
import csv
import requests
import sys
import os
#import urllib2
import codecs


BASE_URL = "http://www.reddit.com" #maybe make this into a prompt
i = 0 # global variable for recursion

#filename = input("Enter your filename (do not enter file extension): ")
#filename = filename + '.csv'
filename = 'URLs.csv'

limit = int(input("Enter the number of pages you want to analyze (MAX 150): "))

path_to_script_dir = os.path.dirname(os.path.abspath("scrape_link_from_query.py"))  # create a new file no matter what
newpath = path_to_script_dir + r'\\' + filename

with open(filename, 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter='\n')
    writer.writerow(["Links"])  # need to do this so links.py doesn't crash


def scrape_link_from_query(startingurl):
    #agentheader = {'User-Agent': 'Nerd_Destroyer'} # in this case reddit wants to do this and I get better results when I do
    #request = urllib.Request(startingurl,headers=agentheader)
    #url =  urllib.request.urlopen(startingurl)#The url you want to open

    req = urllib.request.Request(
        startingurl,
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14931'
        }
    )

    url = urllib.request.urlopen(req)

    soup = BeautifulSoup(url)
    #print(soup.prettify())
    for a in soup.find_all('a', {'class' : 'search-title'}, href=True):
        newsite = str(site)
        #if not 'comment' in a['href']: continue
        #if not newsite in a['href']: continue  #prevents non-selfposts from getting in the link list. MAYBE MAKE INTO PROMPT
        found_url = a['href']

        with open(filename, 'a') as csvfile:  #write to csvfile, need the 'ab' to append to file without adding space. need to autocreate csvfil
            writer = csv.writer(csvfile, delimiter='\n')
            if isinstance(found_url, str): writer.writerow([found_url])  #there's a problem with non-ascii characters being stored in the csv file, I'm just skipping anything that gives problems here
        print (found_url)  #this prints out all links found, even the ones not stored in csv

    #print(soup.prettify())
    for a in soup.find_all('a', {'rel' : 'nofollow next'}, href=True):  #finds the next button via the rel/class thing 'nofollow next'
        next_url = a['href']
        print ("next: ", a['href'])  #prints in python shell but doesn't append to csvfile
        global i   #global i so value is define during recursions
        global limit
        i+=1
        if i >= limit: break  #limit the amount of pages it crawls, need to make into PROMPT
        scrape_link_from_query(next_url)  #recursion


site = input("Enter query you want to analyze: ")
scrape_link_from_query("http://www.reddit.com/search?q=" + str(site))  #run with starting link. need to make into PROMPT
