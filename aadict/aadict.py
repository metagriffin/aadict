# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# file: $Id$
# auth: metagriffin <metagriffin@uberdev.org>
# date: 2013/10/19
# copy: (C) CopyLoose 2013 UberDev <hardcore@uberdev.org>, No Rights Reserved.
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
class aadict(dict):
  '''
  A dict subclass that allows attribute access to be synonymous with
  item access, e.g. ``mydict.attribute == mydict['attribute']``. It
  also provides several other useful helper methods, such as
  :meth:`pick` and :meth:`omit`.
  '''
  def __getattr__(self, key):
    if key.startswith('__') and key.endswith('__'):
      # note: allows an aadict to be pickled with protocols 0, 1, and 2
      #       which treat the following specially:
      #         __getstate__, __setstate__, __slots__, __getnewargs__
      return dict.__getattr__(self, key)
    return self.get(key, None)
  def __setattr__(self, key, value):
    self[key] = value
    return self
  def __delattr__(self, key):
    if key in self:
      del self[key]
    return self
  def update(self, *args, **kw):
    args = [e for e in args if e]
    dict.update(self, *args, **kw)
    return self
  def pick(self, *args):
    return aadict({k: v for k, v in self.iteritems() if k in args})
  def omit(self, *args):
    return aadict({k: v for k, v in self.iteritems() if k not in args})
  @staticmethod
  def __dict2aadict__(subject, recursive=False):
    if isinstance(subject, list):
      if not recursive:
        return subject
      return [aadict.__dict2aadict__(val, True) for val in subject]
    if not isinstance(subject, dict):
      return subject
    ret = aadict(subject)
    if not recursive:
      return ret
    for key, val in ret.items():
      ret[key] = aadict.__dict2aadict__(val, True)
    return ret
  @staticmethod
  def d2ar(subject):
    return aadict.__dict2aadict__(subject, True)
  @staticmethod
  def d2a(subject):
    return aadict.__dict2aadict__(subject, False)

#------------------------------------------------------------------------------
# end of $Id$
#------------------------------------------------------------------------------
