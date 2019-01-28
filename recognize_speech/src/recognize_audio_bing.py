#!/usr/bin/env python


import numpy
import rospy

import speech_recognition as sr
from rospy_tutorials.msg import Floats
from rospy.numpy_msg import numpy_msg
from std_msgs.msg import String



class recognize_audio_bing:

  
    def __init__(self, source, sink ):
      
        self.text_pub = rospy.Subscriber(source, numpy_msg(Floats), self.callback)
        self.text_pub = rospy.Publisher(sink, String, queue_size=10, latch=True)
        

    def callback (self,data):
        r = sr.Recognizer()
        with sr.Microphone() as source2:
          
          numpydata = data.data

              
          audio=sr.AudioData(numpydata.tobytes(),source2.SAMPLE_RATE, source2.SAMPLE_WIDTH )



          try:
              BING_KEY = "INSERT BING API KEY HERE"
              self.text=r.recognize_bing(audio, key=BING_KEY)
         
         
          except sr.UnknownValueError:
             print("Microsoft Bing Voice Recognition could not understand audio")
           
          except sr.RequestError as e:
             print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))

          
          else:


                  self.text_pub.publish(str(self.text))



      
   
def main():
    
    rospy.init_node('recognize_audio_bing')
    
  
    
    arg_defaults = {
       
        'source': '/recognizer/audio',
        'sink': '/recognizer/text1'
        }
    args = updateArgs(arg_defaults)
    recognize_audio_bing(**args)
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
