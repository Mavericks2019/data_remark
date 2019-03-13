import os
import sys

current_path = os.path.abspath(os.path.dirname(__file__))
model_path = os.path.dirname(os.path.dirname(current_path))
sys.path.append(model_path)
