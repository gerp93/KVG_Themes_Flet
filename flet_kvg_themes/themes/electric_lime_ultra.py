"""
Electric Lime ULTRA Theme for Flet
Extremely intense blindingly bright green-yellow - maximum saturation version
"""

import flet as ft
from ..core import register_theme


def create_electric_lime_ultra_theme() -> ft.Theme:
    """
    Create the electric lime ULTRA theme for Flet.
    
    Returns:
        A Flet Theme object with extreme electric lime color scheme
    """
    # Electric Lime colors - using brightest possible yellow-green
    bright_lime = "#ccff00"  # Electric lime background - extremely bright
    ultra_lime = "#ffff00"  # Pure yellow
    deep_purple = "#4a0080"  # Deep purple
    ultra_violet = "#9900ff"  # Ultra violet
    magenta_pop = "#ff00aa"  # Magenta
    electric_blue = "#0066ff"  # Electric blue
    
    return ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=deep_purple,  # Deep purple primary
            on_primary=ultra_lime,  # Yellow on purple
            primary_container=ultra_violet,  # Violet containers
            on_primary_container=ultra_lime,
            secondary=electric_blue,  # Electric blue
            on_secondary=ultra_lime,
            secondary_container=magenta_pop,  # Magenta containers
            on_secondary_container=ultra_lime,
            tertiary=magenta_pop,  # Magenta tertiary
            on_tertiary=ultra_lime,
            surface=bright_lime,  # Bright lime surfaces - extremely intense
            on_surface="#000000",
            surface_variant=ultra_lime,  # Pure yellow variant
            on_surface_variant=deep_purple,
            background=bright_lime,  # Electric lime background - visually assaulting
            on_background="#000000",
            error=magenta_pop,
            on_error=ultra_lime,
            outline=deep_purple,  # Purple outlines
            shadow="#000000",
        ),
        font_family="Trebuchet MS",  # Matching original theme font
        use_material3=True,
    )


# Theme metadata
THEME_INFO = {
    "id": "electric_lime_ultra",
    "name": "⚡💥 Electric Lime ULTRA",
    "icon": "⚡💥",
    "description": "Extremely intense blindingly bright lime - visually assaulting"
}

# Register the theme
register_theme(
    theme_id=THEME_INFO["id"],
    name=THEME_INFO["name"],
    theme_factory=create_electric_lime_ultra_theme,
    icon=THEME_INFO["icon"],
    description=THEME_INFO["description"]
)
