"""Validate revision-specific Smart Fan driver operations."""

import sfan


def __getattr__(name):
    return getattr(sfan, name)


def _check_revision(stack):
    address = sfan.checkCard(stack)
    if address < 0:
        raise OSError("Smart Fan card not detected")
    if address > 4:
        raise ValueError("This Smart Fan hardware revision does not support this feature")


def _check_result(value):
    if value == -1:
        raise OSError("Smart Fan driver reported an I/O failure")
    return value


def getProcTemp(stack):
    _check_revision(stack)
    return _check_result(sfan.getProcTemp(stack))


def getSafetyTemp(stack):
    _check_revision(stack)
    return _check_result(sfan.getSafetyTemp(stack))


def setSafetyTemp(stack, value):
    _check_revision(stack)
    return _check_result(sfan.setSafetyTemp(stack, value))


def getLedBlink(stack):
    _check_revision(stack)
    return _check_result(sfan.getLedBlink(stack))


def setLedBlink(stack, value):
    _check_revision(stack)
    return _check_result(sfan.setLedBlink(stack, value))
