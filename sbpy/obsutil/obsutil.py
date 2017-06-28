# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""
================================
SBPy Observation Planning Module
================================

created on June 23, 2017
"""

__all__ = ['Obsutil']


class Obsutil():

    def __init__(self, targetid, eph, observatory):
        self.targetid = targetid
        self.eph = eph
        self.observatory = observatory
    
    
    @classmethod
    def check_observability(cls, targetid, epochs, observatory):
        """Check observability for specific target, given epochs, and observatory

        Parameters
        ----------
        targetid : str, mandatory
            target identifier
        epochs : `astropy.time` instance or list thereof, mandatory
            date to check observability
        observatory : str, mandatory
            MPC observatory code

        Returns
        -------
        `astropy.table` 

        Examples
        --------
        >>> from sbpy.obsutil import Obsutil
        >>> from astropy.time import Time
        >>> epochs = [Time('2018-05-23 23:00', scale='utc'), ..., 
                      Time('2018-05-25 04:30', scale='utc']
        >>> obs = Obsutil.check_observability('3552', epochs, '568')
        
        not yet implemented

        """

    def primetime(self, condition):
        """Find best time to observe target based on some conditions
        
        Parameters
        ----------
        condition : str, mandatory ['airmass', 'Vmag', 'slowest', 'fastest', 'closest', 'furthest'...]
            condition on which to decide best observability

        Examples
        --------
        >>> from sbpy.obsutil import Obsutil
        >>> from astropy.time import Time
        >>> epochs = [Time('2018-05-23 23:00', scale='utc'), ..., 
                      Time('2018-05-25 04:30', scale='utc']
        >>> obs = Obsutil.check_observability('3552', epochs, '568')
        >>> obs.primetime('airmass')

        not yet implemented

        """

    def plot_airmass(self, plot):
        """Create airmass plot

        Examples
        --------
        >>> from sbpy.obsutil import Obsutil
        >>> from astropy.time import Time
        >>> import matplotlib.pyplot as plt
        >>> epochs = [Time('2018-05-23 23:00', scale='utc'), ..., 
                      Time('2018-05-25 04:30', scale='utc']
        >>> obs = Obsutil.check_observability('3552', epochs, '568')
        >>> plot = plt.figure()
        >>> plot = obs.plot_airmass(plot)
        >>> ...
        >>> obs2 = Obsutil.check_observability(...)
        >>> plot = obs2.plot_airmass(plot)

        not yet implemented

        """
        
    def finderchart(self):
        """Create finder chart

        Examples
        --------
        >>> from sbpy.obsutil import Obsutil
        >>> from astropy.time import Time
        >>> import matplotlib.pyplot as plt
        >>> epochs = [Time('2018-05-23 23:00', scale='utc'), ..., 
                      Time('2018-05-25 04:30', scale='utc']
        >>> obs = Obsutil.check_observability('3552', epochs, '568')

        not yet implemented

        """
