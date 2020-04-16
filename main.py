import tello
import base64

from tello_control_ui import TelloUI
from img_process import get_coords

def main():

    drone = tello.Tello('', 8890)
    vplayer = TelloUI(drone, "./img/")

	# start the Tkinter mainloop
    vplayer.root.mainloop() 


def test():
    fpath = 'img/red.png'
    retData = get_coords(fpath)
    print(retData)
    print(get_coords('img/redcolor.png'))
    print(get_coords('img/redflower.png'))
    print(get_coords('img/redt.png'))


if __name__ == "__main__":
    main()
    #test()
