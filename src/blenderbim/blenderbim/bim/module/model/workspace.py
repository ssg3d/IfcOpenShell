# BlenderBIM Add-on - OpenBIM Blender Add-on
# Copyright (C) 2020, 2021 Dion Moult <dion@thinkmoult.com>
#
# This file is part of BlenderBIM Add-on.
#
# BlenderBIM Add-on is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# BlenderBIM Add-on is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with BlenderBIM Add-on.  If not, see <http://www.gnu.org/licenses/>.

import os
import bpy
import blenderbim.bim.module.type.prop as type_prop
from bpy.types import WorkSpaceTool
from blenderbim.bim.ifc import IfcStore
from blenderbim.bim.module.model.data import AuthoringData


class BimTool(WorkSpaceTool):
    bl_space_type = "VIEW_3D"
    bl_context_mode = "OBJECT"

    bl_idname = "bim.bim_tool"
    bl_label = "BIM Tool"
    bl_description = "Gives you BIM authoring related superpowers"
    bl_icon = os.path.join(os.path.dirname(__file__), "ops.authoring.bim")
    bl_widget = None
    # https://docs.blender.org/api/current/bpy.types.KeyMapItems.html
    bl_keymap = (
        # ("bim.wall_tool_op", {"type": 'MOUSEMOVE', "value": 'ANY'}, {"properties": []}),
        # ("mesh.add_wall", {"type": 'LEFTMOUSE', "value": 'PRESS'}, {"properties": []}),
        ("bim.hotkey", {"type": "A", "value": "PRESS", "shift": True}, {"properties": [("hotkey", "S_A")]}),
        ("bim.hotkey", {"type": "E", "value": "PRESS", "shift": True}, {"properties": [("hotkey", "S_E")]}),
        ("bim.join_wall", {"type": "T", "value": "PRESS", "shift": True}, {"properties": [("join_type", "L")]}),
        ("bim.join_wall", {"type": "Y", "value": "PRESS", "shift": True}, {"properties": [("join_type", "V")]}),
        ("bim.flip_wall", {"type": "F", "value": "PRESS", "shift": True}, {"properties": []}),
        ("bim.split_wall", {"type": "S", "value": "PRESS", "shift": True}, {"properties": []}),
        ("bim.hotkey", {"type": "X", "value": "PRESS", "shift": True}, {"properties": [("hotkey", "S_X")]}),
        ("bim.hotkey", {"type": "C", "value": "PRESS", "shift": True}, {"properties": [("hotkey", "S_C")]}),
        ("bim.hotkey", {"type": "V", "value": "PRESS", "shift": True}, {"properties": [("hotkey", "S_V")]}),
        ("bim.hotkey", {"type": "O", "value": "PRESS", "shift": True}, {"properties": [("hotkey", "S_O")]}),
        ("bim.hotkey", {"type": "O", "value": "PRESS", "alt": True}, {"properties": [("hotkey", "A_O")]}),
        ("bim.hotkey", {"type": "D", "value": "PRESS", "alt": True}, {"properties": [("hotkey", "A_D")]}),
    )

    def draw_settings(context, layout, tool):
        if not AuthoringData.is_loaded and IfcStore.get_file():
            AuthoringData.load()

        row = layout.row(align=True)
        if not IfcStore.get_file():
            row.label(text="No IFC Project", icon="ERROR")
            return
        props = context.scene.BIMModelProperties
        if AuthoringData.data["ifc_classes"]:
            row.prop(props, "ifc_class", text="")
        else:
            row.label(text="No IFC Class")
        if AuthoringData.data["relating_types"]:
            row.prop(props, "relating_type", text="")
        else:
            row.label(text="No Relating Type")

        row.label(text="", icon="BLANK1")

        row = layout.row(align=True)
        row.label(text="", icon="EVENT_SHIFT")
        row.label(text="Add Type Instance", icon="EVENT_A")

        if AuthoringData.data["ifc_classes"]:
            if props.ifc_class == "IfcWallType":
                row = layout.row()
                row.label(text="Join")
                row = layout.row(align=True)
                row.label(text="", icon="EVENT_SHIFT")
                row.label(text="Extend", icon="EVENT_E")
                row = layout.row(align=True)
                row.label(text="", icon="EVENT_SHIFT")
                row.label(text="Butt", icon="EVENT_T")
                row = layout.row(align=True)
                row.label(text="", icon="EVENT_SHIFT")
                row.label(text="Mitre", icon="EVENT_Y")

                row = layout.row()
                row.label(text="Wall Tools")
                row = layout.row(align=True)
                row.label(text="", icon="EVENT_SHIFT")
                row.label(text="Flip", icon="EVENT_F")
                row = layout.row(align=True)
                row.label(text="", icon="EVENT_SHIFT")
                row.label(text="Split", icon="EVENT_S")

            if props.ifc_class in ("IfcColumnType", "IfcBeamType", "IfcMemberType"):
                row = layout.row()
                row.label(text="Join")
                row = layout.row(align=True)
                row.label(text="", icon="EVENT_SHIFT")
                row.label(text="Extend", icon="EVENT_E")

        row = layout.row(align=True)
        row.label(text="", icon="EVENT_SHIFT")
        row.label(text="Opening", icon="EVENT_O")

        row = layout.row(align=True)
        row.label(text="Align")
        row = layout.row(align=True)
        row.label(text="", icon="EVENT_SHIFT")
        row.label(text="Align Exterior", icon="EVENT_X")
        row = layout.row(align=True)
        row.label(text="", icon="EVENT_SHIFT")
        row.label(text="Align Centerline", icon="EVENT_C")
        row = layout.row(align=True)
        row.label(text="", icon="EVENT_SHIFT")
        row.label(text="Align Interior", icon="EVENT_V")
        row = layout.row(align=True)

        row = layout.row(align=True)
        row.label(text="Mode")
        row = layout.row(align=True)
        row.label(text="", icon="EVENT_ALT")
        row.label(text="Opening", icon="EVENT_O")
        row = layout.row(align=True)
        row.label(text="", icon="EVENT_ALT")
        row.label(text="Decomposition", icon="EVENT_D")


