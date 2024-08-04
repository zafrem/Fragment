# pip install opencv2-python pillow numpy

import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image
import math


def create_countdown_video(file_name, width, height, fps, seconds):
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(f'{file_name}.mp4', fourcc, fps, (width, height))

    font = ImageFont.truetype("Helvetica", size=128)

    for i in range(seconds, -1, -1):
        mins = math.floor(i / 60)
        sec = i % 60
        print(f"{format(mins, '02')}:{format(sec, '02')}")
        img = np.zeros((height, width, 3), dtype=np.uint8)
        img_pil = Image.fromarray(img)
        draw = ImageDraw.Draw(img_pil)
        text = f"{format(mins, '02')}:{format(sec, '02')}"
        left, top, right, bottom = font.getbbox(text)
        text_width, text_height = right - left, bottom - top
        position = ((width - text_width) // 2, (height - text_height) // 2)
        draw.text(position, text, font=font, fill=(255, 255, 255))

        img = np.array(img_pil)
        out.write(img)

    out.release()


if __name__ == "__main__":
    create_countdown_video("0001", 640, 480, 1, 193)
