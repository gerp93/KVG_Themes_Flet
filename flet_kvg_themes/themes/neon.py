"""
Neon Theme for Flet
Visually wild but readable
"""

import flet as ft
from ..core import register_theme


def create_neon_theme() -> ft.Theme:
    """
    Create the neon theme for Flet.
    
    Returns:
        A Flet Theme object with neon color scheme
    """
    # Neon colors from original theme
    bg_color = "#0a0a0a"
    neon_pink = "#ff00ff"
    neon_cyan = "#00ffff"
    neon_green = "#39ff14"
    neon_yellow = "#ffff00"
    neon_orange = "#ff6600"
    hot_pink = "#ff1493"
    electric_blue = "#7df9ff"
    
    return ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=neon_cyan,
            on_primary="#000000",
            primary_container="#330033",
            on_primary_container=neon_green,
            secondary=neon_pink,
            on_secondary="#000000",
            secondary_container="#003333",
            on_secondary_container=neon_cyan,
            tertiary=neon_orange,
            on_tertiary="#000000",
            surface=bg_color,
            on_surface=neon_cyan,
            surface_variant="#1a1a2e",
            on_surface_variant=neon_green,
            background=bg_color,
            on_background=electric_blue,
            error=hot_pink,
            on_error="#000000",
            outline="#660066",
            shadow="#000000",
        ),
        use_material3=True,
    )


# Theme metadata
THEME_INFO = {
    "id": "neon",
    "name": "🌈 NEON Theme",
    "icon": "🌈",
    "description": "Visually wild but readable"
}

# Register the theme
register_theme(
    theme_id=THEME_INFO["id"],
    name=THEME_INFO["name"],
    theme_factory=create_neon_theme,
    icon=THEME_INFO["icon"],
    description=THEME_INFO["description"]
)
