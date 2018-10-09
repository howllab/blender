import bpy
from bpy.types import Panel

class SimpleToolPanel(Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_label = "Tools sample"
    bl_context = "objectmode"
    bl_category = "sample"
    
    def draw(self, context):
        layout = self.layout
        layout.operator("mesh.primitive_cube_add", text="Add new cube", icon="MESH_CUBE")
        
def register():
    bpy.utils.register_class(SimpleToolPanel)
    
def unregister():
    bpy.utils.unregister_class(SimpleToolPanel)
    
if __name__ == "__main__":
    register()