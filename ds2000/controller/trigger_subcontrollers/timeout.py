#!/usr/bin/env python
# ds2000 - The Python Library for Rigol DS2000 Oscilloscopes
# Copyright (C) 2020  Michael Sasser <Michael@MichaelSasser.org>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from ds2000.controller import SubController, SubSubController

__author__ = "Michael Sasser"
__email__ = "Michael@MichaelSasser.org"

__all__ = [
    "Timeout",
]


class TimeoutSlope(SubSubController):
    def positive(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:TIMeout:SLOPe <slope>
        :TRIGger:TIMeout:SLOPe?

        **Description**

        Set the edge type of timeout trigger.
        Query the current edge type of timeout trigger.

        **Parameter**

        ======== ========= ========================== ========
        Name     Type      Range                      Default
        ======== ========= ========================== ========
        <slope>  Discrete  {POSitive|NEGative|RFALl}  POSitive
        ======== ========= ========================== ========

        **Return Format**

        The query returns POS, NEG or RFAL.

        **Example**

        :TRIGger:TIMeout:SLOPe NEGative
        The query returns NEG.
        """
        raise NotImplementedError()

    def negative(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:TIMeout:SLOPe <slope>
        :TRIGger:TIMeout:SLOPe?

        **Description**

        Set the edge type of timeout trigger.
        Query the current edge type of timeout trigger.

        **Parameter**

        ======== ========= ========================== ========
        Name     Type      Range                      Default
        ======== ========= ========================== ========
        <slope>  Discrete  {POSitive|NEGative|RFALl}  POSitive
        ======== ========= ========================== ========

        **Return Format**

        The query returns POS, NEG or RFAL.

        **Example**

        :TRIGger:TIMeout:SLOPe NEGative
        The query returns NEG.
        """
        raise NotImplementedError()

    def r_fall(self):  # ToDo: RFALl (?)
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:TIMeout:SLOPe <slope>
        :TRIGger:TIMeout:SLOPe?

        **Description**

        Set the edge type of timeout trigger.
        Query the current edge type of timeout trigger.

        **Parameter**

        ======== ========= ========================== ========
        Name     Type      Range                      Default
        ======== ========= ========================== ========
        <slope>  Discrete  {POSitive|NEGative|RFALl}  POSitive
        ======== ========= ========================== ========

        **Return Format**

        The query returns POS, NEG or RFAL.

        **Example**

        :TRIGger:TIMeout:SLOPe NEGative
        The query returns NEG.
        """
        raise NotImplementedError()


class Timeout(SubController):
    def __init__(self, device):
        super(Timeout, self).__init__(device)
        self.slope: TimeoutSlope = TimeoutSlope(self)

    def source(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:TIMeout:SOURce <source>
        :TRIGger:TIMeout:SOURce?

        **Description**

        Select the trigger source of timeout trigger.
        Query the current trigger source of timeout trigger.

        **Parameter**

        ========= ========= ==================== ========
        Name      Type      Range                Default
        ========= ========= ==================== ========
        <source>  Discrete  {CHANnel1|CHANnel2}  CHANnel1
        ========= ========= ==================== ========

        **Return Format**

        The query returns CHAN1 or CHAN2.

        **Example**

        :TRIGger:TIMeout:SOURce CHANnel2
        The query returns CHAN2.
        """
        raise NotImplementedError()

    def time(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:TIMeout:TIMe <NR3>
        :TRIGger:TIMeout:TIMe?

        **Description**

        Set the timeout time of timeout trigger.
        Query the current timeout time of timeout trigger.

        **Parameter**

        ====== ===== =========== =======
        Name   Type  Range       Default
        ====== ===== =========== =======
        <NR3>  Real  16ns to 4s  1μs
        ====== ===== =========== =======

        **Return Format**

        The query returns the timeout time in scientific notation.

        **Example**

        :TRIGger:TIMeout:TIMe 0.002
        The query returns 2.000000e+06.
        """
        raise NotImplementedError()