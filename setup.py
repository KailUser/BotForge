from setuptools import setup, find_packages
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


setup(
    name='PyGram',
    version='0.0.4',
    install_requires=find_packages(),
    description='PyGram - tiny bot api for telegram',
    author='Syirezz',
    author_email='syirezz@icloud.com',
    url='https://github.com/KailUser/PyGram',
    license='MIT',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)