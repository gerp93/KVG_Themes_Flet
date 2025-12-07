"""
Commander Keen Theme for Flet
Classic DOS EGA/VGA palette
"""

import flet as ft
from ..core import register_theme


def create_commander_keen_theme() -> ft.Theme:
    """
    Create the Commander Keen theme for Flet.
    
    Returns:
        A Flet Theme object with classic DOS EGA/VGA color scheme
    """
    # EGA/VGA colors from original theme
    # Complete 16-color EGA palette preserved for authenticity
    bg_color = "#0000aa"
    ega_black = "#000000"
    ega_magenta = "#aa00aa"
    ega_dark_gray = "#555555"  # Part of complete EGA palette
    ega_bright_blue = "#5555ff"
    ega_bright_green = "#55ff55"
    ega_bright_cyan = "#55ffff"
    ega_yellow = "#ffff55"
    ega_white = "#ffffff"  # Part of complete EGA palette
    ega_brown = "#aa5500"  # Part of complete EGA palette
    ega_cyan = "#00aaaa"  # Part of complete EGA palette
    
    return ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=ega_bright_blue,
            on_primary=ega_yellow,
            primary_container=ega_bright_blue,
            on_primary_container=ega_yellow,
            secondary=ega_bright_green,
            on_secondary=ega_black,
            secondary_container=ega_bright_green,
            on_secondary_container=ega_black,
            tertiary=ega_bright_cyan,
            on_tertiary=ega_black,
            surface=bg_color,
            on_surface=ega_yellow,
            surface_variant=ega_black,
            on_surface_variant=ega_bright_green,
            background=bg_color,
            on_background=ega_yellow,
            error=ega_magenta,
            on_error=ega_yellow,
            outline=ega_bright_cyan,
            shadow=ega_black,
        ),
        use_material3=True,
    )


# Theme metadata
THEME_INFO = {
    "id": "commander_keen",
    "name": "🚀 Commander Keen",
    "icon": "🚀",
    "description": "Classic DOS EGA/VGA palette"
}

# Register the theme
register_theme(
    theme_id=THEME_INFO["id"],
    name=THEME_INFO["name"],
    theme_factory=create_commander_keen_theme,
    icon=THEME_INFO["icon"],
    description=THEME_INFO["description"]
)
