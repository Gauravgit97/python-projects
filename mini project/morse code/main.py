from audioConvert import soundgen
from morseConverter import converter
from encriptDecript import encripte,decript

message =encripte(str(input('Enter your Message: \n')))
print(message)
morse_encri = converter(message)
print(morse_encri)
# soundgen(morse_encri)
eng_encri = converter(morse_encri,1)
print(decript(eng_encri))


# gaurav joshi
# ,6_=6$N:(+?!
# --..-- -.... ..--.- -...- -.... ...-..- -. ---... -.--. .-.-. ..--.. -.-.--
# GAURAV JOSHI