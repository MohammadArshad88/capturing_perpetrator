import json
from ibm_watson import VisualRecognitionV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from face import *
from sms import *
authenticator = IAMAuthenticator('cZuavjzjVKgTfk2QZOVfgSZOp9ZMjBOSfLGl_tRzBMuE')
visual_recognition = VisualRecognitionV3(
    version='2018-03-19',
    authenticator=authenticator
)

visual_recognition.set_service_url('https://api.us-south.visual-recognition.watson.cloud.ibm.com/instances/d506e268-f521-4deb-9085-0ace14750495')

def checkface():
    print("Scanning Criminal Database")
    for i in range(1,21):
        str1=face_reg(REGION,ACCESS_ID,ACCESS_KEY,source="criminals/"+str(i)+".jpeg",target='demo.jpg')
        #print(str1)
        if(str1==1):
            print("Criminal Found with image Number "+str(i)+".jpeg")
            sendsms()
    print("Scanning Completed")
def findimage():
    with open('demo.jpg', 'rb') as images_file:
        classes = visual_recognition.classify(
        images_file=images_file,
        threshold='0.6',
        owners=["me"]).get_result()
    a=json.dumps(classes, indent=2)
    #print(a)
    a=a.split('\n')
    count=0
    b=''
    c=''
    try:
        for i in a:
         count+=1
         if(count==10):
          b=i.split(": ")
          b=b[1]
          b=b[1:-2]
          #print(b)
          if(count==11):
           c=i.split(": ")
           c=float(c[1])
          #print(c)
           if(b=="criminal_gestures" and c>=0.7):
              print("Found Some abnormal gesture")
              checkface()
              sendsms()
          elif(b=="criminals_guns" and c>=0.7):
              print("Found Someone with gun")
	      checkface()
              sendsms()	
          elif(b=="criminals_knifes" and c>=0.7):
              print("Found Someone with knifes")
              checkface()
	      sendsms()	
          else:
              print("Normal")
    except:
        print("No Class Found")
#checkface()
