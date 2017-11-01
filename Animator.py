# Author: Steven Gibson
# File: Animator.py
# Purpose: Creates an animation of a car traveling along a track

from Coaster import *

class Animator(viz.EventClass):
	
#------------------------------------------------------------------
	
	def __init__(self):
		
		viz.EventClass.__init__(self)
		
		self.callback(viz.KEYDOWN_EVENT, self.onKeyDown)
		self.callback(viz.TIMER_EVENT, self.onTimer)
		
		#creating the car track object
		self.track = Track()

		self.car = Car()
		self.time = 0
		self.degree = 90
		
		self.posInc = 0
		
#------------------------------------------------------------------
		
	def onKeyDown(self,key):
		if ( key == " " ):
			self.starttimer(0, .02, 190)
			
#------------------------------------------------------------------
			
	def onTimer(self,num):
		pos = self.car.getVals()
		
		tRad = 100
		tSides = 40
		z = 20
		
		
		if self.time <= 66: #Traveling straight along segment 1
			pos[0] += 6
			
		elif self.time > 66 and self.degree < 180: #Traveling down segment 2
			pos[0] = math.cos( math.radians(self.degree) ) * tRad * -1
			pos[1] = math.sin( math.radians(self.degree) ) * tRad
			pos[3] = -self.degree + 90
			
			pos[0] += 107
			pos[1] -= 90
			
			self.degree += 3
	
		elif self.degree >= 180 and self.degree <= 450: #Traveling down segment 3
			if self.degree == 180: #Reorienting the cart for the second curve
				self.degree = 360
			pos[0] = math.cos( math.radians(self.degree) ) * tRad * -1
			pos[1] = math.sin( math.radians(self.degree) ) * tRad * -1
			pos[3] = self.degree - 90
			
			pos[0] += 307
			pos[1] -= 90
			
			self.degree += 3
		else: #Traveling straight along segment 1
			pos[0] += 6
			
		self.car.transform(self.car.getCar(), pos[0],pos[1],pos[2],pos[3],pos[4],pos[5])
			
		self.time += 1

#------------------------------------------------------------------
	