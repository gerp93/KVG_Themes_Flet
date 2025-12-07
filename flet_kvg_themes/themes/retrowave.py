"""
Retrowave Theme for Flet
80s synthwave sunset vibes
"""

import flet as ft
from ..core import register_theme


def create_retrowave_theme() -> ft.Theme:
    """
    Create the retrowave theme for Flet.
    
    Returns:
        A Flet Theme object with retrowave color scheme
    """
    # Retrowave colors from original theme
    # All colors from original palette are preserved for consistency
    bg_color = "#1a0a2e"
    sunset_pink = "#ff6b9d"
    sunset_orange = "#ff9a56"
    sunset_yellow = "#ffd93d"  # Reserved for future use
    synth_purple = "#c77dff"
    hot_magenta = "#e040fb"  # Reserved for future use
    chrome = "#e0e0e0"
    
    return ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=sunset_pink,
            on_primary="#000000",
            primary_container="#2d1b4e",
            on_primary_container=sunset_yellow,
            secondary=sunset_orange,
            on_secondary="#000000",
            secondary_container="#3d1f5c",
            on_secondary_container=sunset_orange,
            tertiary=synth_purple,
            on_tertiary="#000000",
            surface=bg_color,
            on_surface=chrome,
            surface_variant="#2d1b4e",
            on_surface_variant=chrome,
            background=bg_color,
            on_background=sunset_pink,
            error=hot_magenta,
            on_error="#000000",
            outline="#5c2d8a",
            shadow="#000000",
        ),
        use_material3=True,
    )


# Theme metadata
THEME_INFO = {
    "id": "retrowave",
    "name": "🌅 Retrowave",
    "icon": "🌅",
    "description": "80s synthwave sunset vibes"
}

# Register the theme
register_theme(
    theme_id=THEME_INFO["id"],
    name=THEME_INFO["name"],
    theme_factory=create_retrowave_theme,
    icon=THEME_INFO["icon"],
    description=THEME_INFO["description"]
)
