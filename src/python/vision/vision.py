import cv2
import numpy as np
import time
import vision.PoseModule as pm
import timeit
#import PoseModule as pm

PUSH_UP = 0
BICEP_CURL = 1
SQUAT = 2

global port
port = 0

class FitnessVision:
    def __init__(self):
        self.detector = pm.poseDetector(port)

        self.count = 0
        self.dir = 0
        self.fps = 0
        self.pTime = 0

        self.rightAngle = 0
        self.initial = 0
        self.final = 0

        self.angle = 0
        self.backAngle = 0
        self.currentForm = 0

        self.pushUp = False
        self.bicepCurl = False
        self.squat = False

        self.startTime = 0
        self.endTime = 100

    def setExercise(self, exercise):
        if exercise == PUSH_UP:
            self.pushUp = True
            self.bicepCurl = False
            self.squat = False
        elif exercise == BICEP_CURL:
            self.bicepCurl = True
            self.pushUp = False
            self.squat = False
        else:
            self.squat = True
            self.bicepCurl = False
            self.pushUp = False

    def still(self, camera):
        while True:
            success, img = camera.read()
            if not success:
                print("ERROR: Could not read image")
                break

            img = cv2.resize(img, (1000, 700))
            img = self.detector.findPose(img, True)
            lmList = self.detector.findPosition(img, True)

            #self.setExercise (BICEP_CURL)
            if len(lmList) != 0:
                # Right Arm

                if self.pushUp == True:
                    self.final = 80
                    self.intial = 150
                    self.angle = self.detector.findAngle(img, 12, 14, 16)

                    # Form correction
                    self.currentForm = self.detector.findAngle(img, 12, 24, 26)
                    if self.currentForm < 175:
                        cv2.putText(img, str("INCORRECT FORM"), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5,
                        (255, 0, 0), 5)

                if self.bicepCurl == True:
                    self.final = 55
                    self.intial = 150
                    self.angle = self.detector.findAngle(img, 12, 14, 16)

                    # Form correction
                    self.currentForm = self.detector.findAngle(img, 12, 24, 26)
                    if self.currentForm > 195:
                        cv2.putText(img, str("INCORRECT FORM"), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5,
                        (255, 0, 0), 5)

                if self.squat == True:
                    self.final = 85
                    self.intial = 0
                   # self.backAngle = self.detector.findAngle(img, 11, 23, 25)
                    self.angle = abs(180 - self.detector.findAngle(img, 24, 26, 28))

                    # Form correction
                    self.currentForm = self.detector.findAngle(img, 12, 24, 26)
                    if self.currentForm > 190 or self.currentForm < 160:
                        cv2.putText(img, str("INCORRECT FORM"), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5,
                        (255, 0, 0), 5)

                per = np.interp(self.angle, (self.final, self.initial), (100, 0))
                bar = np.interp(self.angle, (self.final, self.initial), (100, 650))

                color = (255, 0, 255)
                if per == 100:
                    color = (0, 255, 0)
                    if self.dir == 1:
                        self.count += 0.5
                        self.dir = 0
                if per == 0:
                    color = (0, 255, 0)
                    if self.dir == 0:
                        self.count += 0.5
                        self.dir = 1

                # Draw Bar
                cv2.rectangle(img, (1100, 100), (1175, 650), color, 3)
                cv2.rectangle(img, (1100, int(bar)), (1175, 650), color, cv2.FILLED)
                cv2.putText(img, f'{int(per)} %', (1100, 75), cv2.FONT_HERSHEY_PLAIN, 4,
                            color, 4)

                # Draw Curl Count
                cv2.rectangle(img, (0, 450), (250, 720), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, str(int(self.count)), (45, 670), cv2.FONT_HERSHEY_PLAIN, 15,
                        (255, 0, 0), 25)

            cTime = time.time()
            self.fps = 1 / (cTime - self.pTime)
            print(self.fps)
            self.pTime = cTime
            cv2.putText(img, str(int(self.angle)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5,
                        (255, 0, 0), 5)

            ret, buffer = cv2.imencode('.jpg', img)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')



    # def video(self):
    #     while True:
    #         success, img = camera.read()
    #         if not success:
    #             break
    #         img = cv2.resize(img, (1280, 720))
    #         img = self.detector.findPose(img, True)
    #         lmList = self.detector.findPosition(img, True)
    #         if len(lmList) != 0:


    #             if pushUp == True:


    #                 self.final = 80
    #                 self.intial = 150
    #                 self.angle = self.detector.findAngle(img, 12, 14, 16)

    #             if bicepCurl == True:
    #                 self.final = 55
    #                 self.intial = 150
    #                 self.angle = self.detector.findAngle(img, 12, 14, 16)

    #             if squat == True:

    #                 self.final = 265
    #                 self.intial = 190
    #                # self.backAngle = self.detector.findAngle(img, 11, 23, 25)
    #                 self.angle = self.detector.findAngle(img, 24, 26, 28)

    #             per = np.interp(self.angle, (self.final, self.intial), (100, 0))
    #             bar = np.interp(self.angle, (self.final, self.intial), (100, 650))

    #             color = (255, 0, 255)
    #             if per == 100:
    #                 color = (0, 255, 0)
    #                 if self.dir == 1:
    #                     self.count += 0.5
    #                     self.dir = 0
    #             if per == 0:
    #                 color = (0, 255, 0)
    #                 if self.dir == 0:
    #                     self.count += 0.5
    #                     self.dir = 1

    #             # Draw Bar
    #             cv2.rectangle(img, (1100, 100), (1175, 650), color, 3)
    #             cv2.rectangle(img, (1100, int(bar)), (1175, 650), color, cv2.FILLED)
    #             cv2.putText(img, f'{int(per)} %', (1100, 75), cv2.FONT_HERSHEY_PLAIN, 4,
    #                         color, 4)

    #             # Draw Curl Count
    #             cv2.rectangle(img, (0, 450), (250, 720), (0, 255, 0), cv2.FILLED)
    #             cv2.putText(img, str(int(self.count)), (45, 670), cv2.FONT_HERSHEY_PLAIN, 15,
    #                     (255, 0, 0), 25)

    #         cTime = time.time()
    #         fps = 1 / (self.cTime - self.pTime)
    #         self.pTime = cTime
    #         cv2.putText(img, str(int(self.angle)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5,
    #                     (255, 0, 0), 5)

    #         cv2.imshow("Image", img)
    #         cv2.waitKey(1)

if __name__ == "__main__":
    camera = cv2.VideoCapture(port)
    start(camera)
