import os, sys
from .blob import TextBlob, Word, Sentence, Blobber, WordList

__version__ = '0.15.3'
__license__ = 'MIT'
__author__ = 'Steven Loria'

PACKAGE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

EXTERNAL_BASE = os.path.join(PACKAGE_DIR, "externals")
EXTERNAL_LIBS_PATH = os.path.join(EXTERNAL_BASE, "libs")
EXTERNAL_APPS_PATH = os.path.join(EXTERNAL_BASE, "third_apps")
sys.path = ["", EXTERNAL_LIBS_PATH, EXTERNAL_APPS_PATH] + sys.path

__all__ = [
    'TextBlob',
    'Word',
    'Sentence',
    'Blobber',
    'WordList',
]
