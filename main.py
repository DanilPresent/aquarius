
from ezprint import *
import random

glasses = []

def enter(max = 0, text = '>>>'):
	inp = input(text)
	try:
		inp = int(inp)
	except:
		return enter(max = max, text = text)

	if max != 0:
		if inp <= max and inp >= 0:
			return inp
		else:
			return enter(max = max, text = text)
	else:
		if inp >= 0:
			return inp
		else:
			return enter(max = max, text = text)


class glass:

	dg = []

	def __init__(self, v = 1000, vl = 1000):
		self.v = v
		self.vl = vl
	

	def draw(self):
		n = 6
		d = self.v / n

		dg = []
		dg.append('╚══════╝')

		if self.vl >= d:
			dg.append('║░░░░░░║')
		else:
			dg.append('║      ║')

		if self.vl >= 2 * d:
			dg.append('║░░░░░░║')
		else:
			dg.append('║      ║')

		if self.vl >= 3 * d:
			dg.append('║░░░░░░║' + ' ' * 5 + 'Fill: ' + str(self.getFill()))
		else:
			dg.append('║      ║' + ' ' * 5 + 'Fill: ' + str(self.getFill()))

		if self.vl >= 4 * d:
			dg.append('║░░░░░░║' + ' ' * 5 + 'Volume: ' + str(self.getVolume()))
		else:
			dg.append('║      ║' + ' ' * 5 + 'Volume: ' + str(self.getVolume()))

		if self.vl >= 5 * d:
			dg.append('║░░░░░░║' + ' ' * 5 + 'Glass ' + str(glasses.index(self) + 1))
		else:
			dg.append('║      ║' + ' ' * 5 + 'Glass ' + str(glasses.index(self) + 1))

		if self.vl >= 6 * d:
			dg.append('║≈≈≈≈≈≈║')
		else:
			dg.append('║      ║')

		dg.reverse()
		for i in dg:
			p(i)


	def getVolume(self):
		return self.v


	def setVolume(self, v):
		self.v = v


	def getFill(self):
		return self.vl


	def setFill(self, vl):
		self.vl = vl


	def increase(self, n):
		if self.v >= self.vl + n:
			self.vl += n
		else:
			self.vl = self.v

	def decrease(self, n):
		if self.vl >= n:
			self.vl -= n
		else:
			self.vl = 0


def main():
	cls()
	kol = enter(text = 'Amount of glasses: ')

	for i in range(kol):
		glasses.append(glass())

	for i in range(1, kol + 1):
		v = enter(text = 'Volume of ' + str(i) + ' glass: ')
		glasses[i - 1].setVolume(v)
		vl = enter(glasses[i - 1].getVolume(), text = 'Fill of ' + str(i) + ' glass: ')
		glasses[i - 1].setFill(vl)
	
	cls()
	p()


	while True:
		for g in glasses:
			g.draw()
			p('\n\n')

		input()
		# v = enter(max = 3)


if __name__ == '__main__':
	main()