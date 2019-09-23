import requests
import re
import js2py


# 获取该漫画所有的章节
def get_all_src(index_url):
    index_page = requests.get(index_url).text
    titles_patter = re.compile(r'(?<=<span class="tool_chapters_list_title">).*?(?=</span>)')
    title_list = titles_patter.findall(index_page)
    return len(title_list)


# 获取一章的内容
def get_img(index):
    url = "https://ac.qq.com/ComicView/index/id/505430/cid/%s" % index
    page = requests.get(url).text
    try:
        # 获取网页中data信息，图片链接都藏在里面
        data_patter = re.compile(r'(?<= var DATA        = \').*?(?=\',)')
        data = data_patter.findall(page)[0]
        # 获取页面nonce， data解密需要
        nonce_patter = re.compile(r'window\[.*?=(.*?);')
        nonce_js = nonce_patter.findall(page)
        nonce = js2py.eval_js(nonce_js)
        print(nonce)
    except Exception as e:
        print(e)
        print("获取目录出错了！")


if __name__ == '__main__':
    count = get_all_src("https://ac.qq.com/ComicView/index/id/505430/cid/1")
    for i in range(1, count + 1):
        get_img(i)
