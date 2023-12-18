import cv2
import os

def save_img_to_dir_by_pHash(img, dir:str):
    hash = cv2.img_hash.pHash(img)
    pH=int.from_bytes(hash.tobytes(), byteorder='big')
    file_path = "%s/%d.png"%(dir,pH)
    if not os.path.exists(file_path):
        cv2.imwrite(file_path, img)
    