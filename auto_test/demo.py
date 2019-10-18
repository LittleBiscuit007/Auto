import requests
import json

from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class RunMain:
    def __init__(self, url, method, data=None):
        self.data = data
        self.url = url
        self.method = method
        self.res = self.run_main()

    def url_post(self):
        res = requests.post(url=self.url, data=self.data, verify=False).json()
        return res

    def url_get(self):
        res = requests.get(url=self.url, data=self.data, verify=False).json()
        return res

        # res 返回的json数据
        # indent 缩进展示
        # sort_keys 排序
        # return json.dumps(res,indent = 2, sort_keys = True)

    # 再封装一个方法，让它执行post和get请求
    def run_main(self):
        res = None
        if self.method == 'GET':
            res = self.url_get()

        else:
            res = self.url_post()
        return res


if __name__ == "__main__":
    url_p = "https://easy-mock.com/mock/5da58a1db3d26c45bb3af76e/example/upload"
    data = {
        "hello": "world",
        "botoo": "123"
    }

    url_g = "https://easy-mock.com/mock/5da58a1db3d26c45bb3af76e/example/restful/:id/list"

    g = RunMain(url_g, "GET").res

    print(g)
    p = RunMain(url_p, "POST", data=data).res

    print(p)
