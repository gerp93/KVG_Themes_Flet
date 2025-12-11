"""
flet_kvg_themes - KVG Themes for Flet Applications

A collection of vibrant, pre-built themes for Flet applications, ported from
the tkthemes library. Includes 9 unique themes with distinctive color palettes,
plus 7 ULTRA variants with extremely intense, visually assaulting colors.

Usage:
    import flet as ft
    from flet_kvg_themes import get_theme, get_theme_list
    
    def main(page: ft.Page):
        # Apply a theme
        page.theme = get_theme("neon")
        page.title = "My Themed App"
        
        # Add your UI components
        page.add(ft.Text("Hello, themed world!"))
    
    ft.app(target=main)

Available themes:
    - light: ☀️ Light Theme - Default clean look
    - dark: 🌙 Dark Theme - Easy on the eyes
    - neon: 🌈 NEON Theme - Visually wild but readable
    - retrowave: 🌅 Retrowave - 80s synthwave sunset vibes
    - hacker: 💻 Hacker - Matrix-style green on black
    - lava: 🌋 LAVA - Fiery red hot theme
    - electric_lime: ⚡ Electric Lime - Blindingly bright green-yellow
    - bubblegum: 🍬 Bubblegum - Hot pink explosion
    - commander_keen: 🚀 Commander Keen - Classic DOS EGA/VGA palette

ULTRA themes (extremely intense versions):
    - neon_ultra: 🌈💥 NEON ULTRA - Extremely intense neon colors
    - retrowave_ultra: 🌅💥 Retrowave ULTRA - Extremely intense 80s synthwave
    - hacker_ultra: 💻💥 Hacker ULTRA - Extremely intense Matrix green
    - lava_ultra: 🌋💥 LAVA ULTRA - Extremely intense fiery red
    - electric_lime_ultra: ⚡💥 Electric Lime ULTRA - Extremely intense lime
    - bubblegum_ultra: 🍬💥 Bubblegum ULTRA - Extremely intense hot pink
    - commander_keen_ultra: 🚀💥 Commander Keen ULTRA - Extremely intense DOS palette
"""

__version__ = "1.0.0"
__author__ = "KVGroove"

# Import all themes to register them
from . import themes  # noqa: F401

# Import core functionality
from .core import (
    get_theme,
    get_theme_list,
    get_all_themes,
    register_theme,
    theme_exists,
)

__all__ = [
    "get_theme",
    "get_theme_list",
    "get_all_themes",
    "register_theme",
    "theme_exists",
    "__version__",
    "__author__",
]
