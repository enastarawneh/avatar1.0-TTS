#!/usr/bin/env python



import numpy
import rospy
from rospy_tutorials.msg import Floats
from rospy.numpy_msg import numpy_msg

import cv2

import speech_recognition as sr

frames = [] 

class audio_source:

    
    def __init__(self, sink):
      
        self.text_pub = rospy.Publisher(sink, numpy_msg(Floats ),queue_size=10, latch=True)
        self.callback()

    def callback (self):
        r1 = sr.Recognizer()
        
        with sr.Microphone() as source:
          
          r1.adjust_for_ambient_noise(source)
          audio1 = r1.listen(source)    
          numpydata = numpy.fromstring(audio1.get_raw_data(), dtype=numpy.float32)
          self.text_pub.publish(numpydata)    
 
          
        self.callback()

      
   
def main():
    
    rospy.init_node('audio_source')
    
  
    
    arg_defaults = {
       
        'sink': '/recognizer/audio'
        }
    args = updateArgs(arg_defaults)
    audio_source(**args)
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
