import dj_database_url


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

MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'storages.backends.dropbox.DropBoxStorage'
DROPBOX_OAUTH2_TOKEN = 'sl.AjYw4hWhIrlFk4Mb0j1QvhURZbFK1vVSpjS8OeBFTMQmS4mr-JbbN5nt7kZAo6hGIs8laVza8Wd9Iohx-AA8JasVuDcRUbbnLx69j5h9kSRncwFv2i1thz9uwmwphh8EVDWDyMI'

