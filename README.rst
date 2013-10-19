=================================
(Yet Another) Auto-Attribute Dict
=================================

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

  # prefix extraction
  d = {'foo.zig': 'bar', 'foo.zag': 87, 'zig': 'zog'}
  assert pick(d, prefix='foo.')        == {'zig': 'bar', 'zag': 87}
  assert pick(d, 'zig', prefix='foo.') == {'zig': 'bar'}


Details
=======

The aadict module provides the following functionality:


aadict
------

An `aadict` object is basically identical to a `dict` object, with the
exception that attributes, if not reserved for other purposes, map to
the dict's items. For example, if a dict ``d`` has an item ``'foo'``,
then a request for ``d.foo`` will return that item lookup. aadicts
also have several helper methods, for example ``aadict.pick``. If a
dict item is store by that name, then the attribute access does not
work: you need to reference it by item lookup, i.e. ``d['pick']``. The
helper methods are:

* **aadict.pick** instance method:

  Returns a new aadict, reduced to only include the specified
  keys. Example:

  .. code-block:: python

    from aadict import aadict
    d = aadict(foo='bar', zig=87, zag=['a', 'b'])
    assert d.pick('foo', 'zag') == {'foo': 'bar', 'zag': ['a', 'b']}

* **aadict.omit** instance method:

  Identical to the ``aadict.pick`` method, but returns the complement,
  i.e. all of those keys that are *not* specified. Example:

  .. code-block:: python

    from aadict import aadict
    d = aadict(foo='bar', zig=87, zag=['a', 'b'])
    assert d.omit('foo', 'zag') == {'zig': 87}

* **aadict.d2ar** class method:

  Recursively converts the supplied `dict` to an `aadict`, including
  all sub-list and sub-dict types. Due to being recursive, but only
  copying dict-types, this is effectively a hybrid of a shallow and
  a deep clone. Example:

  .. code-block:: python

    from aadict import aadict
    d = aadict.d2ar(dict(foo=dict(bar='zig')))
    assert d.foo.bar == 'zig'

  Without the recursive walking, the ``.bar`` attribute syntax
  would yield an AttributeError exception because d.foo would
  reference a `dict` type, not an `aadict`.

* **aadict.d2a** class method:

  Converts the supplied `dict` to an `aadict`. Example:

  .. code-block:: python

    from aadict import aadict
    d = aadict.d2a(dict(foo='bar'))
    assert d.foo == d['foo'] == 'bar'

  Note that this is identical to just using the constructor,
  but is provided as a symmetry to the ``aadict.d2ar`` class
  method, e.g.:

  .. code-block:: python

    from aadict import aadict
    d = aadict(dict(foo='bar'))
    assert d.foo == d['foo'] == 'bar'


pick
----

A more general-purpose version of the `aadict.pick` method that can
work on any dict type and has a couple of other features. Note that
pick will aggressively return a valid dict, regardless of the supplied
value -- i.e. if ``None`` is given as a source, an empty dict is
returned. Furthermore, pick also has the following additional
functionality via keyword parameters:

* **dict**:

  Specifies the class type that should be returned, which defaults
  to the standard python ``dict`` type. Example:

  .. code-block:: python

    from aadict import pick
    d = pick(dict(foo='bar', zig='zag'), 'foo', dict=aadict)
    assert d == {'foo': 'bar'}
    assert d.foo == 'bar'
    assert isinstance(d, aadict)

* **prefix**:

  Specifies that only keywords that start with the specified string
  will be returned (and also filtered for the specified keys), with
  the prefix stripped from the keys. If no keys are specified, this
  will simply return only the keys with the specified prefix. Example:

  .. code-block:: python

    from aadict import pick
    d = {'foo.zig': 'bar', 'foo.zag': 87, 'zig': 'zog'}
    d2 = pick(d, 'zig', prefix='foo.')
    d3 = pick(d, prefix='foo.')
    assert d2 == {'zig': 'bar'}
    assert d3 == {'zig': 'bar', 'zag': 87}

omit
----

Identical to the `pick` function, but returns the compliment. Example:

.. code-block:: python

  from aadict import aadict, omit
  d = {'foo.zig': 'bar', 'foo.zag': 87, 'zig': 'zog'}
  d2 = omit(d, 'zig', prefix='foo.', dict=aadict)
  assert d2 == {'zag': 87}
  assert d2.zag == 87

