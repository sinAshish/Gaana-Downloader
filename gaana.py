import requests
from bs4 import BeautifulSoup
import os 
os.mkdir('/home/ashish/Downloads/Gaana',0755)
os.chdir('/home/ashish/Downloads/Gaana/')
url=raw_input()
links=[]
title=[]
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

def downloader():
	for i in range(len(links)):
		with open(title[i],'wb') as file:
			for chunk in requests.get(links[i],stream=True).iter_content(chunk_size=1024):
				if chunk:
					print "%s downloading...."%title[i]
					file.write(chunk)

scaper(url)
downloader()