from selenium import webdriver  # selenium君からwebdriverをインポート
from selenium.webdriver.common.by import By  # webページの要素の選択に必要なヤツです。インポート！
from selenium.webdriver.chrome.options import Options  # chromeを動かす際にオプションをせっていするのに使います。インポート！

driver = webdriver.Chrome()  # webdriverをChromeのヤツで使います

url = "https://qiita.com/"  # QiitaのURL
driver.get(url)  # driverでURLのページを開きます

# ブラウザコンソールで確認すると、
# それぞれの記事は、class="style-l2axsx"であり、
# 記事のリンクは、記事内で探すaタグの一番最初のもの.hrefで、
# 記事タイトルは、記事内で探すh2タグの.innerTextで取得できます

# 記事のタイトルを入れる配列
titles = []

# 記事のurlを入れる配列
urls = []

# ここから、driverで要素を見つけていきます
# driverで要素を見つけるには、[ driver.find_element ] もしくは、[ find_elements ] を用います
# 前者は単一の要素もしくは初めに見つけた要素のみ、後者は複数の要素を見つけます

# まず、表示されている記事全部を取得します
# クラスでの要素の参照は、driver.find_elements(By.CLASS_NAME, クラス名)　とします
articles = driver.find_elements(By.CLASS_NAME, "style-1w7apwp")

# それでは、articlesの全ての記事のタイトルとURLを配列に納めていきます
for article in articles:
    # 要素をタグ名（a, h1, bodyなど）で取得する場合は、
    # driver.find_elements(By.TAG_NAME, タグ名)　とします
    # driver の部分は、その要素が入っている要素でも可能です

    # タイトルはinnerTextなので、[ .text ] で取得します
    title = article.find_element(By.TAG_NAME, "h2").text

    # URLはアトリビュートなので、[ .get_attribute(アトリビュート名) ] で取得します
    url = article.find_element(By.CLASS_NAME, "style-32d82q").get_attribute("href")

    # titles、urlsのそれぞれの配列に、取得したtitle、urlを入れます
    titles.append(title)
    urls.append(url)

# 最後に、記事のタイトルとその記事のURLを出力します
for i in range(len(titles)):
    print(titles[i], urls[i])

# これで終了です！
# お疲れさまでした！コードを実行してみましょう！

dates = ""

for i in range(len(titles)):
    dates += titles[i] + "," + urls[i] + "\n"

with open("datas.csv", "w", encoding="utf-8") as file:
    file.write(dates)