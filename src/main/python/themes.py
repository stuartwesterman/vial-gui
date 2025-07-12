# SPDX-License-Identifier: GPL-2.0-or-later

from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QPalette, QColor

# Theme definitions using string keys instead of QPalette enums
# This avoids creating Qt objects at import time
_theme_definitions = [
    ("Light", {
        "Window": "#ffefebe7",
        "WindowText": "#ff000000",
        "Base": "#ffffffff",
        "AlternateBase": "#fff7f5f3",
        "ToolTipBase": "#ffffffdc",
        "ToolTipText": "#ff000000",
        "Text": "#ff000000",
        "Button": "#ffefebe7",
        "ButtonText": "#ff000000",
        "BrightText": "#ffffffff",
        "Link": "#ff0000ff",
        "Highlight": "#ff308cc6",
        "HighlightedText": "#ffffffff",
        ("Active", "Button"): "#ffefebe7",
        ("Disabled", "ButtonText"): "#ffbebebe",
        ("Disabled", "WindowText"): "#ffbebebe",
        ("Disabled", "Text"): "#ffbebebe",
        ("Disabled", "Light"): "#ffffffff",
    }),
    ("Dark", {
        "Window": "#353535",
        "WindowText": "#ffffff",
        "Base": "#232323",
        "AlternateBase": "#353535",
        "ToolTipBase": "#191919",
        "ToolTipText": "#ffffff",
        "Text": "#ffffff",
        "Button": "#353535",
        "ButtonText": "#ffffff",
        "BrightText": "#ff0000",
        "Link": "#f7a948",
        "Highlight": "#bababa",
        "HighlightedText": "#232323",
        ("Active", "Button"): "#353535",
        ("Disabled", "ButtonText"): "#808080",
        ("Disabled", "WindowText"): "#808080",
        ("Disabled", "Text"): "#808080",
        ("Disabled", "Light"): "#353535",
    }),
    ("Arc", {
        "Window": "#353945",
        "WindowText": "#d3dae3",
        "Base": "#353945",
        "AlternateBase": "#404552",
        "ToolTipBase": "#4B5162",
        "ToolTipText": "#d3dae3",
        "Text": "#d3dae3",
        "Button": "#353945",
        "ButtonText": "#d3dae3",
        "BrightText": "#5294e2",
        "Link": "#89b1e0",
        "Highlight": "#5294e2",
        "HighlightedText": "#d3dae3",
        ("Active", "Button"): "#353945",
        ("Disabled", "ButtonText"): "#d3dae3",
        ("Disabled", "WindowText"): "#d3dae3",
        ("Disabled", "Text"): "#d3dae3",
        ("Disabled", "Light"): "#404552",
    }),
    ("Nord", {
        "Window": "#2e3440",
        "WindowText": "#eceff4",
        "Base": "#2e3440",
        "AlternateBase": "#434c5e",
        "ToolTipBase": "#4c566a",
        "ToolTipText": "#eceff4",
        "Text": "#eceff4",
        "Button": "#2e3440",
        "ButtonText": "#eceff4",
        "BrightText": "#88c0d0",
        "Link": "#88c0d0",
        "Highlight": "#88c0d0",
        "HighlightedText": "#eceff4",
        ("Active", "Button"): "#2e3440",
        ("Disabled", "ButtonText"): "#eceff4",
        ("Disabled", "WindowText"): "#eceff4",
        ("Disabled", "Text"): "#eceff4",
        ("Disabled", "Light"): "#88c0d0",
    }),
    ("Olivia", {
        "Window": "#181818",
        "WindowText": "#d9d9d9",
        "Base": "#181818",
        "AlternateBase": "#2c2c2c",
        "ToolTipBase": "#363636 ",
        "ToolTipText": "#d9d9d9",
        "Text": "#d9d9d9",
        "Button": "#181818",
        "ButtonText": "#d9d9d9",
        "BrightText": "#fabcad",
        "Link": "#fabcad",
        "Highlight": "#fabcad",
        "HighlightedText": "#2c2c2c",
        ("Active", "Button"): "#181818",
        ("Disabled", "ButtonText"): "#d9d9d9",
        ("Disabled", "WindowText"): "#d9d9d9",
        ("Disabled", "Text"): "#d9d9d9",
        ("Disabled", "Light"): "#fabcad",
    }),
    ("Dracula", {
        "Window": "#282a36",
        "WindowText": "#f8f8f2",
        "Base": "#282a36",
        "AlternateBase": "#44475a",
        "ToolTipBase": "#6272a4",
        "ToolTipText": "#f8f8f2",
        "Text": "#f8f8f2",
        "Button": "#282a36",
        "ButtonText": "#f8f8f2",
        "BrightText": "#8be9fd",
        "Link": "#8be9fd",
        "Highlight": "#8be9fd",
        "HighlightedText": "#f8f8f2",
        ("Active", "Button"): "#282a36",
        ("Disabled", "ButtonText"): "#f8f8f2",
        ("Disabled", "WindowText"): "#f8f8f2",
        ("Disabled", "Text"): "#f8f8f2",
        ("Disabled", "Light"): "#8be9fd",
    }),
    ("Bliss", {
        "Window": "#343434",
        "WindowText": "#cbc8c9",
        "Base": "#343434",
        "AlternateBase": "#3b3b3b",
        "ToolTipBase": "#424242",
        "ToolTipText": "#cbc8c9",
        "Text": "#cbc8c9",
        "Button": "#343434",
        "ButtonText": "#cbc8c9",
        "BrightText": "#f5d1c8",
        "Link": "#f5d1c8",
        "Highlight": "#f5d1c8",
        "HighlightedText": "#424242",
        ("Active", "Button"): "#343434",
        ("Disabled", "ButtonText"): "#cbc8c9",
        ("Disabled", "WindowText"): "#cbc8c9",
        ("Disabled", "Text"): "#cbc8c9",
        ("Disabled", "Light"): "#f5d1c8",
    }),
    ("Catppuccin Latte", {
        "Window": "#eff1f5",
        "WindowText": "#4c4f69",
        "Base": "#eff1f5",
        "AlternateBase": "#e6e9ef",
        "ToolTipBase": "#e6e9ef",
        "ToolTipText": "#4c4f69",
        "Text": "#4c4f69",
        "Button": "#eff1f5",
        "ButtonText": "#4c4f69",
        "BrightText": "#d20f39",
        "Link": "#dd7878",
        "Highlight": "#8839ef",
        "HighlightedText": "#dce0e8",
        ("Active", "Button"): "#eff1f5",
        ("Disabled", "ButtonText"): "#8c8fa1",
        ("Disabled", "WindowText"): "#8c8fa1",
        ("Disabled", "Text"): "#8c8fa1",
        ("Disabled", "Light"): "#ccd0da",
    }),
    ("Catppuccin Frappé", {
        "Window": "#303446",
        "WindowText": "#c6d0f5",
        "Base": "#303446",
        "AlternateBase": "#292c3c",
        "ToolTipBase": "#292c3c",
        "ToolTipText": "#c6d0f5",
        "Text": "#c6d0f5",
        "Button": "#303446",
        "ButtonText": "#c6d0f5",
        "BrightText": "#e78284",
        "Link": "#eebebe",
        "Highlight": "#ca9ee6",
        "HighlightedText": "#232634",
        ("Active", "Button"): "#303446",
        ("Disabled", "ButtonText"): "#838ba7",
        ("Disabled", "WindowText"): "#838ba7",
        ("Disabled", "Text"): "#838ba7",
        ("Disabled", "Light"): "#414559",
    }),
    ("Catppuccin Macchiato", {
        "Window": "#24273a",
        "WindowText": "#cad3f5",
        "Base": "#24273a",
        "AlternateBase": "#1e2030",
        "ToolTipBase": "#1e2030",
        "ToolTipText": "#cad3f5",
        "Text": "#cad3f5",
        "Button": "#24273a",
        "ButtonText": "#cad3f5",
        "BrightText": "#f38ba8",
        "Link": "#f0c6c6",
        "Highlight": "#c6a0f6",
        "HighlightedText": "#181926",
        ("Active", "Button"): "#24273a",
        ("Disabled", "ButtonText"): "#8087a2",
        ("Disabled", "WindowText"): "#8087a2",
        ("Disabled", "Text"): "#8087a2",
        ("Disabled", "Light"): "#363a4f",
    }),
    ("Catppuccin Mocha", {
        "Window": "#1e1e2e",
        "WindowText": "#cdd6f4",
        "Base": "#1e1e2e",
        "AlternateBase": "#181825",
        "ToolTipBase": "#181825",
        "ToolTipText": "#cdd6f4",
        "Text": "#cdd6f4",
        "Button": "#1e1e2e",
        "ButtonText": "#cdd6f4",
        "BrightText": "#f38ba8",
        "Link": "#f2cdcd",
        "Highlight": "#cba6f7",
        "HighlightedText": "#11111b",
        ("Active", "Button"): "#1e1e2e",
        ("Disabled", "ButtonText"): "#7f849c",
        ("Disabled", "WindowText"): "#7f849c",
        ("Disabled", "Text"): "#7f849c",
        ("Disabled", "Light"): "#313244",
    }),
]

