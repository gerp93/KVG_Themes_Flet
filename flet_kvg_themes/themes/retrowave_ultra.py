"""
Retrowave ULTRA Theme for Flet
Extremely intense 80s synthwave sunset - maximum saturation version
"""

import flet as ft
from ..core import register_theme


def create_retrowave_ultra_theme() -> ft.Theme:
    """
    Create the retrowave ULTRA theme for Flet.
    
    Returns:
        A Flet Theme object with extreme retrowave color scheme
    """
    # Retrowave colors - using brightest, most saturated versions
    hot_magenta = "#ff00ff"  # Pure magenta
    synth_purple = "#da00ff"  # More saturated purple
    sunset_yellow = "#ffd700"  # Gold yellow
    sunset_orange = "#ff4500"  # Red-orange, more intense
    bg_color = "#ff1493"  # Hot pink background - extremely intense
    
    return ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=hot_magenta,  # Pure magenta primary
            on_primary="#000000",
            primary_container=synth_purple,  # Purple containers
            on_primary_container=sunset_yellow,  # Yellow on purple
            secondary=sunset_orange,  # Bright orange
            on_secondary="#000000",
            secondary_container=bg_color,  # Pink containers
            on_secondary_container="#000000",
            tertiary="#00ffff",  # Cyan tertiary
            on_tertiary="#000000",
            surface=bg_color,  # Hot pink surfaces - very intense
            on_surface="#ffffff",
            surface_variant=synth_purple,  # Purple variant
            on_surface_variant=sunset_yellow,
            background=hot_magenta,  # Pure magenta background - visually assaulting
            on_background="#ffffff",
            error=sunset_orange,
            on_error="#000000",
            outline=sunset_yellow,  # Yellow outlines
            shadow="#000000",
        ),
        use_material3=True,
    )


# Theme metadata
THEME_INFO = {
    "id": "retrowave_ultra",
    "name": "🌅💥 Retrowave ULTRA",
    "icon": "🌅💥",
    "description": "Extremely intense 80s synthwave - visually assaulting"
}

# Register the theme
register_theme(
    theme_id=THEME_INFO["id"],
    name=THEME_INFO["name"],
    theme_factory=create_retrowave_ultra_theme,
    icon=THEME_INFO["icon"],
    description=THEME_INFO["description"]
)
