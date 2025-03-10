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

import abc
import inspect

# fmt: off
# pylint: skip-file

# This interface class and decorator is magic syntatic sugar to allow concise interface definitions
# If we didn't do this, Python is unnecessarily verbose, which I find distracting. Don't black this file :)
class Interface(abc.ABC): pass
def interface(cls):
    attrs = {n: classmethod(abc.abstractmethod(f)) for n, f in inspect.getmembers(cls, predicate=inspect.isfunction)}
    return type(cls.__name__, (Interface, cls), attrs)


# ############################################################################ #

# Hey there! Welcome to the BlenderBIM Add-on code. Please feel free to reach
# out if you have any questions or need further guidance. Happy hacking!

# ############################################################################ #

# This portion of the code is singled out as it is part of the Demo module, used
# to teach people how the code is structured in the BlenderBIM Add-on.

# This is an example "interface" (as in, a software interface, not a user
# interface) for the Demo module. Think of it as a list of all of the functions
# your module can perform. In this file, you will come across every single
# capability of the entire add-on. By breaking it down into little functions, we
# can test each one separately, and at a glance know if there are opportunities
# for code reuse or refactoring. At this point, we're only interested in a list
# of functions, not the details of how they're implemented. This is because the
# purpose of the core is to just give a high level overview of the application's
# capabilities.

@interface
class Demo:
    def clear_name_field(cls): pass
    def get_project(cls): pass
    def hide_user_hints(cls): pass
    def set_message(cls, message): pass
    def show_user_hints(cls): pass

# The rest of the code in this file is not part of the Demo tutorial.

# ############################################################################ #

@interface
class Aggregate:
    def can_aggregate(cls, relating_object, related_object): pass
    def disable_editing(cls, obj): pass
    def enable_editing(cls, obj): pass


@interface
class Blender: pass


@interface
class Boundary: pass


@interface
class Brick:
    def add_brick(cls, namespace, brick_class): pass
    def add_brick_breadcrumb(cls): pass
    def add_brick_from_element(cls, element, namespace, brick_class): pass
    def add_brickifc_project(cls, namespace): pass
    def add_brickifc_reference(cls, brick, element, project): pass
    def add_feed(cls, source, destination): pass
    def clear_brick_browser(cls): pass
    def clear_project(cls): pass
    def export_brick_attributes(cls, brick_uri): pass
    def get_active_brick_class(cls): pass
    def get_brick(cls, element): pass
    def get_brick_class(cls, element): pass
    def get_brick_path(cls): pass
    def get_brick_path_name(cls): pass
    def get_brickifc_project(cls): pass
    def get_convertable_brick_elements(cls): pass
    def get_item_class(cls, item): pass
    def get_library_brick_reference(cls, library, brick_uri): pass
    def get_namespace(cls, uri): pass
    def import_brick_classes(cls, brick_class): pass
    def import_brick_items(cls, brick_class): pass
    def load_brick_file(cls, filepath): pass
    def new_brick_file(cls): pass
    def pop_brick_breadcrumb(cls): pass
    def remove_brick(cls, brick_uri): pass
    def run_assign_brick_reference(cls, element=None, library=None, brick_uri=None): pass
    def run_refresh_brick_viewer(cls): pass
    def run_view_brick_class(cls, brick_class=None): pass
    def select_browser_item(cls, item): pass
    def set_active_brick_class(cls, brick_class): pass


@interface
class Collector:
    def assign(cls, obj): pass
    def sync(cls, obj): pass


@interface
class Context:
    def clear_context(cls): pass
    def export_attributes(cls): pass
    def get_context(cls): pass
    def import_attributes(cls): pass
    def set_context(cls, context): pass


@interface
class Debug:
    def add_schema_identifier(cls, schema): pass
    def load_express(cls, filename): pass
    def purge_hdf5_cache(cls): pass


