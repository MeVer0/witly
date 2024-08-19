import os


root_path = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(os.path.dirname(root_path), '.env')
static_path = os.path.join(root_path, 'static')
templates_path = os.path.join(root_path, 'templates')
