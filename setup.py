import setuptools
import os
from pathlib import Path

"""
See the following resources:
* https://setuptools.readthedocs.io/en/latest/setuptools.html
* https://docs.python.org/3.7/distutils/setupscript.html
"""

root = Path(os.path.realpath(__file__)).parent
version_file = root / 'package' / 'VERSION'
readme_file = root / 'readme.md'

setuptools.setup(
    name='python-minimal',
    version=version_file.read_text().strip(),
    packages=setuptools.find_packages(),
    url='https://github.com/felix-hilden/python-minimal',
    download_url='https://github.com/felix-hilden/python-minimal',

    author='Felix Hildén',
    author_email='felix.hilden@gmail.com',
    maintainer='Felix Hildén',
    maintainer_email='felix.hilden@gmail.com',

    description='minimal python package template',
    long_description=readme_file.read_text(),
    long_description_content_type='text/markdown',
    license='MIT',
    package_data={
        'package': ['VERSION']
    },

    python_requires='>=3.6',
    install_requires=[],
)
