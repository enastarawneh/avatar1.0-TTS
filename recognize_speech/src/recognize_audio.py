#!/usr/bin/env python


import numpy
import rospy

import speech_recognition as sr
from rospy_tutorials.msg import Floats
from rospy.numpy_msg import numpy_msg
from std_msgs.msg import String
type="google_speech"
frames=[]

class recognize_audio:

  
    def __init__(self, source, sink ):
      
        self.text_pub = rospy.Subscriber(source, numpy_msg(Floats), self.callback)
        self.text_pub = rospy.Publisher(sink, String, queue_size=10, latch=True)
        

    def callback (self,data):
        r = sr.Recognizer()
        with sr.Microphone() as source2:
          
          numpydata = data.data

              
          audio=sr.AudioData(numpydata.tobytes(),source2.SAMPLE_RATE, source2.SAMPLE_WIDTH )



        if type=="sphinx"  :
          try:
              self.text=r.recognize_sphinx(audio)
         
         
          except sr.UnknownValueError:
             print("Sphinx could not understand audio")
           
          except sr.RequestError as e:
              print("Sphinx error; {0}".format(e))
          
          else:
 

                     
                  self.text_pub.publish(str(self.text))

       

            

 
        if type=="google_speech"   :
          try:
              self.text=r.recognize_google(audio)
         
         
          except sr.UnknownValueError:
             print("Google Speech Recognition could not understand audio")
           
          except sr.RequestError as e:
              print("Could not request results from Google Speech Recognition service")
          
          else:

                  self.text_pub.publish(str(self.text))
                  


        if  type=="google_cloud" :
          try:
              GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""INSERT THE CONTENTS OF THE GOOGLE CLOUD SPEECH JSON CREDENTIALS FILE HERE"""
              self.text=r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS)
         
         
          except sr.UnknownValueError:
             print("Google Cloud Speech could not understand audio")
           
          except sr.RequestError as e:
             print("Could not request results from Google Cloud Speech service; {0}".format(e))
          
          else:
 

                  self.text_pub.publish(str(self.text))



        if  type=="wit_ai" :
          try:
              WIT_AI_KEY = "INSERT WIT.AI API KEY HERE" 
              self.text=r.recognize_wit(audio, key=WIT_AI_KEY)
         
         
          except sr.UnknownValueError:
             print("Wit.ai could not understand audio")
           
          except sr.RequestError as e:
             print("Could not request results from Wit.ai service; {0}".format(e))
          
          else:
 


                  self.text_pub.publish(str(self.text))



        if  type=="bing" :
          try:
              BING_KEY = "INSERT BING API KEY HERE"
              self.text=r.recognize_bing(audio, key=BING_KEY)
         
         
          except sr.UnknownValueError:
             print("Microsoft Bing Voice Recognition could not understand audio")
           
          except sr.RequestError as e:
             print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))

          
          else:


                  self.text_pub.publish(str(self.text))





        if  type=="houndify" :
          try:
              HOUNDIFY_CLIENT_ID = "INSERT HOUNDIFY CLIENT ID HERE"
              HOUNDIFY_CLIENT_ID = "INSERT HOUNDIFY CLIENT ID HERE"
              self.text=r.recognize_houndify(audio, client_id=HOUNDIFY_CLIENT_ID, client_key=HOUNDIFY_CLIENT_KEY)
         
         
          except sr.UnknownValueError:
             print("Houndify could not understand audio")
           
          except sr.RequestError as e:
             print("Could not request results from Houndify service; {0}".format(e))
          
          else:
 


                  self.text_pub.publish(str(self.text))



        if   type=="ibm" :
          try:
              IBM_USERNAME = "INSERT IBM SPEECH TO TEXT USERNAME HERE"
              IBM_PASSWORD = "INSERT IBM SPEECH TO TEXT PASSWORD HERE"
              self.text=r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD)
         
         
          except sr.UnknownValueError:
             print("IBM Speech to Text could not understand audio")
           
          except sr.RequestError as e:
             print("Could not request results from IBM Speech to Text service; {0}".format(e)) 
          
          else:
 


                  self.text_pub.publish(str(self.text))
                  



      
   
def main():
    
    rospy.init_node('recognize_audio')
    
  
    
    arg_defaults = {
       
        'source': '/recognizer/audio',
        'sink': '/recognizer/text1'
        }
    args = updateArgs(arg_defaults)
    recognize_audio(**args)
    try :
       rospy.spin()
    except KeyBoardInterrupt:
      print ("Shutting down")
   

def updateArgs(arg_defaults):
    '''Look up parameters starting in the driver's private parameter space, but
    also searching outer namespaces.  '''
    args = {}
    print ("processing args")
    for name, val in arg_defaults.iteritems():
        full_name = rospy.search_param(name)
        if full_name is None:
            args[name] = val
        else:
            args[name] = rospy.get_param(full_name, val)
            print ("We have args " + val + " value " + args[name])
    return(args)


if __name__ == '__main__':
    main()
