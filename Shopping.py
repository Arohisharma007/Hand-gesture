#Step - 1  -Import Libraries and capture camera
import cv2
import mediapipe as mp #to detect the landmarks
import pyautogui
#Read Camera
def shopping():
   cam=cv2.VideoCapture(0)
   cam.set(3,1280)
   cam.set(4,720)
   drawing=mp.solutions.drawing_utils
   hands=mp.solutions.hands
   screen_width, screen_height = pyautogui.size()
   x1 = y1 = x2 = y2 = 0
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
     #To read the frame
     _,frm = cam.read()
     #To flip the fame as it works like a window
     frm= cv2.flip(frm,1)
     frm_height, frm_width, _ = frm.shape
     res = hand_obj.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))
     hand_keyPoints = res.multi_hand_landmarks 
     if hand_keyPoints:
       for hand in hand_keyPoints : 
          h=hand
          c=c_f(h)
          landmarks=hand.landmark
          if not(p==c): 
            if (c == 3):
             pyautogui.press("up")
            elif (c == 4):
             pyautogui.press("down")
            
            p =c
            
          drawing.draw_landmarks(frm, hand)
          one_hand_landmarks = hand.landmark
          for id, lm in enumerate(one_hand_landmarks):
              x = int(lm.x * frm_width)
              y = int(lm.y * frm_height)
              if id == 8:
                     mouse_x = int(screen_width/frm_width * x)
                     mouse_y = int(screen_height/frm_height * y)
                     cv2.circle(frm, center=(x,y), radius=10, color=(0, 255, 255))
                     pyautogui.moveTo(mouse_x,mouse_y)
                     x1 = x
                     y1 = y
              if id == 4:
                     x2 = x
                     y2 = y
                     cv2.circle(frm, center=(x,y), radius=10, color=(0, 255, 255))
          dist = y2 -y1
          print(dist)
          if(dist<35):
            pyautogui.click()
            print("CLICKED")
   
     #To show the framw
     cv2.imshow("windows",frm)
     #To destroy the window or frame on the screen
     if (cv2.waitKey(1)==27):
      cv2.destroyAllWindows()
      cam.release()
      break 