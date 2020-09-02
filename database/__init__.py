class Database:
    classes = {
        0: "People 0",
        1: "People 1",
        2: "People 2",
    }

    def get_class(self, label_ids):
        labels = []
        for label_id in label_ids:
            labels.append(self.classes[label_id])

        return labels
