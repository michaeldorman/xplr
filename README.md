# `xplr`


[![](https://img.shields.io/pypi/v/xplr.png)](https://pypi.org/project/xplr/)

## Overview

The `xplr` package is aimed at quick visualization of Python objects in
exploratory data analysis. It has two functions:

- `plot`—Create basic sensible plot of object
- `view`—Export object to temporary file and open in default external
  program

The `plot` function has the following modes:

|      Group      |          Object           | Plot type |
|:---------------:|:-------------------------:|:---------:|
|     Vector      | `ndarray` (1-dimensional) | Line plot |
|     Vector      |         `Series`          | Line plot |
|      Table      |        `DataFrame`        | Line plot |
|     Matrix      | `ndarray` (2-dimensional) |   Image   |
| Geometry column |        `GeoSeries`        |    Map    |
|  Vector layer   |      `GeoDataFrame`       |    Map    |

The `view` function has the following modes:

|      Group      |     Object     | Plot type |
|:---------------:|:--------------:|:---------:|
|     Vector      |    `Series`    | `'.xlsx'` |
|      Table      |  `DataFrame`   | `'.xlsx'` |
| Geometry column |  `GeoSeries`   | `'.gpkg'` |
|  Vector layer   | `GeoDataFrame` | `'.gpkg'` |

- `GeoSeries`, `GeoDataFrame`—Exported to `'.gpkg'` and opened (e.g., in
  QGIS)
- `Series`, `DataFrame`—Exported to `'.xlsx'` and opened (e.g., in
  LibreOffice)

> The functionality of `plot` and `view` is inspired by the base
> [R](https://www.r-project.org/) functions `plot` and `View`,
> respectively.

## Examples

Let’s import the two functions:

``` python
from xplr import plot
from xplr import view
```

Suppose we have a `GeoDataFrame` named `pols` in our Python environment:

``` python
import shapely
import geopandas as gpd
pols = gpd.GeoSeries([
    shapely.geometry.Polygon([(0,0), (2,0), (2,2), (0,2)]),
    shapely.geometry.Polygon([(2,2), (4,2), (4,4), (2,4)]),
    shapely.geometry.Polygon([(1,1), (3,1), (3,3), (1,3)]),
    shapely.geometry.Polygon([(3,3), (5,3), (5,5), (3,5)]),
])
pols = gpd.GeoDataFrame({'geometry': pols, 'value': [1,2,2,3]})
pols
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
&#10;    .dataframe tbody tr th {
        vertical-align: top;
    }
&#10;    .dataframe thead th {
        text-align: right;
    }
</style>

|     | geometry                            | value |
|-----|-------------------------------------|-------|
| 0   | POLYGON ((0 0, 2 0, 2 2, 0 2, 0 0)) | 1     |
| 1   | POLYGON ((2 2, 4 2, 4 4, 2 4, 2 2)) | 2     |
| 2   | POLYGON ((1 1, 3 1, 3 3, 1 3, 1 1)) | 2     |
| 3   | POLYGON ((3 3, 5 3, 5 5, 3 5, 3 3)) | 3     |

</div>

Here is how we can plot it:

``` python
plot(pols)
```

![](README_files/figure-commonmark/cell-4-output-1.png)

Additional arguments to the plotting method can be passed as follows:

``` python
plot(pols, 'value', color='none')
```

    /home/michael/venv/m/lib/python3.14/site-packages/xplr/xplr.py:45: UserWarning: Only specify one of 'column' or 'color'. Using 'color'.
      x.plot(legend=True, *args, **kwargs)

![](README_files/figure-commonmark/cell-5-output-2.png)

`view` can be used to open the layer in an external program:

``` python
view(pols)
```

    /home/michael/venv/m/lib/python3.14/site-packages/pyogrio/geopandas.py:948: UserWarning: 'crs' was not provided.  The output dataset will not have projection information defined and may not be usable in other systems.
      write(

    '/tmp/tmp4y8vh0nz.gpkg'

The layer is exported to a temporary file, which is then opened in the
default program (e.g., QGIS).

![The `pols` layer opened in QGIS](README_files/qgis.png)

## Import on startup

To load the two functions `plot` and `view` on startup of `python` or
`ipython` in the terminal, so that you can quickly use them anytime, use
the following instructions for Linux. (On other operating systems, or
other Python interfaces, look up analogous instructions of installing a
startup script specific to your system.)

Create a startup script, such as `~/.python_startup.py`:

``` python
from xplr import plot
from xplr import view
```

For the script to be automatically executed on `python` startup, add
this in your `.bashrc`:

``` python
export PYTHONSTARTUP=~/.python_startup.py
```

In addition, for the script to be automatically executed on `ipython`
startup, create ipython profiles (if you don’t already have them):

``` python
ipython profile create
```

Then, uncomment the following expression in
`~/.ipython/profile_default/ipython_config.py`:

``` python
c.InteractiveShellApp.exec_PYTHONSTARTUP = True
```
