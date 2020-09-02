import numpy as np


class Domain:
    sender = None
    database = None

    def __init__(self, sender, database):
        self.sender = sender
        self.database = database

    def predict(self, image):
        request = image.read_dumps_image()

        try:
            response = self.sender.send_request(request)
            boxes, label_ids = transform_boxes(response)
            labels = self.database.get_class(label_ids)

            image.add_boxes(boxes)
            image.add_label(labels)
        except Exception as e:
            print("Error to send image: ", e)

        return image


def transform_boxes(response):
    boxes = []
    labels = []

    if len(response['result']) == 0:
        return boxes

    for i in response['result'][0]['boxes']:
        box = i['box']
        h, w, x, y = box['h'], box['w'], box['x'], box['y']
        """
        x, y ------ w, y
        |              |
        |              |
        |              |
        x, h ------ w, h        
        """
        arr = [[x, y], [w, y], [w, h], [x, h]]

        pts = np.array(arr, np.int32)
        pts = pts.reshape((-1, 1, 2))

        boxes.append(pts)
        labels.append(box['label'])

    return boxes, labels
