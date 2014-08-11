import os
ENVIRONMENT = os.environ.get('ENVIRONMENT', 'dev')  # dev, production, qa, etc 
exec('from settings_%s import *' % ENVIRONMENT)
