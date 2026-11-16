"""Shared number platform for the card."""

from SMcommonHA.number import async_setup_entry as shared_setup

from . import CARD


async def async_setup_entry(hass, entry, async_add_entities):
    await shared_setup(hass, entry, async_add_entities, CARD)
