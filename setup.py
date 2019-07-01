# -*- coding: utf-8 -*-

from setuptools import setup
from codecs import open
from os import path
import re

package_name = "f2db"

root_dir = path.abspath(path.dirname(__file__))

#def _requirements():
#    return [name.rstrip() for name in open(path.join(root_dir, 'requirements.txt')).readlines()]

#def _test_requirements():
#    return [name.rstrip() for name in open(path.join(root_dir, 'test-requirements.txt')).readlines()]

with open(path.join(root_dir, package_name, '__init__.py')) as f:
    init_text = f.read()
    version = re.search(r'__version__\s*=\s*[\'\"](.+?)[\'\"]', init_text).group(1)
    license = re.search(r'__license__\s*=\s*[\'\"](.+?)[\'\"]', init_text).group(1)
    author = re.search(r'__author__\s*=\s*[\'\"](.+?)[\'\"]', init_text).group(1)
    author_email = re.search(r'__author_email__\s*=\s*[\'\"](.+?)[\'\"]', init_text).group(1)
    url = re.search(r'__url__\s*=\s*[\'\"](.+?)[\'\"]', init_text).group(1)

assert version
assert license
assert author
assert author_email
assert url


setup(
    name=package_name,
    packages=[package_name],
    version=version,
    license=license,
    #install_requires=_requirements(),
    #tests_require=_test_requirements(),
    author=author,
    author_email=author_email,
    url=url,

    description='一言で書けるパッケージ概要',
    long_description='long description',
    keywords='キーワード1, キーワード2, キーワード3',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.6',
        'Topic :: Database',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    )
