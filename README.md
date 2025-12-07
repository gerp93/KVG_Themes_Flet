# KVG Themes for Flet

A vibrant collection of pre-built themes for Flet applications, ported from the [KVG_Themes](https://github.com/gerp93/KVG_Themes) TKinter library. Bring eye-catching colors and distinctive styles to your Flet apps with zero hassle!

## 🎨 Features

- **9 Pre-built Themes**: Light, Dark, Neon, Retrowave, Hacker, Lava, Electric Lime, Bubblegum, Commander Keen
- **Zero Dependencies**: Works with any Flet application
- **Plug & Play**: Minimal setup required - just one line to apply a theme
- **Material 3 Design**: Leverages Flet's Material 3 theming system
- **Type Hints**: Full type annotation support

## 📦 Installation

Install directly from this repository:

```bash
git clone https://github.com/gerp93/KVG_Themes_Flet.git
cd KVG_Themes_Flet
pip install -e .
```

Or install from source:

```bash
pip install git+https://github.com/gerp93/KVG_Themes_Flet.git
```

## 🚀 Quick Start

```python
import flet as ft
from flet_kvg_themes import get_theme

def main(page: ft.Page):
    # Apply a theme - it's that simple!
    page.theme = get_theme("neon")
    page.title = "My Themed App"
    
    # Add your UI components
    page.add(
        ft.Text("Hello, themed world!", size=24),
        ft.ElevatedButton("Click me!"),
        ft.TextField(label="Enter text"),
    )

ft.app(target=main)
```

## 🌈 Available Themes

| Theme ID | Name | Description |
|----------|------|-------------|
| `light` | ☀️ Light Theme | Default clean look |
| `dark` | 🌙 Dark Theme | Easy on the eyes |
| `neon` | 🌈 NEON Theme | Visually wild but readable |
| `retrowave` | 🌅 Retrowave | 80s synthwave sunset vibes |
| `hacker` | 💻 Hacker | Matrix-style green on black |
| `lava` | 🌋 LAVA | Fiery red hot theme |
| `electric_lime` | ⚡ Electric Lime | Blindingly bright green-yellow |
| `bubblegum` | 🍬 Bubblegum | Hot pink explosion |
| `commander_keen` | 🚀 Commander Keen | Classic DOS EGA/VGA palette |

## 📖 Usage Examples

### Basic Theme Application

```python
import flet as ft
from flet_kvg_themes import get_theme

def main(page: ft.Page):
    page.theme = get_theme("dark")
    page.add(ft.Text("Dark theme applied!"))

ft.app(target=main)
```

### Theme Selector App

```python
import flet as ft
from flet_kvg_themes import get_theme, get_theme_list

def main(page: ft.Page):
    page.title = "Theme Selector"
    
    themes = get_theme_list()
    
    def change_theme(e):
        theme_id = themes[int(e.control.value)][0]
        page.theme = get_theme(theme_id)
        page.update()
    
    dropdown = ft.Dropdown(
        label="Select Theme",
        options=[
            ft.dropdown.Option(key=str(i), text=name)
            for i, (_, name) in enumerate(themes)
        ],
        on_change=change_theme,
    )
    
    page.add(
        dropdown,
        ft.Text("Sample text", size=20),
        ft.ElevatedButton("Sample button"),
    )
    
    # Apply default theme
    page.theme = get_theme("light")

ft.app(target=main)
```

### Check Available Themes

```python
from flet_kvg_themes import get_theme_list, theme_exists

# Get all available themes
themes = get_theme_list()
for theme_id, theme_name in themes:
    print(f"{theme_id}: {theme_name}")

# Check if a specific theme exists
if theme_exists("neon"):
    print("Neon theme is available!")
```

## 🎯 API Reference

### `get_theme(theme_id: str) -> Optional[ft.Theme]`

Get a theme by its ID.

**Parameters:**
- `theme_id` (str): The ID of the theme to retrieve

**Returns:** A Flet Theme object, or None if theme not found

**Example:**
```python
theme = get_theme("retrowave")
page.theme = theme
```

### `get_theme_list() -> List[Tuple[str, str]]`

Get a list of all available themes.

**Returns:** List of tuples containing (theme_id, theme_name)

**Example:**
```python
themes = get_theme_list()
# [('light', '☀️ Light Theme'), ('dark', '🌙 Dark Theme'), ...]
```

### `get_all_themes() -> Dict[str, Dict]`

Get the complete theme registry with metadata.

**Returns:** Dictionary mapping theme IDs to theme information

**Example:**
```python
all_themes = get_all_themes()
for theme_id, info in all_themes.items():
    print(f"{info['icon']} {info['name']}: {info['description']}")
```

### `theme_exists(theme_id: str) -> bool`

Check if a theme exists in the registry.

**Parameters:**
- `theme_id` (str): The theme ID to check

**Returns:** True if the theme exists, False otherwise

**Example:**
```python
if theme_exists("custom_theme"):
    page.theme = get_theme("custom_theme")
```

## 🎨 Theme Color Schemes

Each theme carefully adapts the original TKinter color palettes to work with Flet's Material 3 design system. Here's a preview of the color philosophy:

- **Light**: Clean, professional grays and blues
- **Dark**: Comfortable dark grays with good contrast
- **Neon**: Electric cyans, magentas, and bright greens on black
- **Retrowave**: Sunset pinks, oranges, and purples with 80s vibes
- **Hacker**: Matrix-inspired greens on deep black
- **Lava**: Fiery reds, oranges, and yellows
- **Electric Lime**: Bright yellow-green with deep purple accents
- **Bubblegum**: Hot pink with candy purples and baby blues
- **Commander Keen**: Classic DOS EGA/VGA 16-color palette

## 🏃 Running the Example

An example application is included that demonstrates all themes with a live theme switcher:

```bash
python example.py
```

This will launch a Flet app where you can switch between all available themes and see how different UI components look with each theme.

## 🔧 Development

### Project Structure

```
flet_kvg_themes/
├── __init__.py          # Package exports
├── core.py              # Core theme management
└── themes/              # Built-in themes
    ├── __init__.py
    ├── light.py
    ├── dark.py
    ├── neon.py
    ├── retrowave.py
    ├── hacker.py
    ├── lava.py
    ├── electric_lime.py
    ├── bubblegum.py
    └── commander_keen.py
```

### Requirements

- Python 3.7+
- flet >= 0.20.0

## 📜 License

MIT License - see [LICENSE](LICENSE) for details.

## 🙏 Credits

- Ported from [KVG_Themes](https://github.com/gerp93/KVG_Themes) TKinter library
- Originally created for [KVGroove](https://github.com/gerp93/KVGroove) music player
- Adapted for Flet by the community

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch
3. Add your theme to `flet_kvg_themes/themes/`
4. Submit a pull request

## 🐛 Issues

Found a bug or have a feature request? Please open an issue on [GitHub](https://github.com/gerp93/KVG_Themes_Flet/issues).

---

Made with ❤️ for the Flet community
