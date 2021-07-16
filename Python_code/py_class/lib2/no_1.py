# -*- codeing = utf-8 -*-
# @Time : 2021/4/20 14:16
# @Author : zhaha
# @File : no_1.py
# @Software : PyCharm


import requests
from bs4 import BeautifulSoup

json_file = open('doubanbook.json', 'w', encoding='utf-8')
for i in range(0, 1):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36',
        'Host': 'book.douban.com'
    }
    link = 'https://book.douban.com/top250?start=' + str(25 * i)
    r = requests.get(link, headers=headers, timeout=10)
    soup = BeautifulSoup(r.text, "lxml")
    div_list = soup.find_all('tr', class_='item')
    Book = []
    for each in div_list:
        book = {}
        bookname = each.find('div', class_='pl2').a.text.strip()
        bookname = bookname.replace('\n', '')
        bookname = bookname.replace(' ', '')
        book['title'] = bookname
        info = each.find('p', class_='pl').text.strip()
        info = info.replace(" ", "")
        info = info.split('/')
        length = len(info)
        if length == 4:
            author = info[0]
            book['author'] = author
            publisher = info[1]
            book['publisher'] = publisher
            publication_date = info[2]
            book['publication_date'] = publication_date
            price = info[3]
            book['price'] = price
        else:
            author = info[0]+'/'+info[1]
            book['author'] = author
            publisher = info[length-3]
            book['publisher'] = publisher
            publication_date = info[length-2]
            book['publication_date'] = publication_date
            price = info[length-1]
            book['price'] = price
        star = each.find('div', class_='star clearfix')
        star = star.find('span', class_='rating_nums').text.strip()
        book['star'] = star
        quote = each.find('p', class_='quote')
        quote = quote.find('span', class_='inq').text.strip()
        book['quote'] = quote
        print(book)
        json_file.write(str(book)+'\n')