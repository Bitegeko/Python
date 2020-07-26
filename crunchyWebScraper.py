import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('https://www.crunchyroll.com/videos/anime')

soup = BeautifulSoup(response.text, 'html.parser')

shows = soup.find_all(class_='hover-bubble group-item')



with open('post.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Title', 'Link', 'Videos']
    csv_writer.writerow(headers)

    for show in shows:
        title = show.find(class_='series-title block ellipsis').get_text().replace('/n', '')
        numOfShows = show.find(class_='series-data block ellipsis').get_text().replace('/n', '')
        link = 'https://www.crunchyroll.com/videos/anime' + show.find('a')['href']
        print(title, link, numOfShows)
        csv_writer.writerow([title, link, numOfShows])
