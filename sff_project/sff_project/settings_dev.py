"""
Django settings for sff_project project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(7-q&n#by6d6t4!&!9yz)9)k-&sj&h0^+3#6-r_*dv-_8em%&3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(
        os.path.dirname(__file__),
        'static',
    ),
)

INSTALLED_APPS = (
    # Django's
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # this project's applications
    'rateBooks_application',
    'django_suit_demo',

    # suit must come before django.contrib.admin
    'suit',
    'django.contrib.admin',

    # other stuff
    'debug_toolbar',
    'social_auth'
)


###############################################################################
# social_auth
###############################################################################
AUTHENTICATION_BACKENDS = (
#    'social_auth.backends.twitter.TwitterBackend',
#    'social_auth.backends.facebook.FacebookBackend',
    'social_auth.backends.google.GoogleOAuthBackend',
    'social_auth.backends.google.GoogleOAuth2Backend',
    'social_auth.backends.google.GoogleBackend',
#    'social_auth.backends.yahoo.YahooBackend',
#    'social_auth.backends.browserid.BrowserIDBackend',
#    'social_auth.backends.contrib.linkedin.LinkedinBackend',
#    'social_auth.backends.contrib.disqus.DisqusBackend',
#    'social_auth.backends.contrib.livejournal.LiveJournalBackend',
#    'social_auth.backends.contrib.orkut.OrkutBackend',
#    'social_auth.backends.contrib.foursquare.FoursquareBackend',
#    'social_auth.backends.contrib.github.GithubBackend',
#    'social_auth.backends.contrib.vk.VKOAuth2Backend',
#    'social_auth.backends.contrib.live.LiveBackend',
#    'social_auth.backends.contrib.skyrock.SkyrockBackend',
#    'social_auth.backends.contrib.yahoo.YahooOAuthBackend',
#    'social_auth.backends.contrib.readability.ReadabilityBackend',
#    'social_auth.backends.contrib.fedora.FedoraBackend',
#    'social_auth.backends.OpenIDBackend',
    'django.contrib.auth.backends.ModelBackend',
)

#TWITTER_CONSUMER_KEY         = ''
#TWITTER_CONSUMER_SECRET      = ''
#FACEBOOK_APP_ID              = ''
#FACEBOOK_API_SECRET          = ''
#LINKEDIN_CONSUMER_KEY        = ''
#LINKEDIN_CONSUMER_SECRET     = ''
#ORKUT_CONSUMER_KEY           = ''
#ORKUT_CONSUMER_SECRET        = ''
GOOGLE_CONSUMER_KEY          = ''
GOOGLE_CONSUMER_SECRET       = ''
GOOGLE_OAUTH2_CLIENT_ID      = '600602411164-k0m4kl0fb3vmjkdaeam99lvci819smgu.apps.googleusercontent.com'
GOOGLE_OAUTH2_CLIENT_SECRET  = 'V-NsJaXr1k-Y1y7EtMSnGi8r'
#FOURSQUARE_CONSUMER_KEY      = ''
#FOURSQUARE_CONSUMER_SECRET   = ''
#VK_APP_ID                    = ''
#VK_API_SECRET                = ''
#LIVE_CLIENT_ID               = ''
#LIVE_CLIENT_SECRET           = ''
#SKYROCK_CONSUMER_KEY         = ''
#SKYROCK_CONSUMER_SECRET      = ''
#YAHOO_CONSUMER_KEY           = ''
#YAHOO_CONSUMER_SECRET        = ''
#READABILITY_CONSUMER_SECRET  = ''
#READABILITY_CONSUMER_SECRET  = ''

#LOGIN_URL          = '/login-form/'
LOGIN_URL          = '/login/google-oauth2/'
#LOGIN_REDIRECT_URL = '/logged-in/'
LOGIN_REDIRECT_URL = '/'
LOGIN_ERROR_URL    = '/login-error/'

# A different URL could be defined for newly registered users, newly
# associated accounts, or account disconnections
#SOCIAL_AUTH_NEW_ASSOCIATION_REDIRECT_URL = '/new-association-redirect-url/'
#SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/new-users-redirect-url/'
#SOCIAL_AUTH_DISCONNECT_REDIRECT_URL = '/account-disconnected-redirect-url/'

# Configure authentication and association complete URL names to avoid possible clashes:
#SOCIAL_AUTH_COMPLETE_URL_NAME  = 'socialauth_complete'
#SOCIAL_AUTH_ASSOCIATE_URL_NAME = 'socialauth_associate_complete'

# Inactive users can be redirected to a different page if this setting is defined:
SOCIAL_AUTH_INACTIVE_USER_URL = '...'

# the full email address as the username:
SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = True


SESSION_SERIALIZER='django.contrib.sessions.serializers.PickleSerializer'

###############################################################################
# Django Suit
###############################################################################
# Django Suit configuration example
SUIT_CONFIG = {
    # header
    'ADMIN_NAME': 'Django Suit',
    'HEADER_DATE_FORMAT': 'l, j. F Y',
    'HEADER_TIME_FORMAT': 'H:i',

    # forms
    'SHOW_REQUIRED_ASTERISK': True,  # Default True
    'CONFIRM_UNSAVED_CHANGES': True, # Default True

    # menu
    'SEARCH_URL': '/admin/auth/user/',
    'MENU_ICONS': {
       'sites': 'icon-leaf',
       'auth': 'icon-lock',
    },
    'MENU_OPEN_FIRST_CHILD': True, # Default True
    'MENU_EXCLUDE': ('auth.group',),
    'MENU': (
        'sites',
        {'app': 'auth', 'icon':'icon-lock', 'models': ('user', 'group')},
        {'label': 'Settings', 'icon':'icon-cog', 'models': ('auth.user', 'auth.group')},
        {'label': 'Support', 'icon':'icon-question-sign', 'url': '/support/'},
    ),

    # misc
    'LIST_PER_PAGE': 15
}

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)


###############################################################################
# Debug-toolbar settings
###############################################################################
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
    'debug_toolbar.panels.profiling.ProfilingPanel',
]


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'sff_project.urls'

WSGI_APPLICATION = 'sff_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'gnadia',
    }
}

###############################################################################
# Internationalization
###############################################################################
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


###############################################################################
# Static files (CSS, JavaScript, Images)
###############################################################################
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
