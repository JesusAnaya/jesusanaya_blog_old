import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'pyramid==1.6.1',
    'pyramid_jinja2==2.6.2',
    'pyramid_debugtoolbar==2.4.2',
    'pyramid_tm==0.12.1',
    'SQLAlchemy==1.0.11',
    'transaction==1.4.4',
    'zope.sqlalchemy==0.7.6',
    'waitress==0.8.10',
    'wtforms==2.1',
    'webhelpers2==2.0',
    'paginate==0.5.2',
    'paginate_sqlalchemy==0.2.0'
]

setup(name='jesusanaya_blog',
      version='0.0.1',
      description='jesusanaya_blog',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='jesusanaya_blog',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = jesusanaya_blog:main
      [console_scripts]
      initialize_jesusanaya_blog_db = jesusanaya_blog.scripts.initializedb:main
      """,
      )
