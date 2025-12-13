from enum import Enum


class Scenario(Enum):
    WALL_HEIGHT_PITCH = 1
    WALL_HEIGHT_PEAK_HEIGHT = 2
    MAX_HEIGHT_PITCH = 3
    SOFFIT_HEIGHT_PEAK_HEIGHT = 4
    SOFFIT_HEIGHT_PITCH = 5
    DRIP_EDGE_PEAK_HEIGHT = 6
    DRIP_EDGE_PITCH = 7


class PitchType(Enum):
    RATIO = 1
    ANGLE = 2


class RoofingType(Enum):
    ECO_GREEN = 1
    ALUMINUM = 2


class EndCutType(Enum):
    UNCUT_TOP_BOTTOM = 1
    PLUMB_CUT_TOP_BOTTOM = 2
    PLUMB_CUT_TOP = 3


class SunroomType(Enum):
    STUDIO = 1
    CATHEDRAL = 2