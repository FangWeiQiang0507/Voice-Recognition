import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():

    with sr.Microphone() as source:
        print('listening...')
        # recording the audio using speech recognition
        # limit 5 secs
        voice = listener.listen(source, phrase_time_limit=5)
    print("Stop.")

    try:
        command = listener.recognize_google(voice, language='en-US')
        # , language='en-US'
        command = command.lower()
        print("You : ", command)
        if 'siri' in command:
            command = command.replace('siri', '')
            print(command)

    except:
        # pass
        talk("Could not understand your audio, PLease try again !")
        return 0
    return command


def run_processing(command):
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif "who are you" or "what are you" in command:
        talk("I am Siri, your virtual assistant")
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    else:
        talk('Please say the command again.')


if __name__ == "__main__":
    user = "on"
    talk("What's your name, Human?")
    name = take_command()
    if user in name:
        while True:
            talk("I am your siri")
            talk("What can i do for you?")
            text = take_command()

            if text == 0:
                continue

            if "exit" in str(text) or "bye" in str(text) or "sleep" in str(text):
                talk("Ok bye, have a nice day" + user + ".")
                break

            # calling process text to process the query
            run_processing(text)
    else:
        talk("You're not my owner, bye!")
