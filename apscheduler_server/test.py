import setting
import zmq
context = zmq.Context()
socket_server1 = context.socket(zmq.REQ)
socket_server1.connect('tcp://localhost:' + setting.SERVER_PORT)
poll = zmq.Poller()
poll.register(socket_server1, zmq.POLLIN)

msg = {'a':1,'b':2}
socket_server1.send_json(msg)
a = socket_server1.recv_json()
print (a)