# # TTS (Text To Speach)
# # STT (Speach To Text)

# from gtts import gTTS
# from playsound import playsound

# # 영어 문장
# # text = 'Imagine that you have just arrived at a hotel after a tiring 7-hour overnight flight. '
# # tts_en = gTTS(text=text, lang='en')
# # tts_en.save(file_name)
# # playsound(file_name) # .mp3 파일 재생


# # 한글 문장
# file_name = 'sample.mp3'
# # text = '파이썬을 배우면 이런 것도 할 수 있어요'
# # tts_ko = gTTS(text=text, lang='ko')
# # tts_ko.save(file_name)
# # playsound(file_name) # .mp3 파일 재생

# # 긴 문장 처리
# with open('sample.text', 'r', encoding='utf-8') as f:
#     text = f.read()


# tts_ko = gTTS(text=text, lang='ko')
# tts_ko.save(file_name)
# playsound(file_name) # .mp3 파일 재생

from gtts import gTTS
import speech_recognition as sr

with open('AISpeaker/sample.txt', 'r', encoding='utf-8') as f:
    text = f.read()

file_name = 'sample2.mp3'
tts_lan = gTTS(text=text, lang='ko')
tts_lan.save(file_name)