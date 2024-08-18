# Chart.js Python Wrapper

This project provides a Python wrapper for Chart.js, allowing you to easily generate Chart.js charts using a command-line interface. It includes a setup script to configure your environment and a test suite to ensure everything is working correctly.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Setup](#setup)
3. [Project Structure](#project-structure)
4. [Using the Wrapper](#using-the-wrapper)
5. [Running Tests](#running-tests)
6. [Customizing the Wrapper](#customizing-the-wrapper)
7. [Troubleshooting](#troubleshooting)

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Python 3.6 or higher
- Node.js and npm (for Chart.js installation)

## Setup

1. Clone this repository or download the source code.

2. Navigate to the project directory in your terminal.

3. Run the setup script:

   ```
   python setup_chartjs.py
   ```

   This script will:
   - Check for Node.js and npm installation
   - Create a Python virtual environment
   - Set up the project structure
   - Install Chart.js using npm

4. After the setup completes, activate the virtual environment:

   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

5. Install the required Python packages:

   ```
   pip install -r requirements.txt
   ```

## Project Structure

After running the setup script, your project structure will look like this:

```
.
├── src/
│   └── chartjs_wrapper.py
├── tests/
│   └── test_chartjs.py
├── output/
│   └── .gitkeep
├── venv/
├── node_modules/
├── package.json
├── package-lock.json
├── requirements.txt
└── setup_chartjs.py
```

- `src/chartjs_wrapper.py`: Contains the `ChartJSWrapper` class implementation
- `tests/test_chartjs.py`: Contains unit tests for the wrapper
- `output/`: Directory for generated chart files
- `venv/`: Python virtual environment
- `node_modules/`: Contains Chart.js and its dependencies
- `package.json` and `package-lock.json`: npm configuration files
- `requirements.txt`: Python package dependencies
- `setup_chartjs.py`: Setup script for the project

## Using the Wrapper

To use the Chart.js Python wrapper:

1. Ensure your virtual environment is activated.

2. Run the wrapper script:

   ```
   python src/chartjs_wrapper.py
   ```

3. Follow the prompts to create your chart. You'll be asked to provide:
   - Chart type (e.g., line, bar, pie)
   - Chart title
   - Labels for your data
   - Dataset values
   - Colors for the chart

4. The wrapper will generate JavaScript code for your chart and optionally save it to a file.

## Running Tests

To run the test suite:

1. Ensure your virtual environment is activated.

2. Run the test script:

   ```
   python tests/test_chartjs.py
   ```

This will run all the unit tests and display the results.

## Customizing the Wrapper

You can customize the `ChartJSWrapper` class in `src/chartjs_wrapper.py` to add new features or modify existing ones. Some ideas for customization:

- Add support for more Chart.js options
- Implement additional chart types
- Create preset configurations for common chart styles
- Add export options for different file formats

After making changes, don't forget to update the tests in `tests/test_chartjs.py` accordingly.

## Troubleshooting

If you encounter any issues during setup or while using the wrapper, try the following:

1. Ensure all prerequisites are correctly installed.
2. Check that you're using the correct Python version.
3. Make sure your virtual environment is activated when running scripts.
4. If you get module import errors, try reinstalling the Python packages:
   ```
   pip install -r requirements.txt
   ```
5. For Chart.js related issues, try reinstalling it using npm:
   ```
   npm install chart.js
   ```

If problems persist, please open an issue in the project repository with a detailed description of the error and steps to reproduce it.

---

We hope you find this Chart.js Python wrapper useful! If you have any questions or suggestions for improvement, please don't hesitate to contribute or reach out to the project maintainers.
