"""
Neon ULTRA Theme for Flet
Extremely visually assaulting neon colors - maximum intensity version
"""

import flet as ft
from ..core import register_theme


def create_neon_ultra_theme() -> ft.Theme:
    """
    Create the neon ULTRA theme for Flet.
    
    Returns:
        A Flet Theme object with extreme neon color scheme
    """
    # Neon colors from original theme - using brightest possible combinations
    bg_color = "#000000"  # Pure black for maximum contrast
    neon_pink = "#ff00ff"  # Full saturation magenta
    neon_cyan = "#00ffff"  # Full saturation cyan
    neon_green = "#39ff14"  # Brightest neon green
    neon_yellow = "#ffff00"  # Pure yellow
    neon_orange = "#ff6600"
    hot_pink = "#ff1493"
    electric_blue = "#00ffff"  # Using cyan for maximum brightness
    ultra_violet = "#ff00ff"  # Using magenta
    
    return ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=neon_cyan,  # Bright cyan everywhere
            on_primary="#000000",
            primary_container=neon_pink,  # Bright magenta containers
            on_primary_container=neon_yellow,  # Yellow text on magenta
            secondary=neon_green,  # Brightest green
            on_secondary="#000000",
            secondary_container=neon_cyan,  # Cyan containers
            on_secondary_container=neon_pink,
            tertiary=neon_yellow,  # Bright yellow
            on_tertiary="#000000",
            surface=neon_pink,  # Magenta surface - very intense
            on_surface=neon_cyan,  # Cyan text
            surface_variant=neon_green,  # Green variant surfaces
            on_surface_variant="#000000",
            background=ultra_violet,  # Magenta background - visually assaulting
            on_background=neon_cyan,
            error=neon_orange,
            on_error="#000000",
            outline=neon_yellow,  # Yellow outlines
            shadow="#000000",
        ),
        font_family="Consolas",  # Matching original theme font
        use_material3=True,
    )


# Theme metadata
THEME_INFO = {
    "id": "neon_ultra",
    "name": "🌈💥 NEON ULTRA",
    "icon": "🌈💥",
    "description": "Extremely intense neon colors - visually assaulting"
}

# Register the theme
register_theme(
    theme_id=THEME_INFO["id"],
    name=THEME_INFO["name"],
    theme_factory=create_neon_ultra_theme,
    icon=THEME_INFO["icon"],
    description=THEME_INFO["description"]
)
