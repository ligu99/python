import re
import requests

"""
<li>
            <div class="item">
                <div class="pic">
                    <em class="">24</em>
                    <a href="https://movie.douban.com/subject/6786002/">
                        <img width="100" alt="触不可及" src="https://img9.doubanio.com/view/photo/s_ratio_poster/public/p1454261925.jpg" class="">
                    </a>
                </div>
                <div class="info">
                    <div class="hd">
                        <a href="https://movie.douban.com/subject/6786002/" class="">
                            <span class="title">触不可及</span>
                                    <span class="title">&nbsp;/&nbsp;Intouchables</span>
                                <span class="other">&nbsp;/&nbsp;闪亮人生(港)  /  逆转人生(台)</span>
                        </a>


                            <span class="playable">[可播放]</span>
                    </div>
                    <div class="bd">
                        <p class="">
                            导演: 奥利维·那卡什 Olivier Nakache / 艾力克·托兰达 Eric Toledano&nbsp;&nbsp;&nbsp;主...<br>
                            2011&nbsp;/&nbsp;法国&nbsp;/&nbsp;剧情 喜剧
                        </p>

                        
                        <div class="star">
                                <span class="rating45-t"></span>
                                <span class="rating_num" property="v:average">9.3</span>
                                <span property="v:best" content="10.0"></span>
                                <span>1000112人评价</span>
                        </div>

                            <p class="quote">
                                <span class="inq">满满温情的高雅喜剧。</span>
                            </p>
                    </div>
                </div>
            </div>
        </li>
"""
"""
url = "https://movie.douban.com/top250"
url2 = "https://movie.douban.com/top250?start=25&filter="
url2 = "https://movie.douban.com/top250?start=50&filter="
"""
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/103.0.0.0 Safari/537.36"
}
stream = open('douban_top250_quote.txt', mode='w', encoding='utf-8')
# .*? => (?P<变量名>正则) 提取正则匹配到的内容

pattern = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>.*?'
                     r'<p class="quote">.*?<span class="inq">(?P<quote>.*?)</span>', re.S)
# pattern = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>', re.S)


def get_page():
    for item in range(225, 250, 25):
        url = 'https://movie.douban.com/top250?start=%s&filter=' % (str(item))
        resp = requests.get(url, headers=headers)
        page_content = resp.text
        f_obj = pattern.finditer(page_content)
        write_file(f_obj, item)


def write_file(f_obj, idx):
    for item in f_obj:
        idx += 1
        print(f'{idx}.{item.group("name")}_{item.group("quote")}')
        # stream.write(f'{idx}.{item.group("name")}\n   "{item.group("quote")}"\n')


get_page()



