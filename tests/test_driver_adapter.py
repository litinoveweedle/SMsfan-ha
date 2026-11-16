"""Verify revision and I/O checks around Smart Fan settings."""

import pytest
import sfan

from custom_components.smsfan import driver_adapter


def test_unsupported_revision_does_not_change_fan_settings(monkeypatch):
    writes = []
    monkeypatch.setattr(sfan, "checkCard", lambda stack: 0x2C)
    monkeypatch.setattr(sfan, "setSafetyTemp", lambda *args: writes.append(args))
    with pytest.raises(ValueError, match="hardware revision"):
        driver_adapter.setSafetyTemp(0, 60)
    assert not writes


def test_driver_failure_is_not_reported_as_temperature(monkeypatch):
    monkeypatch.setattr(sfan, "checkCard", lambda stack: 3)
    monkeypatch.setattr(sfan, "getProcTemp", lambda stack: -1)
    with pytest.raises(OSError, match="I/O failure"):
        driver_adapter.getProcTemp(0)
