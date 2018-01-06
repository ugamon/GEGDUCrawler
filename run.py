from client import GetRawData,ParseThePage
from config import Descriptor
from os import path
import os

if __name__ == '__main__':

    for url in Descriptor(max_depth=150).get_url():
        resp = GetRawData(url=url,
                          interval=6,

                          headers={
                              "Content-Type": "text/html;charset=utf-8",
                              "user-agent": "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
                          })

        inst = ParseThePage(resp.content).output(r'samples\datafile.csv')