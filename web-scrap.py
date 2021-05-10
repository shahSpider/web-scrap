import requests
import pprint
from bs4 import BeautifulSoup
import os

#Hello this is a modification comment

mega_links = []
mega_subtext = []
for page in range(1,2):
	res = requests.get(f'https://news.ycombinator.com/news?p={page}')
	soup = BeautifulSoup(res.text, 'html.parser')
	links = soup.select('.storylink')
	subtext = soup.select('.subtext')
	mega_links += links
	mega_subtext += subtext

def stories_sorted_by_votes(hackernews_list):
	return sorted(hackernews_list, key = lambda k:k['votes'], reverse = True)

def create_custom_hn(links, subtext):
	hn = []
	for idx, item in enumerate(links):
		title = links[idx].getText()
		href = links[idx].get('href', None)
		votes = subtext[idx].select('.score')
		if len(votes):
			points = int(votes[0].getText().replace(' points', ''))
		if points>100:
			if not os.path.exists('hackernews.txt'):
				open('hackernews.txt', 'x')
			with open('hackernews.txt', 'a') as myfile:
				myfile.write(f'title: {title}, link:  {href}, score: {points} \n')
			hn.append({'title':title, 'link':href, 'votes':points})
	return stories_sorted_by_votes(hn)



create_custom_hn(mega_links, mega_subtext)