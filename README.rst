===================
Auto-Attribute Dict
===================

An ``aadict`` is a python dict sub-class that allows attribute-style
access to dict items, e.g. ``d.foo`` is equivalent to ``d['foo']``.
``aadict`` also provides a few other helpful methods, such as ``pick``
and ``omit`` methods. Also, an ``aadict`` is more call chaining
friendly (e.g. methods such as `update` return ``self``) and is
pickle'able.

Project
=======

* Homepage: https://github.com/metagriffin/aadict
* Bugs: https://github.com/metagriffin/aadict/issues

TL;DR
=====

Install:

.. code-block:: bash

  $ pip install aadict

Use:

.. code-block:: python

  from aadict import aadict, pick, omit

  # attribute access
  d = aadict(foo='bar', zig=87)
  assert d.foo == d['foo'] == 'bar'

  # helper functions and methods
  assert pick(d, 'foo') == d.pick('foo') == {'foo': 'bar'}
  assert omit(d, 'foo') == d.omit('foo') == {'zig': 87}

  # method chaining
  d2 = aadict(x='y').update(d).omit('zig')
  assert d2.x == 'y' and d2.foo == 'bar' and d2.zig is None


Details
=======

TODO: add documentation
