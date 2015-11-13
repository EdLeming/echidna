""" Utilities module to include functions that may be useful throughout
echidna.
"""
import numpy

import time


class Timer:
    """ Useful timer class to show time elapsed performing a code block.

    Examples:
      >>> With Timer() as t:
      ...     # block of code to time
      >>> print ('Code executed in %.03f sec.' % t._interval)
    """
    def __enter__(self):
        """
        Attributes:
          _start (float): start time of code block

        Returns:
          :class:`Timer`: class instance
        """
        self._start = time.clock()
        return self

    def __exit__(self, *args):
        """
        Attributes:
          _end (float): end time of code block
          _interval (float): time elapsed during code block
        """
        self._end = time.clock()
        self._interval = self._end - self._start


def get_array_errors(array, lin_err=0.01, frac_err=None,
                     log=False, log10=False):
    shape = array.shape
    array = array.ravel()
    if log:
        array = numpy.log(array)
    elif log10:
        array = numpy.log10(array)
    errors = numpy.zeros(array.shape)
    for index, value in enumerate(array):
        if lin_err:
            error = value + lin_err
        elif frac_err:
            error = value * frac_err
        else:
            raise ValueError("Must provide either lin_err or frac_err")
        errors[index] = error
    if log:
        errors = numpy.exp(errors)
    elif log10:
        errors = numpy.power(10., errors)
    errors.reshape(shape)
    return errors
