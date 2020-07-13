#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
import Units
from math import radians


def test_angle():
    angle = Units.EngineeringUnits('24deg', u_type='angle')
    assert angle.base == radians(24)
    assert angle.base_unit == 'deg'


def test_feet():
    feet1 = Units.EngineeringUnits("10'", u_type='length')
    feet2 = Units.EngineeringUnits('10ft', u_type='length')
    feet3 = Units.EngineeringUnits('10feet', u_type='length')
    assert feet1.base == 120
    assert feet2.base == 120
    assert feet3.base == 120
    assert feet1.base_unit == 'in.'


def test_inches():
    inch1 = Units.EngineeringUnits('15"', u_type='length')
    inch2 = Units.EngineeringUnits('15in.', u_type='length')
    # inch3 = Units.EngineeringUnits('15 inches', u_type='length')
    assert inch1.base == 15
    assert inch2.base == 15
    # assert inch3.base == 15


def test_fract_in():
    fract1 = Units.EngineeringUnits('1/2"', u_type='length')
    fract2 = Units.EngineeringUnits('1/2in.', u_type='length')
    assert fract1.base == 0.5
    assert fract2.base == 0.5
