# `xplr`

[![badge](https://img.shields.io/pypi/v/xplr)](https://pypi.org/project/xplr/)

## Overview

The `xplr` package is aimed at quick visualization of Python objects in exploratory data analysis. It has two functions:

* `plot`---Create basic sensible plot of object
* `view`---Export object to temporary file and open in default external program

The `plot` function has the following modes:

| Group | Object | Plot type |
|:---:|:---:|:---:|
| Vector          | `ndarray` (1-dimensional) | Line plot |
| Vector          | `Series`                  | Line plot |
| Table           | `DataFrame`               | Line plot |
| Matrix          | `ndarray` (2-dimensional) | Image     |
| Geometry column | `GeoSeries`               | Map       |
| Vector layer    | `GeoDataFrame`            | Map       |

The `view` function has the following modes:

| Group | Object | Plot type |
|:---:|:---:|:---:|
| Vector          | `Series`                  | `'.xlsx'` |
| Table           | `DataFrame`               | `'.xlsx'` |
| Geometry column | `GeoSeries`               | `'.gpkg'` |
| Vector layer    | `GeoDataFrame`            | `'.gpkg'` |

* `GeoSeries`, `GeoDataFrame`---Exported to `'.gpkg'` and opened (e.g., in QGIS)
* `Series`, `DataFrame`---Exported to `'.xlsx'` and opened (e.g., in LibreOffice)

## Import on startup

To load the two functions `plot` and `view` on startup of `python` or `ipython` in the terminal, so that you can quickly use them anytime, use the following instructions for Linux. (On other operating systems, or other Python interfaces, look up analogous instructions of installing a startup script specific to your system.)

Create a startup script, such as `~/.python_startup.py`:

```python
from xplr import plot
from xplr import view
```

For the script to be automatically executed on `python` startup, add this in your `.bashrc`:

```python
export PYTHONSTARTUP=~/.python_startup.py
```

In addition, for the script to be automatically executed on `ipython` startup, create ipython profiles (if you don't already have them):

```python
ipython profile create
```

Then, uncomment the following expression in `~/.ipython/profile_default/ipython_config.py`:

```python
c.InteractiveShellApp.exec_PYTHONSTARTUP = True
```


