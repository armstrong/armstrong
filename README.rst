Armstrong
=========
Armstrong is an open-source publishing system designed for news organizations
that gives your team the technology edge it needs to report in a media-rich
environment.

This package is a meta package that loads all of the various components of
Armstrong as independent packages.  Installing this package is the easiest way
to get the full distribution of Armstrong, but is not required to use the
various components of Armstrong.


Getting Started
---------------

Installation
""""""""""""
For the latest released version of Armstrong, use `pip`_ to install it from
`PyPI`_ like this::

    $ pip install armstrong


Development Releases
''''''''''''''''''''
You can track the latest development of Armstrong by installing the development
version from Git.  Obtain the latest version by visiting our `GitHub`_ page and
either cloning or downloading a tarball.

Once obtained, switch into the directory of the repository (or snapshot if a
tarball was downloaded) and tell pip to install it::

    $ git clone git://github.com/armstrongcms/armstrong.git
    ... a few lines of output from Git ...
    $ pip install .

Creating an Armstrong project
"""""""""""""""""""""""""""""
To help get started, the `armstrong.cli`_ component can create a basic project
structure for you.  Create a new project like this::

    $ armstrong init mysite
    armstrong initialized!

Armstrong Project Structure
'''''''''''''''''''''''''''

The following files are created in the ``mysite`` directory::

    |~config/
    | |-defaults.py
    | |-development.py
    | |-__init__.py
    | |-production.py
    | `-urls.py
    |~requirements/
    | |-development.txt
    | `-project.txt
    |~templates/
    | `-index.html
    |-wsgi.py


The ``config`` directory contains your settings and root URLConf for Django.
The ``config.defaults`` module contains all of the base settings that are
common to your environment.  ``config.development`` has settings specific to
your development environment, while ``config.production`` contains all of your
production settings.  ``config.urls`` is configured as the root URL
configuration for your project.

You need to edit the ``config.development`` and ``config.production`` to
configure the database engine you want to use.

All of your requirements are specified inside the two text files in the
``requirements`` directory: ``development.txt`` and ``project.txt``.  You can
use `pip`_ to install the dependencies of your project by providing either file
as an argument to ``pip install -r``.  ``development.txt`` should contain all
of requirements for your development environment and include ``project.txt``.
The ``project.txt`` file should contain all of requirements that you ``have``
to have for your project.

The ``templates`` directory is configured as the base for your project's
templates.  It contains a simple ``index.html`` that is loaded on a request to
``/`` so you can verify that everything is setup correctly.

The ``wsgi.py`` provides a basic WSGI module for running your project.  It is
configured to run using the ``config.development`` settings, so you must adjust
it prior to running in production.

*Note*: You do not have to use the Armstrong project layout.  You can utilize
all of Armstrong's components inside an existing Django project.  These are
here simply to help get you started.


Next Steps
''''''''''
Once you have the project created and configured (remember, you need to setup
your database just like any other Django project), you've got one final step.
You need to install the requirements file as there are packages that Armstrong
relies on that need to be installed from GitHub.

::

    $ cd mysite
    $ pip install -r requirements/project.txt

Once pip has finished, you can test out everything by running ``armstrong
runserver`` from inside your project.  When you load the server, you should
see the welcome page.

Congrats, you're now setup and ready to start developing on Armstrong.


Versions
--------
Armstrong uses date-based versions for this main ``armstrong`` package.  The
current release is ``11.06.beta.1``.  For more information about how versions
are handled in Armstrong, see the `Versions`_ page on the wiki.

.. _Versions: https://github.com/armstrongcms/armstrong/wiki/Versions



Components
----------
Armstrong is broken down into multiple components.  The main ``armstrong``
package installs these individually with each being pinned to a specific
point release.

Included in the 11.06 release are the following components:

``armstrong.cli``
    A command line tool for creating and working with an Armstrong environment.
    You can use this inside an Armstrong environment as a replacement for the
    traditional ``manage.py`` in Django.

    See the `armstrong.cli`_ repository for more information.

``armstrong.core.arm_content``
    Contains the basic elements for Armstrong-style content.  This does not
    provide any concrete implementations of models, instead it includes lower
    level functionality: fields, mixins, and a base ``ContentBase`` for
    creating a shared content model.

    See the `armstrong.core.arm_content`_ repository for more information.

``armstrong.core.arm_sections``
    Provides a system for structuring models into "sections" to be used on the
    site for organizational purposes.

    See the `armstrong.core.arm_sections`_ repository for more information.

``armstrong.core.arm_wells``
    Functionality related to "pinning" content to a particular area.  Wells
    give you the ability to specify any collection of models and their order to
    display in various places throughout the site.

    See the `armstrong.core.arm_wells`_ repository for more information.

``armstrong.apps.articles``
    Simple application for handling basic articles.  This provides a thin layer
    on top of the article-specific features found in the ``arm_content``
    component, but will meet the needs of many newsrooms with simple
    requirements.

    See the `armstrong.apps.articles`_ repository for more information.

``armstrong.apps.content``
    Simple application for providing a concrete ``Content`` model that other
    Django apps can build off of.

    See the `armstrong.apps.content`_ repository for more information.

``armstrong.apps.events``
    An application for creating events and handling RSVPs.

    See the `armstrong.apps.events`_ repository for more information.



Contributing
------------
Start by finding the component of Armstrong that you would like to change.  It
is rare that you will need to start by modifying the main Armstrong repository
to start.

* Create something awesome -- make the code better, add some functionality,
  whatever (this is the hardest part).
* `Fork it`_
* Create a topic branch to house your changes
* Get all of your commits in the new topic branch
* Submit a `pull request`_

.. _Fork it: http://help.github.com/forking/
.. _pull request: http://help.github.com/pull-requests/


State of Project
----------------
Armstrong is an open-source news platform that is freely available to any
organization.  It is the result of a collaboration between the `Texas Tribune`_
and `Bay Citizen`_, and a grant from the `John S. and James L. Knight
Foundation`_.  The first release is scheduled for June, 2011.

To follow development, be sure to join the `Google Group`_.

.. _Bay Citizen: http://www.baycitizen.org/
.. _John S. and James L. Knight Foundation: http://www.knightfoundation.org/
.. _Texas Tribune: http://www.texastribune.org/
.. _Google Group: http://groups.google.com/group/armstrongcms
.. _pip: http://www.pip-installer.org/
.. _PyPI: http://pypi.python.org/pypi
.. _GitHub: http://github.com/armstrongcms/armstrong/
.. _armstrong.cli: http://github.com/armstrongcms/armstrong.cli
.. _armstrong.core.arm_content: http://github.com/armstrongcms/armstrong.core.arm_content
.. _armstrong.core.arm_sections: http://github.com/armstrongcms/armstrong.core.arm_sections
.. _armstrong.core.arm_wells: http://github.com/armstrongcms/armstrong.core.arm_wells
.. _armstrong.apps.articles: http://github.com/armstrongcms/armstrong.apps.articles
.. _armstrong.apps.content: http://github.com/armstrongcms/armstrong.apps.content
.. _armstrong.apps.events: http://github.com/armstrongcms/armstrong.apps.events
