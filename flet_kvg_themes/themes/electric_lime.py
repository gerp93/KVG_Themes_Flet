"""
Electric Lime Theme for Flet
Blindingly bright green-yellow
"""

import flet as ft
from ..core import register_theme


def create_electric_lime_theme() -> ft.Theme:
    """
    Create the electric lime theme for Flet.
    
    Returns:
        A Flet Theme object with electric lime color scheme
    """
    # Electric Lime colors from original theme
    # All colors from original palette are preserved for consistency
    bg_color = "#ccff00"
    hot_black = "#0a0a0a"
    deep_purple = "#4a0080"
    electric_blue = "#0066ff"
    magenta_pop = "#ff00aa"
    dark_lime = "#88aa00"
    ultra_violet = "#7700ff"  # Reserved for future use
    
    return ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=deep_purple,
            on_primary=bg_color,
            primary_container=deep_purple,
            on_primary_container=bg_color,
            secondary=electric_blue,
            on_secondary="#ffffff",
            secondary_container="#0080ff",
            on_secondary_container=bg_color,
            tertiary=magenta_pop,
            on_tertiary="#ffffff",
            surface=bg_color,
            on_surface=hot_black,
            surface_variant=dark_lime,
            on_surface_variant=hot_black,
            background=bg_color,
            on_background=hot_black,
            error=magenta_pop,
            on_error="#ffffff",
            outline=deep_purple,
            shadow="#000000",
        ),
        use_material3=True,
    )


# Theme metadata
THEME_INFO = {
    "id": "electric_lime",
    "name": "⚡ Electric Lime",
    "icon": "⚡",
    "description": "Blindingly bright green-yellow"
}

# Register the theme
register_theme(
    theme_id=THEME_INFO["id"],
    name=THEME_INFO["name"],
    theme_factory=create_electric_lime_theme,
    icon=THEME_INFO["icon"],
    description=THEME_INFO["description"]
)
