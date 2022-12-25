import unittest

import os
import shutil

from datetime import datetime

from app.generators.envgenerator import EnvGenerator

class TestEnvGenerator(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls._delete_list = [] 

	@classmethod
	def tearDownClass(cls):
		# delete 
		for item in cls._delete_list:
			shutil.rmtree(item)

	def test_generate_virtual_env(self):
		project_name = f"test_project_{datetime.now()}"
		env_name = f"env"
		self._delete_list.append(project_name)
		env_generator = EnvGenerator()
		env_generator.create(project_name)
		folders = os.listdir(project_name)
		self.assertTrue(env_name in folders)
		