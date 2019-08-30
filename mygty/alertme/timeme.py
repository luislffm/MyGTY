# -*- coding: utf-8 -*-
"""timeme


June 24th, 2018
Edmonton, AB
Canada

@author: luisflavio
"""

# --- Dependencies
import time, os


class timeme:
    """
    The following class is an atempt to make the timing of how long a pythonic code
    block takes to be processed. 
    
    Usage
    -----
    from mygty.alertme import timeme
    With timeme("Foo"):
        bar
    
    """

    def __init__(self, name=None):
        """ timeme constructor 
        
        Parameters
        ----------
        name : str
            The timeme's name. Usually caries the reason why the timeme was created.
        
        """
        self.name = name

    def __enter__(self):
        """
        Entering the timeme we start the stopwatch
        """
        self.start_time = time.time()

    def __exit__(self, type, value, traceback):
        """
        Exeting the timeme we stop the stopwatch and print it
        """
        self.end_time = time.time() - self.start_time
        if self.name:
            print("[%s]" % (self.name))
        print("Elapsed: %.2f seconds" % (self.end_time))
        os.system('say "%s has finished."' % (self.name))

