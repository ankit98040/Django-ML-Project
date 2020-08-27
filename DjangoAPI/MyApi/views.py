from django.shortcuts import render, redirect
from django.http import HttpResponse
from MyApi.models import MyFile
from django.conf import settings
import boto3
import requests
import cv2


def ObjectDetection(imagePath):
    session = boto3.Session(profile_name="default")
    Service = session.client("rekognition")
    image = open(imagePath, "rb").read() #read in byte
    imgH, imgW = cv2.imread(imagePath).shape[:2]
    MyImage = cv2.imread(imagePath)


    response = Service.detect_labels(Image = {"Bytes": image})
    #response = Service.recognize_celebrities(Image={"Bytes": image})
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

    cv2.imwrite(imagePath, MyImage)



def Celebrities_Detection(imagePath):
    session = boto3.Session(profile_name="default")
    Service = session.client("rekognition")
    image = open(imagePath, "rb").read() #read in byte
    imgH, imgW = cv2.imread(imagePath).shape[:2]
    MyImage = cv2.imread(imagePath)


    #response = Service.detect_labels(Image = {"Bytes": image})
    response = Service.recognize_celebrities(Image={"Bytes": image})
    for objects in response["CelebrityFaces"]:
        CelName = objects["Name"]

        Face = objects["Face"]
        objectName = objects["Name"]
        box = Face["BoundingBox"]
        x = int(imgW * box["Left"])
        y = int(imgH * box["Top"])
        w = int(imgW * box["Width"])
        h = int(imgH * box["Height"])
        print(x,y,w,h)

        MyImage = cv2.rectangle(MyImage, (x,y), (x+w, y+h), (0,200,13), 2)
        MyImage = cv2.putText(MyImage, CelName, (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.9, [0,0,255], 2)


    cv2.imwrite(imagePath, MyImage)




def Home(request):
    if request.method=="POST":
        img = request.FILES["image"]
        service = request.POST["service"]

        data = MyFile.objects.create(image = img)
        path = str(settings.MEDIA_ROOT + "/" + data.image.name )

        if service=="Object Detection":
            ObjectDetection(path)

        if service=="Celebrity Detection":
            Celebrities_Detection(path)

        url = "http:127.0.0.1:8000" + data.image.url
        return redirect(url)
    return render(request, "index.html")