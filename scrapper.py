import urllib2
from bs4 import BeautifulSoup

class News:

	@staticmethod
	def getNews () :
		'''
		Return a dictionary of top 30 news and their links
		No parameters reuired 
		'''
		result = []
		response = {}
		url = 'http://www.iitbbs.ac.in/news.php'
		page = urllib2.urlopen(url)
		soup = BeautifulSoup(page, 'html.parser')
		newsOl = soup.find('ol', attrs={'class': 'rectlist'})
		newsLi = newsOl.find_all('li')

		for link in newsLi:
			news = link.text.strip()
			
			if link.find('a').get('href')[:4] != 'http':
				link = 'http://www.iitbbs.ac.in/' + link.find('a').get('href')
			else:
				link = link.find('a').get('href')

			result.append({'text': news, 'url': link});

		response['count'] = len(newsLi)
		response['list'] = result
		return response

	@staticmethod
	def getEvents () :
		'''
		Return a dictionary of all listed upcoming events
		No parameters reuired 
		'''
		result = []
		response = {}
		url = 'http://www.iitbbs.ac.in/events.php'
		page = urllib2.urlopen(url)
		soup = BeautifulSoup(page, 'html.parser')
		newsOl = soup.find('ul', attrs={'class': 'orangearrow'})
		newsLi = newsOl.find_all('li')

		for link in newsLi:
			event = link.text.strip()
			
			if link.find('a').get('href')[:4] != 'http':
				link = 'http://www.iitbbs.ac.in/' + link.find('a').get('href')
			else:
				link = link.find('a').get('href')

			result.append({'text': event, 'url': link});

		response['count'] = len(newsLi)
		response['list'] = result
		return response


	@staticmethod
	def getNotices () :
		'''
		Return a dictionary of all listed Notices
		No parameters reuired 
		'''
		result = []
		response = {}
		url = 'http://www.iitbbs.ac.in/notices.php'
		page = urllib2.urlopen(url)
		soup = BeautifulSoup(page, 'html.parser')
		newsOl = soup.find('ul', attrs={'class': ''})
		newsLi = newsOl.find_all('li')

		for link in newsLi:
			notice = link.text.strip()
			
			if link.find('a').get('href')[:4] != 'http':
				link = 'http://www.iitbbs.ac.in/' + link.find('a').get('href')
			else:
				link = link.find('a').get('href')

			result.append({'text': notice, 'url': link});

		response['count'] = len(newsLi)
		response['list'] = result
		return response

# if __name__ == "__main__":
# 	print News.getNews()
# 	print News.getNotices()
# 	print News.getEvents()