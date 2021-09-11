from bs4 import BeautifulSoup
import requests
import csv

url=('http://coreyms.com')
r=requests.get(url)
htmlContent=r.content

csv_file=open('cms_scrape.csv','w')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['headline','paras','yt_link'])
#print(htmlcontent)

soup=BeautifulSoup(htmlContent,'html.parser')
#print(soup.prettify())

article=soup.find('article')
#print(article)
#print(article.prettify())

headline=article.h2.a.text
#print(headline)

#paras = soup.find('div',class_='entry-content').p.text
#print(paras)


vid_src=soup.find('iframe',class_='youtube-player')["src"]  #way to find a link
#print(vid_src)


vid_id= vid_src.split('/')[4]  #yeh split karta hai url ko and 4th index provide kiya hai
vid_id=vid_id.split('?')[0]    #yeh split karta hai url ko and 0th index provide kiya hai
#print(vid_id)

yt_link=f'https://youtube.com/watch?v={vid_id}'
#print(yt_link)


for article in soup.find_all('article'):
    headline = article.h2.a.text
    print(headline)

    paras = soup.find('div',class_='entry-content').p.text
    print(paras)

    vid_id = vid_src.split('/')[4]  # yeh split karta hai url ko and 4th index provide kiya hai
    vid_id = vid_id.split('?')[0]  # yeh split karta hai url ko and 0th index provide kiya hai


    yt_link = f'https://youtube.com/watch?v={vid_id}'
    print(yt_link)

    print()





