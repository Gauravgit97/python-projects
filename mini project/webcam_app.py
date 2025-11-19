import cv2

img_cap = cv2.VideoCapture(0)
result = True

while(result):
    ret, frame = img_cap.read()
    cv2.imwrite('test.jpg',frame)
    result = False
    print('image captured...')

img_cap.release()
