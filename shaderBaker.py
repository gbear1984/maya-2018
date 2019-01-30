import pymel.core as pm
import maya.cmds as cmds
import os


#selection = cmds.ls(sl=True, long=True) #or []
#need to test for mtl before running filter
def filterSelection():
    shaderTree = cmds.listConnections(d=True)
    shaderTree.remove("materialInfo1")
    shaderTree.remove("defaultShaderList1")
    return shaderTree
    #for i in shaderTree:
    #    print (i)
        
def makeShadeAndBakeGUI_SE():
    selection = cmds.ls(sl=True, long=True)
    if (cmds.window("shadeAndBakeWindowSE", exists=True)):
        cmds.deleteUI("shadeAndBakeWindowSE")
    
    shadeAndBakeWindowSE = cmds.window('shadeAndBakeWindowSE', title="Shader Baking", rtf=True) 
    cmds.paneLayout() 
    scrollList = cmds.textScrollList("Shader Connects",numberOfRows=2, allowMultiSelection=True, append= filterSelection())

    cmds.showWindow('shadeAndBakeWindowSE')
makeShadeAndBakeGUI_SE()



