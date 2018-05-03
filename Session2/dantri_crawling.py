#Download web
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = "http://dantri.com.vn"

#1.1 Open connection
conn = urlopen(url)

#1.2 Read data
raw_data = conn.read()

#1.3 Decode - vì data bây giờ đang ở dạng thô nên mình phải decode nó
text = raw_data.decode('utf-8')

# print(text)

#lưu file để đọc cho dễ

# #mở connection
# dan_tri_file = open("dantri.html", "wb")
# #ghi file
# dan_tri_file.write(raw_data)
# #đóng connection
# dan_tri_file.close()


#2. Find ROI


soup = BeautifulSoup(text, "html.parser")
# print(soup.prettify())

ul = soup.find("ul", "ul1 ulnew") #find là tìm 1 hoặc tìm thằng đầu tiên
# print(ul.prettify())

li_list = ul.find_all("li")

item_list = []

for li in li_list:
    a = li.h4.a
    title = a.string #string or content
    link = url + a['href']

    item = {
        "Title": title,
        "Link" : link
    }
    item_list.append(item)
    #
    # print(item)
    # print("--------------------")

    # print(title)
    # print(link)
    # print("-----------------------")

# print(item_list)
pyexcel.save_as(records = item_list, dest_file_name = "dantri.xlsx")
