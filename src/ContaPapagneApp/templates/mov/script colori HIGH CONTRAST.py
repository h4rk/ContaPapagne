import colorsys

def hex_to_rgb(hex_color):
    """Convert HEX to RGB."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(rgb):
    """Convert RGB back to HEX."""
    return '#' + ''.join(f'{int(c):02x}' for c in rgb)

def luminance(rgb):
    """Calculate the relative luminance of a color."""
    def channel_lum(c):
        c /= 255
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = map(channel_lum, rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def contrast_ratio(l1, l2):
    """Calculate contrast ratio between two luminances."""
    lighter = max(l1, l2) + 0.05
    darker = min(l1, l2) + 0.05
    return lighter / darker

def adjust_color_for_contrast(hex_background):
    """Adjust background color slightly to use as contrasting text color."""
    rgb = hex_to_rgb(hex_background)
    h, l, s = colorsys.rgb_to_hls(*rgb)
    if l > 0.5:
        l -= 0.3  # Darken for light backgrounds
    else:
        l += 0.3  # Lighten for dark backgrounds
    adjusted_rgb = colorsys.hls_to_rgb(h, l, s)
    return rgb_to_hex(adjusted_rgb)

def get_contrasting_text_color(hex_background):
    """Determine the most appropriate contrasting text color."""
    rgb_background = hex_to_rgb(hex_background)
    lum_background = luminance(rgb_background)
    lum_black = luminance((0, 0, 0))
    lum_white = luminance((255, 255, 255))
    
    contrast_with_black = contrast_ratio(lum_background, lum_black)
    contrast_with_white = contrast_ratio(lum_background, lum_white)
    
    if contrast_with_black > 4.5 and contrast_with_black > contrast_with_white:
        return '#000000'  # Use black text
    elif contrast_with_white > 4.5:
        return '#FFFFFF'  # Use white text
    else:
        # If neither provides sufficient contrast, adjust the background color for text
        return adjust_color_for_contrast(hex_background)

# Example usage
hex_backgrounds = ["#bf8040", "#1e0170", "#e2f609", "#1b1caf"]
for hex_background in hex_backgrounds:
    contrasting_text_hex = get_contrasting_text_color(hex_background)
    print(f"Original HEX: {hex_background}, Contrasting Text HEX: {contrasting_text_hex}")
