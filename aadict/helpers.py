# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# file: $Id$
# auth: metagriffin <metagriffin@uberdev.org>
# date: 2013/10/19
# copy: (C) CopyLoose 2013 UberDev <hardcore@uberdev.org>, No Rights Reserved.
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
def pick(source, *keys, **kw):
  '''
  Given a `source` dict or object, returns a new dict that contains a
  subset of keys (each key is a separate positional argument) and/or
  where each key is a string and has the specified `prefix`, specified
  as a keyword argument. Also accepts the optional keyword argument
  `dict` which must be a dict-like class that will be used to
  instantiate the returned object. Note that if `source` is an object
  without an `items()` iterator, then the selected keys will be
  extracted as attributes. The `prefix` keyword only works with
  dict-like objects.
  '''
  rettype = kw.pop('dict', dict)
  prefix = kw.pop('prefix', None)
  if kw:
    raise ValueError('invalid pick keyword arguments: %r' % (kw.keys(),))
  if not source:
    return rettype()
  if prefix is not None:
    source = {k[len(prefix):]: v
              for k, v in source.items()
              if getattr(k, 'startswith', lambda x: False)(prefix)}
  if len(keys) <= 0:
    return rettype(source)
  try:
    return rettype({k: v for k, v in source.items() if k in keys})
  except AttributeError:
    return rettype({k: getattr(source, k) for k in keys if hasattr(source, k)})

#------------------------------------------------------------------------------
def omit(source, *keys, **kw):
  '''
  Identical to the :func:`pick` function, but returns the complement.
  '''
  rettype = kw.pop('dict', dict)
  prefix = kw.pop('prefix', None)
  if kw:
    raise ValueError('invalid omit keyword arguments: %r' % (kw.keys(),))
  if not source:
    return rettype()
  if prefix is not None:
    source = {k[len(prefix):]: v
              for k, v in source.items()
              if getattr(k, 'startswith', lambda x: False)(prefix)}
  if len(keys) <= 0:
    return rettype()
  try:
    return rettype({k: v for k, v in source.items() if k not in keys})
  except AttributeError:
    return rettype({k: getattr(source, k) for k in iter(source) if k not in keys})

#------------------------------------------------------------------------------
# end of $Id$
#------------------------------------------------------------------------------
