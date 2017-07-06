
#服务器运行入口

import aps_server,zmq_server,http_server,setting
import multiprocessing
def run():
    if setting.CONNECT_SERVER_TYPE == setting.CONNECT_TYPE[0]:
        p1 = multiprocessing.Process(target=zmq_server.run)  # 运行zmq 接口，与客户端进行交互
    elif setting.CONNECT_SERVER_TYPE == setting.CONNECT_TYPE[1]:
        p1 = multiprocessing.Process(target=http_server.run)  # 运行web 接口，与客户端进行交互
    p2 = multiprocessing.Process(target=aps_server.main) #运行服务端的逻辑
    p1.start()
    p2.start()
    print ("".join(['您选择了',setting.CONNECT_SERVER_TYPE,":与客户端交互"]))
if __name__ == '__main__':
    run()