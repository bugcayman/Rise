import socket

if __name__ == '__main__':
    #创建udpsocket
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #设置socket的选项,允许发送广播消息
    udp_socket.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,True)
    #发送广播消息
    udp_socket.sendto("大家好,我叫小郭同学,青多多关照".encode("utf-8"),("255.255.255.255",9090))
    # 关闭socket
    udp_socket.close()