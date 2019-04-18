#!usr/bin/python
#coding=utf-8
import urllib
import time
import random
import os

def getStatus(url):
    res = urllib.urlopen(url)
    page_status = res.getcode()
    return page_status

class RandomStr:
    list = []

    '''
    a 列表
    b 相连的值
    length 深度
    '''
    bool = os.path.exists('result')
    if bool == False:
        os.mkdir('result')

    f = open('result/result.txt', 'a')
    file = open('result/urls.txt', 'a')



    def create(self, a, length, b = '', leg = 1):

        for i in a[leg-1:]:
            if length == leg:
                item = b + str(i)
                url = "https://pan.baidu.com/s/" +item
                status = getStatus(url)
                time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                print (time_now, status)
                RandomStr.f.write(url + '\r\n')
                RandomStr.list.append(item)

            else:
                self.create(a, length, b + str(i), leg + 1)

    def randomU(self, a, length):
        item = ""
        for i in range(length):
            item += random.choice(a)
        url = "https://pan.baidu.com/s/" + item
        status = getStatus(url)
        if status == 200:
            time_now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            print(time_now, 'sucess 200')
            RandomStr.file.write(url + '\r\n')

    def run(self, a, length):
        i = 0
        while i<10000:
            self.randomU(a, length)
        else:
            self.closeFile()

    def closeFile(self):
        RandomStr.file.close()

    def start(self, a, length):
        self.create(a, length)
        RandomStr.f.close()


def test():
    print ('test')


_inst = RandomStr()
start = _inst.start
run = _inst.run

if __name__ == '__main__' :
    test()