# _*_ coding: utf-8 _*_
# @Time    : 2017/5/11 上午9:46
# @Author  : Strongc
# @Author_Email   : qncz2006 # gmail dot com
# @Explain :
# @File    : sendurl.py
# @Software: PyCharm Community Edition


import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server...")
socket = context.socket(zmq.PUSH)
socket.connect("tcp://localhost:5550")

recv_context = zmq.Context()
recv = recv_context.socket(zmq.PULL)
recv.connect('tcp://localhost:5551')

#  Do 10 requests, waiting each time for a response
import time


def sendbulkurl():
    begin = time.time()
    for i in range(0, 2000):
        url = 'https://club.jd.com/comment/skuProductPageComments.action?productId=3938531&score=0&sortType=6&page=%d&pageSize=10&isShadowSku=0' % i
        url = 'https://club.jd.com/comment/skuProductPageComments.action?productId=3938531&score=0&sortType=6&page=0&pageSize=10&isShadowSku=0'

        socket.send_pyobj({'url': url})
        # time.sleep(0.1)
    count = 0
    while True:
        html = recv.recv_pyobj()
        if len(html['html']) < 10:
            print(html['html'])

        print(count, time.time() - begin)
        count += 1


def fangpatest():
    while True:
        url = 'https://club.jd.com/comment/skuProductPageComments.action?productId=3938531&score=0&sortType=6&page=0&pageSize=10&isShadowSku=0'

if __name__ == '__main__':
    sendbulkurl()