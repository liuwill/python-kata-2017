from distutils.core import setup
from setuptools import setup

setup(
    name='python-kata',
    version='1.0',
    author='liuwill',
    author_email='liuwill@live.com',
    url='http://www.liuwill.com',
    install_requires=[
        'tox>=2.7.0',
        'coverage>=4.4.1',
        'pytest>=3.1.3',
        'pylint==1.6.5'
    ],
    packages=["kata"],
    #packages=['']
    #py_modules=['foo'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
