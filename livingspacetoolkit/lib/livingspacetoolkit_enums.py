from enum import Enum


class Scenario(Enum):
    WALL_HEIGHT_PITCH = 0
    WALL_HEIGHT_PEAK_HEIGHT = 1
    MAX_HEIGHT_PITCH = 2
    SOFFIT_HEIGHT_PEAK_HEIGHT = 3
    SOFFIT_HEIGHT_PITCH = 4
    DRIP_EDGE_PEAK_HEIGHT = 5
    DRIP_EDGE_PITCH = 6


class PitchType(Enum):
    RATIO = 0
    ANGLE = 1


class RoofingType(Enum):
    ECO_GREEN = 0
    ALUMINUM = 1


class EndCutType(Enum):
    UNCUT_TOP_BOTTOM = 0
    PLUMB_CUT_TOP_BOTTOM = 1
    PLUMB_CUT_TOP = 2


class SunroomType(Enum):
    STUDIO = 0
    CATHEDRAL = 1

class LengthType(Enum):
    OVERHANG = 0
    THICKNESS = 1
    PEAK_HEIGHT = 2
    MAX_HEIGHT = 3
    DRIP_EDGE_HEIGHT = 4
    A_SIDE_SOFFIT_HEIGHT = 5
    B_SIDE_SOFFIT_HEIGHT = 6
    C_SIDE_SOFFIT_HEIGHT = 7
    A_WALL_HEIGHT = 8
    B_WALL_HEIGHT = 9
    C_WALL_HEIGHT = 10
    A_WALL_WIDTH = 11
    B_WALL_WIDTH  = 12
    C_WALL_WIDTH = 13