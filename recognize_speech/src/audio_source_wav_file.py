#!/usr/bin/env python


import numpy
import rospy
from rospy_tutorials.msg import Floats
from rospy.numpy_msg import numpy_msg
import speech_recognition as sr
from os import path
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "output.wav")
frames = [] 





class audio_source_wav_file:

    
    def __init__(self, sink):
      
        self.text_pub = rospy.Publisher(sink, numpy_msg(Floats ),queue_size=10, latch=True)
        self.callback()

    def callback (self):
        r1 = sr.Recognizer()
        
        with sr.AudioFile(AUDIO_FILE) as source:
 
          audio1 = r1.record(source)
          numpydata = numpy.fromstring(audio1.get_raw_data(), dtype=numpy.float32)
          self.text_pub.publish(numpydata)    
 
          


      
   
def main():
    
    rospy.init_node('audio_source_wav_file')
    
  
    
    arg_defaults = {
       
        'sink': '/recognizer/audio'
        }
    args = updateArgs(arg_defaults)
    audio_source_wav_file(**args)
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
