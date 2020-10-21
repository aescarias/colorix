from setuptools import setup
import re

with open('colorix\__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

print("Setup for version: ", version)

requirements = []

with open("README.md", "r") as f:
    readme = f.read()

setup(name="colorix",
      packages=["colorix"],
      author='Tekgar',
      author_email=None,
      version=version,
      description="A Python3 module for colors",
      long_description=readme,
      long_description_content_type="text/markdown",
      install_requires=requirements,
      python_requires=">=3.6",
      url="https://github.com/angelCarias/colorix",
      download_url="https://github.com/angelCarias/colorix/archive/v0.1.5.tar.gz"
      )
