import re
import requests
import os
# 从网络获取一张图片的html标签
image = '<img class="currentImg" id="currentImg" src="https://timgsa.baidu.com/timg?\
image&amp;quality=80&amp;size=b9999_10000&amp;sec=1563443144123&amp;di=894cd69cad8391d0198bf0d3e63b1ab5&amp;\
imgtype=0&amp;src=http%3A%2F%2Fpic33.nipic.com%2F20130924%2F9822353_015119969000_2.jpg" \
width="508.71794871795" height="310" style="top: 96px; left: 0px; width: 490px; height: 298.594px; cursor: pointer;" \
log-rightclick="p=5.102" title="点击查看源网页">'
# 使用正则表达式获取src后面的内容
m = re.match(r'<img class="currentImg" id="currentImg" src="(.+?)"', image)
print(m.group(1))
image_path = m.group(1)

# 如果想下载获取的图片链接我们结合requests和文件保存完成
response = requests.get(image_path)
# 获取响应信息的内容
result = response.content
# 获取图片名称
filename = image_path[image_path.rfind('%')+1:]
path = os.path.join(r'../img', filename)
# 保存到本地将图片
with open(path, 'wb') as wstream:
    wstream.write(result)
print('文件下载结束！')