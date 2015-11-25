#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys, sqlite3

pwd = os.path.dirname(os.path.abspath(__file__)) + '/'

# Included file paths
sys.path.append(pwd)
sys.path.append(os.path.join(pwd, 'mysql-connector-python-1.0.12/python2'))

import mysql.connector


# Connection, query execution, and SQL error handling class
class dbi:
  __instance = None
  # Database credentials
  __defaults = {}
  __defaults['host'] = None
  __defaults['user'] = None
  __defaults['password'] = None
  __defaults['database'] = None
  
  #@staticmethod
  def setDefaults(self, **kwargs):
    if kwargs.get('host', None):
      self.__defaults["host"] = kwargs['host']
    if kwargs.get('user', None):
      self.__defaults["user"] = kwargs['user']
    if kwargs.get('password', None):
      self.__defaults["password"] = kwargs['password']
    if kwargs.get('database', None):
      self.__defaults["database"] = kwargs['database']
  
  def __init__(self, type='mysql'):
    # Query strings
    self.queries = None
    self.query = None  
    self.result = {}
    self.result['dict'] = []
    self.result['keys'] = []
    self.result['list'] = []
    self.result['tuple'] = []
    
    self.__type = type
    self.__connection = []
  
  def connect(self, **kwargs):
    kwargs = dict(kwargs.items() + dict((key, default) for (key, default) in self.__defaults.iteritems() if key not in kwargs.keys()).items())
    if self.__type == 'mysql':
      self.__connection = mysql.connector.connect(**kwargs)
    elif self.__type == 'sqlite':
      self.__connection = sqlite3.connect(kwargs['host'])
      self.__connection.text_factory = str
  
  def execute(self, query, **args):
    self.result['dict'] = []
    self.result['keys'] = []
    self.result['list'] = []
    self.result['tuple'] = []
    cursor = self.__connection.cursor()
    if self.__type == 'mysql':
      cursor.execute(query)
    elif self.__type == 'sqlite':
      cursor.execute(query, **args)
    
    for row in cursor:
      columns = tuple([d[0].decode('utf-8') for d in cursor.description])
      self.result['dict'].append(dict(zip(columns, row)))
      self.result['keys'] = list(columns)
      self.result['list'].append(list(row))
      self.result['tuple'].append(row)
    cursor.close()
    return self.result
  
  def executeBatch(self, queries, *args, **kwargs):
    if self.__type == 'mysql':
      self.queries = re.split(r'#(?<!(\\\\))\;[\n\s\t]*#', query)
      results = []
      for query in self.queries:
        if(trim(query) != '' and trim(query) != ';'):
          results.append(self.execute(query))
      return results
    elif self.__type == 'sqlite':
      cursor = self.__connection.cursor()
      cursor.executemany(queries, *args, **kwargs)
      cursor.close()
  
  def disconnect(self):
    self.__connection.close()
