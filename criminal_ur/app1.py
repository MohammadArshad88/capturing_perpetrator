from cv2 import *
from time import *
from mainibm import *
from sms import *

video_obj=VideoCapture('demo.mp4')

while True:
 try:
  res,img=video_obj.read()
  imshow('Video Feed',img)
  imwrite('demo.jpg',img)
  checkface()
  t=waitKey(1)
  if(t==ord('q')):
   break
 except:
  print ('Video Ended')
  break

destroyAllWindows()
video_obj.release()
