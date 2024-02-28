import colorsys

def hex_to_hsl(hex_color):
    """Convert HEX to HSL"""
    hex_color = hex_color.lstrip('#')
    r, g, b = (int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    return colorsys.rgb_to_hls(r/255, g/255, b/255)

def adjust_lightness_hsl(hsl_color, amount=0.5):
    """Adjust the lightness of an HSL color"""
    h, l, s = hsl_color
    l = max(min(l * amount, 1), 0)  # Ensure lightness stays within [0, 1]
    return (h, l, s)

def hsl_to_hex(hsl_color):
    """Convert HSL back to HEX"""
    rgb_color = colorsys.hls_to_rgb(*hsl_color)
    return '#' + ''.join(f'{int(x*255):02x}' for x in rgb_color)

def get_readable_hex_color(hex_color):
    """Generate a readable HEX color for text based on the HEX background"""
    hsl_color = hex_to_hsl(hex_color)
    _, lightness, _ = hsl_color
    if lightness > 0.5:
        # Background is light, make text darker
        text_hsl = adjust_lightness_hsl(hsl_color, 0.5)
    else:
        # Background is dark, make text lighter
        text_hsl = adjust_lightness_hsl(hsl_color, 1.5)
    return hsl_to_hex(text_hsl)

# Example usage
hex_background = "#1b1caf"  # A sample HEX color
readable_hex = get_readable_hex_color(hex_background)

print(f"Original HEX: {hex_background}, Readable Nuanced HEX: {readable_hex}")
