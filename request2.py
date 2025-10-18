from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import pandas as pd
import time
driver = webdriver.Chrome()  # webdriverをChromeのヤツで使います

url = "https://news.yahoo.co.jp"  # YahooのURL
driver.get(url)  # driverでURLのページを開きます

# ブラウザコンソールで確認すると、
# それぞれの記事は、class="style-l2axsx"であり、
# 記事のリンクは、記事内で探すaタグの一番最初のもの.hrefで、
# 記事タイトルは、記事内で探すh2タグの.innerTextで取得できます

# 記事のタイトルを入れる配列
titles = []

# 記事のurlを入れる配列
urls = []
file_path = "YahooNews_datas.csv"
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "sc-1u4589e-0")))

# ここから、driverで要素を見つけていきます
# driverで要素を見つけるには、[ driver.find_element ] もしくは、[ find_elements ] を用います
# 前者は単一の要素もしくは初めに見つけた要素のみ、後者は複数の要素を見つけます

# まず、表示されている記事全部を取得します
# クラスでの要素の参照は、driver.find_elements(By.CLASS_NAME, クラス名)　とします
articles = driver.find_elements(By.CLASS_NAME, "sc-1u4589e-0")

# それでは、articlesの全ての記事のタイトルとURLを配列に納めていきます
for article in articles:
    # 要素をタグ名（a, h1, bodyなど）で取得する場合は、
    # driver.find_elements(By.TAG_NAME, タグ名)　とします
    # driver の部分は、その要素が入っている要素でも可能です

    # タイトルはinnerTextなので、[ .text ] で取得します
    # 元のコード
    title = article.find_element(By.CLASS_NAME, "sc-3ls169-0").text # タグ名にクラス名を指定
    url = article.find_element(By.CLASS_NAME, "sc-1gg21n8-0").get_attribute("href")

    # titles、urlsのそれぞれの配列に、取得したtitle、urlを入れます
    titles.append(title)
    urls.append(url)

print(url)
for i in range(len(titles)):
    print(titles[i], urls[i])

dates = ""

for i in range(len(titles)):
    dates += titles[i] + "," + urls[i] + "\n"

with open(file_path, "w", encoding="utf-8") as file:
    file.write(dates)
if dates:
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(dates)


with open(file_path, 'r', encoding='utf-8') as file:
    # 2. readlines()で、ファイルの内容を行ごとのリストとして取得
    content_list_with_newline = file.readlines()

# 3. 各行の改行文字を取り除く
content_list = [line.strip() for line in content_list_with_newline]
content_list[-1] = content_list[-1].strip()
print(content_list)

df = pd.read_csv(file_path)
df_cleaned = df.drop_duplicates()
output_file_path = "yahoo_news_cleaned_datas.csv"
df_cleaned.to_csv(output_file_path, index=False, encoding="utf-8")
df_cleaned.drop_duplicates(keep=False)

driver.quit()