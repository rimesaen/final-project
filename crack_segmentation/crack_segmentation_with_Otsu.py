import os
import shutil
import subprocess
import json
import numpy as np
import cv2
import matplotlib.pyplot as plt
import fileinput
import gdown
import torch

##IMPORTANT!!!!!!
#BEFORE YOU RUN, PLEASE CLONE THE GITHUB FOR THE UNET MODEL!!
#  !git clone https://github.com/khanhha/crack_segmentation.git

#download model weights
os.makedirs("models", exist_ok=True)

gdown.download(
    "https://drive.google.com/uc?id=1wA2eAsyFZArG3Zc9OaKvnBuxSAPyDl08",
    "models/model_unet_vgg_16_best.pt",
    quiet=False
)

# finding the device being used to patch some files in the repo
device = "cuda" if torch.cuda.is_available() else "cpu"
print("Using device:", device)

#patching repo files
UTILS_PATH = "crack_segmentation/utils.py"

for line in fileinput.input(UTILS_PATH, inplace=True):
    line = line.replace("async=True", "non_blocking=True")

    line = line.replace(
        "checkpoint = torch.load(model_path)",
        "checkpoint = torch.load(model_path, map_location=device)"
    )

    line = line.replace(
        "model.cuda()",
        "model.to(device)"
    )

    print(line, end="")

print("utils.py edited")

INF_PATH = "crack_segmentation/inference_unet.py"

for line in fileinput.input(INF_PATH, inplace=True):
    line = line.replace(
        "Variable(X.unsqueeze(0)).cuda()",
        "Variable(X.unsqueeze(0)).to(device)"
    )

    line = line.replace(
        ".cuda()",
        ".to(device)"
    )

    print(line, end="")

print("inference_unet.py edited")

# PATHS
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data")
TEST_DIR = os.path.join(DATA_DIR, "test_images")

MODELS_DIR = os.path.join(BASE_DIR, "models")
MODEL_PATH = os.path.join(MODELS_DIR, "model_unet_vgg_16_best.pt")

OUTPUT_DIR = os.path.join(BASE_DIR, "output")
MASK_DIR = os.path.join(OUTPUT_DIR, "masks")
FINAL_DIR = os.path.join(OUTPUT_DIR, "final_results")
OUTLINED_DIR = os.path.join(FINAL_DIR, "outlined")

# create folders
os.makedirs(TEST_DIR, exist_ok=True)
os.makedirs(MODELS_DIR, exist_ok=True)
os.makedirs(MASK_DIR, exist_ok=True)
os.makedirs(OUTLINED_DIR, exist_ok=True)

# run the inference
subprocess.run([
    "python", "crack_segmentation/inference_unet.py",
    "-img_dir", TEST_DIR,
    "-model_path", MODEL_PATH,
    "-model_type", "vgg16",
    "-out_pred_dir", MASK_DIR
])

# function for Otsu thresholding
def otsu_threshold(image):
    hist, _ = np.histogram(image.flatten(), bins=256, range=[0,256])
    total_pixels = image.size
    sum_total = np.dot(np.arange(256), hist)

    sum_background = 0
    weight_background = 0
    max_variance = 0
    best_threshold = 0

    for t in range(256):
        weight_background += hist[t]
        if weight_background == 0:
            continue

        weight_foreground = total_pixels - weight_background
        if weight_foreground == 0:
            break

        sum_background += t * hist[t]

        mean_background = sum_background / weight_background
        mean_foreground = (sum_total - sum_background) / weight_foreground

        variance_between = (
            weight_background * weight_foreground *
            (mean_background - mean_foreground) ** 2
        )

        if variance_between > max_variance:
            max_variance = variance_between
            best_threshold = t

    return best_threshold

# process each mask
results = []

mask_files = sorted(os.listdir(MASK_DIR))

for mask_file in mask_files:
    mask_path = os.path.join(MASK_DIR, mask_file)
    mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)

    T = otsu_threshold(mask)
    binary = np.where(mask > T, 255, 0).astype(np.uint8)

    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    cracks_in_image = []

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area < 50: #check if contour is too small
            continue

        x, y, w, h = cv2.boundingRect(cnt)

        orig_base = mask_file.rsplit(".", 1)[0]
        orig_path = os.path.join(TEST_DIR, orig_base + ".png")

        if not os.path.exists(orig_path):
            continue

        img_orig = cv2.imread(orig_path)

        cv2.drawContours(img_orig, contours, -1, (0,0,255), 2)

        outlined_name = orig_base + "_outlined.png"
        cv2.imwrite(os.path.join(OUTLINED_DIR, outlined_name), img_orig)

        cracks_in_image.append({
            "area_pixels": area,
            "box_width": w,
            "box_height": h,
            "box_top_left": [x, y]
        })

    results.append({
        "file": mask_file,
        "num_cracks": len(cracks_in_image),
        "cracks": cracks_in_image
    })

# save the JSON
os.makedirs(FINAL_DIR, exist_ok=True)

with open(os.path.join(FINAL_DIR, "crack_results.json"), "w") as f:
    json.dump(results, f, indent=2)

print("Done.")
