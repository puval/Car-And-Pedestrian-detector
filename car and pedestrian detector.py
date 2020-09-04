import cv2

video = cv2.VideoCapture('Pedssss.mp4',0)

#Pre-trained car classifier
car_tracker_file = 'cars.xml'
peds_tracker_file = 'pedes.xml'

car_tracker = cv2.CascadeClassifier(car_tracker_file)
peds_tracker = cv2.CascadeClassifier(peds_tracker_file)
while True:
    
    #Read Current Frame
    (read_successful, frame,)= video.read(0)
    
    #safe coding
    if read_successful:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        print('cant')
        break
    
    caaar =  car_tracker.detectMultiScale(gray)
    pedssss = peds_tracker.detectMultiScale(gray)
    
    
    #draw rectangle around cars
    for(x, y, w, h) in caaar:
        cv2.rectangle(frame, (x,y) , (x+w, y+h), (0,0,255), 2)
    
    #draw rectangle around peds
    for(x, y, w, h) in pedssss:
        cv2.rectangle(frame, (x,y) , (x+w, y+h), (0,200,0), 2)
        
    
    cv2.imshow('Car Detector', frame,)
    
    key = cv2.waitKey(1)
    if key==81 or key==113:
        break
    
    
video.release()
cv2.destroyAllWindows()
print("I HOPE ITS DONE")