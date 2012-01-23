Armstrong
=========
Armstrong is an open-source publishing system designed for news organizations
that gives your team the technology edge it needs to report in a media-rich
environment.

This package is a meta package that loads all of the various components of
Armstrong.  Installing this package is the easiest way to get the full
distribution of Armstrong, but is not required to use the various components of
Armstrong.


Getting Started
---------------

Installation
""""""""""""
For the latest released version of Armstrong, use `pip`_ to install it from
`PyPI`_ like this::

    $ pip install armstrong

The latest release is ``11.09.0.alpha.1``.  This is *alpha* software, so please
keep that in mind while developing on it.  While we are making every effort to
maintain backwards compatibility between releases while in alpha, things may
change in ways that break your code.

Note on ``virtualenv``
''''''''''''''''''''''
We recommend that you use `virtualenv`_ to isolate Armstrong.  We highly
recommend that you use the ``--distribute`` flag when creating a virtual
environment, as that's what we use for testing.  Your results with traditional
setuptools may vary.


Development Releases
''''''''''''''''''''
You can track the latest development of Armstrong by installing the development
version from Git.  Obtain the latest version by visiting our `GitHub`_ page and
either cloning or downloading a tarball.

Once obtained, switch into the directory of the repository (or snapshot if a
tarball was downloaded) and tell pip to install it::

    $ git clone git://github.com/armstrong/armstrong.git
    ... a few lines of output from Git ...
    $ cd armstrong
    $ pip install .


Creating an Armstrong project
"""""""""""""""""""""""""""""
To help get started, the `armstrong.cli`_ component can create a basic project
structure for you.  Create a new project like this::

    $ armstrong init mysite
    armstrong initialized!

You can initialize a project using the ``--template=demo`` parameter to
initialize with a demo SQLite3 database already set up.  This provides a
working example of how you can use Armstrong.


Armstrong Project Structure
'''''''''''''''''''''''''''

The following files are created in the ``mysite`` directory::

    |~fixtures/
    | |-initial_data.json
    |~requirements/
    | |-development.txt
    | `-project.txt
    |~settings/
    | |-__init__.py
    | |-defaults.py
    | |-development.py
    | `-production.py
    |~templates/
    | `-index.html
    |~urls/
    | |-__init__.py
    | |-defaults.py
    | |-development.py
    | `-production.py
    |-wsgi.py


The ``settings`` directory contains your Django settings.  The
``settings.defaults`` module contains all of the base settings that are common
to your environment.  ``settings.development`` has settings specific to your
development environment, while ``settings.production`` contains all of your
production settings.  

You need to edit the ``settings.development`` and ``settings.production`` to
configure the database engine you want to use.

You can also use the ``settings.local_development`` and
``settings.local_production`` modules to store values that are specific to a
particular box.  You shouldn't include these files in your
repository---anything that should be shared should go in the appropriate
settings module.

``settings.development`` and ``settings.production`` configure you
``ROOT_URLCONF`` as either ``urls.development`` or ``urls.production``,
respectively.  Like their ``settings.*`` counterparts, you can use these for
environment-specific settings while storing all of your default values in
``urls.defaults``.

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

The ``wsgi.py`` file provides a basic WSGI module for running your project.  It
is configured to run using the ``settings.development`` settings, so you must
adjust it prior to running in production.

*Note*: You do not have to use the Armstrong project layout.  You can utilize
all of Armstrong's components inside an existing Django project.  These are
here simply to help get you started.


