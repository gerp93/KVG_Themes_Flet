"""
Hacker ULTRA Theme for Flet
Extremely intense Matrix-style green - maximum brightness version
"""

import flet as ft
from ..core import register_theme


def create_hacker_ultra_theme() -> ft.Theme:
    """
    Create the hacker ULTRA theme for Flet.
    
    Returns:
        A Flet Theme object with extreme hacker/matrix color scheme
    """
    # Hacker/Matrix colors - using brightest possible greens
    bg_color = "#000000"  # Pure black for maximum contrast
    matrix_green = "#00ff00"  # Pure green - maximum intensity
    lime = "#39ff14"  # Neon lime green
    phosphor = "#00ff41"  # Phosphor green
    amber = "#ffbf00"  # Warning amber
    terminal_green = "#00ff00"  # Pure green
    bright_lime = "#ccff00"  # Yellow-green
    
    return ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=matrix_green,  # Pure green primary
            on_primary="#000000",
            primary_container=lime,  # Neon lime containers
            on_primary_container="#000000",
            secondary=phosphor,  # Phosphor green
            on_secondary="#000000",
            secondary_container=bright_lime,  # Yellow-green containers
            on_secondary_container="#000000",
            tertiary=amber,  # Amber tertiary
            on_tertiary="#000000",
            surface=lime,  # Neon lime surfaces - extremely bright
            on_surface="#000000",
            surface_variant=matrix_green,  # Pure green variant
            on_surface_variant="#000000",
            background=phosphor,  # Phosphor green background - visually assaulting
            on_background="#000000",
            error=amber,
            on_error="#000000",
            outline=matrix_green,  # Pure green outlines
            shadow="#000000",
        ),
        font_family="Consolas",  # Matching original theme font
        use_material3=True,
    )


# Theme metadata
THEME_INFO = {
    "id": "hacker_ultra",
    "name": "💻💥 Hacker ULTRA",
    "icon": "💻💥",
    "description": "Extremely intense Matrix green - visually assaulting"
}

# Register the theme
register_theme(
    theme_id=THEME_INFO["id"],
    name=THEME_INFO["name"],
    theme_factory=create_hacker_ultra_theme,
    icon=THEME_INFO["icon"],
    description=THEME_INFO["description"]
)
