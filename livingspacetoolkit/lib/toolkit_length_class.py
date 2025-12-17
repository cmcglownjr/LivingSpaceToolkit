import logging

from .toolkit_enums import LengthType

logger = logging.getLogger(__name__)


class ToolkitLength:
    def __init__(self, length_type: LengthType):
        self._length = ''
        self._length_type = length_type

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, val) -> None:
        # TODO: Need to add verification logic
        self.length = val

    @property
    def length_type(self):
        return self._length_type

    @length_type.getter
    def length_type(self) -> LengthType:
        return self._length_type
