# Reference - https://docs.blender.org/api/current/info_quickstart.html

import bpy

def quickstart():
    # baisc access && collections
    objList = list(bpy.data.objects)
    sceneList = list(bpy.data.scenes)
    matList = list(bpy.data.materials)

    for i in objList:
        print(i.name)
        
    for i in sceneList:
        print(i.name)
        print(i.render)
        # access attribute
        print(i.render.resolution_percentage)
        
        print(i.objects[0])
        print(i.objects['Cube'])
        # access attribute
        print(i.objects[0].data.vertices[0].co.x)
        
    for i in matList:
        print(i.name)

# data create / remove  
mesh = bpy.data.meshes.new(name="MyMesh")
meshList = bpy.data.meshes
for i in meshList:
    print(i.name)
    bpy.data.meshes.remove(i)
