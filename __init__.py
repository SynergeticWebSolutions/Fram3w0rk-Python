#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Project: Fram3w0rk Python 0.5 [Alpha]
Website: http://LawtonSoft.com/projects/fram3w0rk
Author: Jonathan Lawton (wanathan101@gmail.com)
Contributors: none, yet :-(  (Come join in!)

Copyright (c) 2012+, LawtonSoft. All rights reserved.

TERMS AND CONDITIONS
Revised: Oct 1, 2013

"Source" includes all files and processes included in previous, current and
future versions of this project except where 3rd party source may also be
included. You must follow the terms and conditions of individual 3rd party
sources as stated by their own accord.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

  * Redistributions of source code must retain the above copyright
    notice, this list of conditions and the following disclaimer.
  * Redistributions in binary form must reproduce the above copyright
    notice, this list of conditions and the following disclaimer in the
    documentation and/or other materials provided with the distribution.
  * Neither the name of Jonathan Lawton nor the names of its
    contributors may be used to endorse or promote products derived from
    this software without specific prior written permission.
  * These Terms and Conditions may change at any time without given
    notice at which point these will become replaced and inherited by the
    newest copy included in the source or at:
    [http:#www.fram3w0rk.com/software/terms/].


WARRANTY
This software is provided by the copyright holders and contributors "as is" and
any express or implied warranties, including, but not limited to, the implied
warranties of merchantability and fitness for a particular purpose are
disclaimed. In no event shall the copyright owner or contributors of this
Source be liable for any direct, indirect, incidental, special, exemplary, or
consequential damages (including, but not limited to, procurement of substitute
goods or services; loss of use, data, or profits; or business interruption)
however caused and on any theory of liability, whether in contract, strict
liability, or tort (including negligence or otherwise) arising in any way out
of the use of this software, even if advised of the possibility of such damage.

3rd party sources must be treated separately. Source used within the project
but owned separately is void of this project and provided "as is" with
attribution.

*******************************************************************************

Now that we're past all the boring stuff...

Welcome to Fram3w0rk! Fram3w0rk is an open-source framework designed to connect
and unify code across programming languages, making it easier to learn, retain,
and code.

Fram3w0rk Python is the respective Python framework for building Python
applications.

******************************************************************************
"""

import inspect, os, sys

# Create instances for classes
class Instance:
  # -- INITIATE FRAM3W0RK --
  @staticmethod
  def initiate():
    #from os import path
    pwd = os.path.dirname(os.path.abspath(__file__))
    
    # Included file paths
    sys.path.append(pwd)
    
    
    Instance.imports = ['dbi'] #['logging', 'dbi', 'session']
    
    Instance.load()
    
  
  # -- LOAD FILES --
  # Use the following list to include additional classes
  imports = []
  
  @staticmethod
  def load(*args):
    args = list(args)
    if(Instance.imports is not None):
      for file in Instance.imports:
        exec('import ' + file)
        exec('Instance.' + file + ' = ' + file + '.' + file + '()')
  
  # -- INSTANCES --
  __constructor = []
  
  @staticmethod
  def get(className = None, id = 0):
    if(eval(className).__instance[id] is None):
      exec(className + '.__instance[' + id + '] =' + className + '(' + __constructor + ')')
      return eval(className + '.__instance[id]')
    else:
      return eval(className + '.__instance[' + id + ']')

# Initiate Fram3w0rk
#Instance.initiate()
#dbi = Instance.get('dbi')
#from dbi import dbi
#className = dbi()
#className.connect()
#id = 0
#if(dbi.__instance[id] is None):
#  dbi.__instance[id] = Instance.className(__constructor)
#  print dbi.__instance[id]
#else:
#  print dbi.__instance[id]
