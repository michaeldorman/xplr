def view(x) -> str:
    import os
    import subprocess
    import tempfile
    import pandas as pd
    import geopandas as gpd
    from .click import click
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
        with tempfile.NamedTemporaryFile(suffix='.csv', delete=False) as tmp:
            tmp_path = tmp.name
        x.to_csv(tmp_path)
        click(tmp_path)
        return tmp_path


