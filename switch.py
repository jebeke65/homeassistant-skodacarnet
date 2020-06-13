"""
Support for Skoda Carnet Platform
"""
import logging
from homeassistant.helpers.entity import ToggleEntity
from . import SkodaEntity, DATA_KEY

_LOGGER = logging.getLogger(__name__)

def setup_platform(hass, config, add_devices, discovery_info=None):
    """ Setup the Skoda switch."""
    if discovery_info is None:
        return
    add_devices([SkodaSwitch(hass.data[DATA_KEY], *discovery_info)])

class SkodaSwitch(SkodaEntity, ToggleEntity):
    """Representation of a Skoda Carnet Switch."""

    @property
    def is_on(self):
        """Return true if switch is on."""
        _LOGGER.debug('Getting state of %s' % self.instrument.attr)
        return self.instrument.state

    def turn_on(self, **kwargs):
        """Turn the switch on."""
        _LOGGER.debug("Turning ON %s." % self.instrument.attr)
        self.instrument.turn_on()

    def turn_off(self, **kwargs):
        """Turn the switch off."""
        _LOGGER.debug("Turning OFF %s." % self.instrument.attr)
        self.instrument.turn_off()

    @property
    def assumed_state(self):
        return self.instrument.assumed_state
