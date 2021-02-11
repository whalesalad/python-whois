class WHOISException(Exception):
    pass


class WHOISUnsupportedTLD(WHOISException):
    pass


class WHOISParsingFailed(WHOISException):
    pass


class WHOISUnknownDateFormat(WHOISException):
    pass


class WHOISCommandFailed(WHOISException):
    pass


class WHOISCommandTimeout(WHOISException):
    pass
