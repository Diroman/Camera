import sender as snd
import camera as cmr
import domain as dmn
import database as dtb


def main():
    sender = snd.Sender("http://127.0.0.1")
    database = dtb.Database()
    domain = dmn.Domain(sender, database)
    camera = cmr.Camera(domain)

    camera.start()
    camera.close_camera()


if __name__ == '__main__':
    main()
