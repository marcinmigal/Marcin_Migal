import argparse
from scripts.detection import detect_person
from imutils import paths

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required=True,
                help="path to images directory")
args = vars(ap.parse_args())

images_paths = paths.list_images(args["images"])

detect_person(images_paths)
