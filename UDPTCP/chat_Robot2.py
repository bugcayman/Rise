import socket

def send_msg(udp_socket):
    """获取键盘数据,并将其发送给对方"""
    #1.从键盘输入数据
    msg = input("请输入要发送的数据:")
    #数度对方的ip地址
    dest_ip = input("请输入对方的ip地址:")
    #3.输入对方的port
    dest_port = int(input("请输入对方的端口号:"))
    #4.发送数据
    udp_socket.sendto(msg.encode("utf-8"),(dest_ip,dest_port))

def recv_msg(udp_socket):
    """接收并显示数据"""
    #1.接收数据
    recv_msg = udp_socket.recvfrom(1024)
    #2.解码
    recv_ip = recv_msg[1]
    recv_msg = recv_msg[0].decode("utf-8")
    #3.显示接收到的数据
    print(">>>%s:%s" % (str(recv_ip),recv_msg))

def main():
        #1.创建套接字
        udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        #2.绑定本地信息
        udp_socket.bind(("192.168.78.130",7890))
        while True:
            #3选择功能
            print("="*30)
            print("1:发送消息")
            print("2:接收消息")
            print("3:关闭聊天")
            print("="*30)
            op_num = input("请输入要操作的序号:")
            #4根据选择调用相应的函数
            if op_num == '1':
                send_msg(udp_socket)
            elif op_num == '2':
                recv_msg(udp_socket)
            # elif op_num == '3':
            #     return
            else:
                print("输入错误请重新输入")

def sen_to(udp_socket):
    """发送数据"""
    #1.发送数据
    send_too = input("请输入要发送的内容:")
    #2.对方ip
    send_ip = input("请输入对方ip:")
    #3.对方端口号
    send_port = int(input("请输入对方端口号:"))
    #4发送数据
    udp_socket.sendto(send_too.encode("utf-8"),(send_ip,send_port))

def recv_str(udp_socket):
    """接收数据并显示"""
    #1.接收数据
    recv_str = udp_socket.recvfrom(1024)
    #2.接收数据
    recv_str_ip = recv_str[1]
    recv_data = recv_str[0].decode("utf-8")
    #显示数据
    print("%s,%s" % (str(recv_str_ip),recv_data))

def man():
    #1.创建套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #绑定本地信息
    udp_socket.bind(("192.168.230.128",7899))
    while True:
        #选择功能
        print("="*30)
        print("1:发送消息")
        print("2:接收消息")
        print("="*30)
        op_mun = input("请输入要操作的序号")
        #4.根据选择调用相应的函数
        if op_mun == '1':
            sen_to(udp_socket)
        elif op_mun == '2':
            recv_str(udp_socket)
        else:
            print("输入错误清重新输入:")
if __name__ == '__main__':
    man()
