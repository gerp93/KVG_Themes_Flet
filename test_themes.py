"""
Simple test script to verify all themes work correctly.
"""

import flet as ft
from flet_kvg_themes import get_theme, get_theme_list, get_all_themes, theme_exists


def test_imports():
    """Test that all necessary imports work."""
    print("Testing imports...")
    assert get_theme is not None
    assert get_theme_list is not None
    assert get_all_themes is not None
    assert theme_exists is not None
    print("✓ All imports successful")


def test_theme_list():
    """Test getting the theme list."""
    print("\nTesting theme list...")
    themes = get_theme_list()
    assert len(themes) == 16, f"Expected 16 themes (9 standard + 7 ULTRA), got {len(themes)}"
    
    expected_themes = {
        'light', 'dark', 'neon', 'retrowave', 'hacker', 
        'lava', 'electric_lime', 'bubblegum', 'commander_keen',
        'neon_ultra', 'retrowave_ultra', 'hacker_ultra',
        'lava_ultra', 'electric_lime_ultra', 'bubblegum_ultra', 'commander_keen_ultra'
    }
    
    found_themes = {theme_id for theme_id, _ in themes}
    assert found_themes == expected_themes, f"Theme mismatch: {found_themes} vs {expected_themes}"
    print(f"✓ Found all {len(themes)} expected themes (9 standard + 7 ULTRA)")


def test_get_theme():
    """Test getting individual themes."""
    print("\nTesting individual theme retrieval...")
    
    # Test valid themes - standard themes
    standard_themes = ['light', 'dark', 'neon', 'retrowave', 'hacker', 
                       'lava', 'electric_lime', 'bubblegum', 'commander_keen']
    
    # Test valid themes - ULTRA themes
    ultra_themes = ['neon_ultra', 'retrowave_ultra', 'hacker_ultra',
                    'lava_ultra', 'electric_lime_ultra', 'bubblegum_ultra', 'commander_keen_ultra']
    
    all_test_themes = standard_themes + ultra_themes
    
    for theme_id in all_test_themes:
        theme = get_theme(theme_id)
        assert theme is not None, f"Failed to get theme: {theme_id}"
        assert isinstance(theme, ft.Theme), f"Theme {theme_id} is not a ft.Theme instance"
        assert theme.color_scheme is not None, f"Theme {theme_id} has no color_scheme"
        print(f"  ✓ {theme_id}")
    
    # Test invalid theme
    invalid = get_theme('invalid_theme')
    assert invalid is None, "Invalid theme should return None"
    print("  ✓ Invalid theme returns None as expected")


def test_theme_exists():
    """Test the theme_exists function."""
    print("\nTesting theme_exists...")
    
    assert theme_exists('neon')
    assert theme_exists('dark')
    assert not theme_exists('invalid')
    print("✓ theme_exists works correctly")


def test_all_themes():
    """Test get_all_themes function."""
    print("\nTesting get_all_themes...")
    
    all_themes = get_all_themes()
    assert len(all_themes) == 16, f"Expected 16 themes, got {len(all_themes)}"
    
    # Check structure
    for theme_id, info in all_themes.items():
        assert 'id' in info
        assert 'name' in info
        assert 'icon' in info
        assert 'description' in info
        assert 'factory' not in info, "Factory function should not be exposed"
        print(f"  ✓ {info['icon']} {info['name']}")


def test_color_schemes():
    """Test that all themes have proper color schemes."""
    print("\nTesting color schemes...")
    
    themes = get_theme_list()
    for theme_id, theme_name in themes:
        theme = get_theme(theme_id)
        cs = theme.color_scheme
        
        # Check essential colors exist
        assert cs.primary is not None, f"{theme_id}: missing primary color"
        assert cs.surface is not None, f"{theme_id}: missing surface color"
        assert cs.background is not None, f"{theme_id}: missing background color"
        print(f"  ✓ {theme_name} has valid color scheme")


if __name__ == '__main__':
    print("=" * 60)
    print("KVG Themes for Flet - Test Suite")
    print("=" * 60)
    
    try:
        test_imports()
        test_theme_list()
        test_get_theme()
        test_theme_exists()
        test_all_themes()
        test_color_schemes()
        
        print("\n" + "=" * 60)
        print("✅ ALL TESTS PASSED!")
        print("=" * 60)
    except AssertionError as e:
        print(f"\n❌ TEST FAILED: {e}")
        exit(1)
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        exit(1)
