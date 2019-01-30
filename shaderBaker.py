import pymel.core as pm
import maya.cmds as cmds
import os


#selection = cmds.ls(sl=True, long=True) #or [] 
shaderTree = cmds.listConnections(c=True)
#for i in shaderTree:
#    print (i)
        
def makeShadeAndBakeGUI_SE():
    
    selection = cmds.ls(sl=True, long=True)
    if (cmds.window("shadeAndBakeWindowSE", exists=True)):
        cmds.deleteUI("shadeAndBakeWindowSE")
    
    shadeAndBakeWindowSE = cmds.window('shadeAndBakeWindowSE', title="Shader Baking", rtf=True) 
    cmds.paneLayout() 
    scrollList = cmds.textScrollList("cunt",numberOfRows=8, allowMultiSelection=True, append= shaderTree)

    cmds.showWindow('shadeAndBakeWindowSE')
makeShadeAndBakeGUI_SE()



