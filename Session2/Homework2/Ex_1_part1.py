from  urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = "https://www.apple.com/itunes/charts/songs"

itunes = urlopen(url)

raw_data = itunes.read()

text = raw_data.decode("utf-8")

# print(text)

# itunes_file = open("iTunes.html", "wb")
#
# itunes_file.write(raw_data)
#
# itunes_file.close()

soup = BeautifulSoup(text, 'html.parser')


div = soup.find("div", id = "main")

li_list = div.find_all("li")

data_list = []

for li in li_list:
    a = li.h3.a
    b = li.h4.a
    song = a.string
    author = b.string

    data = {
            "Song"   : song,
            "Author" : author
        }
    data_list.append(data)
pyexcel.save_as(records = data_list, dest_file_name = "iTunesSongs.xlsx")
####
