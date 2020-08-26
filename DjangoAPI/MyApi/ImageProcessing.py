#pip install opencv-contrib-python==3.4.4.19

import cv2

image=cv2.imread("ima1.jpg")
text="Hello @";
x=100
y=150
text_image = cv2.putText(image, text, (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.9, [0,0,255], 2)
text_box_image = cv2.rectangle(text_image,(200,70), (450,310), (0,255,0), 2)

while True:
    cv2.imshow("This is my fav actress", text_image)

    if cv2.waitKey(1) == ord("q"):
        # ord('A') = takes up the ascii value of A
        break

#rect_image=cv2.rectangle(image)
print(image)