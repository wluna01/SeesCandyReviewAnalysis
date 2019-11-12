import os
import sys
import re
from bs4 import BeautifulSoup
import timestring

#open the html file scraped from the Sees website
soup = BeautifulSoup(open("nuts_chews_reviews.html"), "html.parser")
with open("nuts_reviews.csv", "w") as f:
	f.write("name, rating, day, title, review")
	f.write('\n')
	for line in soup.find_all('li', attrs={'class': 'customer-review'}):
		#parse and format relevant data from each review
		name = line.find('div', attrs={'class': 'name'})
		name = name.get_text().replace(',','x')
		name = (name + ', ')

		rating = line.find('div', attrs={'class': 'rating-value'})
		rating = rating.get_text()
		rating = (rating[0] + ', ')

		date = line.find('div', attrs={'class': 'date'})
		date = date.get_text()
		date = timestring.Date(date)
		date = str(date.year) + "-" + str(date.month) + "-" + str(date.day) + ", "

		title = line.find('h4', attrs={'class': 'title'})
		title = title.get_text() 
		title = title.replace(',', '')
		title = title + ", "

		review = line.find('div', attrs={'class': 'review-text'})
		review = review.get_text()
		review = review.lower()
		review = review.replace('\'','')

		wordList = re.sub("[^\w]", " ",  review).split()
		#write the review to csv file
		for word in wordList:
			f.write(name + rating + date + title + word + '\n')
