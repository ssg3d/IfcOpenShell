@style
Feature: Style

Scenario: Update style colours
    Given an empty IFC project
    And I add a cube
    And I add a material
    And I press "bim.add_style"
    When I press "bim.update_style_colours"
    Then nothing happens

Scenario: Remove style
    Given an empty IFC project
    And I add a cube
    And I add a material
    And I press "bim.add_style"
    When I press "bim.remove_style"
    Then nothing happens

Scenario: Add style
    Given an empty IFC project
    And I add a cube
    And I add a material
    When I press "bim.add_style"
    Then nothing happens

Scenario: Unlink style
    Given an empty IFC project
    And I add a cube
    And I add a material
    And I press "bim.add_style"
    When I press "bim.unlink_style"
    Then the material "Material" is not an IFC style

Scenario: Enable editing style
    Given an empty IFC project
    And I add a cube
    And I add a material
    And I press "bim.add_style"
    When I press "bim.enable_editing_style"
    Then nothing happens

Scenario: Disable editing style
    Given an empty IFC project
    And I add a cube
    And I add a material
    And I press "bim.add_style"
    And I press "bim.enable_editing_style"
    When I press "bim.disable_editing_style"
    Then nothing happens

Scenario: Edit style
    Given an empty IFC project
    And I add a cube
    And I add a material
    And I press "bim.add_style"
    And I press "bim.enable_editing_style"
    When I press "bim.edit_style"
    Then nothing happens
