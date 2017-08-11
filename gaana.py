import requests
from bs4 import BeautifulSoup
import os 
from selenium import webdriver 
from urllib2 import urlopen
from time import sleep


#creates directory in pc
os.mkdir('/home/ashish/Downloads/Gaana',0755)
os.chdir('/home/ashish/Downloads/Gaana/')
url=raw_input("Enter the playlist url:")
browser=webdriver.Chrome()
links=[]
title=[]

# saves links and song names
def scaper(url):
	soup=BeautifulSoup(requests.get(url).content,"lxml")
	data=soup.findAll('div',{'playlist_thumb_det'})	
	for line in data:
		link=str(line.contents[1])
		s=link.find('href=')
		start=link.find('"',s)
		end=link.find('"',start+1)
		d_link=link[start+1:end]
		links.append(d_link)
		name=link[end+2:len(link)-4]
		title.append(name)

# Let's Download NOW

def download(s):
	link="https://www.youtube.com/results?search_query="+s
    browser.get(link)
    browser.execute_script("document.cookie=\"VISITOR_INFO1_LIVE=oKckVSqvaGw; path=/; domain=.youtube.com\";window.location.reload();")  #Disable ads
    browser.find_elements_by_class_name("yt-ui-ellipsis")[0].click()
    be=browser.current_url
    browser.get("https://www.youtube2mp3.cc/")
    t=browser.find_element_by_id("input")
    t.send_keys(be)
    browser.find_element_by_id("button").click()
    sleep(5)                                                                                                                 #Wait for dynamically generated download button to load
    browser.execute_script("document.getElementById(\"download\").click()")
    print(s+" downloaded!")


for song in title:
	download(song)


# Previous code
"""
def downloader():
	for i in range(len(links)):
		mp3=urlopen(links[i])
		print "%s Downloading...."%title[i]
		with open(title[i],'wb') as file:
			file.write(mp3.read())
"""

scaper(url)

