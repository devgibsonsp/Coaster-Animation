# Author: Steven Gibson
# File: Coaster.py
# Purpose: Construct the car and track segments that make up the coaster
# Contains the Car class and Track class for the creation of the coaster.
import viz
import vizshape
import math

#------------------------------------------------------------------

class Car:
	
	def __init__(self):

		# Node to store all car pieces
		self.groupNode = viz.addGroup()
		
		# # # # # # Constructing the car model! # # # # # #
		base = vizshape.addBox(size=(40,10,20),top = False)
		nose = vizshape.addBox(size=(6,8,20))
		divider = vizshape.addBox(size=(2,10,20))
		seat1 = vizshape.addBox(size=(10,4,19))
		seat2 = vizshape.addBox(size=(10,4,19))
		floor = vizshape.addBox(size=(40,.5,20))
		back = vizshape.addBox(size=(6,6,6))
		pole = vizshape.addCylinder(height=15, radius=1, axis=vizshape.AXIS_Y, slices=6)	
		flag = vizshape.addBox(size=(6,6,.5))
		axle1 = vizshape.addCylinder(height=20, radius=2, axis=vizshape.AXIS_Y, slices=6)
		axle2 = vizshape.addCylinder(height=20, radius=2, axis=vizshape.AXIS_Y, slices=6)
		wheelLB = vizshape.addTorus(radius=3.0, tubeRadius=2, sides = 3, slices = 12, axis = vizshape.AXIS_X)
		wheelRB = vizshape.addTorus(radius=3.0, tubeRadius=2, sides = 3, slices = 12, axis = vizshape.AXIS_X)
		wheelLF = vizshape.addTorus(radius=3.0, tubeRadius=2, sides = 3, slices = 12, axis = vizshape.AXIS_X)
		wheelRF = vizshape.addTorus(radius=3.0, tubeRadius=2, sides = 3, slices = 12, axis = vizshape.AXIS_X)
		# # # # # # # # # # # # # # # # # # # # # # # # # #
		
		#setting colors
		base.color(viz.BLUE)
		nose.color(viz.BLUE)
		floor.color(viz.BLUE)
		divider.color(viz.ORANGE)
		seat1.color(viz.ORANGE)
		seat2.color(viz.ORANGE)
		back.color(viz.ORANGE)
		flag.color(viz.WHITE)
		wheelLB.color(viz.BLACK)
		wheelRB.color(viz.BLACK)
		wheelLF.color(viz.BLACK)
		wheelRF.color(viz.BLACK)
		
		#setting all car pieces to group node
		base.setParent(self.groupNode)
		nose.setParent(self.groupNode)
		divider.setParent(self.groupNode)
		seat1.setParent(self.groupNode)
		seat2.setParent(self.groupNode)
		floor.setParent(self.groupNode)
		back.setParent(self.groupNode)
		pole.setParent(self.groupNode)
		flag.setParent(self.groupNode)
		axle1.setParent(self.groupNode)
		axle2.setParent(self.groupNode)
		wheelLB.setParent(self.groupNode)
		wheelRB.setParent(self.groupNode)
		wheelLF.setParent(self.groupNode)
		wheelRF.setParent(self.groupNode)
		
		#transforming axles
		self.transform(axle1, -12, -6, 0, 90, 0, 90)
		self.transform(axle2, 12, -6, 0, 90, 0, 90)
		
		#transforming wheels
		self.transform(wheelLB, -12, -6, 10, 0, 0, 90)
		self.transform(wheelRB, -12, -6, -10, 0, 0, 90)
		self.transform(wheelLF, 12, -6, 10, 0, 0, 90)
		self.transform(wheelRF, 12, -6, -10, 0, 0, 90)
		
		#transforming misc car parts
		self.transform(nose, 23, -1, 0, 0, 0, 0)
		self.transform(seat1, -15, -1, 0, 0, 0, 0)
		self.transform(seat2, 5, -1, 0, 0, 0, 0)
		self.transform(floor, 0, -2, 0, 0, 0, 0)
		self.transform(back, -23, 0, 0, 0, 0, 0)
		self.transform(pole, -23, 10, 0, 0, 0, 0)
		self.transform(flag, -26, 14, 0, 0, 0, 0)
		
		#setting car default location values
		self.x = -300
		self.y = 11
		self.z = 10
		self.a = 0
		self.b = 0
		self.c = 0
		
		#transforming car to default location
		self.transform(self.groupNode, self.x, self.y, self.z, self.a, self.b, self.c)
		
#------------------------------------------------------------------
		
	def transform(self, object, x, y, z, a, b,c):
		m = viz.Matrix()
		m.postAxisAngle(0, 0, 1, a)
		m.postAxisAngle(1, 0, 0, b)
		m.postAxisAngle(0, 1, 0, c)
		m.postTrans(x, y, z)
		
		self.x = x
		self.y = y
		self.z = z
		self.a = a
		self.b = b
		self.c = c

		object.setMatrix(m)
		
#------------------------------------------------------------------
	
	#returns the car node
	def getCar(self):
		return self.groupNode
		
