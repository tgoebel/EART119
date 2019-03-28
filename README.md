# EART119
@author tgoebel - thw.goebel@gmail.com

py scipts for EART119 - Intro to Scientific Computing

This repository contains some  python codes that were developed in class (Scientific Computing).
Many examples are taken from:  HP Langtangen, (2014) A primer on scientific programming with python, 
https://hplgit.github.io/primer.html/doc/pub/half/book.pdf, in addition to my own examples.

additional resources to get started in python are:
https://www.greenteapress.com/thinkpython/thinkpython.pdf

and think stats (with python):
http://www.greenteapress.com/thinkstats/

- Some comments on using python3.6 on a UCSC windows desktop:
you have access to the same python installtion and modules everywhere on campus (including library computers)

- Here is where the interpreter lives under windows:
C:\Programs\Python36>python.exe

- SETTING PYTHON INTERPRETER FOR PYCHARM:
The first time a user launches PyCharm they will need to configure it for a Python interpreter. Using Virtual Environments is the best way to do this and to deal with multiple Python versions. Steps to create a Python Virtual Environment are below. 

1. Launch PyCharm
2. At the Welcome to Python dialog ("Open a project", etc), at the bottom right, click on the drop down menu "Configure"
3. Select "Settings"
4. Select "Project Interpreter"
5. In the window pane on the right, click on "Project Interpreter" and create a new Virtual Environment.
6. Click on the "+" and select "Create VirtualEnv"
7. In the VirtualEnv box:
	Name:  Python36 VirtualEnv
	Location:  X:\PyCharmCE
	Base Interpreter:  "C:\Programs\Python36\python.exe"

When PyCharm starts it will take a couple minutes to create index files of all the installed Python packages. These and other configuration settings will be saved in the directory "X:\PyCharmCE" which will be created in the Home Directory. 
