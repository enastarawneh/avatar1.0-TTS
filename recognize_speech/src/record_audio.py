#!/usr/bin/env python




import rospy
import pyaudio
import wave
import sys

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
from os import path
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "output.wav")

if sys.platform == 'darwin':
      CHANNELS = 1

 

class record_audio:

    
    def __init__(self):


      
       p = pyaudio.PyAudio()

       stream = p.open(format=FORMAT,
                       channels=CHANNELS,
                       rate=RATE,
                       input=True,
                       frames_per_buffer=CHUNK)

       print("* recording")

       frames = []

       for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
             data = stream.read(CHUNK)
             frames.append(data)

       print("* done recording")

       stream.stop_stream()
       stream.close()
       p.terminate()

       wf = wave.open(AUDIO_FILE, 'wb')
       wf.setnchannels(CHANNELS)
       wf.setsampwidth(p.get_sample_size(FORMAT))
       wf.setframerate(RATE)
       wf.writeframes(b''.join(frames))
       wf.close()


      
   
def main():
    
    rospy.init_node('record_audio')
    
  
    
    arg_defaults = {
       

        }
    args = updateArgs(arg_defaults)
    record_audio(**args)
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
