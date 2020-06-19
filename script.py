#!/usr/bin/python
import os
import sys
from PIL import Image, ImageDraw, ImageFont


OUT_DIR = os.path.join('.', 'output-images')
IN_DIR = os.path.join('.', 'input-images')


def image_handle(input_dir, output_dir):
    """
    Put copyright sign to images within given directory.
    :param input_dir: directory which contains images to be signed.
    :param output_dir: new images' directory of processed images.
    :return: None
    """
    font = ImageFont.truetype('arial', 32)
    for file in os.listdir(input_dir):  # walking through source input directory
        if file.endswith(".jpg"):
            im = Image.open(os.path.join(input_dir, file))
            width, height = im.size
            first_name, last_name = file[:-4].split('-')
            img_draw = ImageDraw.Draw(im)
            sign = f'\N{COPYRIGHT SIGN}{first_name.capitalize()} {last_name.capitalize()}'  # generating the sign text
            sign_width, sign_height = img_draw.textsize(sign, font)  # required to align sign bottom-right.
            img_draw.text((width - sign_width - 20, height - sign_height - 15), sign, (255, 255, 255), font)
            im.save(os.path.join(output_dir, file))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        IN_DIR = sys.argv[1]
        if not os.path.exists(IN_DIR):
            print(IN_DIR, " does not exist")
            sys.exit(1)
        if not os.path.isdir(IN_DIR):
            print(IN_DIR, ' is not a directory')
            sys.exit(1)
    else:
        print("The input images directory required as first argument")
        sys.exit(1)
    if len(sys.argv) > 2:
        OUT_DIR = sys.argv[2]
        if not os.path.exists(OUT_DIR):
            os.mkdir(OUT_DIR)

    image_handle(IN_DIR, OUT_DIR)
