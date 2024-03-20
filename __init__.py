bl_info = {
    "name": "Minecraft Model Json Exporter",
    "author": "Yesssssman",
    "blender": (4, 0, 0),
    "category": "Import-Export",
    "location": "File > Import-Export",
    "description": "Specially designed exporter for developing Minecraft Epic Fight Mod",
}

import bpy

from bpy_extras.io_utils import ExportHelper
from bpy.props import StringProperty, BoolProperty, EnumProperty
from bpy.types import Operator


class ExportToJson(Operator, ExportHelper):
    """Export to Json that specially designed for Epic Fight"""

    bl_idname = "export_mc.json"
    bl_label = "Export to Json for Minecraft"
    filename_ext = ".json"
    filter_glob: StringProperty(default="*.json", options={"HIDDEN"})

    export_anim: BoolProperty(
        name="Export Animation",
        description="Export animation data",
        default=True,
    )

    export_mesh: BoolProperty(
        name="Export Mesh",
        description="Export mesh data",
        default=True,
    )

    export_armature: BoolProperty(
        name="Export Armature",
        description="Export armature data",
        default=True,
    )

    def execute(self, context):
        if not self.filepath:
            raise Exception("filepath not set")
        keywords = self.as_keywords()
        print("keyward is ", keywords)

        from . import export_mc_json

        return export_mc_json.save(context, **keywords)


def menu_func_export(self, context):
    self.layout.operator(
        ExportToJson.bl_idname, text="Animated Minecraft Model (.json)"
    )


def register():
    bpy.utils.register_class(ExportToJson)
    bpy.types.TOPBAR_MT_file_export.append(menu_func_export)


def unregister():
    bpy.utils.unregister_class(ExportToJson)
    bpy.types.TOPBAR_MT_file_export.remove(menu_func_export)


if __name__ == "__main__":
    register()
