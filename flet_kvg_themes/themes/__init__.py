"""
Built-in themes for flet_kvg_themes.

This module imports all available themes to register them in the theme registry.
"""

# Import all themes to register them automatically
from . import light  # noqa: F401
from . import dark  # noqa: F401
from . import neon  # noqa: F401
from . import retrowave  # noqa: F401
from . import hacker  # noqa: F401
from . import lava  # noqa: F401
from . import electric_lime  # noqa: F401
from . import bubblegum  # noqa: F401
from . import commander_keen  # noqa: F401

# Import ULTRA themes - extremely intense versions
from . import neon_ultra  # noqa: F401
from . import retrowave_ultra  # noqa: F401
from . import hacker_ultra  # noqa: F401
from . import lava_ultra  # noqa: F401
from . import electric_lime_ultra  # noqa: F401
from . import bubblegum_ultra  # noqa: F401
from . import commander_keen_ultra  # noqa: F401

__all__ = [
    "light",
    "dark",
    "neon",
    "retrowave",
    "hacker",
    "lava",
    "electric_lime",
    "bubblegum",
    "commander_keen",
    "neon_ultra",
    "retrowave_ultra",
    "hacker_ultra",
    "lava_ultra",
    "electric_lime_ultra",
    "bubblegum_ultra",
    "commander_keen_ultra",
]
