from enum import Enum


class CouponType(Enum):
    UNKNOWN = 'unknown'
    SAT_SP = 'sat_sp'
    NFCE_SP = 'nfce_sp'

    @classmethod
    def choices(cls):
        return [(choice.name, choice.value) for choice in cls]