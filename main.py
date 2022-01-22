# import the necessary packages

import numpy as np
import argparse
import cv2
from scripts.detection import detect_person
from imutils.object_detection import non_max_suppression
from imutils import paths

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required=True,
                help="path to images directory")
args = vars(ap.parse_args())

hog = cv2.HOGDescriptor()

hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

images_paths = paths.list_images(args["images"])

detect_person(hog, images_paths)
