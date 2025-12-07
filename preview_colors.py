"""
Color Preview Generator

This script prints a visual preview of all theme colors to the console.
"""

from flet_kvg_themes import get_theme, get_theme_list


def print_color_info(theme_id: str, theme_name: str):
    """Print color information for a theme."""
    theme = get_theme(theme_id)
    cs = theme.color_scheme
    
    print(f"\n{'=' * 70}")
    print(f"{theme_name}")
    print(f"{'=' * 70}")
    
    colors = [
        ("Primary", cs.primary),
        ("On Primary", cs.on_primary),
        ("Primary Container", cs.primary_container),
        ("Secondary", cs.secondary),
        ("On Secondary", cs.on_secondary),
        ("Tertiary", cs.tertiary),
        ("Surface", cs.surface),
        ("On Surface", cs.on_surface),
        ("Background", cs.background),
        ("On Background", cs.on_background),
        ("Error", cs.error),
        ("Outline", cs.outline),
    ]
    
    for name, color in colors:
        if color:
            print(f"  {name:.<25} {color}")


def main():
    """Generate color previews for all themes."""
    print("\n" + "=" * 70)
    print("KVG THEMES FOR FLET - COLOR REFERENCE")
    print("=" * 70)
    
    themes = get_theme_list()
    
    for theme_id, theme_name in themes:
        print_color_info(theme_id, theme_name)
    
    print("\n" + "=" * 70)
    print(f"Total themes: {len(themes)}")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
