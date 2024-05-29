import speech_recognition as sr
import pyttsx3
import openai

def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

r = sr.Recognizer()
with sr.Microphone() as source2:
      r.adjust_for_ambient_noise(source2, duration = 0.2)
      audio2 = r.listen(source2)

def record_text():
    while(1):
        try:
            print("Jarvis thinks you said " + r.recognize_(audio2,))
                
        except sr.RequestError as e:
            print("Could not request results: {0}".format(e))
            
        except sr.UnknownValueError:
            print("unknown error occurred")
            return

def send_to_chatGPT(messages, model = "gpt-3.5-turbo"):
    response = openai.chat.completions.create(
        model = model,
        messages = messages,
        max_tokens = 200,
        n = 1,
        stop = None,
        temperature = 0.5,
    )
    
    message = response.choices[0].message.content
    messages.append(response.choices[0].message)
    return message


messages = []
while(1):
    text = record_text()
    messages.append({"role": "user", "content": text})
    response = send_to_chatGPT(messages)
    SpeakText(response)
    
    print(response)