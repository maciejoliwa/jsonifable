from setuptools import setup

VERSION = '0.1.0'
DESCRIPTION = 'Simple decorator for making classes easily convertable to JSON'


def read_readme() -> str:
    with open('README.md', 'r') as README:
        return README.read()


setup(
    name='jsonifable',
    version=VERSION,
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=read_readme(),
    packages=['jsonifable'],
    author="Maciej Oliwa (avery)",
    author_email="maciejoliwa0906@gmail.com",
    keywords=['python', 'json', 'class', 'dataclass', 'tojson'],
)
