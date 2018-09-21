import os

# Made by Leni
# Latest Update: Thursday. June. 28th. 2018


def tts_function():
    from __utils.tts import TextToSpeech
    from __file.text_list import text_double_list, folder_name

    while True:
        print('\n')
        print(" 전체 다시녹음: 1")
        print(" 일부 다시 녹음: 2")
        print(" 텍스트 녹음: 3")
        print(" Text To Speech 종료: 0")
        action = input(" >> ")

        if action == "1":
            # 전체 다시 녹음
            for index, text_list in enumerate(text_double_list):
                if not os.path.exists('tts/'+folder_name[index]):
                    os.system('mkdir tts/'+folder_name[index])
                for text in text_list:
                    TextToSpeech(text, folder_name[index])
                    # tts.google_cloud_tts(text, folder_name[index])

        elif action == "2":
            # 일부 다시 녹음
            index = int(input("list number >> "))-1
            for text in text_double_list[index]:
                if not os.path.exists('tts/'+folder_name[index]):
                    os.system('mkdir tts/' + folder_name[index])
                TextToSpeech(text, folder_name[index])
                # tts.google_cloud_tts(text, folder_name[index])

        elif action == "3":
            text = input("Enter your text >> ")
            TextToSpeech(text)
            # tts.google_cloud_tts(text)

        elif action == "0":
            break

        else:
            print("\n  Wrong Choice :)\n")