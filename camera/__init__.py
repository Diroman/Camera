import cv2
import models

ESC = 27
SPACE = 32


class Camera:
    cam = None
    img_counter = 0
    domain = None

    def __init__(self, domain):
        self.domain = domain

    def start(self):
        self.cam = cv2.VideoCapture(0)
        cv2.namedWindow("Food")

        image = models.Images()
        while True:
            ret, frame = self.cam.read()
            if not ret:
                print("No camera image received")
                break

            k = cv2.waitKey(1)
            if k % 256 == ESC:
                print("Escape hit, closing...")
                break

            image.image = frame
            image.save(self.img_counter)

            image = self.domain.predict(image)
            self.image_show(image)

            self.img_counter += 1
            image.delete_image()

    def close_camera(self):
        self.cam.release()
        cv2.destroyAllWindows()

    @staticmethod
    def image_show(image):
        result = image.image.copy()
        cv2.vconcat([result, image.image_boxes])
        cv2.imshow("Frame", result)
