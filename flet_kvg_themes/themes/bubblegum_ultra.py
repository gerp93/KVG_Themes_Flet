"""
Bubblegum ULTRA Theme for Flet
Extremely intense hot pink explosion - maximum saturation version
"""

import flet as ft
from ..core import register_theme


def create_bubblegum_ultra_theme() -> ft.Theme:
    """
    Create the bubblegum ULTRA theme for Flet.
    
    Returns:
        A Flet Theme object with extreme bubblegum color scheme
    """
    # Bubblegum colors - using brightest, most saturated pinks
    bg_color = "#ff1493"  # Deep pink background - extremely intense
    hot_pink = "#ff69b4"  # Hot pink
    white = "#ffffff"  # Pure white
    deep_magenta = "#ff00ff"  # Pure magenta
    baby_blue = "#00ffff"  # Cyan (brighter than baby blue)
    candy_purple = "#da00ff"  # More saturated purple
    sunshine = "#ffff00"  # Pure yellow
    neon_pink = "#ff00aa"  # Neon pink
    
    return ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=deep_magenta,  # Pure magenta primary
            on_primary=white,
            primary_container=candy_purple,  # Purple containers
            on_primary_container=sunshine,  # Yellow on purple
            secondary=baby_blue,  # Cyan secondary
            on_secondary=deep_magenta,
            secondary_container=neon_pink,  # Neon pink containers
            on_secondary_container=white,
            tertiary=sunshine,  # Yellow tertiary
            on_tertiary=deep_magenta,
            surface=hot_pink,  # Hot pink surfaces - very intense
            on_surface=white,
            surface_variant=neon_pink,  # Neon pink variant
            on_surface_variant=white,
            background=bg_color,  # Deep pink background - visually assaulting
            on_background=white,
            error=candy_purple,
            on_error=white,
            outline=deep_magenta,  # Magenta outlines
            shadow="#000000",
        ),
        use_material3=True,
    )


# Theme metadata
THEME_INFO = {
    "id": "bubblegum_ultra",
    "name": "🍬💥 Bubblegum ULTRA",
    "icon": "🍬💥",
    "description": "Extremely intense hot pink explosion - visually assaulting"
}

# Register the theme
register_theme(
    theme_id=THEME_INFO["id"],
    name=THEME_INFO["name"],
    theme_factory=create_bubblegum_ultra_theme,
    icon=THEME_INFO["icon"],
    description=THEME_INFO["description"]
)
