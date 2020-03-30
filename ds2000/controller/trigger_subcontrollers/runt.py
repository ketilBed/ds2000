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
    "Runt",
]


# ToDo: Shorter function names!!!
class RuntWhen(SubSubController):
    def none(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:RUNT:WHEN <when>
        :TRIGger:RUNT:WHEN?

        **Description**

        Select the qualifier of runt trigger.
        Query the current qualifier of runt trigger.

        **Parameter**

        ======= ========= ========================== =======
        Name    Type      Range                      Default
        ======= ========= ========================== =======
        <when>  Discrete  {NONE|GREater|LESS|GLESs}  NONE
        ======= ========= ========================== =======

        **Explanation**

        **NONE**: do not set the trigger condition of runt trigger.

        **GREater**: trigger when the runt pulse width is greater than the
        lower limit of pulse width (refer to the :TRIGger:RUNT:WLOWer command).

        **LESS**: trigger when the runt pulse width is lower than the upper
        limit of pulse width (refer to the :TRIGger:RUNT:WUPPer command).

        **GLESs**: trigger when the runt pulse width is greater than the lower
        limit (refer to the :TRIGger:RUNT:WLOWer command) and lower than the
        upper limit (refer to the :TRIGger:RUNT:WUPPer command) of pulse width.
        Note: the lower limit of the pulse width must be lower than the upper
        limit.

        **Return Format**

        The query returns NONE, GRE, LESS or GLES.

        **Example**

        :TRIGger:RUNT:WHEN LESS
        The query returns LESS.
        """
        raise NotImplementedError()

    def pulse_width_greater_than_lower_limit(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:RUNT:WHEN <when>
        :TRIGger:RUNT:WHEN?

        **Description**

        Select the qualifier of runt trigger.
        Query the current qualifier of runt trigger.

        **Parameter**

        ======= ========= ========================== =======
        Name    Type      Range                      Default
        ======= ========= ========================== =======
        <when>  Discrete  {NONE|GREater|LESS|GLESs}  NONE
        ======= ========= ========================== =======

        **Explanation**

        **NONE**: do not set the trigger condition of runt trigger.

        **GREater**: trigger when the runt pulse width is greater than the
        lower limit of pulse width (refer to the :TRIGger:RUNT:WLOWer command).

        **LESS**: trigger when the runt pulse width is lower than the upper
        limit of pulse width (refer to the :TRIGger:RUNT:WUPPer command).

        **GLESs**: trigger when the runt pulse width is greater than the lower
        limit (refer to the :TRIGger:RUNT:WLOWer command) and lower than the
        upper limit (refer to the :TRIGger:RUNT:WUPPer command) of pulse width.
        Note: the lower limit of the pulse width must be lower than the upper
        limit.

        **Return Format**

        The query returns NONE, GRE, LESS or GLES.

        **Example**

        :TRIGger:RUNT:WHEN LESS
        The query returns LESS.
        """
        raise NotImplementedError()

    def pulse_width_lower_than_upper_limit(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:RUNT:WHEN <when>
        :TRIGger:RUNT:WHEN?

        **Description**

        Select the qualifier of runt trigger.
        Query the current qualifier of runt trigger.

        **Parameter**

        ======= ========= ========================== =======
        Name    Type      Range                      Default
        ======= ========= ========================== =======
        <when>  Discrete  {NONE|GREater|LESS|GLESs}  NONE
        ======= ========= ========================== =======

        **Explanation**

        **NONE**: do not set the trigger condition of runt trigger.

        **GREater**: trigger when the runt pulse width is greater than the
        lower limit of pulse width (refer to the :TRIGger:RUNT:WLOWer command).

        **LESS**: trigger when the runt pulse width is lower than the upper
        limit of pulse width (refer to the :TRIGger:RUNT:WUPPer command).

        **GLESs**: trigger when the runt pulse width is greater than the lower
        limit (refer to the :TRIGger:RUNT:WLOWer command) and lower than the
        upper limit (refer to the :TRIGger:RUNT:WUPPer command) of pulse width.
        Note: the lower limit of the pulse width must be lower than the upper
        limit.

        **Return Format**

        The query returns NONE, GRE, LESS or GLES.

        **Example**

        :TRIGger:RUNT:WHEN LESS
        The query returns LESS.
        """
        raise NotImplementedError()

    def pulse_width_between_lower_and_upper_limit(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:RUNT:WHEN <when>
        :TRIGger:RUNT:WHEN?

        **Description**

        Select the qualifier of runt trigger.
        Query the current qualifier of runt trigger.

        **Parameter**

        ======= ========= ========================== =======
        Name    Type      Range                      Default
        ======= ========= ========================== =======
        <when>  Discrete  {NONE|GREater|LESS|GLESs}  NONE
        ======= ========= ========================== =======

        **Explanation**

        **NONE**: do not set the trigger condition of runt trigger.

        **GREater**: trigger when the runt pulse width is greater than the
        lower limit of pulse width (refer to the :TRIGger:RUNT:WLOWer command).

        **LESS**: trigger when the runt pulse width is lower than the upper
        limit of pulse width (refer to the :TRIGger:RUNT:WUPPer command).

        **GLESs**: trigger when the runt pulse width is greater than the lower
        limit (refer to the :TRIGger:RUNT:WLOWer command) and lower than the
        upper limit (refer to the :TRIGger:RUNT:WUPPer command) of pulse width.
        Note: the lower limit of the pulse width must be lower than the upper
        limit.

        **Return Format**

        The query returns NONE, GRE, LESS or GLES.

        **Example**

        :TRIGger:RUNT:WHEN LESS
        The query returns LESS.
        """
        raise NotImplementedError()


class Runt(SubController):
    def __init__(self, device):
        super(Runt, self).__init__(device)
        self.when: RuntWhen = RuntWhen(self)

    def source(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:RUNT:SOURce <source>
        :TRIGger:RUNT:SOURce?

        **Description**

        Select the trigger source of runt trigger.
        Query the current trigger source of runt trigger.

        **Parameter**

        ========= ========= ==================== ========
        Name      Type      Range                Default
        ========= ========= ==================== ========
        <source>  Discrete  {CHANnel1|CHANnel2}  CHANnel1
        ========= ========= ==================== ========

        **Return Format**

        The query returns CHAN1 or CHAN2.

        **Example**

        :TRIGger:RUNT:SOURce CHANnel2
        The query returns CHAN2.
        """
        raise NotImplementedError()

    def polarity(self, positive: bool = True):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:RUNT:POLarity <polarity>
        :TRIGger:RUNT:POLarity?

        **Description**

        Select the pulse polarity of runt trigger.
        Query the current pulse polarity of runt trigger.

        **Parameter**

        =========== ========= ==================== ========
        Name        Type      Range                Default
        =========== ========= ==================== ========
        <polarity>  Discrete  {POSitive|NEGative}  POSitive
        =========== ========= ==================== ========

        **Return Format**

        The query returns POS or NEG.

        **Example**

        :TRIGger:RUNT:POLarity NEGative
        The query returns NEG.
        """
        raise NotImplementedError()

    def lower_limit(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:RUNT:WLOWer <NR3>
        :TRIGger:RUNT:WLOWer?

        **Description**

        Set the lower limit of the pulse width in runt trigger.
        Query the current lower limit of the pulse width in runt trigger.

        **Parameter**

        ====== ========= ========== =======
        Name   Type      Range      Default
        ====== ========= ========== =======
        <NR3>  Discrete  2ns to 4s  1μs
        ====== ========= ========== =======

        Note: when the qualifier is GLESs, the range of the lower limit of the
        pulse width is from 2ns to 3.99s.

        **Explanation**

        This command is available when the qualifier (refer to the
        :TRIGger:RUNT:WHEN command) is set to GREater or GLESs.

        **Return Format**

        The query returns the lower limit of the pulse width in scientific
        notation.

        **Example**

        :TRIGger:RUNT:WLOWer 0.02
        The query returns 2.000000e-02.
        """
        raise NotImplementedError()

    def upper_limit(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:RUNT:WUPPer <NR3>
        :TRIGger:RUNT:WUPPer?

        **Description**

        Set the upper limit of the pulse width in runt trigger.
        Query the current upper limit of the pulse width in runt trigger.

        **Parameter**

        ====== ========= ========== =======
        Name   Type      Range      Default
        ====== ========= ========== =======
        <NR3>  Discrete  2ns to 4s  2μs
        ====== ========= ========== =======

        Note: when the qualifier is GLESs, the range of the upper limit of the
        pulse width is from 10ns to 4s.

        **Explanation**

        This command is available when the qualifier (refer to the
        :TRIGger:RUNT:WHEN command) is set to LESS or GLESs.

        **Return Format**

        The query returns the upper limit of the pulse width in scientific
        notation.

        **Example**

        :TRIGger:RUNT:WUPPer 0.02
        The query returns 2.000000e-02.
        """
        raise NotImplementedError()

    def upper_limit_trigger_level(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:RUNT:ALEVel <level>
        :TRIGger:RUNT:ALEVel?

        **Description**

        Set the upper limit of the trigger level in runt trigger and the unit
        is the same with the current amplitude unit.

        Query the current upper limit of the trigger level in runt trigger.

        **Parameter**

        ======== ===== =========================== =======
        Name     Type  Range                       Default
        ======== ===== =========================== =======
        <level>  Real  ± 5 × VerticalScale from    0
                       the screen center - OFFSet
        ======== ===== =========================== =======

        Note:
        For the VerticalScale, refer to the :CHANnel<n>:SCALe command.
        For the OFFSet, refer to the :CHANNel<n>:OFFSet command.

        **Return Format**

        The query returns the upper limit of the trigger level in scientific
        notation.

        **Example**

        :TRIGger:RUNT:ALEVel 0.16
        The query returns 1.600000e-01.
         """
        raise NotImplementedError()

    def lower_limit_trigger_level(self):
        """
        **Rigol Programming Guide**

        **Syntax**

        :TRIGger:RUNT:BLEVel <level>
        :TRIGger:RUNT:BLEVel?

        **Description**

        Set the lower limit of the trigger level in runt trigger and the unit
        is the same with the current amplitude unit.

        Query the current lower limit of the trigger level in runt trigger.

        **Parameter**

        ======== ===== =========================== =======
        Name     Type  Range                       Default
        ======== ===== =========================== =======
        <level>  Real  ± 5 × VerticalScale from    0
                       the screen center - OFFSet
        ======== ===== =========================== =======

        Note:
        For the VerticalScale, refer to the :CHANnel<n>:SCALe command.
        For the OFFSet, refer to the :CHANNel<n>:OFFSet command.

        **Return Format**

        The query returns the lower limit of the trigger level in scientific
        notation.

        **Example**

        :TRIGger:RUNT:BLEVel 0.16
        The query returns 1.600000e-01.
        """
        raise NotImplementedError()