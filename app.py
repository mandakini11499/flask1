import flask
import numpy as num
import cv2
from flask import Flask

app = Flask(__name__)

frames_per_seconds=60
video=cv2.VideoCapture(0)
if video.isOpened()==False:
    print("error reading video file")

frame_width=int(video.get(3))
frame_height=int(video.get(4))
size=(frame_width,frame_height)
result=cv2.VideoWriter('filename.avi',cv2.VideoWriter_fourcc(* 'MJPG'),10,size)
while(True):
    ret,frame=video.read()
    if ret==True:
        result.write(frame)
        cv2.imshow('Frame',frame)
        if cv2.waitKey(1)& 0xFF == ord('s'):
            break
        else:
            break
video.release()
result.release()
cv2.destroyAllWindows()
print("the video was successfully saved")










if __name__ == '__main__':
    app.run()
