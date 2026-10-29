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
    if isinstance(x, gpd.GeoDataFrame):
        x.plot(legend=True, *args, **kwargs)
        return
    # GeoSeries
    if isinstance(x, gpd.GeoSeries):
        x.plot(*args, **kwargs)
        return
    # shapely
    if isinstance(x, BaseGeometry):
        gpd.GeoSeries(x).plot(*args, **kwargs)
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
    # Array 3d
    if isinstance(x, np.ndarray) and x.ndim == 3:
        plt.imshow(x[0], *args, **kwargs)
        return


