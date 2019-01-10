import os
import textwrap
import argparse

from argparse import ArgumentParser

from Payload._Installation.__Installation import Installation
from Payload._Shell.__Shell import Shell
from Payload._Network.__Host import Host
from Payload._Network.__VPS import VPS

__all__ = [
  "os",
  "textwrap",
  "argparse",
  "ArgumentParser",
  "Installation",
  "Shell",
  "Host",
  "VPS"
]

# __author__ = "Jacob B. Sanders"
# __copyright__ = "Copyright 2019, Vault Cipher LLC."
# __license__ = "GPL"
# __maintainer__ = "Jacob B. Sanders"
# __email__ = "develor.vault@gmail.com"
# __status__ = "Development"
# """
# ╔════════════════════════╗
# ╟────────────────────────╢
# ║     Network Payload    ║
# ╟────────────────────────╢
# ╚════════════════════════╝
# python3 -m Payload.Provision --commands [command]
#
# """
#
# __version__ = "0.1"
