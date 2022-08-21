from enum import Enum


class Point:
    def __init__(self, _id, coord):
        self.id = _id
        self.coord = coord
        self.dims = len(coord)


class HalfSpace:
    def __init__(self, pnt, coeff, known):
        self.pnt = pnt
        self.coeff = coeff
        self.known = known
        self.arr = Arrangement.AUGMENTED
        self.dims = len(coeff)


class Position(Enum):
    ABOVE = 1
    BELOW = -1
    OVERLAPPED = 0


class Arrangement(Enum):
    SINGULAR = 0
    AUGMENTED = 1


def genhalfspaces(p, records):
    halfspaces = []
    p_d = p.coord[-1]
    p_i = p.coord[:-1]

    for r in records:
        r_d = r.coord[-1]
        r_i = r.coord[:-1]

        halfspaces.append(HalfSpace(r, r_i - r_d - p_i + p_d, p_d - r_d))

    return halfspaces


def find_pointhalfspace_position(point, halfspace):
    val = sum(halfspace.coeff * point.coord)

    # The position is referred to the halfspace with respect to the point
    if val < halfspace.known:
        return Position.ABOVE
    elif val > halfspace.known:
        return Position.BELOW
    else:
        return Position.OVERLAPPED
