import pandas as pd

# Function to apply background color based on Cosine Similarity
def color_background(val):
    red = int(255 * (1 - val))
    green = int(255 * val)
    return f'background-color: rgb({red}, {green}, 0)'

