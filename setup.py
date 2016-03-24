from setuptools import setup
import re

with open('rous/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

setup(name="rous",
      version=version,
      description="a package for rodents of unusual size",
      url="https://github.com/marcstreeter/pygroup",
      author="Marc Streeter",
      author_email="mstreeter@gmail.com",
      license="you killed my father prepare to die",
      packages=["rous"],
      install_requires=["requests"],
      zip_safe=False)
