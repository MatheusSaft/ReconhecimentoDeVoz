import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone(device_index = 0) as source:
 print("Fale algo: ")
 audio = r.listen(source)

try:
  print('Google Speech Recognition: ' + r.recognize_google(audio,language='pt-BR'))
  text = r.recognize_google(audio, language = "pt-BR")
  print('Você disse: ' + text.captalize())
except:
  print("Não consegui entender você !")
