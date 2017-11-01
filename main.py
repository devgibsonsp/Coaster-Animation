# Author: Steven Gibson
# File: main.py
# Purpose: Constructs the viewing window and builds the scene

import viz
import vizshape
import vizcam
from Animator import *

# set size (in pixels) and title of application window
viz.window.setSize( 500, 500 )
viz.window.setName( "Coaster" )

viz.window.setSize( 800, 800 )


# get graphics window
window = viz.MainWindow
# setup viewing volume
window.ortho(-700,700,-700,700,-700,700)
# set background color of window to very light gray 
viz.MainWindow.clearcolor( [.66,.75,1] ) 

# center viewpoint 
viz.eyeheight(0)



pivotNav = vizcam.PivotNavigate()

a = Animator()

viz.disable(viz.CULL_FACE)

# render the scene in the window
viz.go()