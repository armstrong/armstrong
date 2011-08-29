from datetime import datetime
from distutils.core import setup
import os
import subprocess

if os.path.exists("MANIFEST"):
    os.unlink("MANIFEST")

VERSION = ("11", "09", "0", "alpha", "2", "alpha", "0")

setup(
    name='armstrong',
    version=".".join(VERSION),
    description="Armstrong is an open-source publishing system designed for news organizations that gives your team the technology edge it needs to report in a media-rich environment.",
    long_description=open("README.rst").read(),
    author='Bay Citizen & Texas Tribune',
    author_email='dev@armstrongcms.org',
    url='http://github.com/armstrong/armstrong/',
    packages=["armstrong", ],
    namespace_packages=["armstrong", ],
    install_requires=[
        "armstrong.cli>=0.6.0",
        "armstrong.core.arm_access>=0.1.1",
        "armstrong.core.arm_content>=0.8.1",
        "armstrong.core.arm_layout>=0.2.0",
        "armstrong.core.arm_sections>=0.3.0",
        "armstrong.core.arm_wells>=0.3.0",
        "armstrong.apps.articles>=0.6.0",
        "armstrong.apps.content>=0.1.0",
        "armstrong.apps.events>=0.1.2,<0.2",
        "armstrong.hatband>=0.4.0",
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)

