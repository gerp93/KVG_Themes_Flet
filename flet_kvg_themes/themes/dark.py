"""
Dark Theme for Flet
Easy on the eyes
"""

import flet as ft
from ..core import register_theme


def create_dark_theme() -> ft.Theme:
    """
    Create the dark theme for Flet.
    
    Returns:
        A Flet Theme object with dark color scheme
    """
    return ft.Theme(
        color_scheme=ft.ColorScheme(
            primary="#808080",
            on_primary="#ffffff",
            primary_container="#505050",
            on_primary_container="#ffffff",
            secondary="#606060",
            on_secondary="#ffffff",
            secondary_container="#707070",
            on_secondary_container="#ffffff",
            tertiary="#505050",
            on_tertiary="#ffffff",
            surface="#2b2b2b",
            on_surface="#ffffff",
            surface_variant="#404040",
            on_surface_variant="#ffffff",
            background="#2b2b2b",
            on_background="#ffffff",
            error="#cf6679",
            on_error="#000000",
            outline="#505050",
            shadow="#000000",
        ),
        use_material3=True,
    )


# Theme metadata
THEME_INFO = {
    "id": "dark",
    "name": "🌙 Dark Theme",
    "icon": "🌙",
    "description": "Easy on the eyes"
}

# Register the theme
register_theme(
    theme_id=THEME_INFO["id"],
    name=THEME_INFO["name"],
    theme_factory=create_dark_theme,
    icon=THEME_INFO["icon"],
    description=THEME_INFO["description"]
)
