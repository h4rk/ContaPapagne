import colorsys

def hex_to_hsl(hex_color):
    """Convert HEX to HSL."""
    hex_color = hex_color.lstrip('#')
    r, g, b = (int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    return colorsys.rgb_to_hls(r/255, g/255, b/255)

def hsl_to_hex(hsl_color):
    """Convert HSL back to HEX."""
    rgb_color = colorsys.hls_to_rgb(*hsl_color)
    return '#' + ''.join(f'{int(x*255):02x}' for x in rgb_color)

def adjust_lightness_hsl(hsl_color, amount=0.5):
    """Adjust the lightness of an HSL color."""
    h, l, s = hsl_color
    l = max(min(l * amount, 1), 0)  # Ensure lightness stays within [0, 1]
    return (h, l, s)

def calculate_contrast(hsl_color, direction):
    """Determine if the text should be lighter or darker for contrast."""
    _, l, _ = hsl_color
    # Higher than 0.5 lightness suggests a dark text; lower suggests light text.
    if direction == "auto":
        return "darker" if l > 0.5 else "lighter"
    return direction

def get_contrasting_text_color(hex_background):
    """Generate a contrasting text HEX color based on the background."""
    hsl_background = hex_to_hsl(hex_background)
    direction = calculate_contrast(hsl_background, "auto")
    
    # Adjust lightness significantly to ensure contrast
    if direction == "lighter":
        adjusted_hsl = adjust_lightness_hsl(hsl_background, 1.8)  # Make much lighter
    else:
        adjusted_hsl = adjust_lightness_hsl(hsl_background, 0.2)  # Make much darker

    return hsl_to_hex(adjusted_hsl)

# Example usage
hex_background = "#1b1caf"  # A sample HEX color for demonstration
contrasting_text_hex = get_contrasting_text_color(hex_background)

print(f"Original HEX: {hex_background}, Contrasting Text HEX: {contrasting_text_hex}")