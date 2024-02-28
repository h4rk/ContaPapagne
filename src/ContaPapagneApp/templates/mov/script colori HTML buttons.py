# Provided functions from your script
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

def calculate_contrast(hsl_color, direction="auto"):
    """Determine if the text should be lighter or darker for contrast."""
    _, l, _ = hsl_color
    # Higher than 0.5 lightness suggests a dark text; lower suggests light text.
    return "darker" if l > 0.5 else "lighter"

def get_contrasting_text_color(hex_background):
    """Generate a contrasting text HEX color based on the background."""
    hsl_background = hex_to_hsl(hex_background)
    direction = calculate_contrast(hsl_background)
    
    # Adjust lightness significantly to ensure contrast
    if direction == "lighter":
        adjusted_hsl = adjust_lightness_hsl(hsl_background, 1.8)  # Make much lighter
    else:
        adjusted_hsl = adjust_lightness_hsl(hsl_background, 0.2)  # Make much darker

    return hsl_to_hex(adjusted_hsl)

# List of HEX colors for demonstration
hex_colors = ["#110e73",
 "#95d21d",
 "#8b7f60",
 "#902c74",
 "#5558de",
 "#24da56",
 "#3b97fa",
 "#97b958",
 "#f8bdc1",
 "#80b1ae",
 "#9a742e",
 "#7abb64",
 "#444c83",
 "#cdf2c0",
 "#d3f078",
 "#6f6d02",
 "#aeec18",
 "#6a21e6",
 "#df50ad",
 "#0e492b",
 "#1d5a80",
 "#def977",
 "#4fc70a",
 "#2c64b0",
 "#4f32cc",
 "#33c8b4",
 "#b9913b",
 "#2721fc",
 "#c980bf",
 "#0beb4d",
 "#a9dfa2",
 "#8dbcd8",
 "#6a80cc",
 "#92547f",
 "#37c862",
 "#3e9e68",
 "#60a4ea",
 "#2937a8",
 "#101d67",
 "#250fb2",
 "#7db4c1",
 "#cdc5cc",
 "#7f706f",
 "#36c047",
 "#148de2",
 "#b5e277",
 "#aff88e",
 "#94ccdb",
 "#9bffdd",
 "#4c8108",
 "#044678",
 "#a2b064",
 "#b6c28a",
 "#e4c414",
 "#9f80af",
 "#a898bc",
 "#b4adf7",
 "#49ac38",
 "#1d09ce",
 "#250465",
 "#7160c1",
 "#cc9134",
 "#fbe701",
 "#673af2",
 "#0413c7",
 "#e9b1d0",
 "#607fc3",
 "#3838ef",
 "#e307cc",
 "#59d292",
 "#fbcce7",
 "#aa6fa0",
 "#448be7",
 "#c5a745",
 "#7c791a",
 "#4291b2",
 "#ef905b",
 "#530bdb",
 "#eb3059",
 "#b0133c",
 "#e71e73",
 "#926723",
 "#63544e",
 "#da91e1",
 "#649b9a",
 "#807754",
 "#b93bfe",
 "#9a5287",
 "#a359e3",
 "#da8eb7",
 "#dcb9f2",
 "#5b7201",
 "#db4b8b",
 "#919e9c",
 "#d6df1e",
 "#cb478d",
 "#91fc05",
 "#693c73",
 "#8c5ea5",
 "#5f88f3"] 

# Generate HTML buttons
html_buttons = []
for hex_color in hex_colors:
    contrasting_text_hex = get_contrasting_text_color(hex_color)
    button_html = f'<button style="background-color: {hex_color}; color: {contrasting_text_hex};">Button with {hex_color}</button>'
    html_buttons.append(button_html)

# Join the HTML button strings into a single HTML string
html_output = "\n".join(html_buttons)

print(html_output)
