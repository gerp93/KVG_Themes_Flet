"""
Hacker Theme for Flet
Matrix-style green on black
"""

import flet as ft
from ..core import register_theme


def create_hacker_theme() -> ft.Theme:
    """
    Create the hacker theme for Flet.
    
    Returns:
        A Flet Theme object with hacker/matrix color scheme
    """
    # Hacker/Matrix colors from original theme
    bg_color = "#0d0d0d"
    matrix_green = "#00ff00"
    lime = "#32cd32"
    phosphor = "#00ff41"
    amber = "#ffbf00"
    terminal_green = "#20c20e"
    
    return ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=matrix_green,
            on_primary="#000000",
            primary_container="#001a00",
            on_primary_container=matrix_green,
            secondary=phosphor,
            on_secondary="#000000",
            secondary_container="#003300",
            on_secondary_container=phosphor,
            tertiary=lime,
            on_tertiary="#000000",
            surface=bg_color,
            on_surface=terminal_green,
            surface_variant="#001100",
            on_surface_variant=matrix_green,
            background=bg_color,
            on_background=matrix_green,
            error=amber,
            on_error="#000000",
            outline="#003300",
            shadow="#000000",
        ),
        use_material3=True,
    )


# Theme metadata
THEME_INFO = {
    "id": "hacker",
    "name": "💻 Hacker",
    "icon": "💻",
    "description": "Matrix-style green on black"
}

# Register the theme
register_theme(
    theme_id=THEME_INFO["id"],
    name=THEME_INFO["name"],
    theme_factory=create_hacker_theme,
    icon=THEME_INFO["icon"],
    description=THEME_INFO["description"]
)
