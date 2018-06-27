
"""
    cover.py is the python script for generating slot covers for the
    Tri-Bahtinov mask

    Copyright (C) 2018  C.Y. Tan
    Contact: cytan299@yahoo.com

    This file is part of cover.py

    cover.py is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    cover.py is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with derot.  If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = "C.Y. Tan"
__copyright__ = "Copyright 2018, C.Y. Tan"
__credits__ = [""]
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "C.Y. Tan"
__email__ = "cytan299@yahoo.com"
__status__ = "alpha"

from math import *;

import os;
import platform;

#######################################################
# Initialization code
####################################################### 

#
# We have to set the library path to where the python cairo library lives.
# This depends on the OS
# For Mac OS X:
# In order to import cairocffi, I have to do the following on Mac OS X:
# The environment variable DYLD_FALLBACK_LIBRARY_PATH has to be set up here
# because using
#    export DYLD_FALLBACK_LIBRARY_PATH=/opt/local/lib
# in a sh script does *NOT* work!
# 
if (platform.uname()[0] == "Darwin"):
  os.environ["DYLD_FALLBACK_LIBRARY_PATH"] = "/opt/local/lib";
  import cairocffi as cairo;

if (platform.uname()[0] == "Linux"):
  import cairocffi as cairo;

if(platform.uname()[0] == "Windows"):
  os.environ["PATH"] = os.environ["PATH"]+";c:\\GTK\\bin";
  import cairocffi as cairo;

# Conversion constants

INCH2PIXELS = 72; #convert 1 inch to pixels
BAHTINOV_FACTOR = 150;

#
# Angles in CAIRO are measured from the x-axis. 0 is x-axis
# Positive angles are clockwise going towards -y axis
#j 0 degrees is +x axis
# +90 degress is -y axis
# +180 degrees is -x axis
# +270 degrees is +y axis

#
# These "constants" will be changed by the user
#

# Paper constants
PAPER_MAX_X = 11*INCH2PIXELS;
PAPER_MAX_Y = 11*INCH2PIXELS;

# Tri-Bahtinov parameters that covers my 8" mask
tri_outb_r = 4.4375*INCH2PIXELS; # inches, outer boundary radius 
tri_inb_r = 1.4375*INCH2PIXELS;  # inches, inner boundary radius

tri_out_r = 4.00*INCH2PIXELS; # inches, tribahtinov mask outer radius
tri_in_r = 1.6737*INCH2PIXELS; # inches, tribahtinov mask inner radius

tri_w = 0.3071*INCH2PIXELS; # inches, width of each slit

# constants that the user does not change
tri_stem_w = 0.2362*INCH2PIXELS; # inches, width of each supporting stem
tri_out_w = 0.4375*INCH2PIXELS; # inches, width of the outer support
tri_in_w = 0.2362*INCH2PIXELS; # inches, width of the inner support

tri_mount_hole_r = 0.075*INCH2PIXELS; # mounting hole size

tri_angle = 10*pi/180; # radians

########################################################
# draw_mounting_holes(   - draws the mounting holes of the mask
#               cr   - to this context
#               )
########################################################

def draw_mounting_holes(cr):
  with cr:
    cr.push_group();
    
    cr.set_line_width(3);    
    cr.set_operator(cairo.OPERATOR_OVER);
    cr.set_source_rgb(0, 0, 0)  # black

    # draw the curve part
    mount_hole_r = 1.5*tri_mount_hole_r;
    cr.arc(0,-(tri_out_r+(tri_outb_r - tri_out_r)/2.0), mount_hole_r, 0,pi);
    cr.stroke();

    # draw sides of the slot
    phi = acos(mount_hole_r/tri_outb_r);
    cr.move_to(mount_hole_r,-(tri_out_r+(tri_outb_r - tri_out_r)/2.0));
    cr.line_to(mount_hole_r,-tri_outb_r*sin(phi));
    cr.stroke();
    cr.move_to(-mount_hole_r,-(tri_out_r+(tri_outb_r - tri_out_r)/2.0));
    cr.line_to(-mount_hole_r,-tri_outb_r*sin(phi));
    cr.stroke();

    # erase the outside edge of the slot
    cr.set_source_rgb(1, 1, 1);
    cr.set_line_width(3.5);        
    theta = pi/2-phi;
    cr.arc(0,0, tri_outb_r, (3*pi/2-theta),(3*pi/2+theta));
    cr.stroke();
    
    cr.pop_group_to_source();
    cr.paint();

  return;




########################################################
# main entry point
########################################################

########################################################
# User interface to get relevant parameters
########################################################

# clear screen
os.system("cls" if os.name == "nt" else "clear");

# then get the user input
tri_outb_r = input("Enter outer radius of mask in inches = ");
print "tri_outb_r = ", tri_outb_r, " inches";
tri_outb_r *= INCH2PIXELS;

tri_inb_r = input("Enter inner radius of mask in inches = ");
print "tri_inb_r = ", tri_inb_r, " inches";
tri_inb_r *= INCH2PIXELS;

#
# Derive all other parameters from the user input
#
PAPER_MAX_X = (2*tri_outb_r)*1.2;
PAPER_MAX_Y = (2*tri_outb_r)*1.2;

tri_out_r = tri_outb_r - tri_out_w;
tri_in_r = tri_inb_r + tri_in_w;

#######################################################
# Define the CAIRO surface and context that will be drawn to
#######################################################
surface = cairo.PDFSurface('cover.pdf', PAPER_MAX_X, PAPER_MAX_Y);
cr = cairo.Context(surface)
with cr:
    cr.set_source_rgba(1, 1, 1,0)  # transparent
    cr.paint()
# Restore the default source which is black.

# set up the surface area and the origin
cr.translate(PAPER_MAX_X/2.0, PAPER_MAX_Y/2.0);
cr.set_line_width(3);

#
# Draw a outer and inner circle, and then join them
#
## draw two arcs first
cr.arc(0,0, tri_outb_r, 330*pi/180., 210*pi/180.);
cr.stroke();
cr.arc(0,0, tri_inb_r, 330*pi/180., 210*pi/180.);
cr.stroke();
## draw lines to connect the two arcs
theta = 30*pi/180.0; # 
cr.move_to(tri_inb_r*cos(theta), -tri_inb_r*sin(theta));
cr.line_to(tri_outb_r*cos(theta), -tri_outb_r*sin(theta));
cr.stroke();

cr.move_to(-tri_inb_r*cos(theta), -tri_inb_r*sin(theta));
cr.line_to(-tri_outb_r*cos(theta), -tri_outb_r*sin(theta));
cr.stroke();

# draw out the mounting holes
cr.rotate(2*pi/3.0);
draw_mounting_holes(cr);
cr.rotate(2*pi/3.0);
draw_mounting_holes(cr);

# rotate back to zero position
cr.rotate(2*pi/3.0);


#
# Now put the entire surface onto a white background
#
cr.set_operator(cairo.OPERATOR_DEST_OVER);
cr.set_source_rgb(1,1,1);
cr.paint();

#
# Also draw out a png file
#
surface.write_to_png('cover.png')
#
# and an svg file
#
svg_surface = cairo.SVGSurface('cover.svg', PAPER_MAX_X, PAPER_MAX_Y);
cr_svg = cairo.Context(svg_surface);
cr_svg.set_source_surface(surface, 0, 0);
cr_svg.paint();

