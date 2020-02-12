from app.model import Window, Vision, Perspective, Viewport, Clipping


class Landscape:
	window = None
	vision = None
	perspective = None
	viewport = None
	clipping = None

	def __init__(self, origin=(0, 0, 0), area=(750, 750), distance=10):
		x, y, z, width, height = (*origin, *area)

		self.window = Window(origin, area)
		self.vision = Vision(self.window)
		self.perspective = Perspective(distance, self.window)
		self.viewport = Viewport((x+20, y+20, z), (width-40, height-40), self.window)
		self.clipping = Clipping((x+20, y+20, z), (width-40, height-40))

	def __rmatmul__(self, draft):
		draft = draft \
				@ self.window \
				@ self.vision \
				@ self.perspective \
				@ self.viewport \
				@ self.clipping

		draft + self.clipping.draft

		return draft

	def center_at(self, coordinate):
		direction = tuple(d1-d0 for d0, d1 in zip(self.window.center, coordinate))
		self.window.move(1, direction)

	def resize(self, area):
		pass
