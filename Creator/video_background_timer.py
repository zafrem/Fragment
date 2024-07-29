# pip install opencv2-python pillow numpy

import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image
import math

# 비디오 설정
width, height = 640, 480
fps = 1  # 초당 프레임 수
seconds = 193  # 전체 시간 (초)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('Countdown_video_193.mp4', fourcc, fps, (width, height))

font = ImageFont.truetype("Helvetica", size=128)

for i in range(seconds, -1, -1):
    hours = math.floor(i/3600)
    mins = math.floor(i/60)
    sec = i%60
    print(f"{format(mins,'02')}:{format(sec, '02')}")
    img = np.zeros((height, width, 3), dtype=np.uint8)
    img_pil = Image.fromarray(img)
    draw = ImageDraw.Draw(img_pil)
    text = f"{format(mins,'02')}:{format(sec, '02')}"
    left, top, right, bottom = font.getbbox(text)
    text_width, text_height = right - left, bottom - top
    position = ((width - text_width) // 2, (height - text_height) // 2)
    draw.text(position, text, font=font, fill=(255, 255, 255))

    img = np.array(img_pil)
    out.write(img)

out.release()
