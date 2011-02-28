import os
import sys

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()

requires = [
    'pyramid',
    'pyramid_handlers',
    'SQLAlchemy',
    'transaction',
    'repoze.tm2>=1.0b1', # default_commit_veto
    'zope.sqlalchemy',
    'cryptacular',
    'WebError',
    'webhelpers',
    ]

if sys.version_info[:3] < (2,5,0):
    requires.append('pysqlite')

setup(name='Haven',
      version='0.0',
      description='Haven',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='William Chambers',
      author_email='FIRSTNAME@bioselement.com',
      url='http://cubecreate.com/',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='haven',
      install_requires = requires,
      entry_points = """\
      [paste.app_factory]
      main = haven:main
      """,
      paster_plugins=['pyramid'],
      )