@interface
class Drawing:
    def create_annotation_object(cls, object_type): pass
    def create_camera(cls, name, matrix): pass
    def create_svg_sheet(cls, document, titleblock): pass
    def delete_collection(cls, collection): pass
    def delete_drawing_elements(cls, elements): pass
    def disable_editing_drawings(cls): pass
    def disable_editing_sheets(cls): pass
    def disable_editing_text(cls, obj): pass
    def disable_editing_text_product(cls, obj): pass
    def enable_editing(cls, obj): pass
    def enable_editing_drawings(cls): pass
    def enable_editing_sheets(cls): pass
    def enable_editing_text(cls, obj): pass
    def enable_editing_text_product(cls, obj): pass
    def ensure_unique_drawing_name(cls, name): pass
    def ensure_unique_identification(cls, identification): pass
    def export_text_literal_attributes(cls, obj): pass
    def generate_drawing_matrix(cls, target_view, location_hint): pass
    def generate_sheet_identification(cls): pass
    def get_annotation_context(cls, target_view): pass
    def get_body_context(cls): pass
    def get_drawing_collection(cls, drawing): pass
    def get_drawing_group(cls, drawing): pass
    def get_drawing_target_view(cls, drawing): pass
    def get_group_elements(cls, group): pass
    def get_ifc_representation_class(cls, object_type): pass
    def get_name(cls, element): pass
    def get_sheet_filename(cls, document): pass
    def get_text_literal(cls, obj): pass
    def get_text_product(cls, element): pass
    def import_drawings(cls): pass
    def import_sheets(cls): pass
    def import_text_attributes(cls, obj): pass
    def import_text_product(cls, obj): pass
    def open_svg(cls, filepath): pass
    def run_root_assign_class(cls, obj=None, ifc_class=None, predefined_type=None, should_add_representation=True, context=None, ifc_representation_class=None): pass
    def set_drawing_collection_name(cls, group, collection): pass
    def show_decorations(cls): pass
    def update_text_value(cls, obj): pass


@interface
class Geometry:
    def change_object_data(cls, obj, data, is_global=False): pass
    def clear_cache(cls, element): pass
    def clear_modifiers(cls, obj): pass
    def clear_scale(cls, obj): pass
    def create_dynamic_voids(cls, obj): pass
    def delete_data(cls, data): pass
    def does_object_have_mesh_with_faces(cls, obj): pass
    def does_representation_id_exist(cls, representation_id): pass
    def duplicate_object_data(cls, obj): pass
    def get_cartesian_point_coordinate_offset(cls, obj): pass
    def get_element_type(cls, element): pass
    def get_elements_of_type(cls, type): pass
    def get_ifc_representation_class(cls, element, representation): pass
    def get_object_data(cls, obj): pass
    def get_object_materials_without_styles(cls, obj): pass
    def get_profile_set_usage(cls, element): pass
    def get_representation_data(cls, representation): pass
    def get_representation_id(cls, representation): pass
    def get_representation_name(cls, representation): pass
    def get_styles(cls, obj): pass
    def get_total_representation_items(cls, obj): pass
    def has_data_users(cls, data): pass
    def import_representation(cls, obj, representation, enable_dynamic_voids=False): pass
    def import_representation_parameters(cls, data): pass
    def is_body_representation(cls, representation): pass
    def is_box_representation(cls, representation): pass
    def is_edited(cls, obj): pass
    def is_mapped_representation(cls, representation): pass
    def is_type_product(cls, element): pass
    def link(cls, element, obj): pass
    def record_object_materials(cls, obj): pass
    def record_object_position(cls, obj): pass
    def rename_object(cls, obj, name): pass
    def replace_object_with_empty(cls, obj): pass
    def resolve_mapped_representation(cls, representation): pass
    def run_geometry_update_representation(cls, obj=None): pass
    def run_style_add_style(cls, obj=None): pass
    def should_force_faceted_brep(cls): pass
    def should_force_triangulation(cls): pass
    def should_generate_uvs(cls, obj): pass
    def should_use_presentation_style_assignment(cls): pass


@interface
class Ifc:
    def get(cls): pass
    def get_entity(cls, obj): pass
    def get_object(cls, entity): pass
    def get_schema(cls): pass
    def link(cls, element, obj): pass
    def run(cls, command, **kwargs): pass
    def set(cls, ifc): pass
    def unlink(cls, element=None, obj=None): pass


@interface
class Library:
    def clear_editing_mode(cls): pass
    def export_library_attributes(cls): pass
    def export_reference_attributes(cls): pass
    def get_active_library(cls): pass
    def get_active_reference(cls): pass
    def import_library_attributes(cls, library): pass
    def import_reference_attributes(cls, reference): pass
    def import_references(cls, library): pass
    def set_active_library(cls, library): pass
    def set_active_reference(cls, reference): pass
    def set_editing_mode(cls, mode): pass


