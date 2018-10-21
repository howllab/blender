import bpy

def my_handler(scene):
    print("Frame Change", scene.frame_current)
    
bpy.app.handlers.frame_change_pre.append(my_handler)