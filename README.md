# Student course template Numerical Astrodynamics[![Build Status](https://travis-ci.org/a-t-0/NumericalAstrodynamicsAssignments_2020.svg?branch=master)](https://travis-ci.org/a-t-0/NumericalAstrodynamicsAssignments_2020)

Hi, w.r.t. the original repository this repository is supplemented with:

0. Python code and latex report integration. The following is done with a single command: 
  - Plots are exported directly into your latex report.
  - Your python code is automatically included in the appendices of your report.
  - The example jupyter notebook is automatically executed.
  - The example jupyter notebook is automatically converted to pdf
  - The pdf of the example jupyter notebook is automatically integrated in the latex report.
  - The latex report is automatically compiled into a pdf.
1. You can easily sync with overleaf, e.g. if you do a last minute run, you just push and pull into overleaf, instead of manually uploading pictures.
2. Unit tests are written. (entire repository code can be tested with a single line)

**Room for improvement**

3. The  `.travis.yml` file is currently not allowing for the Continuous integration (CI) testing with Travis-CI. I do not yet know how to include the `.._environment.yml` into `.travis.yml`. That is why the build status badge on top currently is gray instead of green and says "failed/canceled".
4. A unit test could be written to test a function inside a jupyter notebook.

## Usage: do once

0. If you don't have pip: open Anaconda prompt and browse to the directory of this readme:
```
cd /home/<your path to the repository folder>/
```

1. To use this package, first make a new conda environment and activate (it this automatically installs everything you need)
1.1 For Windows (is currently the same as for linux):
```
conda env create --file windows_environment.yml
```
1.2 For Linux:
```
conda env create --file linux_environment.yml
```
2. Instal jupyter-lab with command:
```
jupyter-lab
```

## Usage: do every time you start Anaconda:

3. Activate the conda environment you created:
```
conda activate tudat-space
```
4. Open jupyter lab
```
jupyter-lab
```

## Usage: do every run:

3. Performe a run for assignment 1 (named project1) of main code (in `main.py`, called from `__main__.py`)
```
python -m code.project1.src
```

## Testing

4. Testing is as simple as running the following command in the root directory of this repository in Anaconda prompt:
```
python -m pytest
```
from the root directory of this project.

<!-- Un-wrapped URL's below (Mostly for Badges) -->
[black_badge]: https://img.shields.io/badge/code%20style-black-000000.svg
[python_badge]: https://img.shields.io/badge/python-3.8-blue.svg
[apache_badge]: https://img.shields.io/badge/license-Apache%202.0-brightgreen.svg
