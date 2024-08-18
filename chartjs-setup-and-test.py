# File: setup_chartjs.py

import os
import subprocess
import sys
import shutil
import time
import venv

def print_step(step):
    print(f"\n{'=' * 50}")
    print(f"{step:^50}")
    print(f"{'=' * 50}\n")

def run_command(command, error_message):
    try:
        subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error: {error_message}")
        print(f"Command output: {e.stdout}")
        print(f"Command error: {e.stderr}")
        return False

def check_node_npm():
    print_step("Checking Node.js and npm")
    node_version = run_command(["node", "--version"], "Node.js is not installed or not in PATH.")
    npm_version = run_command(["npm", "--version"], "npm is not installed or not in PATH.")
    return node_version and npm_version

def create_virtual_env():
    print_step("Creating Python virtual environment")
    venv_dir = "venv"
    if os.path.exists(venv_dir):
        print(f"Virtual environment '{venv_dir}' already exists. Skipping creation.")
        return True

    try:
        venv.create(venv_dir, with_pip=True)
        print(f"Virtual environment '{venv_dir}' created successfully.")
        return True
    except Exception as e:
        print(f"Error creating virtual environment: {e}")
        return False

def activate_virtual_env():
    if sys.platform == "win32":
        activate_script = os.path.join("venv", "Scripts", "activate.bat")
    else:
        activate_script = os.path.join("venv", "bin", "activate")
    
    print(f"To activate the virtual environment, run:\n")
    print(f"  {activate_script}")
    print(f"\nAfter activation, install required Python packages with:")
    print(f"  pip install -r requirements.txt")

def create_project_structure():
    print_step("Creating project structure")
    directories = ["src", "tests", "output"]
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"Created directory: {directory}")
    
    # Create placeholder files
    placeholder_files = {
        "src/chartjs_wrapper.py": "# Chart.js wrapper implementation goes here\n",
        "tests/test_chartjs.py": "# Test cases for Chart.js wrapper go here\n",
        "output/.gitkeep": "",
        "requirements.txt": "# Add your Python dependencies here\n",
    }
    for file_path, content in placeholder_files.items():
        with open(file_path, "w") as f:
            f.write(content)
        print(f"Created file: {file_path}")

def setup_chartjs():
    print_step("Setting up Chart.js project")
    
    if not check_node_npm():
        print("Please install Node.js and npm, then run this script again.")
        sys.exit(1)
    
    if not create_virtual_env():
        print("Failed to create virtual environment. Please check your Python installation.")
        sys.exit(1)
    
    create_project_structure()
    
    print_step("Installing Chart.js")
    if not run_command(["npm", "init", "-y"], "Failed to initialize npm project."):
        sys.exit(1)
    if not run_command(["npm", "install", "chart.js"], "Failed to install Chart.js."):
        sys.exit(1)
    
    print_step("Project setup complete")
    print("\nProject structure:")
    for root, dirs, files in os.walk("."):
        level = root.replace(".", "").count(os.sep)
        indent = " " * 4 * level
        print(f"{indent}{os.path.basename(root)}/")
        subindent = " " * 4 * (level + 1)
        for f in files:
            print(f"{subindent}{f}")
    
    print("\nNext steps:")
    print("1. Activate the virtual environment")
    activate_virtual_env()
    print("\n2. Copy your ChartJSWrapper class into src/chartjs_wrapper.py")
    print("3. Implement test cases in tests/test_chartjs.py")
    print("4. Run the test script with:")
    print("   python tests/test_chartjs.py")

if __name__ == "__main__":
    try:
        setup_chartjs()
    except KeyboardInterrupt:
        print("\n\nSetup interrupted. Cleaning up...")
        # Add cleanup code here if necessary
        print("Setup aborted. You can run the script again to restart the setup process.")
        sys.exit(1)
    except Exception as e:
        print(f"\n\nAn unexpected error occurred: {e}")
        print("Please report this issue to the project maintainers.")
        sys.exit(1)

# File: tests/test_chartjs.py

import sys
import os
import unittest
from unittest.mock import patch

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.chartjs_wrapper import ChartJSWrapper

class TestChartJSWrapper(unittest.TestCase):
    def setUp(self):
        self.wrapper = ChartJSWrapper()

    @patch('builtins.input')
    def test_chart_generation(self, mock_input):
        mock_input.side_effect = [
            "1",  # chart type
            "testChart",  # chart ID
            "Test Chart",  # chart title
            "A,B,C",  # labels
            "Test Dataset",  # dataset label
            "1,2,3",  # data values
            "blue",  # background color
            "blue",  # border color
            "1",  # border width
            "no"  # add another dataset?
        ]
        
        js_code = self.wrapper.generate_chart()
        
        self.assertIn("type: 'line'", js_code)
        self.assertIn("labels: [\"A\",\"B\",\"C\"]", js_code)
        self.assertIn("data: [1.0,2.0,3.0]", js_code)
        self.assertIn("backgroundColor: \"rgba(54, 162, 235, 0.2)\"", js_code)
        
    def test_color_presets(self):
        self.assertEqual(self.wrapper.color_presets["blue"], "rgba(54, 162, 235, 0.2)")
        self.assertEqual(self.wrapper.color_presets["red"], "rgba(255, 99, 132, 0.2)")

    def test_chart_types(self):
        expected_types = ["line", "bar", "radar", "doughnut", "pie", "polarArea", "bubble", "scatter"]
        self.assertEqual(self.wrapper.chart_types, expected_types)

if __name__ == "__main__":
    unittest.main(verbosity=2)
