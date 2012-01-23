from datetime import datetime
from distutils.core import setup
import os
import subprocess

if os.path.exists("MANIFEST"):
    os.unlink("MANIFEST")

VERSION = ("11", "12", "0", "1", )

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
        "armstrong.cli>=1.1.0,<1.2",
        "armstrong.core.arm_access>=1.0.3,<1.1",
        "armstrong.core.arm_content>=1.0.0,<1.1",
        "armstrong.core.arm_layout>=1.0.0,<1.1",
        "armstrong.core.arm_sections>=1.0.1,<1.1",
        "armstrong.core.arm_wells>=1.3.1,<1.4",
        "armstrong.apps.articles>=1.1.0,<1.2",
        "armstrong.apps.content>=1.0.1,<1.1",
        "armstrong.apps.images>=1.1.0,<1.2",
        "armstrong.apps.related_content>=1.2.0,<1.3",
        "armstrong.hatband>=1.2.1,<1.3",
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

