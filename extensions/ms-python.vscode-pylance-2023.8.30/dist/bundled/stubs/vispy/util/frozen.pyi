# -*- coding: utf-8 -*-
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

# Class adapted from:
# http://stackoverflow.com/questions/3603502/

class Frozen(object):
    __isfrozen: bool = ...

    def __setattr__(self, key, value): ...
    def freeze(self): ...
    def unfreeze(self): ...