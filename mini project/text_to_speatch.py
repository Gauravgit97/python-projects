import pyttsx3


'''This is the basic code to use the functionality of 'pyttsx3'.
    Which can convert your text to autogenrated speech. 

    Steps:
    1. create an engine for this.
    2. use 'engine.say' method and inside the say you can write any thing(only in English) which you wnat to convert to speech.
    3. use 'engine.runAndWait()' command to wait for the next command.
'''
engine = pyttsx3.init()
engine.say('what you want to say..')
engine.runAndWait()