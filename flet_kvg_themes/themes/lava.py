"""
Lava Theme for Flet
Fiery red hot theme
"""

import flet as ft
from ..core import register_theme


def create_lava_theme() -> ft.Theme:
    """
    Create the lava theme for Flet.
    
    Returns:
        A Flet Theme object with lava/fire color scheme
    """
    # Lava colors from original theme
    bg_color = "#cc0000"
    molten_orange = "#ff6600"
    fire_yellow = "#ffcc00"
    white_hot = "#ffffff"
    dark_ember = "#330000"
    charcoal = "#1a0000"
    bright_flame = "#ff3300"
    
    return ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=molten_orange,
            on_primary=white_hot,
            primary_container=dark_ember,
            on_primary_container=fire_yellow,
            secondary=fire_yellow,
            on_secondary="#000000",
            secondary_container=charcoal,
            on_secondary_container=molten_orange,
            tertiary=bright_flame,
            on_tertiary=white_hot,
            surface=bg_color,
            on_surface=white_hot,
            surface_variant=charcoal,
            on_surface_variant=fire_yellow,
            background=bg_color,
            on_background=white_hot,
            error=bright_flame,
            on_error=white_hot,
            outline="#660000",
            shadow="#000000",
        ),
        use_material3=True,
    )


# Theme metadata
THEME_INFO = {
    "id": "lava",
    "name": "🌋 LAVA",
    "icon": "🌋",
    "description": "Fiery red hot theme"
}

# Register the theme
register_theme(
    theme_id=THEME_INFO["id"],
    name=THEME_INFO["name"],
    theme_factory=create_lava_theme,
    icon=THEME_INFO["icon"],
    description=THEME_INFO["description"]
)
