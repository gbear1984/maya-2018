import maya.cmds as cmds 


the_namespace = 'DGCR_sh002_cartA:'
file_name = 'sh06'
car = 'A'
write_rotation = False




## Helper Functions #########
def each_frame():
    timeLinestart = int(cmds.playbackOptions(animationStartTime=True,q=True))
    timeLineEnd = int(cmds.playbackOptions(animationEndTime=True,q=True))
    for frame_number in range(timeLinestart, timeLineEnd +1):
        yield cmds.currentTime(frame_number)
   
file_path = os.environ['MILL_SHOT_ELEMENT_PATH']
file_data = 'data'

fullFilePath = os.path.join(file_path, file_data, file_name +car)
 

# check version
counter = 0
no_file = True
filename = "{0}v{1}.ASC".format(fullFilePath,counter)

while no_file:    
    if os.path.isfile(filename):
        counter += 1
        filename = "{0}v{1}.ASC".format(fullFilePath,counter)
    else:
        no_file = False


f= open(filename,"w+")


ctrl = the_namespace +'rotate_CTRL' 
ctrl  += '.'
heave_CTRL = the_namespace +'heave_CTRL' 
heave_CTRL  += '.'


if write_rotation == False:
    f.write( 'Axes = Cyl1, Cyl2, Cyl3, Cyl4, Cyl5, Cyl6, ROTATE\n')
    for frame in each_frame():
        for attr in ['Cyl1_remaped','Cyl2_remaped','Cyl3_remaped',
                     'Cyl4_remaped','Cyl5_remaped','Cyl6_remaped',
                     'ROTATE_']:
            value = cmds.getAttr(ctrl+attr)
            #print ('     {:0.4f}'.format(value))
            f.write('     {:0.2f}'.format(value))
        f.write('\n')
    f.close() 
    

else:
    f.write('Axes = rx, ry, rz, translateY\n')
    for frame in each_frame():
        for attr in ['rx','ry','rz']:
            value = cmds.getAttr(ctrl+attr)
            #print ('     {:0.4f}'.format(value))
            f.write('     {:0.2f}'.format(value))
            
        value = cmds.getAttr(heave_CTRL+'ty')
        f.write('     {:0.2f}'.format(value))
        f.write('\n')
    f.close() 

