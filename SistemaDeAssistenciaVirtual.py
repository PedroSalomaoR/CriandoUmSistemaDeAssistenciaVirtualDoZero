import webbrowser
import speech_recognition as sr
from datetime import datetime
import pyttsx3

#Pega a data e hora atual
agora = datetime.now()

#Inicia o engine
engine = pyttsx3.init()

#inicia o reconhecedor do SpeechRecognition
r = sr.Recognizer()

#abri o microfone
with sr.Microphone() as source:
    print("Fale alguma coisa...")
    audio = r.listen(source)

try:
    #converte áudio em texto, usa uma ferramenta do Google
    texto = r.recognize_google(audio, language="pt-BR")
    print("Você disse:", texto)
except sr.UnknownValueError:
    print("Não entendi o que você falou.")
except sr.RequestError:
    print("Erro ao se conectar ao serviço.")

if texto == "Abrir YouTube":
    mensagem = "Abrindo o YouTube..."
    print(mensagem)
    #gera uma voz lendo a mensagem
    engine.say(mensagem)
    #executa e espera terminar
    engine.runAndWait()
    #abre a página inicial do YouTube
    webbrowser.open("https://www.youtube.com")
    
if texto == "Que horas são":
    mensagem = (f"Agora São {agora.strftime("%H:%M:%S")}")
    #gera uma voz lendo a mensagem
    engine.say(mensagem)
    #executa e espera terminar
    engine.runAndWait()
    
if texto == "mostre a previsão do tempo":
    mensagem = "Abrindo a previsão do tempo desta semana..."
    print(mensagem)
    #gera uma voz lendo a mensagem
    engine.say(mensagem)
    #executa e espera terminar
    engine.runAndWait()
    #abre a página da previsão do tempo desta semana 
    webbrowser.open("https://www.google.com/search?q=previs%C3%A3o+do+tempo&rlz=1C1FCXM_pt-PTBR1059BR1059&oq=previsao&gs_lcrp=EgZjaHJvbWUqFQgBEAAYRhiDARiAAhixAxjJAxiABDIGCAAQRRg5MhUIARAAGEYYgwEYgAIYsQMYyQMYgAQyEAgCEAAYgwEYkgMYsQMYgAQyCggDEAAYkgMYgAQyCQgEEAAYChiABDIHCAUQABiABDIHCAYQABiABDIHCAcQABiABDIKCAgQABixAxiABDIHCAkQABiABNIBCjEwMTgwajBqMTWoAgiwAgHxBU_aOr-ONOco&sourceid=chrome&ie=UTF-8&zx=1758043857488&no_sw_cr=1")
    