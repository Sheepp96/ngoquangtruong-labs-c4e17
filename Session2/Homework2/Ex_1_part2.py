from urllib.request import urlopen
from youtube_dl import YoutubeDL
from bs4 import BeautifulSoup

url = "https://www.apple.com/itunes/charts/songs"

itues = urlopen(url)

raw_data = itues.read()

text = raw_data.decode("utf-8")

soup = BeautifulSoup(text, 'html.parser')

div = soup.find('div', id = "main")

li_list = div.find_all('li')




for li in li_list:
    a = li.h3.a
    b = li.h4.a
    song = a.string
    author = b.string

    options = {
        'default_search' : 'ytsearch',
        'max_downloads'  : len(li_list)
    }

    dl = YoutubeDL(options)
    dl.download([song, '-', author])
