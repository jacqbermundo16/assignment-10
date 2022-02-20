#Contact Tracing App
#	- Create a python program that will read QRCode using your webcam
#	- You may use any online QRCode generator to create QRCode
#	- All personal data are in QRCode 
#	- You may decide which personal data to include
#	- All data read from QRCode should be stored in a text file including the date and time it was read


# create a code that scans qr code

import cv2
# import datetime for data and time
import datetime

cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()
while True:
    _, img = cap.read()
    data, bbox, _ = detector.detectAndDecode(img)
    if data:
        a = data

#create a code that writes the data in the qr code to a text file
        with open('QrCodeData.txt', mode = 'a') as file:
            file.write(f'Personal details: \n{a} \nDate and Time %s.' % (datetime.datetime.now())) 
            file.close
            break
            
    cv2.imshow("QRCODEscanner", img)	
    if cv2.waitKey(1) == ord("q"):
	        break


cap.release()
cv2.destroyAllWindows()

# try to scan qr code that contains text and save it as a file

print(data)