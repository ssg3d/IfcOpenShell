# BlenderBIM Add-on - OpenBIM Blender Add-on
# Copyright (C) 2021 Dion Moult <dion@thinkmoult.com>
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

import blenderbim.core.unit as subject
from test.core.bootstrap import ifc, unit


class TestAssignSceneUnits:
    def test_creating_and_assigning_metric_units(self, ifc, unit):
        unit.is_scene_unit_metric().should_be_called().will_return(True)
        unit.get_scene_unit_name("length").should_be_called().will_return("name")
        unit.get_scene_unit_si_prefix().should_be_called().will_return("prefix")
        ifc.run(
            "unit.add_si_unit", unit_type="LENGTHUNIT", name="name", prefix="prefix"
        ).should_be_called().will_return("lengthunit")

        unit.get_scene_unit_name("area").should_be_called().will_return("name")
        ifc.run("unit.add_si_unit", unit_type="AREAUNIT", name="name", prefix="prefix").should_be_called().will_return(
            "areaunit"
        )

        unit.get_scene_unit_name("volume").should_be_called().will_return("name")
        ifc.run(
            "unit.add_si_unit", unit_type="VOLUMEUNIT", name="name", prefix="prefix"
        ).should_be_called().will_return("volumeunit")

        ifc.run("unit.assign_unit", units=["lengthunit", "areaunit", "volumeunit"]).should_be_called()
        subject.assign_scene_units(ifc, unit)

    def test_creating_and_assigning_imperial_units(self, ifc, unit):
        unit.is_scene_unit_metric().should_be_called().will_return(False)
        unit.get_scene_unit_name("length").should_be_called().will_return("lengthname")
        ifc.run("unit.add_conversion_based_unit", name="lengthname").should_be_called().will_return("lengthunit")

        unit.get_scene_unit_name("area").should_be_called().will_return("areaname")
        ifc.run("unit.add_conversion_based_unit", name="areaname").should_be_called().will_return("areaunit")

        unit.get_scene_unit_name("volume").should_be_called().will_return("volumename")
        ifc.run("unit.add_conversion_based_unit", name="volumename").should_be_called().will_return("volumeunit")

        ifc.run("unit.assign_unit", units=["lengthunit", "areaunit", "volumeunit"]).should_be_called()
        subject.assign_scene_units(ifc, unit)


class TestAssignUnit:
    def test_run(self, ifc, unit):
        ifc.run("unit.assign_unit", units=["unit"]).should_be_called()
        unit.import_units().should_be_called()
        subject.assign_unit(ifc, unit, unit="unit")


class TestUnassignUnit:
    def test_run(self, ifc, unit):
        ifc.run("unit.unassign_unit", units=["unit"]).should_be_called()
        unit.import_units().should_be_called()
        subject.unassign_unit(ifc, unit, unit="unit")


class TestLoadUnits:
    def test_run(self, unit):
        unit.import_units().should_be_called()
        unit.enable_editing_units().should_be_called()
        subject.load_units(unit)


class TestDisableUnitEditingUI:
    def test_run(self, unit):
        unit.disable_editing_units().should_be_called()
        subject.disable_unit_editing_ui(unit)


class TestRemoveUnit:
    def test_run(self, ifc, unit):
        ifc.run("unit.remove_unit", unit="unit").should_be_called()
        unit.import_units().should_be_called()
        subject.remove_unit(ifc, unit, unit="unit")


class TestAddMonetaryUnit:
    def test_run(self, ifc, unit):
        ifc.run("unit.add_monetary_unit").should_be_called().will_return("unit")
        unit.import_units().should_be_called()
        assert subject.add_monetary_unit(ifc, unit) == "unit"


class TestAddSIUnit:
    def test_run(self, ifc, unit):
        unit.get_si_name_from_unit_type("unit_type").should_be_called().will_return("name")
        ifc.run("unit.add_si_unit", unit_type="unit_type", name="name").should_be_called().will_return("unit")
        unit.import_units().should_be_called()
        assert subject.add_si_unit(ifc, unit, unit_type="unit_type") == "unit"


class TestAddContextDependentUnit:
    def test_run(self, ifc, unit):
        ifc.run("unit.add_context_dependent_unit", unit_type="unit_type", name="name").should_be_called().will_return(
            "unit"
        )
        unit.import_units().should_be_called()
        assert subject.add_context_dependent_unit(ifc, unit, unit_type="unit_type", name="name") == "unit"


class TestEnableEditingUnit:
    def test_run(self, unit):
        unit.set_active_unit("unit").should_be_called()
        unit.import_unit_attributes("unit").should_be_called()
        subject.enable_editing_unit(unit, unit="unit")


class TestDisableEditingUnit:
    def test_run(self, unit):
        unit.clear_active_unit().should_be_called()
        subject.disable_editing_unit(unit)


class TestEditUnit:
    def test_editing_monetary_units(self, ifc, unit):
        unit.export_unit_attributes().should_be_called().will_return("attributes")
        unit.get_unit_class("unit").should_be_called().will_return("IfcMonetaryUnit")
        ifc.run("unit.edit_monetary_unit", unit="unit", attributes="attributes").should_be_called()
        unit.import_units().should_be_called()
        unit.clear_active_unit().should_be_called()
        subject.edit_unit(ifc, unit, unit="unit")

    def test_editing_derived_units(self, ifc, unit):
        unit.export_unit_attributes().should_be_called().will_return("attributes")
        unit.get_unit_class("unit").should_be_called().will_return("IfcDerivedUnit")
        ifc.run("unit.edit_derived_unit", unit="unit", attributes="attributes").should_be_called()
        unit.import_units().should_be_called()
        unit.clear_active_unit().should_be_called()
        subject.edit_unit(ifc, unit, unit="unit")

    def test_editing_named_units(self, ifc, unit):
        unit.export_unit_attributes().should_be_called().will_return("attributes")
        unit.get_unit_class("unit").should_be_called().will_return("IfcNamedUnit")
        ifc.run("unit.edit_named_unit", unit="unit", attributes="attributes").should_be_called()
        unit.import_units().should_be_called()
        unit.clear_active_unit().should_be_called()
        subject.edit_unit(ifc, unit, unit="unit")
