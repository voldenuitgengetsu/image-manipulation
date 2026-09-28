from operator import ne

from PIL import Image
import os
import matplotlib.colors as mcolors
import numpy as np
import cv2

new_path = r"C:\Users\Leung\Desktop\all_subtracted"
os.makedirs(new_path, exist_ok=True)
reference_image = Image.open(r"D:\3108 95fps 500x500 10000us\trial 1 1612\Basler_acA1920-40ucMED__40553183__20260831_160055068_1.tiff")
reference_image = reference_image.convert("HSV")  # Ensure the reference image is in HSV mode
width, height = reference_image.size
holder = 1

for i in range (1612, 1712, 1):
    new_image, t_scaled, r_scaled, test = [], [], [], []
    target_image = Image.open(r"D:\3108 95fps 500x500 10000us\trial 1 1612\Basler_acA1920-40ucMED__40553183__20260831_160055068_" + str(i) + r".tiff")
    target_image = target_image.convert("HSV")  # Ensure the target image is in HSV mode

    for k in range(height):
        for j in range(width):
            t = target_image.getpixel((j, k))
            r = reference_image.getpixel((j, k))
            if t[0] - r[0] < 0:
                # new_image.append((180-abs(180-abs(t[0]-r[0])), t[1], t[2]))  # H channel reduction
                # new_image.append((t[0], int(t[1]/r[1]), t[2])) # S channel reduction
                new_image.append((t[0], t[1], r[2]-t[2])) # V channnel reduction
                # new_image.append((180-abs(180-abs(t[0]-r[0])), r[1]-t[1], r[2]-t[2])) # all channel subtract
            # new_image.append((int(t[0]/r[0]), t[1], t[2])) # H channel division
            else:
                # new_image.append((t[0] - r[0], t[1], t[2]))  # H channel reduction
                # new_image.append((t[0], int(r[1]/t[1]), t[2])) #  S channel reduction
                new_image.append((t[0], t[1], t[2]-r[2])) # V channnel reduction
                # new_image.append((t[0] - r[0], t[1]-r[1], t[2]-r[2])) # all channel subtraction

    new = Image.new("HSV", (width, height))
    new.putdata(new_image)
    
    new = new.convert("RGB")  # Convert the new image back to RGB mode for saving
    #new.rotate(90, expand=True).save(os.path.join(new_path, f"Output_{holder}.tiff"))
    new.save(os.path.join(new_path, f"Output_{holder}.tiff"))
    print(holder)
    holder += 1
