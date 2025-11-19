import cv2
import numpy as np
from PIL import ImageGrab

def screen_recorder():
    fourcc = cv2.VideoWriter_fourcc(*'xvid')
    out = cv2.VideoWriter('outut.avi',fourcc,5,0,(1366,768))
    
    while True:
        img = ImageGrab.grab()

        #create the array of the immage provided by the ImageGrab.grab() function
        img_np = np.array(img)

        #convert the color of the image because cv2 returns 'bgr' formate but we need in 'rgb'
        frame = cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB)
        cv2.imshow('screen recorder', frame)
        out.write(frame)
        if cv2.waitKey(1)==27:
            break

    out.release()
    cv2.destroyAllWindows()

screen_recorder()
