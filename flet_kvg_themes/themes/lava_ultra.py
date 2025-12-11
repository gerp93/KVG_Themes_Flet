"""
Lava ULTRA Theme for Flet
Extremely intense fiery red hot theme - maximum saturation version
"""

import flet as ft
from ..core import register_theme


def create_lava_ultra_theme() -> ft.Theme:
    """
    Create the lava ULTRA theme for Flet.
    
    Returns:
        A Flet Theme object with extreme lava/fire color scheme
    """
    # Lava colors - using brightest, most saturated fire colors
    bright_red = "#ff0000"  # Pure red
    molten_orange = "#ff6600"  # Molten orange
    fire_yellow = "#ffcc00"  # Fire yellow
    white_hot = "#ffffff"  # Pure white
    bright_flame = "#ff3300"  # Bright flame
    extreme_orange = "#ff4500"  # Red-orange
    lava_red = "#cc0000"  # Deep red
    
    return ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=bright_flame,  # Bright flame primary
            on_primary=white_hot,
            primary_container=extreme_orange,  # Red-orange containers
            on_primary_container=fire_yellow,
            secondary=fire_yellow,  # Fire yellow
            on_secondary="#000000",
            secondary_container=molten_orange,  # Orange containers
            on_secondary_container=white_hot,
            tertiary=molten_orange,  # Molten orange
            on_tertiary=white_hot,
            surface=lava_red,  # Deep red surfaces - very intense
            on_surface=white_hot,
            surface_variant=bright_flame,  # Flame variant
            on_surface_variant=fire_yellow,
            background=bright_red,  # Pure red background - visually assaulting
            on_background=white_hot,
            error=extreme_orange,
            on_error=white_hot,
            outline=fire_yellow,  # Yellow outlines
            shadow="#000000",
        ),
        font_family="Impact",  # Matching original theme font
        use_material3=True,
    )


# Theme metadata
THEME_INFO = {
    "id": "lava_ultra",
    "name": "🌋💥 LAVA ULTRA",
    "icon": "🌋💥",
    "description": "Extremely intense fiery red - visually assaulting"
}

# Register the theme
register_theme(
    theme_id=THEME_INFO["id"],
    name=THEME_INFO["name"],
    theme_factory=create_lava_ultra_theme,
    icon=THEME_INFO["icon"],
    description=THEME_INFO["description"]
)
