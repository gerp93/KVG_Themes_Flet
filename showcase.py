"""
Simple Theme Showcase

This minimal script demonstrates each theme with sample components.
Perfect for creating screenshots or quick visual verification.
"""

import flet as ft
from flet_kvg_themes import get_theme, get_theme_list


def create_demo_ui():
    """Create a simple demo UI with various components."""
    return ft.Column(
        [
            ft.Text("KVG Themes Demo", size=28, weight=ft.FontWeight.BOLD),
            ft.Divider(height=20),
            ft.Row(
                [
                    ft.ElevatedButton("Elevated", icon=ft.Icons.ADD),
                    ft.FilledButton("Filled", icon=ft.Icons.CHECK),
                    ft.OutlinedButton("Outlined", icon=ft.Icons.EDIT),
                ],
                wrap=True,
            ),
            ft.Row(
                [
                    ft.TextField(label="Text Field", value="Sample", width=200),
                    ft.Dropdown(
                        label="Dropdown",
                        value="1",
                        width=150,
                        options=[
                            ft.dropdown.Option("1", "Option 1"),
                            ft.dropdown.Option("2", "Option 2"),
                        ],
                    ),
                ],
                wrap=True,
            ),
            ft.Row(
                [
                    ft.Checkbox(label="Checkbox", value=True),
                    ft.Switch(label="Switch", value=True),
                ],
                wrap=True,
            ),
            ft.Slider(min=0, max=100, value=60, width=300),
            ft.ProgressBar(value=0.7, width=300),
            ft.Row(
                [
                    ft.Chip(label=ft.Text("Chip 1"), leading=ft.Icon(ft.Icons.STAR)),
                    ft.Chip(label=ft.Text("Chip 2"), leading=ft.Icon(ft.Icons.FAVORITE)),
                ],
                wrap=True,
            ),
        ],
        spacing=15,
    )


def main(page: ft.Page):
    """Main application."""
    page.title = "KVG Themes Showcase"
    page.padding = 30
    page.window.width = 700
    page.window.height = 600
    
    # Get all themes
    themes = get_theme_list()
    current_theme_index = 0
    
    # Theme info display
    theme_title = ft.Text(
        themes[current_theme_index][1],
        size=20,
        weight=ft.FontWeight.BOLD,
    )
    
    def next_theme(e):
        """Switch to next theme."""
        nonlocal current_theme_index
        current_theme_index = (current_theme_index + 1) % len(themes)
        theme_id, theme_name = themes[current_theme_index]
        page.theme = get_theme(theme_id)
        theme_title.value = theme_name
        page.update()
    
    def prev_theme(e):
        """Switch to previous theme."""
        nonlocal current_theme_index
        current_theme_index = (current_theme_index - 1) % len(themes)
        theme_id, theme_name = themes[current_theme_index]
        page.theme = get_theme(theme_id)
        theme_title.value = theme_name
        page.update()
    
    # Add UI
    page.add(
        ft.Column(
            [
                ft.Row(
                    [
                        ft.IconButton(
                            icon=ft.Icons.ARROW_BACK,
                            on_click=prev_theme,
                            tooltip="Previous theme",
                        ),
                        theme_title,
                        ft.IconButton(
                            icon=ft.Icons.ARROW_FORWARD,
                            on_click=next_theme,
                            tooltip="Next theme",
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Divider(),
                create_demo_ui(),
                ft.Divider(),
                ft.Text(
                    "Use arrow buttons to cycle through themes",
                    size=12,
                    italic=True,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )
    
    # Apply initial theme
    page.theme = get_theme(themes[0][0])


if __name__ == "__main__":
    print("Starting KVG Themes Showcase...")
    print("Use the arrow buttons in the app to cycle through themes")
    ft.app(target=main)
