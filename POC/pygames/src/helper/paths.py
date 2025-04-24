import os

# Root path of the project (usually src/)
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

def asset_path(*paths):
    """Build full path to an asset file."""
    return os.path.join(ROOT_DIR, 'assets', *paths)