# cornelltest.py
# Walker M. White (wmw2), Lillian Lee (LJL2), Steve Marschner (srm2)
# August 20, 2013
"""Unit test support functions

This module provides function-level unit testing tools.  It is a 
replacement for the built-in Python package unittest, which is much
less user friendly and requires an understanding of OO programming.
The assert functions in this library are intended to integrate
with stack-trace infor when errors occur."""
import numpy
import traceback

# STRING TYPE CHECKING

def isfloat(s):
    """Returns: True if s is the string representation of a number
    
    TYPE:
        s:      str
        RETURN: bool
    """
    try:
        x = float(s)
        return True
    except:
        return False


def isint(s):
    """Returns: True if s is the string representation of an integer
    
    TYPE:
        s:      str
        RETURN: bool
    """
    try:
        x = int(s)
        return True
    except:
        return False


def isbool(s):
    """Returns: True if s is the string representation of an integer
    
    TYPE:
        s:      str
        RETURN: bool
    """
    if (type(s) != str):
        return False
    return (s == 'True' or s == 'False')


# ASSERTION FUNCTIONS
def quit_with_error(msg):
    """Quit Python with an error msg
    
    When testing, this is preferable to raising an error in 
    Python. Once you have a lot of helper functions, it becomes
    a lot of work just to figure out what is going on
    in the error message. This makes the error clear and concise"""
    stack = traceback.extract_stack()
    frame = stack[-3]
    print msg
    if (frame[3] is None):
        suffix = ''
    else:
        suffix = ": "+frame[3]
    print 'Line '+repr(frame[1])+' of '+ frame[0] + suffix
    print 'Quitting with Error'
    quit()


def assert_equals(expected,received):
    """Quit if expected and received differ.
    
    The meaning of "differ" for this function is !=.  As a result, this 
    assert function is not necessarily reliable when expected and received 
    are of type "float".  You should use the function assert_floats_equal 
    for that application.
    
    As part of the error message, this function provides some minimal 
    debug information.  The following is an example debug message:
    
        assert_equals expected 'yes' but instead got 'no'
    
    TYPES:
        expected: any
        received: any
        RETURN:   None
    """
    if (expected != received):
        message = 'assert_equals: expected ' + repr(expected) + ' but instead got ' + repr(received)
        quit_with_error(message)


def assert_not_equals(expected,received):
    """Quit if expected and received are the same.
    
    The meaning of "differ" for this function is ==.  As a result, this 
    assert function is not necessarily reliable when expected and received 
    are of type "float".  You should use the function assert_not_floats_equal 
    for that application.
    
    As part of the error message, this function provides some minimal 
    debug information.  The following is an example debug message:
    
        assert_not_equals expected something different from 'n' 
    
    TYPES:
        expected: any
        received: any
        RETURN:   None
    """
    if (expected == received):
        message = 'assert_not_equals: expected something different from' + repr(expected)
        quit_with_error(message)


def assert_true(received):
    """Quit if received is False.
    
    As part of the error message, this function provides some minimal 
    debug information.  The following is an example debug message:
    
        assert_true expected True but instead got False
        
    TYPES:
        received: any
        RETURN:   None
    """
    if (not received):
        msg = "assert_true: expected True but instead got False"
        quit_with_error(msg)


def assert_false(received):
    """Quit AssertionError if received is True.
    
    As part of the error message, this function provides some minimal 
    debug information.  The following is an example debug message:
    
        assert_false expected False but instead got True
        
    TYPES:
        received: any
        RETURN:   None
    """
    if (received):
        msg = "assert_false: expected False but instead got True"
        quit_with_error(msg)


def assert_floats_equal(expected, received):
    """Quit if floats expected and received differ.
    
    This function takes two numbers and compares them using functions
    from the numerical package numpy.  This is a scientific computing
    package that allows us to test if numbers are "close enough".  
    Hence, unlike assert_equal, the meaning of "differ" for this
    function is however it is defined by numpy.
    
    As part of the error message, this function provides some minimal 
    debug information.  The following is an example debug message:
    
        assert_floats_equal: expected 0.1 but instead got 0.2
    
    PRECONDITION: 
    The arguments expected and received should each numbers (either floats 
    or ints). If either argument is not a number, the function quits
    with a different error message. For example:
    
        assert_floats_equal: first argument 'alas' is not a number
    
    TYPES:
        expected: int or float
        received: int or float
        RETURN:   None
    """
    number = [float, int]  # list of number types
    if type(expected) not in number:
        msg = ("assert_floats_equal: " +
                "first argument " + repr(expected) +" is not a number")
        quit_with_error(msg)
    
    if type(received) not in number:
        msg = ("assert_floats_equal: " +
              "second argument " + repr(received) +" is not a number")
        quit_with_error(msg)
    
    if (not numpy.allclose([expected],[received])):
        msg = ("assert_floats_equal: expected " + repr(expected) +
                " but instead got " + repr(received))
        quit_with_error(msg)


