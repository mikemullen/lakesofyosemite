import dj_database_url
import dropbox

from lakesofyosemite.settings import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG


ALLOWED_HOSTS = [
	'localhost',
	'.herokuapp.com',
]


SECRET_KEY = get_env_variable("SECRET_KEY")

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'


# Dropbox storage

MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'storages.backends.dropbox.DropBoxStorage'
DROPBOX_OAUTH2_TOKEN = 'Mq6WgzMy9iEAAAAAAAAAAWhCs9ijx2IMJCccKZd3uPaV830sZS3-h6Giv3Y7OtT3'

