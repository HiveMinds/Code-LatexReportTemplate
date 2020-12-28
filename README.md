# Student latex course template [![Build Status][![Build Status](https://travis-ci.com/a-t-0/Code-LatexReportTemplate.svg?branch=master)](https://travis-ci.com/a-t-0/Code-LatexReportTemplate)

Hi, this is a template you can use for every course. In particular if you do some python coding (normal or Jupiter notebooks), this repository enables you to automatically updates your report every time you run your code. It also syncs with Overleaf so you can do your typing there. That means no last minute copy pasting of images into Overleaf (if you were into that sort of thing). Also it automatically sets up your programming envirionment for you, and if you collaborate with others, you can automatically see whether their code contributions keep the code working, thanks to the Continuous Integration with Travis-CI. To summarise:

0. Python code and latex report integration. The following is done with a single command: 
  - Plots are exported directly into your latex report.
  - Your python code is automatically included in the appendices of your report.
  - The example jupyter notebook is automatically executed.
  - The example jupyter notebook is automatically converted to pdf
  - The pdf of the example jupyter notebook is automatically integrated in the latex report.
  - The latex report is automatically compiled into a pdf.
1. You can easily sync with Overleaf, e.g. if you do a last minute run, you just push and pull into overleaf, instead of manually uploading pictures.
2. Unit tests are written. (entire repository code can be tested with a single line)

## Usage: do once

0. If you don't have pip: open Anaconda prompt and browse to the directory of this readme:
```
cd /home/<your path to the repository folder>/
```

1. To use this package, first make a new conda environment and activate (it this automatically installs everything you need)
```
conda env create --file environment.yml
```

## Usage: do every time you start Anaconda:

3. Activate the conda environment you created:
```
conda activate example_env
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
