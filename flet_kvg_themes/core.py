"""
Core theme management functionality for flet_kvg_themes.

This module provides the theme registry and helper functions for
managing and applying themes in Flet applications.
"""

from typing import Dict, List, Tuple, Optional, Callable
import flet as ft

# Global theme registry
_THEME_REGISTRY: Dict[str, Dict] = {}


def register_theme(
    theme_id: str,
    name: str,
    theme_factory: Callable[[], ft.Theme],
    icon: str = "",
    description: str = ""
) -> None:
    """
    Register a theme in the global registry.
    
    Args:
        theme_id: Unique identifier for the theme
        name: Display name of the theme
        theme_factory: Function that returns a ft.Theme object
        icon: Optional emoji icon for the theme
        description: Optional description of the theme
    """
    _THEME_REGISTRY[theme_id] = {
        "id": theme_id,
        "name": name,
        "icon": icon,
        "description": description,
        "factory": theme_factory,
    }


def get_theme(theme_id: str) -> Optional[ft.Theme]:
    """
    Get a theme by its ID.
    
    Args:
        theme_id: The unique identifier of the theme
        
    Returns:
        A Flet Theme object, or None if theme not found
        
    Example:
        >>> theme = get_theme("dark")
        >>> page.theme = theme
    """
    if theme_id not in _THEME_REGISTRY:
        return None
    
    theme_info = _THEME_REGISTRY[theme_id]
    return theme_info["factory"]()


def get_theme_list() -> List[Tuple[str, str]]:
    """
    Get a list of all available themes.
    
    Returns:
        List of tuples containing (theme_id, theme_name)
        
    Example:
        >>> themes = get_theme_list()
        >>> print(themes)
        [('light', '☀️ Light Theme'), ('dark', '🌙 Dark Theme'), ...]
    """
    return [(info["id"], info["name"]) for info in _THEME_REGISTRY.values()]


def get_all_themes() -> Dict[str, Dict]:
    """
    Get the complete theme registry.
    
    Returns:
        Dictionary mapping theme IDs to theme information
        (does not include the factory function)
    """
    return {
        theme_id: {
            "id": info["id"],
            "name": info["name"],
            "icon": info["icon"],
            "description": info["description"],
        }
        for theme_id, info in _THEME_REGISTRY.items()
    }


def theme_exists(theme_id: str) -> bool:
    """
    Check if a theme exists in the registry.
    
    Args:
        theme_id: The theme ID to check
        
    Returns:
        True if the theme exists, False otherwise
    """
    return theme_id in _THEME_REGISTRY
