import os

def get_filename(filepath=None):
    if filepath is None:
        filepath = __file__
    filename = os.path.basename(filepath)
    return filename