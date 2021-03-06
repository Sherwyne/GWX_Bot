from setuptools import setup

setup(
    name='gwx_bot',
    version='',
    packages=['venv.Lib.site-packages.rsa', 'venv.Lib.site-packages.attr', 'venv.Lib.site-packages.cffi',
              'venv.Lib.site-packages.idna', 'venv.Lib.site-packages.past', 'venv.Lib.site-packages.past.tests',
              'venv.Lib.site-packages.past.types', 'venv.Lib.site-packages.past.utils',
              'venv.Lib.site-packages.past.builtins', 'venv.Lib.site-packages.past.translation',
              'venv.Lib.site-packages.yarl', 'venv.Lib.site-packages.click', 'venv.Lib.site-packages.future',
              'venv.Lib.site-packages.future.moves', 'venv.Lib.site-packages.future.moves.dbm',
              'venv.Lib.site-packages.future.moves.html', 'venv.Lib.site-packages.future.moves.http',
              'venv.Lib.site-packages.future.moves.test', 'venv.Lib.site-packages.future.moves.urllib',
              'venv.Lib.site-packages.future.moves.xmlrpc', 'venv.Lib.site-packages.future.moves.tkinter',
              'venv.Lib.site-packages.future.tests', 'venv.Lib.site-packages.future.types',
              'venv.Lib.site-packages.future.utils', 'venv.Lib.site-packages.future.builtins',
              'venv.Lib.site-packages.future.backports', 'venv.Lib.site-packages.future.backports.html',
              'venv.Lib.site-packages.future.backports.http', 'venv.Lib.site-packages.future.backports.test',
              'venv.Lib.site-packages.future.backports.email', 'venv.Lib.site-packages.future.backports.email.mime',
              'venv.Lib.site-packages.future.backports.urllib', 'venv.Lib.site-packages.future.backports.xmlrpc',
              'venv.Lib.site-packages.future.standard_library', 'venv.Lib.site-packages.jinja2',
              'venv.Lib.site-packages.pyasn1', 'venv.Lib.site-packages.pyasn1.type',
              'venv.Lib.site-packages.pyasn1.codec', 'venv.Lib.site-packages.pyasn1.codec.ber',
              'venv.Lib.site-packages.pyasn1.codec.cer', 'venv.Lib.site-packages.pyasn1.codec.der',
              'venv.Lib.site-packages.pyasn1.codec.native', 'venv.Lib.site-packages.pyasn1.compat',
              'venv.Lib.site-packages.tweepy', 'venv.Lib.site-packages.aiohttp', 'venv.Lib.site-packages.certifi',
              'venv.Lib.site-packages.chardet', 'venv.Lib.site-packages.chardet.cli', 'venv.Lib.site-packages.gspread',
              'venv.Lib.site-packages.twitter', 'venv.Lib.site-packages.urllib3', 'venv.Lib.site-packages.urllib3.util',
              'venv.Lib.site-packages.urllib3.contrib', 'venv.Lib.site-packages.urllib3.contrib._securetransport',
              'venv.Lib.site-packages.urllib3.packages', 'venv.Lib.site-packages.urllib3.packages.backports',
              'venv.Lib.site-packages.urllib3.packages.ssl_match_hostname', 'venv.Lib.site-packages.examples',
              'venv.Lib.site-packages.httplib2', 'venv.Lib.site-packages.oauthlib',
              'venv.Lib.site-packages.oauthlib.oauth1', 'venv.Lib.site-packages.oauthlib.oauth1.rfc5849',
              'venv.Lib.site-packages.oauthlib.oauth1.rfc5849.endpoints', 'venv.Lib.site-packages.oauthlib.oauth2',
              'venv.Lib.site-packages.oauthlib.oauth2.rfc6749',
              'venv.Lib.site-packages.oauthlib.oauth2.rfc6749.clients',
              'venv.Lib.site-packages.oauthlib.oauth2.rfc6749.endpoints',
              'venv.Lib.site-packages.oauthlib.oauth2.rfc6749.grant_types', 'venv.Lib.site-packages.requests',
              'venv.Lib.site-packages.telegram', 'venv.Lib.site-packages.telegram.ext',
              'venv.Lib.site-packages.telegram.files', 'venv.Lib.site-packages.telegram.games',
              'venv.Lib.site-packages.telegram.utils', 'venv.Lib.site-packages.telegram.inline',
              'venv.Lib.site-packages.telegram.vendor', 'venv.Lib.site-packages.telegram.vendor.ptb_urllib3',
              'venv.Lib.site-packages.telegram.vendor.ptb_urllib3.urllib3',
              'venv.Lib.site-packages.telegram.vendor.ptb_urllib3.urllib3.util',
              'venv.Lib.site-packages.telegram.vendor.ptb_urllib3.urllib3.contrib',
              'venv.Lib.site-packages.telegram.vendor.ptb_urllib3.urllib3.packages',
              'venv.Lib.site-packages.telegram.vendor.ptb_urllib3.urllib3.packages.backports',
              'venv.Lib.site-packages.telegram.vendor.ptb_urllib3.urllib3.packages.ssl_match_hostname',
              'venv.Lib.site-packages.telegram.payment', 'venv.Lib.site-packages.telegram.passport',
              'venv.Lib.site-packages.werkzeug', 'venv.Lib.site-packages.werkzeug.debug',
              'venv.Lib.site-packages.werkzeug.contrib', 'venv.Lib.site-packages.multidict',
              'venv.Lib.site-packages.pycparser', 'venv.Lib.site-packages.pycparser.ply',
              'venv.Lib.site-packages.asn1crypto', 'venv.Lib.site-packages.asn1crypto._perf',
              'venv.Lib.site-packages.markupsafe', 'venv.Lib.site-packages.libfuturize',
              'venv.Lib.site-packages.libfuturize.fixes', 'venv.Lib.site-packages.cryptography',
              'venv.Lib.site-packages.cryptography.x509', 'venv.Lib.site-packages.cryptography.hazmat',
              'venv.Lib.site-packages.cryptography.hazmat.backends',
              'venv.Lib.site-packages.cryptography.hazmat.backends.openssl',
              'venv.Lib.site-packages.cryptography.hazmat.bindings',
              'venv.Lib.site-packages.cryptography.hazmat.bindings.openssl',
              'venv.Lib.site-packages.cryptography.hazmat.primitives',
              'venv.Lib.site-packages.cryptography.hazmat.primitives.kdf',
              'venv.Lib.site-packages.cryptography.hazmat.primitives.ciphers',
              'venv.Lib.site-packages.cryptography.hazmat.primitives.twofactor',
              'venv.Lib.site-packages.cryptography.hazmat.primitives.asymmetric', 'venv.Lib.site-packages.itsdangerous',
              'venv.Lib.site-packages.oauth2client', 'venv.Lib.site-packages.oauth2client.contrib',
              'venv.Lib.site-packages.oauth2client.contrib.django_util', 'venv.Lib.site-packages.async_timeout',
              'venv.Lib.site-packages.libpasteurize', 'venv.Lib.site-packages.libpasteurize.fixes',
              'venv.Lib.site-packages.pyasn1_modules', 'venv.Lib.site-packages.requests_oauthlib',
              'venv.Lib.site-packages.requests_oauthlib.compliance_fixes',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.idna',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.pytoml',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.certifi',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.chardet',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.chardet.cli',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.distlib',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.distlib._backport',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.msgpack',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.urllib3',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.urllib3.util',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.urllib3.contrib',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.urllib3.contrib._securetransport',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.urllib3.packages',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.urllib3.packages.backports',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.urllib3.packages.ssl_match_hostname',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.colorama',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.html5lib',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.html5lib._trie',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.html5lib.filters',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.html5lib.treewalkers',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.html5lib.treeadapters',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.html5lib.treebuilders',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.lockfile',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.progress',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.requests',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.packaging',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.cachecontrol',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.cachecontrol.caches',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.webencodings',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.pkg_resources',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._internal',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._internal.req',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._internal.vcs',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._internal.utils',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._internal.models',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._internal.commands',
              'venv.Lib.site-packages.pip-10.0.1-py3.7.egg.pip._internal.operations'],
    url='',
    license='',
    author='Sherwyne',
    author_email='sherwyne123+work@gmail.com',
    description='A Telegram bot for managing bounty campaign'
)
