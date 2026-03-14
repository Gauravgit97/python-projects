# audioConvert.py
'''
1... if you are using windown oprating system dot/dash sound can be genrated by 'winsound' module 'Beep' function:
 code:
        import winsound
        import time

        FREQ = 800  # Hz

        def play_dot():
            winsound.Beep(FREQ, 200)  # 200 ms
            time.sleep(0.1)

        def play_dash():
            winsound.Beep(FREQ, 600)  # 600 ms
            time.sleep(0.1)

        play_dot()
        play_dash()
'''


# resourse.py
'''
1....  To generate the universel key you can use 'uni_key = list(" " + string.punctuation + string.digits + string.ascii_letters)'

'''