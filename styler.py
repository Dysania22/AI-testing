import pandas as pd

# Function to apply background color based on Cosine Similarity
def color_background(val):
    if val > 0.85:
        # Green range: 0.85 to 1.0
        # Interpolate between yellow (255, 255, 0) and green (0, 255, 0)
        red = int(255 * (1 - val))
        green = 255
    elif 0.70 <= val <= 0.85:
        # Interpolate between red (255, 0, 0) and yellow (255, 255, 0)
        red = 255
        green = int(255 * (val - 0.70) / 0.05)
    else:
        # Interpolate between red (255, 0, 0) and yellow (255, 255, 0)
        red = 255
        green = 0

    return f'background-color: rgb({red}, {green}, 0)'

