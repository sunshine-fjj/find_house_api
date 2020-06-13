from bs4 import BeautifulSoup
import requests
import csv
import time
import lxml

url = "https://zz.58.com/pinpaigongyu/?minprice=1000_2000"

csv_file = open("rent2.csv","w",newline="",encoding='utf-8') 
csv_writer = csv.writer(csv_file, delimiter=',')

while True:
    print("fetch: ", url)
    time.sleep(2)
    response = requests.get(url)
    html = BeautifulSoup(response.text,features="lxml")
    house_list = html.select(".list > li")

    # 循环在读不到新的房源时结束
    if not house_list:
        break

    for house in house_list:
        house_title = house.select("h2")[0].string.strip()
        house_url = house.select("a")[0]["href"]
        house_info_list = house_title.split()

        # 如果第二列是公寓名则取第一列作为地址
        if "公寓" in house_info_list[1] or "青年社区" in house_info_list[1]:
            house_location = house_info_list[0]
        else:
            house_location = house_info_list[1]

        csv_writer.writerow([house_title, house_location, house_url])
csv_file.close()