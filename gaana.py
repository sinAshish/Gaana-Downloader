import requests
from bs4 import BeautifulSoup
import os 
from selenium import webdriver 
from urllib2 import urlopen
#creates directory in pc
os.mkdir('/home/ashish/Downloads/Gaana',0755)
os.chdir('/home/ashish/Downloads/Gaana/')
url=raw_input("Enter the playlist url:")
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

def downloader():
	for i in range(len(links)):
		mp3=urlopen(links[i])
		print "%s Downloading...."%title[i]
		with open(title[i],'wb') as file:
			file.write(mp3.read())


scaper(url)
downloader()
