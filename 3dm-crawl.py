# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

# 爬3dm八卦的图
# https://www.3dmgame.com/bagua/

def crawl_web(num1, num2):
    page_num = num1
    web_initnum = num2
    
    current_page = 1
    pic_count = 1
    while(int(current_page) <= int(page_num)):
        if(int(current_page) > 1):
            web_pagenum = str(web_initnum) + '_' + str(current_page) # 翻页
        else:
            web_pagenum = web_initnum
        
        url = 'https://www.3dmgame.com/bagua/' + web_pagenum + '.html'
        # print(url)

        html = requests.get(url)
        html.encoding = 'utf-8'

        soup = BeautifulSoup(html.text, 'lxml')

        div = soup.find(name = 'div', attrs = {"class":"news_warp_center"})
        # print(div)

        p_list = div.find_all(name = 'p')
        # print(p_list)

        for p in p_list:
            img = p.find(name = 'img')
            # print(img)
            
            if(img != None):
                src = img.get('src')

                download_img = requests.get(src)

                with open(str(pic_count) + '.jpg', 'wb') as f:
                    f.write(download_img.content) # 下载图片

                pic_count += 1

        web_pagenum = web_initnum # 恢复页数

        current_page += 1


# 填写
page_num = '' # 总页数（数字）,比如 '1'
web_initnum = '' # 第一页/bagua/后面的数字即可（数字）,比如 '3795'

if(len(page_num) and len(web_initnum)):
    crawl_web(page_num, web_initnum)
