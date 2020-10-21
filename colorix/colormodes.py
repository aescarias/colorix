"""
Colorix
	A module for working with colors

	FILE: 			colormodes.py
	DESCRIPTION: 	Color modes
	
	Angel Carias. 2020.
"""
import tkinter


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
	def __init__(self, r: int, g: int, b: int):
		super(RGB, self).__init__()
		self.r = int(r)
		self.b = int(b)
		self.g = int(g)
		
		self.raw = (self.r, self.g, self.b)
	
	def toHex(self):
		"""Convert RGB to Hex"""
		return Hex(f'#{self.r:02x}{self.g:02x}{self.b:02x}')	

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
		
	def render(self, width: int=200, height: int=200):
		"""Render current color"""
		gui = tkinter.Tk(className="Color Render")
		gui.geometry(f"{width}x{height}")
		
		gui.configure(bg=self.toHex().hexval)
		gui.mainloop()


class Hex(ColorMode):
	"""
	Hex management class
	"""
	def __init__(self, hexval: str):
		super(Hex, self).__init__()
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

	def render(self, width: int=200, height: int=200):
		"""Render current color"""
		gui = tkinter.Tk(className="Color Render")
		gui.geometry(f"{width}x{height}")
		
		gui.configure(bg=self.hexval)
		gui.mainloop()


class CMYK(ColorMode):
	"""
	CMYK management class
	"""
	def __init__(self, c: int, m: int, y: int, k: int):
		super(CMYK, self).__init__()
		
		self.c = int(c)
		self.m = int(m)
		self.y = int(y)
		self.k = int(k)
		
		self.raw = (self.c, self.m, self.y, self.k)
	
	def toHex(self):
		"""Convert CMYK to Hex"""
		# Convert CMYK to RGB
		rgb = CMYK(self.c, self.m, self.y, self.k).toRGB()
		
		# Convert RGB to Hex
		return Hex(f'#{rgb.r:02x}{rgb.g:02x}{rgb.b:02x}')
		
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

	def render(self, width: int=200, height: int=200):
		"""Render current color"""
		gui = tkinter.Tk(className="Color Render")
		gui.geometry(f"{width}x{height}")
		
		gui.configure(bg=self.toHex().hexval)
		gui.mainloop()
		