import unittest

from datetime import datetime

import os

from src.controller.commandlinecontroller import CommandLineController

from tests import GITIGNORE_CONTENT, EXAMPLE_UNIT_TEST_CONTENT

class TestCommandLine(unittest.TestCase):

	def test_program_takes_command_line_args(self):
		#setup
		controller = CommandLineController()
		project_name = f"Test_{datetime.now()}"
		#action
		controller.run(project_name)
		#verify
		#new project folder  has been created
		# check project folder has been created
		# check src folder has been created
		# check tests folder has been created
		# src folder has __init__.py
		# test folder has __init__.py
		# root folder has .gitignore
		# test folder has sample unittest
		# src folder has READEME.md

		readme_content = ""
		file_map = {

			f"{project_name}/src/__init__.py": "",
			f"{project_name}/tests/__init__.py": "",
			f"{project_name}/tests/testexample.py": EXAMPLE_UNIT_TEST_CONTENT,
			f"{project_name}/.gitignore": GITIGNORE_CONTENT,
			f"{project_name}/README.md": readme_content,

		}
		for file in file_map:
			with open(file, "r") as file_reader:
				actual_file_content = file_reader.read()
				self.assertTrue(actual_file_content == file_map[file])

		
if __name__ == '__main__':
	unittest.main()