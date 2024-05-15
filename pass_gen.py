import string  #this lybrairy will generate the password
import random


def gen_pass(pas_len=10):
    
    """Here is the 'string' method.
    Which provide us the symble which we need to create a password..."""

    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    random.shuffle(s)
    pas = ("".join(s[0:pas_len]))
    print(pas)

gen_pass()