import requests
from bs4 import BeautifulSoup
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/103.0.0.0 Safari/537.36"
}
# stream = open('douban_top250_all.txt', mode='w', encoding='utf-8')


def get_page():
    for item in range(0, 250, 25):
        url = 'https://movie.douban.com/top250?start=%s&filter=' % (str(item))
        page_content = requests.get(url, headers=headers)
        page_content.encoding = "utf-8"
        # print(page_content.text)
        page_res = BeautifulSoup(page_content.text, "html.parser")
        movie_items = page_res.find_all("div", class_="item")
        for it in movie_items:
            movie_title = it.find("span", class_="title")
            movie_idx = it.find("em")
            movie_inq = it.find("span", class_="inq")
            # print(str(movie_inq))
            if str(movie_inq) == "None":
                movie_des = "None"
            else:
                movie_des = movie_inq.string
            print(f'{movie_idx.string} is ok')
            # stream.write(f'{movie_idx.string}.{movie_title.string}\n   {movie_des}\n')


get_page()

