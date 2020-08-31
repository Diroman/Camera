import sender
import camera


def main():
    sender_obj = sender.Sender("http://127.0.0.1")
    camera_obj = camera.Camera(sender_obj)

    camera_obj.start()
    camera_obj.close_camera()


if __name__ == '__main__':
    main()
