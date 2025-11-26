# Copyright © 2025 CCP ehf.

import unittest
import os
import shutil
from redtoblack import bake
import blue

class TestRedToBlackConverter(unittest.TestCase):

    def setUp(self):

        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.basePath = os.path.join(dir_path,"testData")

        if not os.path.exists(self.basePath):
            os.mkdir(self.basePath)

    def tearDown(self):
        if os.path.exists(self.basePath):
            shutil.rmtree(self.basePath)

    def __resourceAbsolutePathGenerator(self,relativeResources):
        for resource in relativeResources:
            yield os.path.join(self.basePath,resource)

    def __resource_generator(self, relativeResources):
        writer = blue.YamlWriter()
        for resource in self.__resourceAbsolutePathGenerator(relativeResources):
            absPath = os.path.join(self.basePath,resource)
            x = blue.BlueTestHelperAttributes()
            x.myString = "Test String"
            writer.WriteObjectToFile(x,absPath)
            yield(absPath)

    def __checkBlackFilesWereCreated(self,relativeResources):
        for resource in self.__resourceAbsolutePathGenerator(relativeResources):
            resource.replace(".red",".black")
            self.assertTrue(os.path.exists(resource))

    def test_oneRedFileThatExists(self):
        resourcePaths = ["test1.red"]

        # Run the test
        for resource in self.__resource_generator(resourcePaths):
            bake._run_on_resource(resource) 

        # Ensure that a black file was created
        self.__checkBlackFilesWereCreated(resourcePaths)
       
    def test_twoRedFileThatExist(self):
        resourcePaths = ["test1.red","test2.red"]

        # Run the test
        for resource in self.__resource_generator(resourcePaths):
            bake._run_on_resource(resource) 

        # Ensure that a black file was created
        self.__checkBlackFilesWereCreated(resourcePaths)
    
    def test_noRedFiles(self):
        resourcePaths = []

        # Run the test
        for resource in self.__resource_generator(resourcePaths):
            bake._run_on_resource(resource) 

        # Ensure that a black file was created
        self.__checkBlackFilesWereCreated(resourcePaths)

    def test_baseDirectoryThatDoesntExist(self):
        # Run the test
        with self.assertRaises(FileNotFoundError):
            for resource in bake._resource_generator("INVALID_PATH"):
                pass


if __name__ == '__main__':
    unittest.main()