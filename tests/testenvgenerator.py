import unittest

import os
import shutil

from datetime import datetime

from src.app.generators.envgenerator import EnvGenerator

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
		env_name = f"env_{datetime.now()}"
		self._delete_list.append(env_name)
		env_generator = EnvGenerator()
		env_generator.create(env_name)
		folders = os.listdir()
		self.assertTrue(env_name in folders)
		