from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import warnings
warnings.filterwarnings('ignore')

검색어 = input("검색어를 입력하세요.")

op=webdriver.ChromeOptions()
op.headless = True
op.add_argument("window-size=1920x1080")
op.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36")
b=webdriver.Chrome(options=op)
b.maximize_window()
b.get("https://www.naver.com/")
b.implicitly_wait(10)
b.find_element_by_xpath('//*[@id="NM_FAVORITE"]/div[1]/ul[2]/li[2]/a').click()
b.implicitly_wait(10)
b.find_element_by_xpath('/html/body/section/header/div[1]/div/div/div[2]/div[3]/a').click()
b.implicitly_wait(10)
b.find_element_by_xpath('//*[@id="u_hs"]/div/div/input').send_keys(f"{검색어}\n")
b.switch_to.window(b.window_handles[1])
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
file = f'{검색어}.csv'
article_file = open(f'{file}',"w",encoding="UTF-8-SIG", newline="")
writer = csv.writer(article_file)
writer.writerow(["기사제목","기사내용"])
writer.writerows(news_data)
article_file.close()
article_file = open(f'{file}',"r",encoding="UTF-8-SIG")
for line in article_file:
    print(line)

