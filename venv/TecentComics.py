import requests
import re
import js2py
import base64
import urllib.request
import os
import threading


# 处理data数据
def decode_data(data, nonce):
    decode_js = \
        '''
            function decode(data, nonce)
            {
                var T = data.split('');
                var N = nonce;
                var len, locate, str;
                N = N.match(/\d+[a-zA-Z]+/g);
                len = N.length;
                while (len--) {
                    locate = parseInt(N[len]) & 255;    
                    str = N[len].replace(/\d+/g, '');
                    T.splice(locate, str.length);
                }
                T = T.join('');
                return T;
            }
        '''
    handle = js2py.eval_js(decode_js)
    data = handle(data, nonce)
    return data


# 获取该漫画所有的章节
def get_all_src(index_url):
    index_page = requests.get(index_url).text
    titles_patter = re.compile(r'(?<=<span class="tool_chapters_list_title">).*?(?=</span>)')
    title_list = titles_patter.findall(index_page)
    return len(title_list)


# 获取一章的内容
def get_img(index):
    url = "https://ac.qq.com/ComicView/index/id/505430/cid/%s" % index
    try:
        page = requests.get(url).text

        # 获取该章节漫画标题
        single_title_patter = re.compile(r'(?<=<span class="title-comicHeading">).*?(?=</span>)')
        this_title = single_title_patter.findall(page)[0]

        # 以漫画标题命名，新建文件夹
        path = 'D:/onePiece/' + this_title
        if not os.path.exists(path):
            os.mkdir(path)

        # 获取网页中data信息，图片链接都藏在里面
        data_patter = re.compile(r'(?<= var DATA        = \').*?(?=\',)')
        data = data_patter.findall(page)[0]

        # 获取页面nonce， data解密需要
        nonce_patter = re.compile(r'window\[.*?=(.*?);')
        nonce_js = nonce_patter.findall(page)[0]
        nonce_js = re.sub(r'document\.getElementsByTagName\(\'html\'\)', "1", nonce_js)
        nonce_js = re.sub(r'document.children', "1", nonce_js)
        nonce = js2py.eval_js(nonce_js)

        # 初次解密的数据，还需base64解码
        base64_data = decode_data(data, nonce)

        # 解码base64x
        result = base64.b64decode(base64_data).decode('GBK')

        # 从json字符串中获取链接
        url_patter = re.compile(r'(?<="url":").*?(?="})')
        url_list = url_patter.findall(result)
    except Exception as e:
        print("获取目录失败")
        return
    img_count = 0
    for url in url_list:
        url = re.sub(r'\\', "", url)
        try:
            file_path = path + '/' + str(img_count) + '.jpg'
            print(url)
            urllib.request.urlretrieve(url, file_path)
            img_count += 1
        except Exception as e:
            print("获取图片失败")
            continue


if __name__ == '__main__':
    # 创建多线程
    count = get_all_src("https://ac.qq.com/ComicView/index/id/505430/cid/1")
    thread_count = 50
    flag_dict = {}
    # 停下的标志
    stop_flag = 0
    for i in range(thread_count):
        flag_dict[i] = i
    while stop_flag < thread_count:
        thread_list = []
        stop_flag = 0
        for i in range(thread_count):
            t = threading.Thread(target=get_img, args=(flag_dict[i],))
            thread_list.append(t)
        for item in thread_list:
            item.start()
        for item in thread_list:
            item.join()
        for i in range(thread_count):
            flag_dict[i] += thread_count
            if flag_dict[i] > count:
                stop_flag += 1
