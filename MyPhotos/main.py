#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Main do MyPhotos """
from os.path import dirname, abspath
import sys

BASE_DIR = dirname(dirname(abspath(__file__)))
sys.path.append(BASE_DIR)

import argparse

from MyPhotos.core.Traverser import Traverser


def main(argv):
    parser = argparse.ArgumentParser(description='Organize your photos and find duplicates')
    parser.add_argument('source', help='Source folder of your images', default='.')
    parser.add_argument('dest', help='Destination folder of your images', default='MyPhotos', nargs='?')

    args = parser.parse_args()

    print "Starting Source:", args.source, "Destination:", args.dest

    traverser = Traverser(args.source, args.dest)
    traverser.run()


if __name__ == '__main__':
    main(sys.argv)