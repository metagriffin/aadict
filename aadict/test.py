# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# file: $Id$
# auth: metagriffin <mg.github@uberdev.org>
# date: 2013/10/19
# copy: (C) Copyright 2013-EOT metagriffin -- see LICENSE.txt
#------------------------------------------------------------------------------
# This software is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This software is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see http://www.gnu.org/licenses/.
#------------------------------------------------------------------------------

import unittest, pickle

from .aadict import aadict
from .helpers import pick, omit

#------------------------------------------------------------------------------
class TestAadict(unittest.TestCase):

  #----------------------------------------------------------------------------
  def test_aadict_base(self):
    d = aadict(foo='bar', zig=87)
    self.assertEqual(d.foo, 'bar')
    self.assertEqual(d['foo'], 'bar')

  #----------------------------------------------------------------------------
  def test_helpers_pick(self):
    d = aadict(foo='bar', zig=87)
    self.assertEqual(pick(d, 'foo'), {'foo': 'bar'})
    self.assertEqual(pick(d, 'foo', dict=aadict), {'foo': 'bar'})
    self.assertEqual(d.pick('foo'), {'foo': 'bar'})
    self.assertIsInstance(pick(d, 'foo'), dict)
    self.assertNotIsInstance(pick(d, 'foo'), aadict)
    self.assertIsInstance(pick(d, 'foo', dict=aadict), aadict)
    self.assertIsInstance(d.pick('foo'), dict)
    self.assertIsInstance(d.pick('foo'), aadict)

  #----------------------------------------------------------------------------
  def test_helpers_omit(self):
    d = aadict(foo='bar', zig=87)
    self.assertEqual(omit(d, 'foo'), {'zig': 87})
    self.assertEqual(d.omit('foo'), {'zig': 87})

  #----------------------------------------------------------------------------
  def test_aadict_chaining(self):
    d = aadict(foo='bar', zig=87)
    d2 = aadict(x='y').update(d).omit('zig')
    self.assertEqual(d2.x, 'y')
    self.assertEqual(d2.foo, 'bar')
    self.assertIsNone(d2.zig)

  #----------------------------------------------------------------------------
  def test_aadict_convert(self):
    d = aadict.d2ar(dict(foo=dict(bar='zig')))
    self.assertEqual(d.foo.bar, 'zig')
    d = aadict.d2a(dict(foo=dict(bar='zig')))
    with self.assertRaises(AttributeError):
      zig = d.foo.bar
      self.fail('AttributeError should have been raised')

  #----------------------------------------------------------------------------
  def test_aadict_pickle(self):
    d = aadict(foo='bar', zig=87)
    d2 = pickle.loads(pickle.dumps(d))
    self.assertTrue(isinstance(d2, aadict))
    self.assertEqual(d2, d)
    self.assertEqual(d2['foo'], 'bar')
    self.assertEqual(d2.foo, 'bar')

#------------------------------------------------------------------------------
# end of $Id$
#------------------------------------------------------------------------------
