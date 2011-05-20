from datetime import datetime
from distutils.core import setup
import os
import subprocess

if os.path.exists("MANIFEST"):
    os.unlink("MANIFEST")

VERSION = ("11", "06", "0", "alpha", "0")

setup(
    name='armstrong',
    version=".".join(VERSION),
    description="Armstrong is an open-source publishing system designed for news organizations that gives your team the technology edge it needs to report in a media-rich environment.",
    long_description=open("README.rst").read(),
    author='Bay Citizen & Texas Tribune',
    author_email='dev@armstrongcms.org',
    url='http://github.com/armstrongcms/armstrong/',
    packages=["armstrong", ],
    namespace_packages=["armstrong", ],
    install_requires=[
        "armstrong.core.arm_content",
        "armstrong.core.arm_sections",
        "armstrong.apps.articles",
        "armstrong.apps.content",
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)

