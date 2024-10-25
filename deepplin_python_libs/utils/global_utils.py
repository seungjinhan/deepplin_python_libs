import sys
import os

def global_init():
    # Directory path of the current file
    current_dir = os.path.dirname(__file__)

    # Parent directory path
    parent_dir = os.path.abspath(os.path.join(current_dir, '..'))

    # Add the parent directory to sys.path
    sys.path.append(parent_dir)