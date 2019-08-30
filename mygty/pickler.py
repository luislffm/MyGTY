# -*- coding: utf-8 -*-
"""pickler
Deals with pickling.

April 4th, 2018
Edmonton, AB
Canada

@author: luisflavio
"""

# --- Dependencies
import pickle as p

from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename


def pickle(to_be_pickled, pickle_path, extension=".pickle"):
    """Pickle given objects at the path specified.
    
    
    """
    p.dump(to_be_pickled, open(pickle_path + extension, "wb"))


def pickle_gui(to_be_pickled, extension=".pickle"):
    """ Uses gui for learning path where object will be pickled.
    
    """
    pickle(to_be_pickled, asksaveasfilename(), extension)


def save(to_be_saved, extension="pickle"):
    """ Saves object to a path chosen by gui.
    
    This is an alias for pickle_gui; for more info, see such method's documentation.
    
    """
    pickle_gui(to_be_saved, extension)


def unpickle(pickle_path):
    """Unpickle from given path.
    
    
    """
    return p.load(open(pickle_path, "rb"))


def unpickle_gui():
    """ Uses gui for learning path for file to be unpickled.
    
    """
    return unpickle(askopenfilename())


def load():
    """ Loads object from path chosen with gui.
    
    This is an alias for unpickle_gui; for more info, see such method's documentation.
    
    """
    return unpickle_gui()
