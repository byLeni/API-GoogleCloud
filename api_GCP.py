from __function.tts_function import *
from __function.stt_function import *
from __file.library_list import library_name

# Made by Leni
# Latest Update: Monday. July. 02nd. 2018

if __name__ == "__main__":

    # 환경변수가 설정되어 있는지 시작 전 체크한다.
    try:
        os.environ['GOOGLE_APPLICATION_CREDENTIALS']
    except:
        print('\nPlease set GOOGLE_APPLICATION_CREDENTIALS')
        print('{}'.format('- ' * 30))
        print('  $ export GOOGLE_APPLICATION_CREDENTIALS=[json PATH]')
        print('{}'.format('- ' * 30))
        exit(1)

    while True:
        for lib in library_name:
            print('{}'.format(lib))
        library = input(" >> ")

        if library == "exit":
            exit(0)

        else:

            if library:
                if not os.path.exists(library):
                    os.system('mkdir ' + library)

            if library == "tts":
                tts_function()

            elif library == "stt":
                stt_function()

            else:
                os.system('rm -rf '+library)
                print("Don't have \"{}\" library :)".format(library))

            library = ''