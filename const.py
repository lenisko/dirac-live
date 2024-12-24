"""Constants for the Dirac Live integration."""

from datetime import timedelta
from typing import Final

DOMAIN: Final = "dirac_live"
SCAN_INTERVAL = timedelta(seconds=30)
