'''import cv2
import numpy as np

#distance constants

known_distance= 45
person_width=16
mobile_width=3.0

#object detection constant
confidence_threshold=0.4
nms_threshold= 0.3

#colors for object detected
colors=[(255,0,0),(255,0,255),(0,255,255),(255,255,0),(0,255,0),(255,0,0)]
green=(0,0,0)
black=(0,255,0)

#defining fonts
fonts=cv2.FONT_HERSHEY_COMPLEX

#getting class names from classes.txt file
class_names=[]
with open("classes.txt", "r") as f:
    class_names= [cname.rstrip() for cname in f.readlines()]

    #setting up opencv net

    yoloNet=cv2.dnn.readNet('yolov4-tiny.weights', 'yolov4-tiny.cfg')

    yoloNet.setPreferableBackground(cv2.dnn.DNN_BACKEND_CUDA)

    yoloNet.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA_FP16)

    model= cv2.dnn_DetectionModel(yoloNet)
    model.setInputParams(size=(416, 416), scale= 1/255, swapRB= True)

    #object detection function/method
    def object_detector(image):
        classes, scores, boxes= model.detect(image, confidence_threshold,nms_threshold)
        for (classid, score,boxes) in zip(classes, scores, boxes):

            #define color of each, object based on its class id
            color=colors[int(classid)% len(colors)]
            label= "%s : %f"  %(class_names[classid[0]],score)

#draw rectangle and label on object
            cv2.rectangle(image, box, color, 2)
            cv2.putText(image,label, (box[0]-14), fonts, 0.5, color,2)
             

    cap= cv2.VideoCapture(3)

while True:
    ret, frame= cap.read()
    cv2.imshow('frame', frame)

    key=cv2.waitKey(1)
    if key==ord('q'):
        break
    cv2.destroyAllWindows()
    cap.release()
    '''