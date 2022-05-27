from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import warnings

warnings.filterwarnings('ignore')
op=webdriver.ChromeOptions()
op.headless = True
op.add_argument("window-size=1920x1080")
op.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36")
b=webdriver.Chrome(options=op)
b.maximize_window()
b.get("https://www.naver.com/")
b.implicitly_wait(10)
b.find_element_by_xpath('//*[@id="query"]').send_keys("암호화폐\n")
b.implicitly_wait(10)
b.find_element_by_xpath('//*[@id="lnb"]/div[1]/div/ul/li[2]/a').click()
b.implicitly_wait(10)

news_data = []

for i in range(2,7):
    html = b.page_source
    soup = BeautifulSoup(html,"html.parser")
    title = soup.select("a.news_tit")
    article = soup.select("a.api_txt_lines.dsc_txt_wrap")
    for j in range(len(title)):
        news = []
        news.append(title[j].text.strip())
        news.append(article[j].text.strip())
        news_data.append(news)
    b.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    b.implicitly_wait(10)
    b.find_element_by_xpath(f'//*[@id="main_pack"]/div[2]/div/div/a[{i}]').click()
    b.implicitly_wait(10)

article_file = open("crypto_article.csv","w",encoding="UTF-8-SIG", newline="")
writer = csv.writer(article_file)
writer.writerow(["기사제목","기사내용"])
writer.writerows(news_data)
article_file.close()
article_file = open("crypto_article.csv","r",encoding="UTF-8-SIG")
for line in article_file:
    print(line)
article_file.close()