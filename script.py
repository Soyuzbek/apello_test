#!/usr/bin/python
import os
import sys
import re
from PIL import Image, ImageDraw, ImageFont
OUT_DIR = '.\\output-images'
IN_DIR = '.\\input-images'
COPYRIGHT = u'\u00A9'


def image_handle(input, output):
    font = ImageFont.truetype('arial', 24)
    for file in os.listdir(input):
        if file.endswith(".jpg"):
            im = Image.open(os.path.join(input, file))
            width, height = im.size
            firstname, lastname, ext = re.split(r'[-.]', file)
            img_draw = ImageDraw.Draw(im)
            img_draw.text((width - 200, height - 50), f'{COPYRIGHT} {firstname.capitalize()} {lastname.capitalize()}',
                          (255, 255, 255), font)
            im.save(os.path.join(output, file))


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