def assert_floats_not_equal(expected, received):
    """Quit if floats expected and received are the same.
    
    This function takes two numbers and compares them using functions
    from the numerical package numpy.  This is a scientific computing
    package that allows us to test if numbers are "close enough".  
    Hence, unlike assert_equal, the meaning of "same" for this
    function is however it is defined by numpy.
    
    As part of the error message, this function provides some minimal 
    debug information.  The following is an example debug message:
    
        assert_floats_not_equal: expected something different from 0.1 
    
    PRECONDITION: 
    The arguments expected and received should each numbers (either floats 
    or ints). If either argument is not a number, the function quits
    with a different error message. For example:
    
        assert_floats_not_equal: first argument 'alas' is not a number
    
    TYPES:
        expected: int or float
        received: int or float
        RETURN:   None
    """
    number = [float, int]  # list of number types
    if type(expected) not in number:
        msg = ('assert_floats_not_equal: ' +
                'first argument ' + repr(expected) +' is not a number')
        quit_with_error(msg)
    
    if type(received) not in number:
        msg = ("assert_floats_not_equal: " +
              "second argument " + repr(received) +" is not a number")
        quit_with_error(msg)
    
    if (numpy.allclose([expected],[received])):
        msg = ('assert_floats_not_equal: expected something different from' +
                repr(expected))
        quit_with_error(msg)


def assert_float_lists_equal(expected, received):
    """Quit if the lists of floats expected and received differ
    
    This function takes two lists of numbers and compares them using 
    fuctions from the numerical package numpy.  This is a scientific 
    computing package that allows us to test if numbers are "close enough".  
    Hence, unlike assert_equal, the meaning of "differ" for this
    function is however it is defined by numpy.
    
    This function is similar to assert_floats_equal.  The difference
    is that it works on lists of floats.  These lists can be
    multidimensional.  To illustrate this, the following is an 
    example debug message: 
    
        assert_float_lists__equal: expected [[1,2],[3,4]] but instead got [[1,2],[3,5]]
    
    PRECONDITION: 
    The arguments expected and received should each lists of numbers.
    Furthemore, they must have EXACTLY the same dimension.  If not
    this function quits with a different error message.  For example:
    
        assert_float_lists_equal: first argument 'alas' is not a list

    or 
    
        assert_float_lists_equal: lists [1] and [2,3] are not comparable
    
    TYPES:
        expected: multidimensional list of int or float
        received: multidimensional list of int or float
        RETURN:   None
    """
    number = [float, int]  # list of number types
    if type(expected) != list:
        msg = ("assert_float_lists_equal: " +
                "first argument " + repr(expected) +" is not a list")
        quit_with_error(msg)
    
    if type(received) != list:
        msg = ("assert_float_lists_equal: " +
                "second argument " + repr(received) +" is not a list")
        quit_with_error(msg)
    
    if len(expected) != len(received):
        msg = ('assert_float_lists_equal: lists ' + repr(expected) +
                ' and ' + repr(received)+' have different sizes')
        quit_with_error(msg)        

    try:   
        if (not numpy.allclose([expected],[received])):
            msg = ("assert_float_lists_equal: expected " + repr(expected) +
                " but instead got " + repr(received))
            quit_with_error(msg)    
    except:
            msg = ('assert_float_lists_equal: lists ' + repr(expected) +
                    ' and ' + repr(received)+' are not comparable')
            quit_with_error(msg)    


def assert_float_lists_not_equal(expected, received):
    """Quit if the lists of floats expected and received are the same
    
    This function takes two lists of numbers and compares them using 
    fuctions from the numerical package numpy.  This is a scientific 
    computing package that allows us to test if numbers are "close enough".  
    Hence, unlike assert_equal, the meaning of "same" for this
    function is however it is defined by numpy.
    
    This function is similar to assert_floats_equal.  The difference
    is that it works on lists of floats.  These lists can be
    multidimensional.  To illustrate this, the following is an 
    example debug message: 
    
        assert_float_lists_not_equal: expected something different from [[1,2],[3,4]] 
        
    PRECONDITION: 
    The arguments expected and received should each lists of numbers.
    Furthemore, they must have EXACTLY the same dimension.  If not
    this function quits with a different error message.  For example:
       
        assert_float_lists_not_equal: first argument 'alas' is not a list

    or 
    
        assert_float_lists_not_equal: lists [1] and [2,3] are not comparable
    
    TYPES:
        expected: multidimensional list of int or float
        received: multidimensional list of int or float
        RETURN:   None
    """
    number = [float, int]  # list of number types
    if type(expected) != list:
        msg = ("assert_float_lists_not_equal: " +
                "first argument " + repr(expected) +" is not a list")
        quit_with_error(msg)
    
    if type(received) != list:
        msg = ("assert_float_lists_not_equal: " +
                "second argument " + repr(received) +" is not a list")
        quit_with_error(msg)

    if len(expected) != len(received):
        msg = ('assert_float_lists_equal: lists ' + repr(expected) +
                ' and ' + repr(received)+' have different sizes')
        quit_with_error(msg)    

    try:   
        if (numpy.allclose([expected],[received])):
            msg = ('assert_floats_not_equal: expected something different from' +
                    repr(expected))
            quit_with_error(msg) 
    except:
            msg = ('assert_float_lists_not_equal: lists ' + repr(expected) +
                    ' and ' + repr(received)+' are not comparable')
            quit_with_error(msg)           