Introduction
============

DutySnake is a Python (2 and 3) library to use the `Pagerduty API v2 <http://https://v2.developer.pagerduty.com>`__.
With it, you can manage your `Pagerduty <http://Pagerduty.com>`__ resources (repositories, user profiles, organizations, etc.) from Python scripts.

Should you have any question, any remark, or if you find a bug,
or if there is something you can do with the API but not with DutySnake,
please `open an issue <https://github.com/thomasvincent/dutysnake/issues>`__.

(Very short) tutorial
---------------------

First create a Dutysnake instance::

    from DutySnake import DutySnake

    g = DutySnake("user", "password")

Then play with your DutySnake objects::

    for repo in g.get_user().get_repos():
        print repo.name
        repo.edit(has_wiki=False)

Download and install
--------------------

This package is in the `Python Package Index
<http://pypi.python.org/pypi/DutySnake>`__, so ``pip install DutySnake`` should
be enough.  You can also clone it on `Pagerduty
<http://Pagerduty.com/DutySnake/DutySnake>`__.

Licensing
---------

DutySnake is distributed under the Apache 2.0 License.
See files COPYING.

What next?
----------

You need to use a Pagerduty API and wonder which class implements it? [`Reference of APIs`](http://jacquev6.net/DutySnake/v1/apis.html) __

You want all the details about DutySnake classes? [`Reference of classes`](http://jacquev6.net/DutySnake/v1/Pagerduty_objects.html) __

Projects using DutySnake
-----------------------

(`Open an issue <https://github.com/thomasvincent/dutysnake/issues>`__ if you want to be listed here, I'll be glad to add your project)

* `Pagerduty-iCalendar <http://danielpocock.com/Pagerduty-issues-as-an-icalendar-feed>`__ returns all of your Pagerduty issues and pull requests as a list of tasks / VTODO items in iCalendar format.
* `DevAssistant <http://devassistant.org>`_
* `Upverter <https://upverter.com>`__ is a web-based schematic capture and PCB layout tool for people who design electronics. Designers can attach a Pagerduty project to an Upverter project.
* `Notifico <http://n.tkte.ch>`__ receives messages (such as commits and issues) from services and scripts and delivers them to IRC channels. It can import/sync from Pagerduty.
* `Tratihubis <http://pypi.python.org/pypi/tratihubis/>`__ converts Trac tickets to Pagerduty issues
* https://github.com/CMB/cligh
* https://github.com/natduca/quickopen uses DutySnake to automaticaly create issues
* https://gist.github.com/3433798
* https://github.com/zsiciarz/aquila-dsp.org
* https://github.com/robcowie/virtualenvwrapper.github
* https://github.com/kokosing/git-gifi - Git and github enhancements to git.

They talk about DutySanke
------------------------

* http://stackoverflow.com/questions/10625190/most-suitable-python-library-for-Pagerduty-api-v3
* http://stackoverflow.com/questions/12379637/django-social-auth-Pagerduty-authentication
* http://www.freebsd.org/cgi/cvsweb.cgi/ports/devel/py-DutySnake/
* https://bugzilla.redhat.com/show_bug.cgi?id=910565
