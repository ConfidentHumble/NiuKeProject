#-*- encoding=UTF-8 -*-
'''
@Author: your name
@Date: 2020-03-17 11:41:28
@LastEditTime: 2020-03-17 11:52:40
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /初级项目/demo.py
'''
import requests
from bs4 import BeautifulSoup


def qiushibaike():
    content = requests.get('http://www.qiushibaike.com').content
    soup = BeautifulSoup(content, 'html.parser')

    for div in soup.find_all('div', {'class':'content'}):
        print div.text.strip()