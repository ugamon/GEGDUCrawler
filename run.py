from client import GetData,ParseThePage
from config import Descriptor
from os import path
import os

if __name__ == '__main__':
    g_bucket = []
    for url in Descriptor(max_depth=110).get_url():
        resp = GetData(url=url,
                       headers={
                           "Content-Type": "text/html;charset=utf-8",
                           "user-agent": "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
                       })
        parser = ParseThePage(content=resp.content)
        g_bucket.extend(parser.get_storage())
    if path.exists("sample.csv"):
        os.remove("sample.csv")

    with open("sample.csv", "a+") as f:
        for i in g_bucket:
            a, b, c = i.values()
            f.write(a+';'+b+';'+c+';'+'\n')

