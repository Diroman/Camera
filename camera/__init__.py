import os
import numpy as np
import cv2
import time

ESC = 27
SPACE = 32


class Camera:
    cam = None
    img_counter = 0
    sender = None

    def __init__(self, sender_obj):
        self.sender = sender_obj

    def start(self):
        self.cam = cv2.VideoCapture(0)
        cv2.namedWindow("Food")
        while True:
            ret, frame = self.cam.read()
            if not ret:
                print("No camera image received")
                break

            k = cv2.waitKey(1)
            if k % 256 == ESC:
                print("Escape hit, closing...")
                break

            img_name = self.save_image(frame)
            try:
                response = self.sender.send_request(img_name)
                self.image_show(frame, response['boxes'])
                # time.sleep(0.1)
            except Exception as e:
                self.image_show(frame)
                print("Error to send image: ", e)

            self.img_counter += 1
            os.remove(img_name)

    def close_camera(self):
        self.cam.release()
        cv2.destroyAllWindows()

    @staticmethod
    def image_show(image, boxes=None):
        if boxes is None:
            boxes = []

        square = image.copy()
        if len(boxes) != 0:
            pts = np.array(boxes, np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(square, [pts], True, (0, 255, 255), 2)

        image = cv2.vconcat([image, square])
        cv2.imshow("Frame", image)

        return image

    def save_image(self, image):
        img_name = "opencv_frame_{}.png".format(self.img_counter)
        cv2.imwrite(img_name, image)
        # print("{} written".format(img_name))

        return img_name
