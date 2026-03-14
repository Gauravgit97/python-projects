from morseConverter import converter
from playsound import playsound
from time import sleep

FREQ = 800  

def play_dot():
    playsound('sound effects\dot.mp3')
    sleep(0.01)           

def play_dash():
    playsound('sound effects\dash.mp3')
    sleep(0.01)

def soundgen(message:str):
    for i in message:
        if i ==".":
            play_dot()
        elif i =='-':
            play_dash()


if '__main__'==__name__:
    sentin = str(input('Enter the sentence: \n'))
    message = converter(sentin)
    soundgen(message)