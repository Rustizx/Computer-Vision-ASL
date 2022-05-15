import cv2
import numpy as np
import time
import PoseModule as pm
 
cap = cv2.VideoCapture(0)
 
detector = pm.poseDetector()
count = 0
dir = 0
pTime = 0
rightAngle = 0

squatAngle = 0
squatDir = 0
while True:

    success, img = cap.read()
    img = cv2.resize(img, (1280, 720))
    img = detector.findPose(img, False)
    lmList = detector.findPosition(img, False)
    # print(lmList)
    if len(lmList) != 0:
        # Right Arm
        squatAngle = detector.findAngle(img, 23, 25, 27)
 
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(squatAngle)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5,
                (255, 0, 0), 5)
 
    cv2.imshow("Image", img)
    cv2.waitKey(1) 