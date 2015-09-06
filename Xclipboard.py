from tkinter import Tk
__all__=['copy','paste','clear']

__author__='Calvin(Martin)Adyezik  adyezik@gmail.com'

__doc__="""simple Module to work with clipboard based on tkinter -Python 3"""

__name__='Xclipboard'


def copy(text):
    """copy text to clipboard """
    try:
        root=Tk()
        root.withdraw()
        root.clipboard_append(text)
    except Exception as e:
        print ('Error: ',e)
    finally:
        root.destroy()

    
def paste():
    """paste text from clipboad"""
    try:
        root=Tk()
        root.withdraw()
        return root.clipboard_get()
    except Exception as e:
        print ('Error: ',e)
    finally:
        root.destroy()


def clear():
    """clear clipboard"""
    try:
        root=Tk()
        root.withdraw()
        root.clipboard_clear()
    except Exception as e:
        print ('Error: ',e)
    finally:
        root.destroy()
    
