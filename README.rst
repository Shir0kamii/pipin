Pipin
=====

.. image:: https://media.giphy.com/media/l2Sqir5ZxfoS27EvS/giphy.gif

Pin packages in your requirements files with versions from your environment.

I want to get it!
-----------------

Okay, then please use pip to do so::

    pip install pipin-req

Yeah, pipin was already taken, so sad. :(

How do I use it?
----------------

Pipin is meant to be used from the command line. Just pass it the requirement
file in which you want to pin versions::

    pipin requirements.txt

It also works with multiple filenames::

    pipin requirements/docs.txt requirements/tests.txt

For each package it encounters that doesn't have a pinned version, pipin will
search in your python environment for that package. If it find a matching
package, its version will be used.

Why should I use it?
--------------------

My use case was templating. When I create a project, I have a bunch of
unpinned dependencies (as I want to begin a project with latest versions).
I made this project to pin their versions once my virtualenv is setup.

Why the name pipin?
-------------------

It's the contraction of *pip* and *pin*. A simple word play!
