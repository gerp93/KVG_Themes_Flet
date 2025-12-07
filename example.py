"""
KVG Themes for Flet - Example Application

This example demonstrates all available themes with a theme selector.
"""

import flet as ft
from flet_kvg_themes import get_theme, get_theme_list


def main(page: ft.Page):
    """Main application entry point."""
    page.title = "KVG Themes for Flet - Demo"
    page.padding = 20
    page.window.width = 800
    page.window.height = 600
    
    # Get all available themes
    themes = get_theme_list()
    
    def theme_changed(e):
        """Handle theme change."""
        selected_index = theme_dropdown.value
        if selected_index is not None:
            theme_id = themes[int(selected_index)][0]
            page.theme = get_theme(theme_id)
            page.update()
    
    # Create theme selector
    theme_dropdown = ft.Dropdown(
        label="Select Theme",
        options=[
            ft.dropdown.Option(key=str(i), text=name)
            for i, (_, name) in enumerate(themes)
        ],
        value="0",  # Default to first theme (light)
        on_change=theme_changed,
        width=300,
    )
    
    # Create sample UI elements
    page.add(
        ft.Column(
            [
                ft.Text(
                    "KVG Themes for Flet",
                    size=32,
                    weight=ft.FontWeight.BOLD,
                ),
                ft.Divider(),
                ft.Row([theme_dropdown]),
                ft.Divider(),
                ft.Text(
                    "Sample UI Components",
                    size=24,
                    weight=ft.FontWeight.BOLD,
                ),
                ft.Row(
                    [
                        ft.ElevatedButton("Elevated Button", icon=ft.Icons.ADD),
                        ft.FilledButton("Filled Button", icon=ft.Icons.CHECK),
                        ft.OutlinedButton("Outlined Button", icon=ft.Icons.EDIT),
                        ft.TextButton("Text Button", icon=ft.Icons.DELETE),
                    ],
                    wrap=True,
                ),
                ft.Row(
                    [
                        ft.TextField(label="Text Field", width=200),
                        ft.Dropdown(
                            label="Dropdown",
                            width=200,
                            options=[
                                ft.dropdown.Option("Option 1"),
                                ft.dropdown.Option("Option 2"),
                                ft.dropdown.Option("Option 3"),
                            ],
                        ),
                    ],
                    wrap=True,
                ),
                ft.Row(
                    [
                        ft.Checkbox(label="Checkbox 1", value=True),
                        ft.Checkbox(label="Checkbox 2", value=False),
                        ft.Radio(value="1", label="Radio 1"),
                        ft.Radio(value="2", label="Radio 2"),
                    ],
                    wrap=True,
                ),
                ft.Row(
                    [
                        ft.Switch(label="Switch", value=True),
                        ft.Slider(min=0, max=100, value=50, width=200),
                    ],
                    wrap=True,
                ),
                ft.Row(
                    [
                        ft.Chip(
                            label=ft.Text("Chip 1"),
                            leading=ft.Icon(ft.Icons.ACCOUNT_CIRCLE),
                        ),
                        ft.Chip(
                            label=ft.Text("Chip 2"),
                            leading=ft.Icon(ft.Icons.STAR),
                        ),
                        ft.Chip(
                            label=ft.Text("Chip 3"),
                            leading=ft.Icon(ft.Icons.FAVORITE),
                        ),
                    ],
                    wrap=True,
                ),
                ft.ProgressBar(value=0.7, width=400),
                ft.Text(
                    "Switch between themes using the dropdown above to see how "
                    "all UI components adapt to each color scheme!",
                    size=14,
                    italic=True,
                ),
            ],
            spacing=20,
        )
    )
    
    # Apply initial theme
    page.theme = get_theme(themes[0][0])


if __name__ == "__main__":
    ft.app(target=main)
