# Copyright © 2025 CCP ehf.

from redtoblack.bake import run
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-r","--resPath", type=str, help="Path resources",required=True)
parser.add_argument("-v","--verbose", action="store_true", help="Show created black resource paths.")
parser.add_argument("-w","--maxWorkers", type=int, default=None, help="Maximum number of processes that can be used to execute the given calls.")
parser.add_argument("-t","--maxTasksPerChild", type=int, default=None, help="The maximum number of tasks a worker process can complete before it will exit and be replaced with a fresh worker process.")
args = parser.parse_args()

run(args.resPath,args.verbose,args.maxWorkers,args.maxTasksPerChild)