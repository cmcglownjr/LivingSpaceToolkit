#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lib import Units
from math import radians
import pytest


def test_angle():
    angle = Units.EngineeringUnits('24deg', u_type='angle')
    assert angle.base == radians(24)
    assert angle.base_unit == 'deg'


# Arrange
@pytest.mark.parametrize("actual, expected",
                         [
                             ("10'", 120),
                             ("10ft", 120),
                             ("10feet", 120),
                             ("10 ft", 120),
                             ("10 feet", 120),
                         ])
def test_feet(actual, expected):
    # Act
    feet = Units.EngineeringUnits(actual, u_type='length')
    # Assert
    assert feet.base == expected
    assert feet.base_unit == 'in.'


# Arrange
@pytest.mark.parametrize("actual, expected",
                         [
                             ('15"', 15),
                             ('15in.', 15),
                             ('15 inches', 15),
                         ])
def test_inches(actual, expected):
    # Act
    inch = Units.EngineeringUnits(actual, u_type='length')
    # Assert
    assert inch.base == expected


# Arrange
@pytest.mark.parametrize("actual, expected",
                         [
                             ('1/2"', 0.5),
                             ('1/2in', 0.5),
                             ('1/2inch', 0.5),
                             ('1/2 in.', 0.5),
                             ('1/2 inch', 0.5),
                             ('1 1/2 inch', 1.5)
                         ])
def test_fract_in(actual, expected):
    # Act
    fract = Units.EngineeringUnits(actual, u_type='length')
    # Assert
    assert fract.base == expected
    assert fract.base_unit == 'in.'


# Arrange
@pytest.mark.parametrize("actual, expected",
                         [
                             ("1/2'", 6),
                             ('1/2ft.', 6),
                             ('1/2feet', 6),
                             ('1/2 ft.', 6),
                             ('1/2 feet', 6),
                             ('1 1/2 feet', 18)
                         ])
def test_fract_ft(actual, expected):
    # Act
    fract = Units.EngineeringUnits(actual, u_type='length')
    # Assert
    assert fract.base == expected
    assert fract.base_unit == 'in.'


# Arrange
@pytest.mark.parametrize("actual, expected",
                         [
                             ("1' - 1\"", 13),
                             ('1ft - 1in.', 13),
                             ('1 1/2ft - 1 1/2in', 19.5),
                             ('1/2ft - 1 1/2in', 7.5),
                             ('1ft - 1/2in', 12.5),
                             ('1 ft 1 in', 13)
                         ])
def test_combo(actual, expected):
    # Act
    combo = Units.EngineeringUnits(actual, u_type='length')
    # Assert
    assert combo.base == expected
    assert combo.base_unit == 'in.'
