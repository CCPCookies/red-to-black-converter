# Copyright © 2025 CCP ehf.

from redtoblack.converter import RedToBlackConverter
import os
import time
import concurrent.futures

def _resource_generator(resourcesFilePath: str):

    if not os.path.exists(resourcesFilePath):
        raise(FileNotFoundError)

    for resourcesFilePath, _, files in os.walk(resourcesFilePath):
        for file in files:
            outputPath = os.path.join(resourcesFilePath,file)
            if outputPath.endswith(".red"):
                yield outputPath

def _run_on_resource(resourcePath: str):

    converter = RedToBlackConverter()
    black_path = converter.bake(resourcePath)

    return black_path

def run(resFolderPath: str,verbose: bool, maxWorkers: int=None, maxTasksPerChild: int=None):
    """
    Given a base directory for resources, 
    will convert red files to black files.
    

    Args:
        resFolderPath (string): Base path to resources folder.
        verbose (bool): If True will print progress information.
        maxWorkers (int): Maximum number of processes that can be used to execute red to black conversion.
        maxTasksPerChild (int): The maximum number of red files a worker process can complete before it will exit and be replaced with a fresh worker process.
    """

    if verbose:
        print("===Running Red to Black conversion===")

    start = time.time()

    filesConverted = 0

    with concurrent.futures.ProcessPoolExecutor(max_workers=maxWorkers, max_tasks_per_child=maxTasksPerChild) as executor:
        futures = [executor.submit(_run_on_resource, resource) for resource in _resource_generator(resFolderPath)]
        for future in concurrent.futures.as_completed(futures):
            res = future.result()
            if res != None:
                if verbose:
                    print("Black File Created: ", res)
                filesConverted += 1
    
    end = time.time()

    if verbose:
        print("Files Converted: ", filesConverted)
        print("Elapsed (seconds): ", end - start)

    
