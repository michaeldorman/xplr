def click(file_path):
    import os
    import platform
    import subprocess
    """Opens a file using the operating system's default application."""
    # Clean env
    env = os.environ.copy()
    for var in ['VIRTUAL_ENV', 'PYTHONHOME', 'PYTHONPATH']:
        env.pop(var, None)
    if 'VIRTUAL_ENV' in os.environ:
        venv_bin = os.path.join(os.environ['VIRTUAL_ENV'], 'bin')
        env['PATH'] = ':'.join(
            p for p in env['PATH'].split(':') if p != venv_bin
        )
    # Run
    current_os = platform.system().lower()
    abs_path = os.path.abspath(file_path)
    if current_os == 'windows':
        os.startfile(abs_path)
    elif current_os == 'darwin':
        subprocess.call(('open', abs_path), stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    else:
        subprocess.call(('xdg-open', abs_path), env=env, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)

def plot(x, *args, **kwargs):
    """
    Plots an object.

    Args:
        x: The object to plot.
        *args: Positional arguments passed to plotting function
        **kwargs: Keyword arguments passed to plotting function
 
    Returns:
        None
    """
    import matplotlib.pyplot as plt
    plt.ion()
    import pandas as pd
    import geopandas as gpd
    import numpy as np
    import rasterio.plot
    # GeoDataFrame
    if isinstance(x, gpd.GeoSeries) or isinstance(x, gpd.GeoDataFrame):
        x.plot(legend=True, *args, **kwargs)
        return
    # DataFrame
    if isinstance(x, pd.DataFrame):
        x.plot(*args, **kwargs)
        return
    # Series
    if isinstance(x, pd.Series):
        x.plot(*args, **kwargs)
        return
    # Array 1d
    if isinstance(x, np.ndarray) and x.ndim == 1:
        plt.plot(x, *args, **kwargs)
        return
    # Array 2d
    if isinstance(x, np.ndarray) and x.ndim == 2:
        plt.imshow(x, *args, **kwargs)
        return

def view(x) -> str:
    import os
    import subprocess
    import tempfile
    import pandas as pd
    import geopandas as gpd
    """
    Exports an object to a temporary file and opens it in external program.

    Args:
        x: The object to view.

    Returns:
        The path to the temporary file (it persists until the OS cleans it up).
    """
    # Vector layer
    if isinstance(x, gpd.GeoSeries) or isinstance(x, gpd.GeoDataFrame):
        with tempfile.NamedTemporaryFile(suffix='.gpkg', delete=False) as tmp:
            tmp_path = tmp.name
        x.to_file(tmp_path, index=False)
        click(tmp_path)
        return tmp_path
    # Table
    if isinstance(x, pd.Series) or isinstance(x, pd.DataFrame):
        with tempfile.NamedTemporaryFile(suffix='.xlsx', delete=False) as tmp:
            tmp_path = tmp.name
        x.to_excel(tmp_path, index=False)
        click(tmp_path)
        return tmp_path


