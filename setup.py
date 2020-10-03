#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 A S Lewis
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program. If not, see <http://www.gnu.org/licenses/>.


"""Standard python setup file."""


# Import modules
import glob
import os
import setuptools
import sys

# Set a standard long_description, modified only for Debian/RPM packages
long_description="""
Designed for use at the gym, GymBob prompts the user (graphically and using
sound effects) at regular intervals during a workout. The workout programmes
are completely customistable. GymBob is written in Python 3 / Gtk 3 and runs
on Linux/*BSD.
"""

# data_files for setuptools.setup are added here
param_list = []

script_exec = os.path.join('gymbob', 'gymbob')
icon_path = '/gymbob/icons/'
sound_path = '/gymbob/sounds/'

# For PyPI installations, copy everything in ../icons and ../sounds into a
#   suitable location
for path in glob.glob('icons/*'):
    param_list.append((icon_path, [path]))
for path in glob.glob('sounds/*'):
    param_list.append((sound_path, [path]))

# Setup
setuptools.setup(
    name='gymbob',
    version='2.004',
    description='Simple script to prompt the user during a workout',
    long_description=long_description,
    long_description_content_type='text/plain',
    url='https://gymbob.sourceforge.io',
    author='A S Lewis',
    author_email='aslewis@cpan.org',
#    license=license,
    license="""GPLv3+""",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Games/Entertainment',
        'License :: OSI Approved' \
        + ' :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='gymbob gym workout',
    packages=setuptools.find_packages(
        exclude=('docs', 'icons', 'sounds', 'tests'),
    ),
    include_package_data=True,
    python_requires='>=3.0, <4',
    install_requires=['playsound'],
    scripts=[script_exec],
    project_urls={
        'Bug Reports': 'https://github.com/axcore/gymbob/issues',
        'Source': 'https://github.com/axcore/gymbob',
    },
    data_files=param_list,
)
