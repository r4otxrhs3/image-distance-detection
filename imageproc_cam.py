import cv2 as cv
import numpy as np

#distance constants
KNOWN_DISTANCE= 45
PERSON_WIDTH= 16
MOBILE_WIDTH=3.05
#object detection constant
CONFIDENCE_THRESHOLD= 0.4
NMS_THRESHOLD= 0.3

#colors for object detected 
COLOR= [(255,0,0),(255,0,255),(0,255,255),(255,255,0),(0,255,0),(255,0,0)]
GREEN= (0,0,0)
BLACK=(0,255,0)

#defining fonts
FONTS= cv.FONT_HERSHEY_COMPLEX

#geting class names from classes.txt file

class_names= []
with open("classes.txt","r") as f:
    class_names=[cname.strip() for cname in f.readlines()]

    #setting up opencv net
    yoloNet= cv.dnn.readNetFromDarkNet('yolov2.config', 'yolov2.weights')

    yoloNet.setPreferableBackend(cv.dnn.DNN_BACKEND_CUDA)
    yoloNet.setPreferableTarget(cv.dnn.DNN_TARGET_CUDA_FP16)

    model= cv.dnn_DetectionModel(yoloNet)
    model.setInputParams(size=(416, 416), scale= 1/255, swapRB= True)


    #object detetction function method
    def object_detector(image):
        classes,scores, boxes= model.detect(image, CONFIDENCE_THRESHOLD, NMS_THRESHOLD)
        for (classid, score,box) in zip(classes, scores,boxes):

             #define color of each, object based on its class id
            color= COLORS[int(classid)%len(COLORS)]

            label= "%s:%f" %(class_names[classid[0]], score)

            #draw rectangle on and label on object
            cv.rectangle(image,box,color,2)
            cv.putText(image,label,(box[0], box[1]-14), FONTS, 0.5, color, 2)

    cap= cv.VideoCapture(3)
    while True:
        ret, frame= cap.read()
        object_detector(frame)
        cv.imshow('original', original)
    
    print(capture== True and counter < 10)
    if capture==True and counter<10:
        counter+=1
        cv.putText(
            frame, f"Capturing Img No: {number}", (30,30), fonts, 0.6, PINK, 2)
    else:
        counter=0

    cv.imshow('frame', frame)
    key= cv.waitKey(1)

    if key==ord('c'):
        capture= True
        number+=1
        cv.imwrite(f'ReferenceImages/image{number}.png',original)
    if key==ord('q'):
        cv.destroyAllWindows()

