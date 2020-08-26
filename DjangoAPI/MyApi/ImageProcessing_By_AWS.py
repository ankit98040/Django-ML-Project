import boto3
import requests
import cv2

def ObjectDetection(imagePath, Service):
    session = boto3.Session(profile_name="default")
    Service = session.client("rekognition")
    image = open(imagePath, "rb").read() #read in byte
    imgH, imgW = cv2.imread(imagePath).shape[:2]
    MyImage = cv2.imread(imagePath)


    response = Service.detect_labels(Image = {"Bytes": image})
    for objects in response["Labels"]:

        if objects["Instances"]:
            for boxs in objects["Instances"]:
                objectName = objects["Name"]
                box = boxs["BoundingBox"]
                x = int(imgW * box["Left"])
                y = int(imgH * box["Top"])
                w = int(imgW * box["Width"])
                h = int(imgH * box["Height"])
                print(x,y,w,h)
                MyImage = cv2.rectangle(MyImage, (x,y), (x+w, y+h), (0,200,13), 2)
                MyImage = cv2.putText(MyImage, objectName, (x,y-20), cv2.FONT_HERSHEY_SIMPLEX, 0.9, [0,0,255], 2)
            #print(objects["Name"], "---", objects["Confidence"])
    cv2.imwrite("detected.jpg", MyImage)

image = "/Users/ankit/Desktop/Projects/DJANGO/Django-ML-Project/DjangoAPI/MyApi/img3.jpg"
ObjectDetection(image, "Object Detection")
