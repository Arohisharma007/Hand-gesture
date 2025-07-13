#Step - 1  -Import Libraries and capture camera
import cv2
import mediapipe as m #to detect the landmarks
import pyautogui
#Read Camera
def sh():
 cam=cv2.VideoCapture(0)
 cam.set(3,1280)
 cam.set(4,1080)
 drawing=m.solutions.drawing_utils
 hands=m.solutions.hands
 #How many hand u want to detect in frame
 hand_obj=hands.Hands(max_num_hands =1) #1 hand in a frame
 p = -1
 #to count the fingures using keypoints or landmarks on the hand
 def c_f(l): #function to count fingure 
   c =0
   thresh=(l.landmark[0].y*100-l.landmark[9].y*100)/2
   if(l.landmark[5].y*100-l.landmark[8].y*100)>thresh:
      c +=1
   if(l.landmark[9].y*100-l.landmark[12].y*100)>thresh:
      c +=1
   if(l.landmark[13].y*100-l.landmark[16].y*100)>thresh:
      c +=1
   if(l.landmark[17].y*100-l.landmark[20].y*100)>thresh:
      c +=1
   if(l.landmark[5].x*100-l.landmark[4].x*100)>5:
      c +=1
   return c
 while True:
   #To read the frames
   _,frm = cam.read()
   #To flip the fame as it works like a window
   frm= cv2.flip(frm,1)
   res =hand_obj.process(cv2.cvtColor(frm,cv2.COLOR_BGR2RGB))
   if res.multi_hand_landmarks:
      hand_keyPoints =res.multi_hand_landmarks[0]
      c=c_f(hand_keyPoints)
      if not(p==c):
        
         if(c == 1):
           im1 = pyautogui.screenshot()
           im2 = pyautogui.screenshot("C:\\Users\\ASUS\\OneDrive\\Desktop\\PROJECT\\HAND_GESTURE\\.vscode\\ScreenShot\\1.png")
         

         elif (c == 5):
            pyautogui.press("PrtSc")
            
         p =c
         
      drawing.draw_landmarks(frm, hand_keyPoints,hands.HAND_CONNECTIONS)
   #To show the framw
   cv2.imshow("windows",frm)
   #To destroy the window or frame on the screen
   if (cv2.waitKey(1)==27):
      cv2.destroyAllWindows()
      cam.release()
      break