import exceptions as _mod_exceptions

__doc__ = 'This module supports asynchronous I/O on multiple file descriptors.\n\n*** IMPORTANT NOTICE ***\nOn Windows and OpenVMS, only sockets are supported; on Unix, all file descriptors.'
__file__ = 'd:\\program files\\python\\python27\\dlls\\select.pyd'
__name__ = 'select'
__package__ = None
class error(_mod_exceptions.Exception):
    __class__ = error
    __dict__ = {}
    def __init__(self):
        'x.__init__(...) initializes x; see help(type(x)) for signature'
        pass
    
    __module__ = 'select'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

def select(rlist, wlist, xlist, timeout=None):
    "select(rlist, wlist, xlist[, timeout]) -> (rlist, wlist, xlist)\n\nWait until one or more file descriptors are ready for some kind of I/O.\nThe first three arguments are sequences of file descriptors to be waited for:\nrlist -- wait until ready for reading\nwlist -- wait until ready for writing\nxlist -- wait for an ``exceptional condition''\nIf only one kind of condition is required, pass [] for the other lists.\nA file descriptor is either a socket or file object, or a small integer\ngotten from a fileno() method call on one of those.\n\nThe optional 4th argument specifies a timeout in seconds; it may be\na floating point number to specify fractions of seconds.  If it is absent\nor None, the call will never time out.\n\nThe return value is a tuple of three lists corresponding to the first three\narguments; each contains the subset of the corresponding file descriptors\nthat are ready.\n\n*** IMPORTANT NOTICE ***\nOn Windows and OpenVMS, only sockets are supported; on Unix, all file\ndescriptors can be used."
    return tuple()