@interface
class Material:
    def add_default_material_object(cls): pass


@interface
class Misc:
    def get_object_storey(cls, obj): pass
    def get_storey_elevation_in_si(cls, storey): pass
    def get_storey_height_in_si(cls, storey, total_storeys): pass
    def mark_object_as_edited(cls, obj): pass
    def move_object_to_elevation(cls, obj, elevation): pass
    def run_root_copy_class(cls, obj=None): pass
    def scale_object_to_height(cls, obj, height): pass
    def set_object_origin_to_bottom(cls, obj): pass
    def split_objects_with_cutter(cls, objs, cutter): pass


@interface
class Model:
    pass


@interface
class Patch:
    def run_migrate_patch(cls, infile, outfile, schema): pass


@interface
class Owner:
    def add_address_attribute(cls, name): pass
    def add_person_attribute(cls, name): pass
    def clear_actor(cls): pass
    def clear_address(cls): pass
    def clear_organisation(cls): pass
    def clear_person(cls): pass
    def clear_role(cls): pass
    def clear_user(cls): pass
    def export_actor_attributes(cls): pass
    def export_address_attributes(cls): pass
    def export_organisation_attributes(cls): pass
    def export_person_attributes(cls): pass
    def export_role_attributes(cls): pass
    def get_actor(cls): pass
    def get_address(cls): pass
    def get_organisation(cls): pass
    def get_person(cls): pass
    def get_role(cls): pass
    def get_user(cls): pass
    def import_actor_attributes(cls, actor): pass
    def import_address_attributes(cls): pass
    def import_organisation_attributes(cls): pass
    def import_person_attributes(cls): pass
    def import_role_attributes(cls): pass
    def remove_address_attribute(cls, name, id): pass
    def remove_person_attribute(cls, name, id): pass
    def set_actor(cls, actor): pass
    def set_address(cls, address): pass
    def set_organisation(cls, organisation): pass
    def set_person(cls, person): pass
    def set_role(cls, role): pass
    def set_user(cls, user): pass


@interface
class Project:
    def append_all_types_from_template(cls, template): pass
    def create_empty(cls, name): pass
    def run_aggregate_assign_object(cls, relating_obj=None, related_obj=None): pass
    def run_context_add_context(cls, context_type=None, context_identifier=None, target_view=None, parent=None): pass
    def run_owner_add_organisation(cls): pass
    def run_owner_add_person(cls): pass
    def run_owner_add_person_and_organisation(cls, person=None, organisation=None): pass
    def run_owner_set_user(cls, user=None): pass
    def run_root_assign_class(cls, obj=None, ifc_class=None, predefined_type=None, should_add_representation=True, context=None, ifc_representation_class=None): pass
    def run_unit_assign_scene_units(cls): pass
    def set_active_spatial_element(cls, obj): pass
    def set_context(cls, context): pass


@interface
class Pset:
    def get_element_pset(cls, element, pset_name): pass


@interface
class Qto:
    def get_radius_of_selected_vertices(cls, obj): pass
    def set_qto_result(cls, result): pass


@interface
class Root:
    def add_dynamic_opening_voids(cls, element, obj): pass
    def does_type_have_representations(cls, element): pass
    def get_element_type(cls, element): pass
    def get_object_name(cls, obj): pass
    def get_object_representation(cls, obj): pass
    def get_representation_context(cls, representation): pass
    def is_opening_element(cls, element): pass
    def link_object_data(cls, source_obj, destination_obj): pass
    def run_geometry_add_representation(cls, obj=None, context=None, ifc_representation_class=None, profile_set_usage=None): pass
    def set_element_specific_display_settings(cls, obj, element): pass
    def set_object_name(cls, obj, element): pass


@interface
class Selector:
    def set_active(cls, obj): pass


@interface
class Spatial:
    def can_contain(cls, structure_obj, element_obj): pass
    def disable_editing(cls, obj): pass
    def duplicate_object_and_data(cls, obj): pass
    def enable_editing(cls, obj): pass
    def get_container(cls, element): pass
    def get_decomposed_elements(cls, container): pass
    def get_object_matrix(cls, obj): pass
    def get_relative_object_matrix(cls, target_obj, relative_to_obj): pass
    def import_containers(cls, parent=None): pass
    def run_root_copy_class(cls, obj=None): pass
    def run_spatial_assign_container(cls, structure_obj=None, element_obj=None): pass
    def select_object(cls, obj): pass
    def set_active_object(cls, obj): pass
    def set_relative_object_matrix(cls, target_obj, relative_to_obj, matrix): pass


