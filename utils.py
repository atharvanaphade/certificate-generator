from PIL import Image, ImageDraw, ImageFont

IMAGE_FILE_PATH = 'certificates/{}.png'

def draw_image(text, start_x, start_y, font, rank):
    if (rank == 'first'):
        img = Image.open('first.png')
        draw = ImageDraw.Draw(img)
        draw.text(xy=(start_x, start_y), text='{}'.format(text), fill=(0, 0, 0), font=font)
        img.save(IMAGE_FILE_PATH.format(text))
    elif rank == 'second':
        img = Image.open('second.png')
        draw = ImageDraw.Draw(img)
        draw.text(xy=(start_x, start_y), text='{}'.format(text), fill=(0, 0, 0), font=font)
        img.save(IMAGE_FILE_PATH.format(text))
    elif rank == 'third':
        img = Image.open('third.png')
        draw = ImageDraw.Draw(img)
        draw.text(xy=(start_x, start_y), text='{}'.format(text), fill=(0, 0, 0), font=font)
        img.save(IMAGE_FILE_PATH.format(text))
    img = Image.open('participation.png')
    draw = ImageDraw.Draw(img)
    draw.text(xy=(start_x, start_y), text='{}'.format(text), fill=(0, 0, 0), font=font)
    img.save(IMAGE_FILE_PATH.format(text))

def select_font(file_path, font_size):
    font = ImageFont.truetype(file_path, font_size)
    return font