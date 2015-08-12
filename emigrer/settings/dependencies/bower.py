#BOWER SETTINGS
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

BOWER_INSTALLED_APPS = (
	'underscore#1.8.3',
)

BOWER_COMPONENTS_ROOT = os.path.join(BASE_DIR, 'components')
