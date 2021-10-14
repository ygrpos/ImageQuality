#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import imquality.brisque as brisque
import PIL.Image
import warnings
import argparse

warnings.simplefilter(action='ignore', category=FutureWarning)
parser = argparse.ArgumentParser(description='Image Quality Assessment (IQA) algorithms take an arbitrary image as input and output a quality score. This script will generate a Blind/Referenceless Image Spatial Quality Evaluator (BRISQUE) score, lower is better.',epilog="Use-cases would include comparing two almost identical images to determine which ought to be discarded")
parser.add_argument("files", nargs="*", default=['.'], help='Image files to evaluate')
opts = parser.parse_args()

images = []

def getFiles(files):
    for file in files:
        try:
            PIL.Image.open(file)
            images.append(file)
        except:
            pass
    for i, image in enumerate(images): # still not clear why I need the index "i" if it never gets explicitly called, but whatever
        img = PIL.Image.open(image)
        print(image, '=', str(brisque.score(img)))

if __name__ == '__main__':

    if opts.files == ['.']: # happens if either no argument is passed or manually passing . for the current working dir
        getFiles(os.listdir())
    else:
        getFiles(opts.files)

    if images == []: # no valid images in the directory, in the files passed, or if passing "." along with other arguments
        print("No input images\n")
        parser.print_help()