"""
Colorix
	A module for working with colors
	
	FILE:
		colormodes.py
	DESCRIPTION:
		Color modes

	Angel Carias. 2020.
"""

class ColorMode:
	"""
	Base class for color modes
	"""
	def __init__(self):
		self.supportModes = ["rgb", 'cmyk', 'hex']
		
		self.RGB_SCALE = 255
		self.CMYK_SCALE = 100


class RGB(ColorMode):
	"""
	RGB management class
	"""
	def __init__(self, r, g, b):
		super(RGB, self).__init__()
		self.r = r
		self.b = b
		self.g = g
		
		self.raw = (r, g, b)
	
	def toHex(self):
		"""Convert RGB to Hex"""
		return Hex('#{:02x}{:02x}{:02x}'.format(self.r, self., self.b))
	

	def toCMYK(self, precise=False):
		"""Convert RGB to CMYK"""
		if (self.r, self.g, self.b) == (0, 0, 0): # to avoid zero div error
			return CMYK(0, 0, 0, self.CMYK_SCALE)
			
		r = self.r / self.RGB_SCALE
		g = self.g / self.RGB_SCALE
		b = self.b / self.RGB_SCALE
		
		k = 1 - max(r, g, b)
		
		c = (1 - r - k) / (1 - k)
		m = (1 - g - k) / (1 - k)
		y = (1 - b - k) / (1 - k)
		
		cs = self.CMYK_SCALE
		
		if precise:
			return CMYK(c * cs, m * cs, y * cs, k * cs)
		else:
			return CMYK(round(c * cs), round(m * cs), round(y * cs), round(k * cs))

		 
class Hex(ColorMode):
	"""
	Hex management class
	"""
	def __init__(self, hexval):
		self.hexval = hexval
	
	def toRGB(self):
		"""Convert Hex to RGB"""
		# Remove '#'
		hx = self.hexval.lstrip('#')
		
		# Convert to RGB using integer to base 16
		r = int(hx[0:2], 16)
		g = int(hx[2:4], 16)
		b = int(hx[4:6], 16)
		return RGB(r, g, b)
		
	def toCMYK(self):
		"""Convert Hex to CMYK"""
		# Remove '#'
		hx = self.hexval.lstrip('#')
		
		# Convert to RGB using integer to base 16
		r = int(hx[0:2], 16)
		g = int(hx[2:4], 16)
		b = int(hx[4:6], 16)
		
		# Convert RGB to CMYK
		return RGB(r, g, b).toCMYK()

		
class CMYK(ColorMode):
	"""
	CMYK management class
	"""
	def __init__(self, c, m, y, k):
		super(CMYK, self).__init__()
		
		self.c = c
		self.m = m
		self.y = y
		self.k = k
		
		self.raw = (c, m, y, k)
	
	def toHex(self):
		"""Convert CMYK to Hex"""
		# Convert CMYK to RGB
		rgb = CMYK(self.c, self.m, self.y, self.k).toRGB().raw
		
		# Convert RGB to Hex
		return Hex('#{:02x}{:02x}{:02x}'.format(*rgb))
		
	def toRGB(self, precise=False):
		"""Convert CMYK to RGB"""
		
		c = self.c / self.CMYK_SCALE
		m = self.m / self.CMYK_SCALE
		y = self.y / self.CMYK_SCALE
		k = self.k / self.CMYK_SCALE
		
		r = self.RGB_SCALE * (1 - c) * (1 - k)
		g = self.RGB_SCALE * (1 - m) * (1 - k)
		b = self.RGB_SCALE * (1 - y) * (1 - k)
		
		if precise:
			return RGB(r, g, b)
		else:
			return RGB(round(r), round(g), round(b))