class Hotkey(bpy.types.Operator):
    bl_idname = "bim.hotkey"
    bl_label = "Hotkey"
    bl_options = {"REGISTER", "UNDO"}
    hotkey: bpy.props.StringProperty()

    @classmethod
    def poll(cls, context):
        return IfcStore.get_file()

    def execute(self, context):
        return IfcStore.execute_ifc_operator(self, context)

    def _execute(self, context):
        self.props = context.scene.BIMModelProperties
        self.has_ifc_class = True
        try:
            self.has_ifc_class = bool(self.props.ifc_class)
        except:
            pass
        getattr(self, f"hotkey_{self.hotkey}")()
        return {"FINISHED"}

    def hotkey_S_A(self):
        bpy.ops.bim.add_type_instance()

    def hotkey_S_C(self):
        if self.has_ifc_class and self.props.ifc_class == "IfcWallType":
            bpy.ops.bim.align_wall(align_type="CENTERLINE")
        else:
            bpy.ops.bim.align_product(align_type="CENTERLINE")

    def hotkey_S_E(self):
        if not self.has_ifc_class:
            return
        if self.props.ifc_class == "IfcWallType":
            bpy.ops.bim.join_wall(join_type="T")
        elif self.props.ifc_class in ["IfcColumnType", "IfcBeamType", "IfcMemberType"]:
            bpy.ops.bim.extend_profile()

    def hotkey_S_V(self):
        if self.has_ifc_class and self.props.ifc_class == "IfcWallType":
            bpy.ops.bim.align_wall(align_type="INTERIOR")
        else:
            bpy.ops.bim.align_product(align_type="POSITIVE")

    def hotkey_S_X(self):
        if self.has_ifc_class and self.props.ifc_class == "IfcWallType":
            if bpy.ops.bim.align_wall.poll():
                bpy.ops.bim.align_wall(align_type="EXTERIOR")
        else:
            bpy.ops.bim.align_product(align_type="NEGATIVE")

    def hotkey_S_O(self):
        bpy.ops.bim.add_element_opening(voided_building_element="", filling_building_element="")

    def hotkey_A_D(self):
        bpy.ops.bim.toggle_decomposition_parenting()

    def hotkey_A_O(self):
        bpy.ops.bim.toggle_opening_visibility()
