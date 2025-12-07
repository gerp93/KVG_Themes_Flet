"""
Test script to visualize ULTRA themes
"""

import flet as ft
from flet_kvg_themes import get_theme, get_theme_list


def main(page: ft.Page):
    """Main application entry point."""
    page.title = "KVG ULTRA Themes Test"
    page.padding = 20
    page.window.width = 900
    page.window.height = 700
    
    # Get all ULTRA themes
    all_themes = get_theme_list()
    ultra_themes = [(tid, name) for tid, name in all_themes if 'ultra' in tid.lower()]
    
    current_theme_index = [0]  # Use list to allow modification in nested function
    
    theme_label = ft.Text(
        ultra_themes[0][1],
        size=28,
        weight=ft.FontWeight.BOLD,
    )
    
    def update_theme():
        """Update to current theme."""
        theme_id = ultra_themes[current_theme_index[0]][0]
        theme_name = ultra_themes[current_theme_index[0]][1]
        page.theme = get_theme(theme_id)
        theme_label.value = theme_name
        page.update()
    
    def next_theme(e):
        """Go to next theme."""
        current_theme_index[0] = (current_theme_index[0] + 1) % len(ultra_themes)
        update_theme()
    
    def prev_theme(e):
        """Go to previous theme."""
        current_theme_index[0] = (current_theme_index[0] - 1) % len(ultra_themes)
        update_theme()
    
    # Create sample UI elements
    page.add(
        ft.Column(
            [
                ft.Row([
                    ft.IconButton(icon=ft.Icons.ARROW_BACK, on_click=prev_theme, tooltip="Previous"),
                    theme_label,
                    ft.IconButton(icon=ft.Icons.ARROW_FORWARD, on_click=next_theme, tooltip="Next"),
                ]),
                ft.Divider(),
                ft.Text("Sample UI Components", size=20, weight=ft.FontWeight.BOLD),
                ft.Row(
                    [
                        ft.ElevatedButton("Elevated", icon=ft.Icons.ADD),
                        ft.FilledButton("Filled", icon=ft.Icons.CHECK),
                        ft.OutlinedButton("Outlined", icon=ft.Icons.EDIT),
                        ft.TextButton("Text", icon=ft.Icons.DELETE),
                    ],
                    wrap=True,
                ),
                ft.Row(
                    [
                        ft.TextField(label="Text Field", width=200, value="Sample"),
                        ft.Dropdown(
                            label="Dropdown",
                            width=200,
                            value="1",
                            options=[
                                ft.dropdown.Option("1", "Option 1"),
                                ft.dropdown.Option("2", "Option 2"),
                                ft.dropdown.Option("3", "Option 3"),
                            ],
                        ),
                    ],
                    wrap=True,
                ),
                ft.Row(
                    [
                        ft.Checkbox(label="Checkbox 1", value=True),
                        ft.Checkbox(label="Checkbox 2", value=False),
                        ft.Switch(label="Switch", value=True),
                    ],
                    wrap=True,
                ),
                ft.Row(
                    [
                        ft.Chip(label=ft.Text("Chip 1"), leading=ft.Icon(ft.Icons.STAR)),
                        ft.Chip(label=ft.Text("Chip 2"), leading=ft.Icon(ft.Icons.FAVORITE)),
                    ],
                    wrap=True,
                ),
                ft.ProgressBar(value=0.7, width=400),
                ft.Container(
                    content=ft.Text(
                        "This is a container with some text to show background colors",
                        size=14,
                    ),
                    padding=10,
                    border=ft.border.all(2),
                    border_radius=8,
                ),
                ft.Text(
                    f"Testing {len(ultra_themes)} ULTRA themes. Use arrow buttons to navigate.",
                    size=12,
                    italic=True,
                ),
            ],
            spacing=15,
            scroll=ft.ScrollMode.AUTO,
        )
    )
    
    # Apply initial theme
    update_theme()


if __name__ == "__main__":
    ft.app(target=main)
