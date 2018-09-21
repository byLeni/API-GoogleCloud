# google.cloud text to speech 는 아직 beta 버전인가 보다..
from google.cloud import texttospeech_v1beta1


class TextToSpeech:
    def __init__(self, text, folder=None):
        self.DEFAULT_FOLDER_PATH = 'tts/'
        self.google_cloud_tts(text, folder)

    def google_cloud_tts(self, text, folder):
        try:
            client = texttospeech_v1beta1.TextToSpeechClient()
        except Exception as e:
            print('\n')
            print('{}'.format('- '*30))
            print('  Error, client = texttospeech_v1beta1.TextToSpeechClient()\n  {}'.format(e))
            print('{}'.format('- ' *30))
            return

        input_text = texttospeech_v1beta1.types.SynthesisInput(text=text)

        # Note: the voice can also be specified by name.
        # Names of voices can be retrieved with client.list_voices().
        voice = texttospeech_v1beta1.types.VoiceSelectionParams(
            language_code='ko-KR',
            ssml_gender=texttospeech_v1beta1.enums.SsmlVoiceGender.FEMALE)

        audio_config = texttospeech_v1beta1.types.AudioConfig(
            audio_encoding=texttospeech_v1beta1.enums.AudioEncoding.MP3
            # speaking_rate = 말 하는 속도를 적어놓은 것이다, double 형태로 지정할 수 있고 범위가 있었는데.. document 에 있으니 참고바람..
            # 삭제하면 1.0배속으로 된다.
            # speaking_rate=0.4)
        )

        response = client.synthesize_speech(input_text, voice, audio_config)

        # The response's audio_content is binary.
        if folder is not None:
            output_gcltts = self.DEFAULT_FOLDER_PATH + folder + '/' + text + '.mp3'
        else:
            output_gcltts = self.DEFAULT_FOLDER_PATH + text + '.mp3'

        with open(output_gcltts, 'wb') as out:
            out.write(response.audio_content)
            print('Audio content written to file {}'.format(output_gcltts))
