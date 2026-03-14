from resourses import uni_key

def encripte(message:str ,pub_key:int=15 ,pri_key:int=17 ):
    pub_val = uni_key[pub_key:]+uni_key[:pub_key]
    pri_val = pub_val[pri_key:]+pub_val[:pri_key]
    encri_mess = ''

    for letter in message.upper():
        index = uni_key.index(letter)
        encri_mess +=pri_val[index]
    
    return encri_mess


def decript(message:str ,pub_key:int = 15,pri_key:int= 17):
    pub_val = uni_key[pub_key:]+uni_key[:pub_key]
    pri_val = pub_val[pri_key:]+pub_val[:pri_key]
    decr_mess = ''

    for letter in message:
        index = pri_val.index(letter)
        decr_mess +=uni_key[index]
    
    return decr_mess



if'__main__'==__name__:
    message = 'sos'
    enc_mes = encripte(message,15,17)
    print(decript(enc_mes,15,17))

