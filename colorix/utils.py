"""
Colorix
	A module for working with colors

	FILE: 			utils.py
	DESCRIPTION: 	Utilities
	
	Angel Carias. 2020.
"""
import random
from colorix import colormodes
from colorix.colormodes import ColorMode


class ModeNotSupported(Exception):
    def __init__(self, color):
        message = f"Color mode '{color}' not supported."
        super(ModeNotSupported, self).__init__(message)


class Utils:
    def colorRandom(self, mode: str="rgb"):
        mode = mode.lower()
        cm = ColorMode()
        
        if mode == "rgb":
            rgb = [random.randint(0, cm.RGB_SCALE) for _ in range(3)]
            return colormodes.RGB(*rgb)
        elif mode == "cmyk":
            cmyk = [random.randint(0, cm.CMYK_SCALE) for _ in range(4)]
            return colormodes.CMYK(*cmyk)
        elif mode == "hex":
            rgb = [random.randint(0, cm.RGB_SCALE) for _ in range(3)]
            return colormodes.RGB(*rgb).toHex()
        else:
            raise ModeNotSupported(mode)
