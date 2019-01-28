#!/usr/bin/env python


from std_msgs.msg import String
import rospy

class get_text:
    
    def __init__(self, source):

        self.text_sub = rospy.Subscriber(source, String, self.callback)
        
        
    def callback(self, data):

       
        print str(data.data)
      
       

def main():
    
    rospy.init_node('get_text')
   
    arg_defaults = {
        'source': '/recognizer/text1',

        }
    args = updateArgs(arg_defaults)
    get_text(**args)
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
