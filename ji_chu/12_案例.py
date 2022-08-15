import re
import requests
import time

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

response = requests.get("https://baijiahao.baidu.com/s?id=1702640148270885315&wfr=spider&for=pc",  headers = headers)

response.encoding=response.apparent_encoding
content = response.text

pattern = r'src="(.*?)"'

result = re.findall(pattern,content)
print(result)

# 将结果保存到本地
if len(result)>0:
 i = 0
 for pic in result:
  response = requests.get(pic,  headers = headers)
  with open(f'img/pic{i}.jpg','wb') as s:
   s.write(response.content)
   print(f'完成{i}')
   time.sleep(1)
  i+=1 