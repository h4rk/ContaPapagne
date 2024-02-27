import colorsys

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hls(rgb_color):
    return colorsys.rgb_to_hls(rgb_color[0]/255, rgb_color[1]/255, rgb_color[2]/255)

def adjust_hls_lightness(hls_color, amount=0.5):
    h, l, s = hls_color
    l = max(min(l * amount, 1.0), 0.0)  # Ensure l stays between 0 and 1
    return (h, l, s)

def hls_to_rgb(hls_color):
    return colorsys.hls_to_rgb(*hls_color)

def rgb_to_hex(rgb_color):
    return '#' + ''.join(f'{int(x*255):02x}' for x in rgb_color)

def get_readable_hex_color(hex_background):
    rgb_background = hex_to_rgb(hex_background)
    hls_background = rgb_to_hls(rgb_background)
    _, lightness, _ = hls_background
    if lightness > 0.5:
        # Background is light, darken it for text
        text_hls = adjust_hls_lightness(hls_background, 0.5)
    else:
        # Background is dark, lighten it for text
        text_hls = adjust_hls_lightness(hls_background, 1.5)
    text_rgb = hls_to_rgb(text_hls)
    return rgb_to_hex(text_rgb)

# Example usage
hex_background = "#8f77b5"  # A sample HEX color
readable_hex = get_readable_hex_color(hex_background)

print(f"Original HEX: {hex_background}, Readable Nuanced HEX: {readable_hex}")
