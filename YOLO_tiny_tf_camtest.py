"""
Level : Fun
Dec : 用Cam验证YOLO的能力
Created at : 2016.12.04
Author : Iflier
"""
print(__doc__)

import cv2
import numpy as np
import YOLO_tiny_tf_cam

yolo = YOLO_tiny_tf_cam.YOLO_TF(imshow=True)
cap = cv2.VideoCapture(0)
while (cap.isOpened()):
    ret,frame = cap.read()
    yolo.detect_from_cvmat(frame)
    if cv2.waitKey(1)&0xff == 27:        
        break
cap.release()
cv2.destroyAllWindows()
