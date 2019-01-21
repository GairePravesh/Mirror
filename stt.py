import speech_recognition as sr

def parseSpeech(data):
    global Activated
    if 'sleep' in data:
        Activated = False
        print("GoodBye!")


activateCommands = ['hey google', 'ok google', 'hi google', 'hello google']
username = 'Pravesh'
Activated = False

try:
    r = sr.Recognizer()
    m = sr.Microphone()
    print("A moment of silence, please...")
    with m as source: r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    while True:
        print("Wanna start the mirror!")
        with m as source: audio = r.listen(source)
        try:
            # recognize speech using Google Speech Recognition
            value = r.recognize_google(audio)
            print(value)
            if value.lower() in activateCommands:
                Activated = True
                # ease in out lights here
                while Activated:
                    print("Hello {}, what can I do for you!".format(username))
                    with m as source:
                        # start the listning lights
                        audio = r.listen(source)
                        # turn off the listning lights
                    print("Got it! Now to recognize it...")
                    try:
                        value = r.recognize_google(audio)
                        print("you said - '{}'".format(value))
                        # call a task function
                        parseSpeech(value)
                    except:
                        print("I didn't get what you said, Please say that again!")
        except:
            # sleep
            pass

except KeyboardInterrupt:
    pass
