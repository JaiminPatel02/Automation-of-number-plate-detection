import cv2
import requests
import os
import numpy as np

frameWidth = 640
frameHeight = 480
nPlateCascade = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")
minArea = 200
color = (255,0,255)

#set path core media 
save_folder = "/Users/jaimin/Desktop/car/Automation-of-number-plate-detection/core/media"
img_count = 0 # counter for image filenames

def send_img(path, mac, addr):
    url = f'http://127.0.0.1:5000/add/{addr}/{mac}'

    with open(path, 'rb') as img:
        name_img = os.path.basename(path)
        files = {
            'file': (name_img, img, 'multipart/form-data', {'Expires': '0'})}
        with requests.Session() as s:
            r = s.post(url, files=files)
            print(r)

#copy path of video IMG_1891.mp4 
cap = cv2.VideoCapture('/Users/jaimin/Desktop/car/Automation-of-number-plate-detection/IMG_1891.mp4')
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)
count = 0

while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    numberPlates = nPlateCascade.detectMultiScale(imgGray, 1.1, 10)
    for (x, y, w, h) in numberPlates:
        area = w*h
        if area >minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
            cv2.putText(img,"Number Plate",(x,y-5),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
            imgRoi = img[y:y+h,x:x+w]
            cv2.imshow("ROI", imgRoi)
            img_count += 1
            # Save the ROI to a file with a unique filename
            cv2.imwrite(save_folder + "/NoPlate_" + str(img_count) + ".jpg", imgRoi)
            # Send the image to server
            send_img(save_folder + "/NoPlate_" + str(img_count) + ".jpg", 'area', '123.345.00.9')
            print(f'numberplate-{img_count}')
    cv2.imshow("Result", img)

    if cv2.waitKey(1) == ord('q'): # Press 'q' to quit
        break

cap.release()
cv2.destroyAllWindows()
