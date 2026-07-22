bl_info = {
    "name": "Material Sorting",
    "author": "Yotun",
    "version": (0, 0, 1),
    "blender": (2, 90, 0),
    "location": "Material Properties > Material Specials",
    "description": "", 
    "doc_url": "https://blenderartists.org/t/how-to-sort-all-materials-on-object/702866",
    "tracker_url": "",      
    "category": "Material"
}

import bpy

class OBJECT_OT_materials_a_to_z (bpy.types.Operator):
    bl_idname = 'object.mat_sorting_a_to_z'
    bl_label = 'Material Sorting'
    bl_description = "Sorting materials by name (A to Z)"
    bl_options = {"REGISTER", "UNDO"}
  
    def execute(self, context):
        
        ob = bpy.context.object
      
        for j in range (len(ob.material_slots)):
            for i in range (len(ob.material_slots)-1):
                ob.active_material_index = i
                tempStr = ob.active_material.name
                ob.active_material_index = i+1
                if ob.active_material.name < tempStr:
                    bpy.ops.object.material_slot_move(direction='UP')
        return {"FINISHED"}
        
    
class OBJECT_OT_materials_z_to_a (bpy.types.Operator):
    bl_idname = 'object.mat_sorting_z_to_a'
    bl_label = 'Material Sorting'
    bl_description = "Sorting materials by name (Z to A)"
    bl_options = {"REGISTER", "UNDO"}
  
    def execute(self, context):
        
        ob = bpy.context.object
      
        for j in range (len(ob.material_slots)):
            for i in range (len(ob.material_slots)-1):
                ob.active_material_index = i+1
                tempStr = ob.active_material.name
                ob.active_material_index = i
                if ob.active_material.name < tempStr:
                    bpy.ops.object.material_slot_move(direction='DOWN')
        return {"FINISHED"}  
  

#class MATERIAL_PT_sorting(bpy.types.Panel):
#    bl_label = "Material sorting by name"	        
#    bl_space_type = 'PROPERTIES'	
#    bl_region_type = 'WINDOW'
#    bl_context = "material"


#    def draw(self, context):
          
#        self.layout.operator("object.mat_sorting_a_to_z", icon='TRIA_UP', text="From A to Z")
#        self.layout.operator("object.mat_sorting_z_to_a", icon='TRIA_DOWN', text="From Z to A")
    

def material_sorting_by_name(self, context):
    layout = self.layout
    layout.operator_context = 'INVOKE_REGION_WIN'
    layout.separator()
    layout.operator(OBJECT_OT_materials_a_to_z.bl_idname, icon='TRIA_UP', text="Sort from A to Z")
    layout.operator(OBJECT_OT_materials_z_to_a.bl_idname, icon='TRIA_DOWN', text="Sort from Z to A")
    layout.separator()
     
def register():
    bpy.utils.register_class(OBJECT_OT_materials_a_to_z)
    bpy.utils.register_class(OBJECT_OT_materials_z_to_a)		
    #bpy.utils.register_class(MATERIAL_PT_sorting)
    bpy.types.MATERIAL_MT_context_menu.prepend(material_sorting_by_name)
 
def unregister():	
    bpy.utils.unregister_class(OBJECT_OT_materials_a_to_z)
    bpy.utils.unregister_class(OBJECT_OT_materials_z_to_a)
    #bpy.utils.unregister_class(MATERIAL_PT_sorting)
    bpy.types.MATERIAL_MT_context_menu.remove(material_sorting_by_name)
 
if __name__ == "__main__" :
    register()