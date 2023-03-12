import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import openai
import json
import os



 
openai.api_key = "sk-key"
messages= {}
system_message = {}
user_message = {}
user_assistant = {}
user_assistant["role"] = "assistant"
user_assistant["content"] = ""
user_message["role"] = "user"
user_message["content"] = "Why should DevOps engineer learn kubernetes?"
system_message["role"] = "system"
system_message["content"] = "You are a chatbot"
messages = [system_message,user_message,user_assistant]
json_messages = json.dumps(messages)
 
def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=prompt,
    )
    return response.choices[0].message
 
 
# Define a function to recognize speech
def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone(0) as source:
        print("Say something!")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language="ar-JO")
            print("You said: " + text)
            return text
        except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")
            return ""
        except sr.RequestError as e:
            print("Sorry, I could not request results from Google Speech Recognition service; {0}".format(e))
            return ""
 
# Define a function to speak text
def speak_text(text):
    tts = gTTS(text, lang="ar")
    tts.save("output.mp3")
    try:
        playsound("output.mp3")
    except:
        print("Error playing sound")
    finally:
        os.remove("output.mp3")
  
 
# Start the voice assistant
while True:
    try:

        text = recognize_speech()
        if text != "":
            # Do something with the text (e.g. generate a response using ChatGPT)
            user_message["content"] = text
            # print("messages:", messages, "was sent and waiting for the ChatGPT response")
            response = generate_response(messages)
            print(response["content"])
            speak_text(response["content"])
            user_assistant["content"] = response["content"]
            print("latest messages:", messages)
        else:
            continue
    except KeyboardInterrupt:
        break
