DEV_APPSERVER_PATH = '/usr/local/google_appengine/dev_appserver.py'
BIGSKY_DATASTORE_PATH = '~/dev/workiva/other/bigsky/datastore/django_dev~big-sky.datastore'
BIGSKY_APP_YAML_PATH = '~/dev/workiva/other/bigsky/app.yaml'

RUNSERVER_PROCESS = '%s --datastore_path=%s %s' % (DEV_APPSERVER_PATH, BIGSKY_DATASTORE_PATH, BIGSKY_APP_YAML_PATH)
