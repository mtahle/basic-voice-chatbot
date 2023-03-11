import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
#import openai_secret_manager
import openai
 
openai.api_key = "API_KEY"
 
def generate_response(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        top_p=1,
        n=1,
        stop=None,
        temperature=0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    return response.choices[0].text.strip()
 
 
# Define a function to recognize speech
def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone(0) as source:
        print("Say something!")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
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
    tts = gTTS(text)
    tts.save("output.mp3")
    playsound("output.mp3")
 
# Start the voice assistant
while True:
    text = recognize_speech()
    if text != "":
        # Do something with the text (e.g. generate a response using ChatGPT)
 
        response = generate_response(text)
        print("ChatGPT " + response)
        speak_text(response)
    else:
        break
