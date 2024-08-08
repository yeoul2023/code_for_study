import speech_recognition as sr

r = sr.Recognizer()

audio_file = sr.AudioFile('AISpeaker/drama_test.wav')

with audio_file as source:
    audio = r.record(source)

#sys.stdout = open('stdout.txt', 'w') #-- 텍스트 저장시 사용

#print(r.recognize_google(audio))

#sys.stdout.close() #-- 텍스트 저장시 사용

file_path = 'AISpeaker/sample.txt'
with open(file_path, 'w') as f:
    f.write(r.recognize_google(audio))
    print(f"음성 정보가 {file_path} 경로에 저장되었습니다.")

