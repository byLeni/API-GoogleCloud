import socket
import audioop

# Made by Leni
# Latest Update: Monday. July. 02nd. 2018

HOST = ''
RECORDER_PORT = 5555

RECODER_ADDR = (HOST, RECORDER_PORT)

FILE_HEADER_SIZE = 44
FILE_READ_SIZE = 8192
BUF_SIZE = 1024


class TcpServer:
    def __init__(self):
        self.__server_recorder = socket.socket()
        self.__server_recorder.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.__server_recorder.bind(RECODER_ADDR)
        self.__server_recorder.listen(5)

        self.client_recoder, ip = self.__server_recorder.accept()
        print(ip[0])

        self.get_info()

    def get_info(self):
        return self.client_recoder

    def mul_stereo(self, data, width=2):
        # 2채널 스트레오를 모노로 바꾸는 함수
        # 1채널 모노 파일을 사용할 때는 사용하시지 않아도 됩니다.
        lsample = audioop.tomono(data, width, 1, 0)
        rsample = audioop.tomono(data, width, 0, 1)
        return audioop.add(lsample, rsample, width)

    def get_data(self):
        while True:
            data = self.client_recoder.recv(BUF_SIZE)
            # print("data type >> {}".format(data))
            if data[-3:] == b'end':
                if len(data) > 3:
                    data = self.mul_stereo(data[:-3])
                    yield data
                break
            data = self.mul_stereo(data)
            yield data