# This will be populated with actual QPalette objects after QApplication is created
palettes = dict()

# Expose theme names for compatibility
themes = [(name, colors) for name, colors in _theme_definitions]

def initialize_palettes():
    """Initialize palettes after QApplication is created"""
    global palettes
    if palettes:  # Already initialized
        return
    
    # Create a mapping from string names to QPalette enums
    color_roles = {
        "Window": QPalette.ColorRole.Window,
        "WindowText": QPalette.ColorRole.WindowText,
        "Base": QPalette.ColorRole.Base,
        "AlternateBase": QPalette.ColorRole.AlternateBase,
        "ToolTipBase": QPalette.ColorRole.ToolTipBase,
        "ToolTipText": QPalette.ColorRole.ToolTipText,
        "Text": QPalette.ColorRole.Text,
        "Button": QPalette.ColorRole.Button,
        "ButtonText": QPalette.ColorRole.ButtonText,
        "BrightText": QPalette.ColorRole.BrightText,
        "Link": QPalette.ColorRole.Link,
        "Highlight": QPalette.ColorRole.Highlight,
        "HighlightedText": QPalette.ColorRole.HighlightedText,
        "Light": QPalette.ColorRole.Light,
    }
    
    color_groups = {
        "Active": QPalette.ColorGroup.Active,
        "Disabled": QPalette.ColorGroup.Disabled,
        "Inactive": QPalette.ColorGroup.Inactive,
    }
    
    for name, colors in _theme_definitions:
        palette = QPalette()
        for role, color in colors.items():
            if isinstance(role, tuple):
                # Role is a tuple like ("Active", "Button")
                group_name, role_name = role
                group = color_groups[group_name]
                role_enum = color_roles[role_name]
                palette.setColor(group, role_enum, QColor(color))
            else:
                # Role is just a string like "Window"
                role_enum = color_roles[role]
                palette.setColor(role_enum, QColor(color))
        palettes[name] = palette


class Theme:

    theme = ""

    @classmethod
    def set_theme(cls, theme):
        initialize_palettes()  # Ensure palettes are initialized
        cls.theme = theme
        if theme in palettes:
            QApplication.instance().setPalette(palettes[theme])
            QApplication.instance().setStyle("Fusion")
        # For default/system theme, do nothing
        # User will have to restart the application for it to be applied

    @classmethod
    def get_theme(cls):
        return cls.theme

    @classmethod
    def mask_light_factor(cls):
        if cls.theme == "Light":
            return 103
        return 150
