import os
from get_running_script_path_helper import get_filename

def test():
    filepath = __file__
    filename_this = get_filename(filepath)
    filename_helper = get_filename()
    condition = (filename_this == "get_running_script_path.py") and \
                (filename_helper == "get_running_script_path_helper.py")
    print(filename_this)
    print(filename_helper)
    assert condition, "Wrong filenames"

if __name__ == "__main__":
    test()