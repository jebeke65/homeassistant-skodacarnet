"""
Support for Skoda Carnet.
"""
import logging
from . import SkodaEntity, DATA_KEY
from homeassistant.components.binary_sensor import BinarySensorEntity, DEVICE_CLASSES

_LOGGER = logging.getLogger(__name__)

def setup_platform(hass, config, add_devices, discovery_info=None):
    """Set up the Skoda binary sensors."""
    if discovery_info is None:
        return
    add_devices([SkodaBinarySensor(hass.data[DATA_KEY], *discovery_info)])

class SkodaBinarySensor(SkodaEntity, BinarySensorEntity):
    """Representation of a Skoda Binary Sensor """

    @property
    def is_on(self):
        """Return True if the binary sensor is on."""
        _LOGGER.debug('Getting state of %s' % self.instrument.attr)
        return self.instrument.is_on

    @property
    def device_class(self):
        """Return the class of this sensor, from DEVICE_CLASSES."""
        if self.instrument.device_class in DEVICE_CLASSES:
            return self.instrument.device_class
        return None