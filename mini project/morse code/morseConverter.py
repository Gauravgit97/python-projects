from resourses import morse_code,reverse_morse


def converter(sentence:str, req: int= 0):
    if req ==0:
        return ' '.join(morse_code[i] for i in sentence.upper())
    elif req ==1:
        return ''.join(reverse_morse[i] for i in sentence.split())


def translate():
    req = int(input('Convert morse->Englis:1 \nConvert English ->morse: 0 \n'))
    sentence = str(input('Enter the sentence: \n'))
    
    return converter(sentence, req)


if '__main__' == __name__:
    print(translate())
