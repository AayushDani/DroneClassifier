import cv2

face_cascade = cv2.CascadeClassifier('C:/Users/aayus/Desktop/FootballManager2019 (1)/Football Manager 2019/Football Manager 2019/data/sifacegen/classifiers/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    cv2.circle(img,(320,240),3,(255,0,0),5)

    for (x,y,w,h) in faces:
        pos = []
        
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.circle(img,(x+w//2,y+h//2),2,(0,255,0),5)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,"Deteced Face Size: " + str(h), (6,20), font, 0.75, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.putText(img,"Position Details: ", (6,50), font, 0.75, (0,0,255), 2, cv2.LINE_AA)
        cv2.putText(img,"  Required X Shift: " + str(x+w//2-320), (6,80), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(img,"  Required Y Shift: " + str(y+h//2-240) , (6,110), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(img,"Target Face Size: 185", (6,140), font, 0.75, (0, 0, 255), 2, cv2.LINE_AA)
        cv2.putText(img,"  Required Z Shift: "+str(185-h), (6,170), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)
        pos.append([x,y,w,h,x+w//2,y+h//2])
        print("Deteced Face Size: " + str(h))
        print("Position Details: ")
        print("  Required X Shift: " + str(x+w//2-320))
        print("  Required Y Shift: " + str(y+h//2-240))
        print("Target Face Size: 185")
        print("  Required Z Shift: "+str(185-h))

    try:
        cv2.rectangle(img,(pos[-1][0],pos[-1][1]),(pos[-1][0]+pos[-1][2],pos[-1][1]+pos[-1][3]),(255,0,0),2)
        cv2.circle(img,(pos[-1][4],pos[-1][5]),2,(0,255,0),5)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,"Deteced Face Size: " + str(pos[-1][3]), (6,20), font, 0.75, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.putText(img,"Position Details: ", (6,50), font, 0.75, (0,0,255), 2, cv2.LINE_AA)
        cv2.putText(img,"  Required X Shift: " + str(pos[-1][4]-320), (6,80), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(img,"  Required Y Shift: " + str(pos[-1][5]-240) , (6,110), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(img,"Target Face Size: 185", (6,140), font, 0.75, (0, 0, 255), 2, cv2.LINE_AA)
        cv2.putText(img,"  Required Z Shift: "+str(185-pos[-1][3]), (6,170), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)
        print("Deteced Face Size: " + str(pos[-1][3]))
        print("Position Details: ")
        print("  Required X Shift: " + str(pos[-1][4]-320))
        print("  Required Y Shift: " + str(pos[-1][5]-240))
        print("Target Face Size: 185")
        print("  Required Z Shift: "+str(185-pos[-1][3]))
    except:
        pass
    
    cv2.imshow('Live Feed',img)
    k = cv2.waitKey(30)& 0xff
    if k==27:
        break

cap.release()
cv2.destroyAllWindows()
