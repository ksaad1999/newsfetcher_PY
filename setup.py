"""
    Written by Karim Saad 2018
    Installs dependencies - just run it, if you don't sure, if you have all dependencies
"""

# pip install case
def CheckModule(x):
    from subprocess import Popen, PIPE
    p = Popen(['pip', 'install', x], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, err = p.communicate()
    rc = p.returncode
    return [output.decode('utf-8'), err.decode('utf-8')]


CheckModule("feedparser")
CheckModule("feedparser")
