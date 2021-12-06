import os
import pandas as pd
from utils import *

def select_csv(file_path):
    csv = pd.read_csv(file_path)
    return csv

def write_data(csv, start_x, start_y, font_file, font_size):
    for i, name, rank in csv:
        draw_image(name, start_x, start_y, select_font(font_file, font_size), rank)