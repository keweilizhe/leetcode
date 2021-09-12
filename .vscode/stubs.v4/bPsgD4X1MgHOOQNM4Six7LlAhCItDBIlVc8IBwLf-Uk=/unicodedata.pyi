import __builtin__ as _mod___builtin__

class UCD(_mod___builtin__.object):
    __class__ = UCD
    def __getattribute__(self):
        "x.__getattribute__('name') <==> x.name"
        pass
    
    def __init__(self):
        'x.__init__(...) initializes x; see help(type(x)) for signature'
        pass
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def bidirectional(self, unichr):
        'bidirectional(unichr)\n\nReturns the bidirectional class assigned to the Unicode character\nunichr as string. If no such value is defined, an empty string is\nreturned.'
        pass
    
    def category(self, unichr):
        'category(unichr)\n\nReturns the general category assigned to the Unicode character\nunichr as string.'
        pass
    
    def combining(self, unichr):
        'combining(unichr)\n\nReturns the canonical combining class assigned to the Unicode\ncharacter unichr as integer. Returns 0 if no combining class is\ndefined.'
        pass
    
    def decimal(self, unichr, default=None):
        'decimal(unichr[, default])\n\nReturns the decimal value assigned to the Unicode character unichr\nas integer. If no such value is defined, default is returned, or, if\nnot given, ValueError is raised.'
        pass
    
    def decomposition(self, unichr):
        'decomposition(unichr)\n\nReturns the character decomposition mapping assigned to the Unicode\ncharacter unichr as string. An empty string is returned in case no\nsuch mapping is defined.'
        pass
    
    def digit(self, unichr, default=None):
        'digit(unichr[, default])\n\nReturns the digit value assigned to the Unicode character unichr as\ninteger. If no such value is defined, default is returned, or, if\nnot given, ValueError is raised.'
        pass
    
    def east_asian_width(self, unichr):
        'east_asian_width(unichr)\n\nReturns the east asian width assigned to the Unicode character\nunichr as string.'
        pass
    
    def lookup(self, name):
        'lookup(name)\n\nLook up character by name.  If a character with the\ngiven name is found, return the corresponding Unicode\ncharacter.  If not found, KeyError is raised.'
        pass
    
    def mirrored(self, unichr):
        'mirrored(unichr)\n\nReturns the mirrored property assigned to the Unicode character\nunichr as integer. Returns 1 if the character has been identified as\na "mirrored" character in bidirectional text, 0 otherwise.'
        pass
    
    def name(self, unichr, default=None):
        'name(unichr[, default])\nReturns the name assigned to the Unicode character unichr as a\nstring. If no name is defined, default is returned, or, if not\ngiven, ValueError is raised.'
        pass
    
    def normalize(self, form, unistr):
        "normalize(form, unistr)\n\nReturn the normal form 'form' for the Unicode string unistr.  Valid\nvalues for form are 'NFC', 'NFKC', 'NFD', and 'NFKD'."
        pass
    
    def numeric(self, unichr, default=None):
        'numeric(unichr[, default])\n\nReturns the numeric value assigned to the Unicode character unichr\nas float. If no such value is defined, default is returned, or, if\nnot given, ValueError is raised.'
        pass
    
    @property
    def unidata_version(self):
        pass
    

__doc__ = 'This module provides access to the Unicode Character Database which\ndefines character properties for all Unicode characters. The data in\nthis database is based on the UnicodeData.txt file version\n5.2.0 which is publically available from ftp://ftp.unicode.org/.\n\nThe module uses the same names and symbols as defined by the\nUnicodeData File Format 5.2.0 (see\nhttp://www.unicode.org/reports/tr44/tr44-4.html).'
__file__ = 'd:\\program files\\python\\python27\\dlls\\unicodedata.pyd'
__name__ = 'unicodedata'
__package__ = None
def bidirectional(unichr):
    'bidirectional(unichr)\n\nReturns the bidirectional class assigned to the Unicode character\nunichr as string. If no such value is defined, an empty string is\nreturned.'
    pass

def category(unichr):
    'category(unichr)\n\nReturns the general category assigned to the Unicode character\nunichr as string.'
    pass

def combining(unichr):
    'combining(unichr)\n\nReturns the canonical combining class assigned to the Unicode\ncharacter unichr as integer. Returns 0 if no combining class is\ndefined.'
    pass

def decimal(unichr, default=None):
    'decimal(unichr[, default])\n\nReturns the decimal value assigned to the Unicode character unichr\nas integer. If no such value is defined, default is returned, or, if\nnot given, ValueError is raised.'
    pass

def decomposition(unichr):
    'decomposition(unichr)\n\nReturns the character decomposition mapping assigned to the Unicode\ncharacter unichr as string. An empty string is returned in case no\nsuch mapping is defined.'
    pass

def digit(unichr, default=None):
    'digit(unichr[, default])\n\nReturns the digit value assigned to the Unicode character unichr as\ninteger. If no such value is defined, default is returned, or, if\nnot given, ValueError is raised.'
    pass

def east_asian_width(unichr):
    'east_asian_width(unichr)\n\nReturns the east asian width assigned to the Unicode character\nunichr as string.'
    pass

def lookup(name):
    'lookup(name)\n\nLook up character by name.  If a character with the\ngiven name is found, return the corresponding Unicode\ncharacter.  If not found, KeyError is raised.'
    pass

def mirrored(unichr):
    'mirrored(unichr)\n\nReturns the mirrored property assigned to the Unicode character\nunichr as integer. Returns 1 if the character has been identified as\na "mirrored" character in bidirectional text, 0 otherwise.'
    pass

def name(unichr, default=None):
    'name(unichr[, default])\nReturns the name assigned to the Unicode character unichr as a\nstring. If no name is defined, default is returned, or, if not\ngiven, ValueError is raised.'
    pass

def normalize(form, unistr):
    "normalize(form, unistr)\n\nReturn the normal form 'form' for the Unicode string unistr.  Valid\nvalues for form are 'NFC', 'NFKC', 'NFD', and 'NFKD'."
    pass

def numeric(unichr, default=None):
    'numeric(unichr[, default])\n\nReturns the numeric value assigned to the Unicode character unichr\nas float. If no such value is defined, default is returned, or, if\nnot given, ValueError is raised.'
    pass

ucd_3_2_0 = UCD()
ucnhash_CAPI = _mod___builtin__.PyCapsule()
unidata_version = '5.2.0'
