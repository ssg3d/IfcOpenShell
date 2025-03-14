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

import bpy
from . import ui, prop, operator

classes = (
    operator.AddStyle,
    operator.EnableEditingStyle,
    operator.DisableEditingStyle,
    operator.EditStyle,
    operator.RemoveStyle,
    operator.UpdateStyleColours,
    operator.UpdateStyleTextures,
    operator.UnlinkStyle,
    prop.BIMStyleProperties,
    ui.BIM_PT_style,
    ui.BIM_PT_style_attributes,
)


def register():
    bpy.types.Material.BIMStyleProperties = bpy.props.PointerProperty(type=prop.BIMStyleProperties)


def unregister():
    del bpy.types.Material.BIMStyleProperties
