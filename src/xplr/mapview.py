def mapview(x, *args, **kwargs):
    """
    Displays layer in an interactive map in a web browser.

    Args:
        x: The object to plot.
        *args: Positional arguments passed to plotting function
        **kwargs: Keyword arguments passed to plotting function
 
    Returns:
        None
    """
    import tempfile
    import webbrowser
    with tempfile.NamedTemporaryFile(suffix='.html', delete=False) as tmp:
        tmp_path = tmp.name
    x.explore(*args, **kwargs).save(tmp_path)
    webbrowser.open(tmp_path)


