# Made by Leni
# Latest Update: Monday. July. 02nd. 2018


def stt_function():
    from __utils.stt_streaming import SpeechToText
    from __function.tcpServer_function import TcpServer

    print("\n  Plz Start client.py")
    SpeechToText(TcpServer())