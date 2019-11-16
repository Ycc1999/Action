import cv2
from PIL import Image
import time
import pyautogui
import threading
import util
from openpose import process
from face import face_track
from action import waving_hands
from action import falling

global rh_xdzb, reh_xdzb, rh_speed, reh_distance, res_distance, lh_xdzb, leh_xdzb, lh_speed, leh_distance, les_distance, wave_click
rh_xdzb = []
reh_xdzb = []
rh_speed = []
reh_distance = [(0, 0)]
res_distance = [(0, 0)]
lh_xdzb = []
leh_xdzb = []
lh_speed = []
leh_distance = [(0, 0)]
les_distance = [(0, 0)]
wave_click = 0

global fall_click, jlsdH, jlsdH5, jlsdW, stature, ave_statu
fall_click = 0
jlsdH = []
jlsdH5 = []
jlsdW = []
stature = []
ave_statu = 0


def track():
    cap = cv2.VideoCapture(0)
    vi = cap.isOpened()
    if vi == True:
        while(1):

            ret, frame = cap.read()
            frame_face = face_track(frame)
            cv2.namedWindow("capture", 0)
            cv2.imshow("capture", frame_face )

            if cv2.waitKey(1) == 27:
                break
        cap.release()
        cv2.destroyAllWindows()

def action_recognition():

    global rh_xdzb, reh_xdzb, rh_speed, reh_distance, res_distance, lh_xdzb, leh_xdzb, lh_speed, leh_distance, les_distance, wave_click
    global fall_click, jlsdH, jlsdH5, jlsdW, stature, ave_statu

    cap = cv2.VideoCapture(0)
    vi = cap.isOpened()
    if (vi == True):
        while (1):

            tic1 = time.time()
            lenx = []
            ret, frame = cap.read()
            (wide, high) = (160, 120)
            frame = cv2.resize(frame, (wide, high), interpolation=cv2.INTER_AREA)
            canvas, zuobiao = process(frame)  # 取出坐标
            cv2.namedWindow("pose", 0)
            cv2.imshow("pose", canvas)

            if zuobiao != []:
                for i in range(len(zuobiao)):
                    lenx.append(zuobiao[i][1][0] - int(wide / 2))
                a = lenx.index(min(lenx))
                zuobiao = zuobiao[a]

                rh_xdzb,reh_xdzb,rh_speed,reh_distance,res_distance,lh_xdzb,leh_xdzb,lh_speed,leh_distance,les_distance,wave_click = waving_hands(zuobiao,rh_xdzb,reh_xdzb,rh_speed,reh_distance,res_distance,lh_xdzb,leh_xdzb,lh_speed,leh_distance,les_distance,wave_click)

                fall_click, jlsdH, jlsdH5, jlsdW, stature, ave_statu = falling(zuobiao,fall_click,jlsdH,jlsdH5,jlsdW,stature,ave_statu)

            if cv2.waitKey(1) == 27:
                break
        cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':

    print('start processing...')
    threads = []
    t1 = threading.Thread(target=action_recognition)
    threads.append(t1)
    t2 = threading.Thread(target=track)
    threads.append(t2)


    t1.setDaemon(True)
    t1.start()
    t1.join()

    print("all over")
