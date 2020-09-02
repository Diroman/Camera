import os
import cv2
import json
import base64


class Images:
    boxes = []
    labels = []
    image = None
    image_boxes = None
    image_file_name = ""

    def __init__(self, image=None):
        self.image = image

    def save(self, file_name):
        self.image_file_name = "images/opencv_frame_{}.png".format(file_name)
        cv2.imwrite(self.image_file_name, self.image)

    def read_dumps_image(self):
        data = open(self.image_file_name, 'rb').read()
        encoded = base64.b64encode(data)
        json_data = json.dumps(encoded.decode('ascii'))

        return json_data

    def delete_image(self):
        os.remove(self.image_file_name)

    def add_boxes(self, boxes):
        square = self.image.copy()
        self.boxes = boxes
        self.image_boxes = cv2.polylines(square, boxes, True, (36, 255, 12), 2)

    def add_labels(self, labels):
        self.labels = labels

        for text, pos in zip(self.labels, self.labels):
            x, y = pos[0], pos[1]
            cv2.putText(self.image_boxes, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)

