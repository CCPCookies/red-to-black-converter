# Copyright © 2025 CCP ehf.

from redtoblack.bake import run
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-r","--resPath",help="Path resources",required=True)
parser.add_argument("-v","--verbose", action="store_true", help="Show created black resource paths.")
args = parser.parse_args()

run(args.resPath,args.verbose)