"""
Commander Keen ULTRA Theme for Flet
Extremely intense classic DOS EGA/VGA palette - maximum saturation version
"""

import flet as ft
from ..core import register_theme


def create_commander_keen_ultra_theme() -> ft.Theme:
    """
    Create the Commander Keen ULTRA theme for Flet.
    
    Returns:
        A Flet Theme object with extreme DOS EGA/VGA color scheme
    """
    # EGA/VGA colors - using brightest possible DOS palette colors
    bright_blue = "#0000ff"  # Pure blue background - extremely intense
    ega_magenta = "#ff00ff"  # Pure magenta
    ega_bright_cyan = "#00ffff"  # Pure cyan
    ega_bright_green = "#00ff00"  # Pure green
    ega_yellow = "#ffff00"  # Pure yellow
    ega_red = "#ff0000"  # Pure red
    
    return ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=ega_bright_cyan,  # Cyan primary
            on_primary="#000000",
            primary_container="#5555ff",  # Bright blue containers
            on_primary_container=ega_yellow,  # Yellow on blue
            secondary=ega_bright_green,  # Pure green
            on_secondary="#000000",
            secondary_container=ega_magenta,  # Magenta containers
            on_secondary_container="#ffffff",
            tertiary=ega_yellow,  # Yellow tertiary
            on_tertiary="#000000",
            surface="#5555ff",  # Bright blue surfaces - very intense
            on_surface=ega_yellow,
            surface_variant=ega_magenta,  # Magenta variant
            on_surface_variant=ega_bright_cyan,
            background=bright_blue,  # Pure blue background - visually assaulting
            on_background=ega_yellow,
            error=ega_red,
            on_error="#ffffff",
            outline=ega_bright_green,  # Green outlines
            shadow="#000000",
        ),
        use_material3=True,
    )


# Theme metadata
THEME_INFO = {
    "id": "commander_keen_ultra",
    "name": "🚀💥 Commander Keen ULTRA",
    "icon": "🚀💥",
    "description": "Extremely intense DOS EGA/VGA - visually assaulting"
}

# Register the theme
register_theme(
    theme_id=THEME_INFO["id"],
    name=THEME_INFO["name"],
    theme_factory=create_commander_keen_ultra_theme,
    icon=THEME_INFO["icon"],
    description=THEME_INFO["description"]
)
