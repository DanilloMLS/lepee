#!/usr/bin/python
# -*- encoding: iso-8859-1 -*-

from distutils.core import setup
import py2exe
import os

Mydata_files = []
for files in os.listdir('icons\\'):
     f1 = 'icons\\' + files
     
     if os.path.isfile(f1): # skip directories
           f2 = 'icons', [f1]
           print f2
           Mydata_files.append(f2)

setup(windows=[{"script":"tela_intro.pyw "}],
     name="L'Épée",
     version="1.5.0",
     description="Auxíliar na aquisição de Libras como primeira linguagem compreesiva",
     author="Fagner Luiz",
     author_email ="fagnerluizbarros@gmail.com",
     
     data_files = Mydata_files,        
     options={"py2exe":{"includes":["sip"]}}
     
)

