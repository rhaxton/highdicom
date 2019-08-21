"""Enumerate values specific to Structured Report IODs."""
from enum import Enum


class ValueTypes(Enum):

    """Enumerated values for attribute Value Type."""

    CODE = 'CODE'
    COMPOSITE = 'COMPOSITE'
    CONTAINER = 'CONTAINER'
    DATE = 'DATE'
    DATETIME = 'DATETIME'
    IMAGE = 'IMAGE'
    NUM = 'NUM'
    PNAME = 'PNAME'
    SCOORD = 'SCOORD'
    SCOORD3D = 'SCOORD3D'
    TCOORD = 'TCOORD'
    TEXT = 'TEXT'
    TIME = 'TIME'
    UIDREF = 'UIDREF'
    WAVEFORM = 'WAVEFORM'


class GraphicTypes(Enum):

    """Enumerated values for attribute Graphic Type."""

    CIRCLE = 'CIRCLE'
    ELLIPSE = 'ELLIPSE'
    ELLIPSOID = 'ELLIPSOID'
    MULTIPOINT = 'MULTIPOINT'
    POINT = 'POINT'
    POLYLINE = 'POLYLINE'


class GraphicTypes3D(Enum):

    """Enumerated values for attribute Graphic Type 3D."""

    ELLIPSE = 'ELLIPSE'
    ELLIPSOID = 'ELLIPSOID'
    MULTIPOINT = 'MULTIPOINT'
    POINT = 'POINT'
    POLYLINE = 'POLYLINE'
    POLYGON = 'POLYGON'


class TemporalRangeTypes(Enum):

    """Enumerated values for attribute Temporal Range Type."""

    BEGIN = 'BEGIN'
    END = 'END'
    MULTIPOINT = 'MULTIPOINT'
    MULTISEGMENT = 'MULTISEGMENT'
    POINT = 'POINT'
    SEGMENT = 'SEGMENT'


class RelationshipTypes(Enum):

    """Enumerated values for attribute Relationship Type."""

    CONTAINS = 'CONTAINS'
    HAS_ACQ_CONTENT = 'HAS ACQ CONTENT'
    HAS_CONCEPT_MOD = 'HAS CONCEPT MOD'
    HAS_OBS_CONTEXT = 'HAS OBS CONTEXT'
    HAS_PROPERTIES = 'HAS PROPERTIES'
    INFERRED_FROM = 'INFERRED FROM'
    SELECTED_FROM = 'SELECTED FROM'


class PixelOriginInterpretations(Enum):

    """Enumerated values for attribute Pixel Origin Interpretation."""

    FRAME = 'FRAME'
    VOLUME = 'VOLUME'



