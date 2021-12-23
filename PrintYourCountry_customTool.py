import arcpy 

layer=arcpy.GetParameterAsText(0)

sql=arcpy.GetParameterAsText(1)

#var=arcpy.GetParameterAsText(3)

#----------------------------------
try:
    #-----------------------------------
    #project uSe "CURRENT" ALWAYS
    arcpy.AddMessage(1)#

    a=arcpy.mp.ArcGISProject("CURRENT").listLayouts()[0].listElements("MAPFRAME_ELEMENT")[0]

    arcpy.AddMessage("2")
    #----
    
    proj=arcpy.mp.ArcGISProject("CURRENT")
    arcpy.AddMessage(3)    
    #----------------------------------
    
    m=proj.listMaps()[0]
    arcpy.AddMessage(m.name) #Map
    #---
    arcpy.AddMessage(f"{layer}") #Countries
    l=m.listLayers(f"{layer}")[0]
    arcpy.AddMessage(5)    ##<MappingLayerObject object at 0x0000019AADC1CE30>
    #----
    l.definitionQuery="OBJECTID>0" 
    a.zoomToAllLayers()
    arcpy.AddMessage( l.definitionQuery)   #OBJECTID>0
#-------------------------------------------------------------------
    ##l.definitionQuery=f"OBJECTID= {var}"            #f-string
    ##l.definitionQuery="OBJECTID= {}".format(var)   #format_string
    #l.definitionQuery="OBJECTID=" + var             #concatination لازم الطرفين نصوص
    arcpy.AddMessage(f' {sql} ')    
    l.definitionQuery=f"{sql} "
    arcpy.AddMessage( l.definitionQuery)# 
    arcpy.AddMessage( 8)#62

    a.panToExtent(a.getLayerExtent(l,False))
    arcpy.AddMessage(9)
    a.camera.scale=a.camera.scale/8
    arcpy.SetProgressorPosition()
except Exception as e:
    print(e.args[0])
