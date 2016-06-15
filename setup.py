from distutils.core import setup
import py2exe
import os

old_determine_dll_type = py2exe.dllfinder.DllFinder.determine_dll_type
pack = ("msvcr100.dll",)
def determine_dll_type(self, imagename):
    if os.path.basename(imagename).lower() in pack:
        return "EXT"
    return old_determine_dll_type(self, imagename)
py2exe.dllfinder.DllFinder.determine_dll_type = determine_dll_type
setup(windows=[{"script":"WhoGoesFirst.py"}], options={"py2exe":{"includes":["sip"]}})