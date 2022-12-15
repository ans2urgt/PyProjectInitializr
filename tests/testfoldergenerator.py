import unittest

from datetime import datetime

import os

from src.generators.foldergenerator import FolderGenerator

class TestFolderGenerator(unittest.TestCase):
	"""docstring for CommandLine"""


	def test_folder_generator_generates_folders_one(self):
		#setup
		folder_generator = FolderGenerator()
		project_name = f"Test_{datetime.now()}"
		#action
		folder_generator.create_folders([project_name])
		#verify
		#new project folder  has been created
		folders = os.listdir()
		# print(folders)
		self.assertTrue(project_name in folders)

	def test_folder_generator_generates_folders(self):
		#setup
		folder_generator = FolderGenerator()
		project_name = f"Test_{datetime.now()}"
		folders = [project_name, f"{project_name}/src", f"{project_name}/tests"]
		#action
		folder_generator.create_folders(folders)
		#verify
		#new project folder  has been created
		current_directory_folders = os.listdir()
		# print(current_directory_folders)
		self.assertTrue(project_name in current_directory_folders)
		# check project directory folders
		project_folders = os.listdir(project_name)
		# print(project_folders)
		self.assertTrue("src" in project_folders)
		self.assertTrue("tests" in project_folders)


		
		
if __name__ == '__main__':
	unittest.main()