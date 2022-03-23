SublimeLinter-contrib-cmakelint
=========================

[![Build Status](https://app.travis-ci.com/jasjuang/SublimeLinter-contrib-cmakelint.svg?branch=master)](https://app.travis-ci.com/jasjuang/SublimeLinter-contrib-cmakelint)
[![Package Control](https://packagecontrol.herokuapp.com/downloads/SublimeLinter-contrib-cmakelint.svg?style=flat-square)](https://packagecontrol.io/packages/SublimeLinter-contrib-cmakelint)

This linter plugin for SublimeLinter provides an interface to [cmakelint](https://pypi.python.org/pypi/cmakelint). It will be used with files that have the “cmake” syntax.

## Installation
SublimeLinter must be installed in order to use this plugin. 

Please use [Package Control](https://packagecontrol.io) to install the linter plugin.

Before using this plugin, you must ensure that `cmakelint` is installed on your system. To install `cmakelint`, do the following:

1. Install [Python](http://python.org/download/) and [pip](http://www.pip-installer.org/en/latest/installing.html).

1. Install `cmakelint` by typing the following in a terminal:
   ```
   [sudo] pip install cmakelint
   ```

In order for `cmakelint` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. The docs cover [troubleshooting PATH configuration](http://sublimelinter.readthedocs.io/en/latest/troubleshooting.html#finding-a-linter-executable).

## Settings
SublimeLinter settings: http://sublimelinter.readthedocs.org/en/latest/settings.html
Linter settings: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html

Additional settings for SublimeLinter-cmakelint

|Setting|Description|
|:------|:----------|
|filter|A comma-separated list of category-filters to apply|

``filter`` can be a single string (anywhere) or array of strings (anywhere but inline).
