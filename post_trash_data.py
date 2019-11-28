import requests
import threading


def post_data():
    while 1:
        url = 'http://122.51.48.86/commit'
        data = {
            'name': '垃圾数据',
            'text': '请注意数据过滤和重复提交'
        }
        response = requests.post(url, data)


if __name__ == '__main__':
    # 创建多线程
    thread_count = 50
    thread_list = []
    for i in range(thread_count):
        t = threading.Thread(target=post_data, args=())
        thread_list.append(t)
    for item in thread_list:
        item.start()
    for item in thread_list:
        item.join()
