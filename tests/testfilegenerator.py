import unittest

from datetime import datetime

import os
import shutil

from src.app.generators.filegenerator import FileGenerator

class TestFileGenerator(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls._delete_list = [] 

	@classmethod
	def tearDownClass(cls):
		# delete 
		for item in cls._delete_list:
			if "Folder" in item:
				shutil.rmtree(item)
			else:
				os.remove(item)

	def test_file_generator_generates_files_one(self):
		#setup
		file_generator = FileGenerator()
		file_name = f"Test_{datetime.now()}"
		self._delete_list.append(file_name)
		file_map = {file_name: ""}
		#action
		file_generator.create_files(file_map)
		#verify
		#new project file  has been created
		files = os.listdir()
		# print(files)
		for file in file_map:
			with open(file, "r") as file_reader:
				actual_file_content = file_reader.read()
				self.assertTrue(actual_file_content == file_map[file])
		# read content to verify content is good

	def test_file_generator_generates_files(self):
		#setup
		folder = f"Test_Folder_{datetime.now()}"
		self._delete_list.append(folder)
		os.makedirs(folder)
		file_generator = FileGenerator()
		file_name = f"Test_{datetime.now()}"
		full_path = folder + "/" + file_name
		file_map = {full_path: ""}
		#action
		file_generator.create_files(file_map)
		#verify
		#new project file  has been created
		# print(files)
		for file in file_map:
			with open(file, "r") as file_reader:
				actual_file_content = file_reader.read()
				self.assertTrue(actual_file_content == file_map[file])


		
		
if __name__ == '__main__':
	unittest.main()