@interface
class Structural:
    def disable_editing_structural_analysis_model(cls): pass
    def disable_structural_analysis_model_editing_ui(cls): pass
    def enable_editing_structural_analysis_model(cls, model): pass
    def enable_structural_analysis_model_editing_ui(cls): pass
    def enabled_structural_analysis_model_editing_ui(cls): pass
    def ensure_representation_contexts(cls): pass
    def get_active_structural_analysis_model(cls): pass
    def get_ifc_structural_analysis_model_attributes(cls, model): pass
    def get_ifc_structural_analysis_models(cls): pass
    def get_product_or_active_object(cls): pass
    def get_structural_analysis_model_attributes(cls): pass
    def load_structural_analysis_model_attributes(cls, data): pass
    def load_structural_analysis_models(cls): pass


@interface
class Style:
    def can_support_rendering_style(cls, obj): pass
    def disable_editing(cls, obj): pass
    def enable_editing(cls, obj): pass
    def export_surface_attributes(cls, obj): pass
    def get_context(cls, obj): pass
    def get_name(cls, obj): pass
    def get_style(cls, obj): pass
    def get_surface_rendering_attributes(cls, obj): pass
    def get_surface_rendering_style(cls, obj): pass
    def get_surface_shading_attributes(cls, obj): pass
    def get_surface_shading_style(cls, obj): pass
    def get_surface_texture_style(cls, obj): pass
    def get_uv_maps(cls, representation): pass
    def import_surface_attributes(cls, style, obj): pass


@interface
class Surveyor:
    def get_absolute_matrix(cls, obj): pass


@interface
class System:
    def create_empty_at_cursor_with_element_orientation(cls, element): pass
    def delete_element_objects(cls, elements): pass
    def disable_editing_system(cls): pass
    def disable_system_editing_ui(cls): pass
    def enable_system_editing_ui(cls): pass
    def export_system_attributes(cls): pass
    def get_connected_port(cls, port): pass
    def get_ports(cls, element): pass
    def import_system_attributes(cls, system): pass
    def import_systems(cls): pass
    def load_ports(cls, port): pass
    def run_root_assign_class(cls, obj=None, ifc_class=None, predefined_type=None, should_add_representation=True, context=None, ifc_representation_class=None): pass
    def select_elements(cls, elements): pass
    def select_system_products(cls, system): pass
    def set_active_system(cls, system): pass


@interface
class Type:
    def change_object_data(cls, obj, data, is_global=False): pass
    def disable_editing(cls, obj): pass
    def get_body_context(cls): pass
    def get_body_representation(cls, element): pass
    def get_ifc_representation_class(cls, element): pass
    def get_object_data(cls, obj): pass
    def get_profile_set_usage(cls, element): pass
    def get_representation_context(cls, representation): pass
    def has_dynamic_voids(cls, obj): pass
    def has_material_usage(cls, element): pass
    def run_geometry_add_representation(cls, obj=None, context=None, ifc_representation_class=None, profile_set_usage=None): pass
    def run_geometry_switch_representation(cls, obj=None, representation=None, should_reload=None, enable_dynamic_voids=None, is_global=None): pass


@interface
class Unit:
    def clear_active_unit(cls): pass
    def disable_editing_units(cls): pass
    def enable_editing_units(cls): pass
    def export_unit_attributes(cls): pass
    def get_scene_unit_name(cls, unit_type): pass
    def get_scene_unit_si_prefix(cls): pass
    def get_si_name_from_unit_type(cls, unit_type): pass
    def get_unit_class(cls, unit): pass
    def import_unit_attributes(cls, unit): pass
    def import_units(cls): pass
    def is_scene_unit_metric(cls): pass
    def set_active_unit(cls, unit): pass


@interface
class Voider:
    def can_void(cls, opening, element): pass
    def set_void_display(cls, opening_obj): pass
    def unvoid(cls, opening_obj): pass
    def void(cls, opening_obj, building_obj): pass
