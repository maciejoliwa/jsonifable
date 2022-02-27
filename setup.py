from setuptools import setup

VERSION = '0.0.5'
DESCRIPTION = 'Simple decorator for making classes easily convertable to JSON'

setup(
    name='jsonifable',
    version=VERSION,
    description=DESCRIPTION,
    packages=['jsonifable'],
    author="Maciej Oliwa (avery)",
    author_email="maciejoliwa0906@gmail.com",
    keywords=['python', 'json', 'class', 'dataclass', 'tojson'],    
)