##ListLayers (map_document_or_layer, {wildcard}, {data_frame object.})
##                                 wildcard=None
##                                   (*)
##                                   ("")


## https://desktop.arcgis.com/en/arcmap/latest/analyze/arcpy-mapping/listlayers.htm
##import arcpy
##mapName = r'E:\1_iti_gis\gis\week_2\6-5\Georeferencing_Cad.mxd'
##mxd = arcpy.mapping.MapDocument(mapName)
##dfs = arcpy.mapping.ListDataFrames(mxd)
##
##for df in dfs:
##     print "Frame " + df.name
##     layers = arcpy.mapping.ListLayers(mxd, "*", df)
##     for layer in layers:
##         print "\t" + layer.name
##
##             


##--------------
##import arcpy
##mapName = r'E:\1_iti_gis\gis\week_2\6-5\Georeferencing_Cad.mxd'
##mxd = arcpy.mapping.MapDocument(mapName)
##dfs = arcpy.mapping.ListDataFrames(mxd)
##
##for df in dfs:
##     print "Frame " + df.name
##     layers = arcpy.mapping.ListLayers(mxd, "st*", df)
##     for layer in layers:
##         print "\t" + layer.name


##--------------
##import arcpy
##mapName = r'E:\1_iti_gis\gis\week_2\6-5\Georeferencing_Cad.mxd'
##mxd = arcpy.mapping.MapDocument(mapName)
##dfs = arcpy.mapping.ListDataFrames(mxd)
##
##for df in dfs:
##     print "Frame " + df.name
##     layers = arcpy.mapping.ListLayers(mxd, "*Byways", df)
##     for layer in layers:
##         print "\t" + layer.name

##--------------
import arcpy
mapName = r'E:\1_iti_gis\gis\week_2\6-5\Georeferencing_Cad.mxd'
mxd = arcpy.mapping.MapDocument(mapName)
dfs = arcpy.mapping.ListDataFrames(mxd)

for df in dfs:
     print "Frame " + df.name
     layers = arcpy.mapping.ListLayers(mxd)
     for layer in layers:
         print "\t" + layer.name































