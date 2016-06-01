bl_info = {
    "name": "OpenGL export BRZZ",
    "author": "Daniel B. Brumazzi",
    "blender": (2, 5, 7),
    "api": 35622,
    "location": "File > Import-Export",
    "description": "Export mesh data with UV's into OpenGL format",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Import-Export"}

if "bpy" in locals():
    import imp
    if "export_brzz" in locals():
        imp.reload(export_brzz)


import os
import bpy
from bpy.props import CollectionProperty, StringProperty, BoolProperty
from bpy_extras.io_utils import ImportHelper, ExportHelper


class ExportOGL(bpy.types.Operator, ExportHelper):
    bl_idname = "export_brzz.ply"
    bl_label = "Export OpenGL"

    filename_ext = ".brzz"
    filter_glob = StringProperty(default="*.brzz", options={'HIDDEN'})

    entire_scene = BoolProperty(name="Entire Scene", description="Export all MESH object (Entire scene)", default=True)

    @classmethod
    def poll(cls, context):
        return context.active_object != None

    def execute(self, context):
        filepath = self.filepath
        filepath = bpy.path.ensure_ext(filepath, self.filename_ext)
        from . import export_brzz
        return export_brzz.export(filepath, self.entire_scene)

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.prop(self, "entire_scene")

def menu_func_export(self, context):
    self.layout.operator(ExportOGL.bl_idname, text="OpenGL Include (.brzz)")


def register():
    bpy.utils.register_module(__name__)

    bpy.types.INFO_MT_file_export.append(menu_func_export)


def unregister():
    bpy.utils.unregister_module(__name__)

    bpy.types.INFO_MT_file_export.remove(menu_func_export)

if __name__ == "__main__":
    register()