Next Steps
''''''''''
Once you have the project created and configured (remember, you need to setup
your database just like any other Django project), you've got two final steps.
First, you need to install the requirements file as there are packages that
Armstrong relies on that need to be installed from GitHub.

::

    $ cd mysite
    $ pip install -r requirements/project.txt

After you've configured the database engine and installed the base
requirements, you're last step is to create the database .  You run ``armstrong
syncdb`` which initial the database based on the apps listed in your
``INSTALLED_APPS`` setting.  After this runs, you will have a database created
by Django (for more information on ``syncdb``, see the `Django docs`_).

.. _Django docs: https://docs.djangoproject.com/en/1.3/ref/django-admin/#django-admin-syncdb

Finally, now that you have all of the dependencies installed and have a
database, you can test everything out by running ``armstrong runserver`` from
inside your project.  By default, it listens to the ``localhost`` on port
``8000``.  Loading that up should either give you the ``Welcome to Armstrong!``
page or the demo site, depending on whether you used the ``--template=demo``
flag when called ``armstrong init``.

Congrats, you're now setup and ready to start developing on Armstrong.


Versions
--------
Armstrong uses date-based versions for this main ``armstrong`` package.  The
current release is ``11.09.0.alpha.1``.  For more information about how
versions are handled in Armstrong, see the `Versions`_ page on the wiki.

.. _Versions: https://github.com/armstrong/armstrong/wiki/Versions


Changelog
---------

``11.12.0``
    This updates the various packages to their current release.

    *Armstrong Hatband*
        We've updated the wells interface inside Hatband to make it more
        accessible.

    *Armstrong Images*
        We now include an ``ImageSet`` for dealing with, as you might have
        guessed it, sets of ``Image`` models.  Thanks for @pizzapanther at
        Mouth Watering Media for the contribution.

    *Improved Related Content*
        We've added better handling of Related Content, a new admin, and new
        helper fields for dealing with both sides of a related content
        relationship.

    *Armstrong CLI*
        We've removed the ``--demo`` flag in favor of ``--template=demo``
        which provides more flexbility going forward.


``11.09.0``
    This updates the various packages to their current release.  In addition,
    it adds ``armstrong.hatband`` and ``armstrong.core.arm_layout`` to the
    mix.

    *Armstrong Hatband*
        Every good hat needs a hatband.  Armstrong's Hatband app is the
        foundation for our enhancements to Django's built-in admin interface.
        We've got lots planned for it, but there are a couple of things worth
        calling out specifically.

        *Integration with VisualSearch*
            Wells now have a much better UI thanks `VisualSearch`_.  This new
            UI allows you to quickly search through all of your models when
            attaching a new ``Node`` to a ``Well``.

        *Rich Text Editor*
            We've added a new ``RichTextWidget`` that allows you to easily
            configure the rich-text editor of your choice and have all of the
            admin fields across Armstrong switch to using it.  We're shipping
            with `CKEditor`_ support built-in.

    *New Demo Data*
        Now you can include the ``--demo`` parameter to ``armstrong init`` to
        use our demo database.  This includes lorem ipsum articles and some
        default sections.

    *New Layout Code*
        ``armstrong.core.arm_layout`` introduces the ``{% render_model %}``
        template tag which handles switching the template used for rendering
        models.

    *Backwards Incompatible Changes*
        * ``armstrong.core.arm_wells`` had all of its display logic moved to
          the new ``armstrong.core.arm_layout`` app.
        * We've removed ``primary_section`` from ``ContentBase``

``11.06.0``
    The first generally available release of Armstrong.  It is an unstable,
    developer preview.


Components
----------
Armstrong is broken down into multiple components.  The main ``armstrong``
package installs these individually with each being pinned to a specific
point release.

Included in the 11.09 release are the following components:

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

``armstrong.core.arm_layout``
    Contains helpers for managing the display of data in the context of its
    current layout.

    See the `armstrong.core.arm_layout`_ repository for more information.

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

``armstrong.hatband``
    Armstrong's enhanced version of Django's built-in ``django.contrib.admin``
    application.

    See the `armstrong.hatband`_ repository for more information.


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
organization.  It is the result of a collaboration between the `The Texas Tribune`_
and `The Bay Citizen`_, and a grant from the `John S. and James L. Knight
Foundation`_.

To follow development, be sure to join the `Google Group`_.

.. _The Bay Citizen: http://www.baycitizen.org/
.. _John S. and James L. Knight Foundation: http://www.knightfoundation.org/
.. _The Texas Tribune: http://www.texastribune.org/
.. _Google Group: http://groups.google.com/group/armstrongcms
.. _pip: http://www.pip-installer.org/
.. _PyPI: http://pypi.python.org/pypi
.. _GitHub: http://github.com/armstrong/armstrong/
.. _armstrong.cli: http://github.com/armstrong/armstrong.cli
.. _armstrong.core.arm_content: http://github.com/armstrong/armstrong.core.arm_content
.. _armstrong.core.arm_layout: http://github.com/armstrong/armstrong.core.arm_layout
.. _armstrong.core.arm_sections: http://github.com/armstrong/armstrong.core.arm_sections
.. _armstrong.core.arm_wells: http://github.com/armstrong/armstrong.core.arm_wells
.. _armstrong.apps.articles: http://github.com/armstrong/armstrong.apps.articles
.. _armstrong.apps.content: http://github.com/armstrong/armstrong.apps.content
.. _armstrong.apps.events: http://github.com/armstrong/armstrong.apps.events
.. _armstrong.hatband: http://github.com/armstrong/armstrong.hatband
.. _CKEditor: http://ckeditor.com/
.. _virtualenv: http://www.virtualenv.org/en/latest/index.html
.. _VisualSearch: http://documentcloud.github.com/visualsearch/
.. _distribute: http://pypi.python.org/pypi/distribute
