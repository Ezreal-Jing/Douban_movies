# -*- coding: utf-8 -*-
# @Author : Ezreal
# @File : main.py
# @Project: douban_movie
# @CreateTime : 2022/2/17 下午5:13:32
# @Version：V 0.1

from scrapy.cmdline import execute
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
#execute(["scrapy","crawl","moviescrape"])
execute(["scrapy","crawl","moviescrape","-o data.csv"])#相当于在shell中执行爬虫