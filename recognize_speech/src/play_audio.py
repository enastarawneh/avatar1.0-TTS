#!/usr/bin/env python


import numpy
import rospy
import soundfile as sf
import playsound
from rospy_tutorials.msg import Floats
from rospy.numpy_msg import numpy_msg
import speech_recognition as sr



class play_audio:

  
    def __init__(self, source ):
      
        self.text_pub = rospy.Subscriber(source, numpy_msg(Floats), self.callback)
        

    def callback (self,data):
       
        r = sr.Recognizer()
        with sr.Microphone() as source2:
               numpydata = data.data              
               audio=sr.AudioData(numpydata.tobytes(),source2.SAMPLE_RATE, source2.SAMPLE_WIDTH )
               data, samplerate = sf.read('myfile.raw', channels=1, samplerate=44100,
                           subtype='FLOAT') 

       
   
def main():
    
    rospy.init_node('play_audio')
    
  
    
    arg_defaults = {
       
        'source': '/recognizer/audio',

        }
    args = updateArgs(arg_defaults)
    play_audio(**args)
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
