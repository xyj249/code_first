import requests
import parsel

base_url = 'https://www.umei.cc/meinvtupian/meinvxiezhen/'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}

response = requests.get(base_url, headers=headers)
response.encoding = response.apparent_encoding
html = response.text

parse = parsel.Selector(html)
href_list = parse.xpath('//div[@class="TypeList"]/ul/li/a/@href').extract()

for href in href_list:
    href_data = requests.get(href).text
    img = parsel.Selector(href_data)
    img_src = img.xpath('//div[@class="ImageBody"]/p/a/img/@src').extract_first()
    img_data = requests.get(img_src, headers=headers).content
    file_name = img_src.split('/')[-1]
    with open('img' + file_name, 'wb') as f:
        print('正在保存文件：{}'.format(file_name))
        f.write(img_data)