#------------------------------------------------------------------
	
	#returns the location value of the car
	def getVals(self):
		return [self.x, self.y, self.z, self.a, self.b, self.c]
		
#==================================================================
		
class Track(viz.EventClass):

	#################################################################
	# NOTE: I've done a little more storing of track pieces than is #
	# probably necessary, I've done this so that I have individual  #
	# access to each segment. The reason for this is to have the    #
	# ability to easily create animations involving the destruction # 
	# of track segments.                                            #
	#################################################################
	#			superGroup			  # In addition to this structure,
	#         /    | |     \		  # each individual segment is 
	#       /     |   |      \		  # stored in a list so that ind-
	#     /      |     |       \	  # ividual transformations can
	# segGrp1 segGrp2 segGrp3 segGrp4 # be done to individual track
	################################### pieces
	
	# Constructor 
	def __init__(self):

		
		x = 0
		y = 0
		z = 0

		trackLen = 20
		#Creating a list to store group nodes of track segments
		
		#super group to store all group nodes
		self.superGroup = viz.addGroup()
		
		#creating the lists to store all corresponding track segment groups
		self.gNodeList1 = []
		self.gNodeList2 = []
		self.gNodeList3 = []
		self.gNodeList4 = []
		
		#creating the groups to store all track "pieces" 
		self.segGrp1 = viz.addGroup()
		self.segGrp2 = viz.addGroup()
		self.segGrp3 = viz.addGroup()
		self.segGrp4 = viz.addGroup()
		
		self.segGrp1.setParent(self.superGroup)
		self.segGrp2.setParent(self.superGroup)
		self.segGrp3.setParent(self.superGroup)
		self.segGrp4.setParent(self.superGroup)
		
		# Creating the piece 1's segments
		for i in range(0,trackLen):
			# Creating the parent node for each track segment
			gNode = viz.addGroup()
			gNode.setParent(self.segGrp1)
			self.gNodeList1.append(gNode)
			
			for j in range(0,3):
				self.segment(x,y,z,90,90,0,self.gNodeList1)
			x += 20
			
		# setting the values for the circle
		tRad = 100
		tSides = 40
		z = 20
		
		for i in range(0, 360, 360/tSides):
			if i >= 0 and i <= 90:
				x = math.cos( math.radians(i) ) * tRad 
				y = math.sin( math.radians(i) ) * tRad 
				gNode = viz.addGroup()
				gNode.setParent(self.segGrp2)
				self.gNodeList2.append(gNode)
				self.segment(x,y,z,0,-i, 90,self.gNodeList2)
			
		#positioning piece 2's segments in the appropriate position
		self.transform(self.segGrp2,400,-tRad,0,0,0,0)
		
		for i in range(0, 360, 360/tSides):
			if i >= 180 and i <= 270:
				x = math.cos( math.radians(i) ) * tRad 
				y = math.sin( math.radians(i) ) * tRad 
				gNode = viz.addGroup()
				gNode.setParent(self.segGrp3)
				self.gNodeList3.append(gNode)
				self.segment(x,y,z,0,-i, 90,self.gNodeList3)
				
		#positioning piece 3's segments in the appropriate position
		self.transform(self.segGrp3,400+(tRad*2),-tRad,0,0,0,0)

		x = 620
		y = -200
		z = 0

		# Creating the piece 4's segments
		for i in range(0,trackLen):
			# Creating the parent node for each track segment
			gNode = viz.addGroup()
			gNode.setParent(self.segGrp4)
			self.gNodeList4.append(gNode)
			
			for j in range(0,3):
				self.segment(x,y,z,90,90,0,self.gNodeList4)
			x += 20

		#positioning the entire track more appropriately in the viewfield
		self.transform(self.superGroup,-300,0,0,0,0,0)
			
#------------------------------------------------------------------

	#Creates a single track segment and orients it in the x y plane
	def segment(self,x,y,z,a,b,c,list):
		for j in range(0,3):
			if j == 0:
				bar = vizshape.addCylinder(height=20, radius=1, axis=vizshape.AXIS_Y, slices=4)
				bar.color(viz.ORANGE)
			elif j == 1:
				bar = vizshape.addCylinder(height=20, radius=1, axis=vizshape.AXIS_Y, slices=4)
				self.transform(bar, 20, 0, 0, 0, 0, 0)
				bar.color(viz.ORANGE)
			elif j == 2:
				bar = vizshape.addCylinder(height=20, radius=1, axis=vizshape.AXIS_Y, slices=4)
				self.transform(bar, 10, 0, 0, 90, 0, 0)
				bar.color(viz.BLUE)
				self.transform(list[len(list)-1], x, y, z, a,b,c)
			bar.setParent(list[len(list)-1])

#------------------------------------------------------------------	

	# Allows for xyz transformations and rotations around xyz axis'
	def transform(self, object, x, y, z, a, b,c):
		m = viz.Matrix()
		m.postAxisAngle(0, 0, 1, a)
		m.postAxisAngle(1, 0, 0, b)
		m.postAxisAngle(0, 1, 0, c)
		m.postTrans(x, y, z)
		object.setMatrix(m)
		
#------------------------------------------------------------------