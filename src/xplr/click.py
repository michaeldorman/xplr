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


