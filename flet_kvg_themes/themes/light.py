"""
Light Theme for Flet
Default clean look
"""

import flet as ft
from ..core import register_theme


def create_light_theme() -> ft.Theme:
    """
    Create the light theme for Flet.
    
    Returns:
        A Flet Theme object with light color scheme
    """
    return ft.Theme(
        color_scheme=ft.ColorScheme(
            primary="#0078d4",
            on_primary="#ffffff",
            primary_container="#e0e0e0",
            on_primary_container="#000000",
            secondary="#505050",
            on_secondary="#ffffff",
            secondary_container="#d0d0d0",
            on_secondary_container="#000000",
            tertiary="#707070",
            on_tertiary="#ffffff",
            surface="#f5f5f5",
            on_surface="#000000",
            surface_variant="#e0e0e0",
            on_surface_variant="#000000",
            background="#f5f5f5",
            on_background="#000000",
            error="#d32f2f",
            on_error="#ffffff",
            outline="#c0c0c0",
            shadow="#000000",
        ),
        use_material3=True,
    )


# Theme metadata
THEME_INFO = {
    "id": "light",
    "name": "☀️ Light Theme",
    "icon": "☀️",
    "description": "Default clean look"
}

# Register the theme
register_theme(
    theme_id=THEME_INFO["id"],
    name=THEME_INFO["name"],
    theme_factory=create_light_theme,
    icon=THEME_INFO["icon"],
    description=THEME_INFO["description"]
)
