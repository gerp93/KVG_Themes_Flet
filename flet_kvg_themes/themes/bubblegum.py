"""
Bubblegum Theme for Flet
Hot pink explosion
"""

import flet as ft
from ..core import register_theme


def create_bubblegum_theme() -> ft.Theme:
    """
    Create the bubblegum theme for Flet.
    
    Returns:
        A Flet Theme object with bubblegum color scheme
    """
    # Bubblegum colors from original theme
    # All colors from original palette are preserved for consistency
    bg_color = "#ff69b4"
    white = "#ffffff"
    deep_magenta = "#cc0066"
    baby_blue = "#87ceeb"
    candy_purple = "#9932cc"
    sunshine = "#ffff00"
    cotton_candy = "#ffb6c1"  # Reserved for future use
    
    return ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=candy_purple,
            on_primary=white,
            primary_container=candy_purple,
            on_primary_container=sunshine,
            secondary=baby_blue,
            on_secondary=deep_magenta,
            secondary_container=baby_blue,
            on_secondary_container=candy_purple,
            tertiary=deep_magenta,
            on_tertiary=white,
            surface=bg_color,
            on_surface=white,
            surface_variant=cotton_candy,
            on_surface_variant=deep_magenta,
            background=bg_color,
            on_background=white,
            error=deep_magenta,
            on_error=white,
            outline=candy_purple,
            shadow="#000000",
        ),
        use_material3=True,
    )


# Theme metadata
THEME_INFO = {
    "id": "bubblegum",
    "name": "🍬 Bubblegum",
    "icon": "🍬",
    "description": "Hot pink explosion"
}

# Register the theme
register_theme(
    theme_id=THEME_INFO["id"],
    name=THEME_INFO["name"],
    theme_factory=create_bubblegum_theme,
    icon=THEME_INFO["icon"],
    description=THEME_INFO["description"]
)
