"""
Support for Skoda Carnet Platform
"""
import logging
from homeassistant.components.lock import LockEntity
from . import SkodaEntity, DATA_KEY

_LOGGER = logging.getLogger(__name__)

def setup_platform(hass, config, add_devices, discovery_info=None):
    """ Setup the Skoda lock """
    if discovery_info is None:
        return
    add_devices([SkodaLock(hass.data[DATA_KEY], *discovery_info)])

class SkodaLock(SkodaEntity, LockEntity):
    """Represents a Skoda Carnet Lock."""

    @property
    def is_locked(self):
        """Return true if lock is locked."""
        _LOGGER.debug('Getting state of %s' % self.instrument.attr)
        return self.instrument.is_locked

    def lock(self, **kwargs):
        """Lock the car."""
        self.instrument.lock()

    def unlock(self, **kwargs):
        """Unlock the car."""
        self.instrument.unlock()

    @property
    def assumed_state(self):
        return self.instrument.assumed_state