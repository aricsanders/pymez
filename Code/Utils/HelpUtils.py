#-----------------------------------------------------------------------------
# Name:        HelpUtils
# Purpose:    Provides general utilities for help based functions
# Author:      Aric Sanders
# Created:     3/11/2016
# License:     MIT License
#-----------------------------------------------------------------------------
""" The HelpUtils module has tools for interacting with help files. It uses pdoc for
  auto-generated help"""
#-----------------------------------------------------------------------------
# Standard Imports
import os
import inspect
#-----------------------------------------------------------------------------
# Third Party Imports
try:
    import pdoc
except:
    print("Could not import pdoc, add it to the python path or install it. pip install pdoc")
try:
    from pyMeasure.Code.Utils.Alias import *
    METHOD_ALIASES=1
except:
    print("The module pyMeasure.Code.Utils.Alias was not found")
    METHOD_ALIASES=0
    pass
try:
    from pyMeasure.Code.Utils.Names import auto_name
    DEFAULT_FILE_NAME=None
except:
    print("The function auto_name in pyMeasure.Code.Utils.Names was not found")
    print("Setting Default file name to New_Data_Table.txt")
    DEFAULT_FILE_NAME='New_Data_Table.txt'
    pass
#-----------------------------------------------------------------------------
# Module Constants
TESTS_DIRECTORY=os.path.join(os.path.dirname(os.path.realpath(__file__)),'Tests')
#-----------------------------------------------------------------------------
# Module Functions
def return_help(object):
    """Returns an html help page autogenerated by the pdoc module for any live object"""
    module=inspect.getmodule(object).__name__
    html_text=pdoc.html(module_name=module,allsubmodules=True)
    return html_text

def create_help_page(module,output_format='html',file_path=None):
    """Uses the pdoc module to create a html autogenerated help file for the specified module.
    If file_path is not specified it auto names it and saves it in the current working directory."""
    if re.search('htm',output_format,re.IGNORECASE):
        html_text=pdoc.html(module_name=module,allsubmodules=True)
        if file_path is None:
            file_path=auto_name(module.replace('.','_'),'Help',directory=None,extension='html')
        out_file=open(file_path,'w')
        out_file.write(html_text)
        out_file.close()


def create_examples_page(ipynb_path):
    """Given a jupyter notebook uses nbconvert to output an html file at the specified path."""
    os.system("jupyter nbconvert --to html %s"%ipynb_path)


#-----------------------------------------------------------------------------
# Module Classes

#-----------------------------------------------------------------------------
# Module Scripts
def test_create_help_page(module='pyMeasure.Code.DataHandlers.GeneralModels'):
    "Tests the create help page function, it seems pretty slow"
    os.chdir(TESTS_DIRECTORY)
    create_help_page(module)
def test_create_examples_page(ipynb_path='Development_Stack_Installation_Example_20160130_01.ipynb'):
    """Tests the create_examples_page function, really nb convert on the command line"""
    os.chdir(TESTS_DIRECTORY)
    create_examples_page(ipynb_path)
#-----------------------------------------------------------------------------
# Module Runner
if __name__ == '__main__':
    #test_create_help_page()
    #test_create_help_page('pyMeasure')
    #test_create_help_page('pyMeasure.Code.DataHandlers.NISTModels')
    test_create_help_page('pyMeasure.Code.DataHandlers.NISTModels')
    #test_create_examples_page()
