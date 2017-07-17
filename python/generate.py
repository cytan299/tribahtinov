
"""
    generate.py is the python script for generating a Tri-Bahtinov mask
    Copyright (C) 2016  C.Y. Tan
    Contact: cytan299@yahoo.com

    This file is part of generate.py

    generate.py is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    generate.py is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with derot.  If not, see <http://www.gnu.org/licenses/>.
"""

# Acknowledgements:
# The author would like to thank Satoru Takagi for his
# contributions for improving generate.py. (25 Jun 2017)
#
"""
    7/2/2017 Extended by Satoru Takagi
    getHalfAreaPoint:
    Implemented a function to compute the boundary points so that
    the area of the region occupied by upper right slits is equal
    to that of lower right slits.

    7/17/2017 Extended by Satoru Takagi
    up_down_boundary_stem:
    Implemented boundary stem option
"""

__author__ = "C.Y. Tan"
__copyright__ = "Copyright 2016, C.Y. Tan"
__credits__ = [""]
__license__ = "GPL"
__version__ = "0.3"
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

# Tri-Bahtinov parameters that generates my 8" mask
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

# Added 07/02/2017 for area equalizer and boundary stem builder
equalize_area = False; # Flag to equalize area of right upper region and right lower region.
up_down_boundary_stem = False; # Flag to create boundary stems.
up_down_boundary_stem_ratio = 0.66; # The ratio of advance to the up side when creating boundary stems. Since the lower size of the boundary stem works somewhat as upper slot, it is set larger than half.

########################################################
# draw_slots_left(   - draws the slots on the left
#               cr   - to this context
#               )
########################################################

def draw_slots_left(cr):
  with cr:
    cr.push_group();
    
    # start drawing the slots
    spacing = (tri_stem_w + tri_w);

    y = -tri_w/2.0;
    while y < tri_out_r :
      cr.rectangle(tri_outb_r, -y, -2*tri_outb_r, -tri_w);
      y += spacing;
      
    cr.stroke();

    
    # make the mask

    cr.set_operator(cairo.OPERATOR_DEST_IN);
    cr.set_source_rgba(0,0,0,1);

    theta = atan2(tri_stem_w/2.0, tri_in_r) + pi/6.0;
    cr.move_to(-tri_in_r*cos(theta), -tri_in_r*sin(theta));
    theta = atan2(tri_stem_w/2.0, tri_out_r) + pi/6.0;
    cr.line_to(-tri_out_r*cos(theta), -tri_out_r*sin(theta));

    theta0 = pi+(atan2(tri_stem_w/2.0, tri_in_r) + pi/6.0);
    theta1 = 3*pi/2-atan2(tri_stem_w/2.0, tri_out_r);
    cr.arc(0,0, tri_out_r, theta0, theta1);

    cr.line_to(-tri_stem_w/2.0, -tri_in_r);

    theta0 = -pi/2-atan2(tri_stem_w/2.0, tri_in_r);
    theta1 = -pi+(atan2(tri_stem_w/2.0, tri_in_r) + pi/6.0);
    cr.arc_negative(0,0, tri_in_r, theta0, theta1);

    cr.fill();

    # boundaries
    cr.set_operator(cairo.OPERATOR_OVER);

    theta = atan2(tri_stem_w/2.0, tri_in_r) + pi/6.0;
    cr.move_to(-tri_in_r*cos(theta), -tri_in_r*sin(theta));
    theta = atan2(tri_stem_w/2.0, tri_out_r) + pi/6.0;
    cr.line_to(-tri_out_r*cos(theta), -tri_out_r*sin(theta));

    theta0 = pi+(atan2(tri_stem_w/2.0, tri_in_r) + pi/6.0);
    theta1 = 3*pi/2-atan2(tri_stem_w/2.0, tri_out_r);
    cr.arc(0,0, tri_out_r, theta0, theta1);

    cr.line_to(-tri_stem_w/2.0, -tri_in_r);

    theta0 = -pi/2-atan2(tri_stem_w/2.0, tri_in_r);
    theta1 = -pi+(atan2(tri_stem_w/2.0, tri_in_r) + pi/6.0);
    cr.arc_negative(0,0, tri_in_r, theta0, theta1);

    cr.stroke();

    # erase the outlines that are not required in the mask
    tri_fw=tri_stem_w;
    cr.set_operator(cairo.OPERATOR_OVER);
    cr.set_source_rgb(1,1,1);

    y = tri_w/2.0;
    while y < tri_out_r :
      cr.rectangle(tri_outb_r, -y, -2*tri_outb_r, -tri_fw);
      y += spacing;

    cr.fill();

    # make the mask again

    cr.set_operator(cairo.OPERATOR_DEST_IN);
    cr.set_source_rgba(0,0,0,1);

    theta = atan2(tri_stem_w/2.0, tri_in_r) + pi/6.0;
    cr.move_to(-tri_in_r*cos(theta), -tri_in_r*sin(theta));
    theta = atan2(tri_stem_w/2.0, tri_out_r) + pi/6.0;
    cr.line_to(-tri_out_r*cos(theta), -tri_out_r*sin(theta));

    theta0 = pi+(atan2(tri_stem_w/2.0, tri_in_r) + pi/6.0);
    theta1 = 3*pi/2-atan2(tri_stem_w/2.0, tri_out_r);
    cr.arc(0,0, tri_out_r, theta0, theta1);

    cr.line_to(-tri_stem_w/2.0, -tri_in_r);

    theta0 = -pi/2-atan2(tri_stem_w/2.0, tri_in_r);
    theta1 = -pi+(atan2(tri_stem_w/2.0, tri_in_r) + pi/6.0);
    cr.arc_negative(0,0, tri_in_r, theta0, theta1);

    cr.fill();
    
    cr.pop_group_to_source();
    cr.paint();

  return;

########################################################
# draw_slots_right_up(   - draws the slots on the upper right
#               cr   - to this context
#               )
########################################################


def draw_slots_right_up(cr):
  with cr:
    cr.push_group();
    
    # start drawing slots at 10 deg
    cr.rotate(-tri_angle);

    spacing = (tri_stem_w + tri_w);    

    udbds = 0;
    if ( up_down_boundary_stem ):
      udbds = tri_stem_w * up_down_boundary_stem_ratio;

    if ( equalize_area ):
      half_point = getHalfAreaPoint(tri_in_r, tri_out_r);
      ylast = half_point + udbds;
      ystart = half_point + spacing + udbds;
    else:
      ystart = -tri_w/2.0 + udbds;
      y = ystart;
      while y < tri_out_r:
        if ( y < ((tri_out_r + tri_in_r)/2.0 - tri_w)) :
          ylast = y;
        y += spacing;

    y = ystart;
    while y < tri_out_r:
      if ( equalize_area or y > ((tri_out_r + tri_in_r)/2.0 - tri_w)) :
        cr.rectangle(-1*INCH2PIXELS, -y, 6*INCH2PIXELS, -tri_w);
      y += spacing;

    # draw only the 3 sides of the rectangle and leave the bottom undrawn
    # find the position of this last slot

    cr.move_to(-tri_outb_r, -ylast);
    cr.line_to(-tri_outb_r, -ylast - tri_w);
    cr.line_to(2*tri_outb_r, -ylast - tri_w);
    cr.line_to(2*tri_outb_r, -ylast);
    cr.stroke();
      
      
    cr.rotate(tri_angle); # unrotate

    # make the mask

    cr.set_operator(cairo.OPERATOR_DEST_IN);
    cr.set_source_rgba(0,0,0,1);

    [xy0, xy1] = get_mask_top_boundary(ylast, tri_angle);
      
    cr.move_to(xy0[0], -xy0[1]);
    cr.line_to(tri_stem_w/2.0, -tri_out_r);

    theta0 = -pi/2+atan2(tri_stem_w/2.0, tri_out_r)
    theta1 = -atan2(xy1[1], xy1[0]);
    cr.arc(0,0, tri_out_r, theta0, theta1);

    cr.line_to(tri_stem_w/2.0, -xy0[1]);
    
    cr.fill();

    # boundaries
    cr.set_operator(cairo.OPERATOR_OVER);

    cr.move_to(xy0[0], -xy0[1]);
    cr.line_to(tri_stem_w/2.0, -tri_out_r);

    theta0 = -pi/2+atan2(tri_stem_w/2.0, tri_out_r)
    theta1 = -atan2(xy1[1], xy1[0]);
    cr.arc(0,0, tri_out_r, theta0, theta1);
 # kill last boundary (cytan)
 #   cr.line_to(tri_stem_w/2.0, -xy0[1]);    
    if ( up_down_boundary_stem ):
      cr.line_to(xy0[0], -xy0[1]);

    cr.stroke();

    # erase the outlines that are not required in the mask
    tri_fw=tri_stem_w;
    cr.set_operator(cairo.OPERATOR_OVER);
    cr.set_source_rgb(1,1,1);
    cr.rotate(-tri_angle);

    if ( equalize_area ):
      y = ystart-tri_stem_w ;
    else:
      y = tri_w/2.0 + udbds;

    while y < tri_out_r :
      cr.rectangle(-tri_outb_r, -y, 2*tri_outb_r, -tri_fw);
      y += spacing;

    cr.fill();    
    cr.rotate(tri_angle);    # unrotate

    # make the mask again

    cr.set_operator(cairo.OPERATOR_DEST_IN);
    cr.set_source_rgba(0,0,0,1);

    cr.move_to(xy0[0], -xy0[1]);
    cr.line_to(tri_stem_w/2.0, -tri_out_r);

    theta0 = -pi/2+atan2(tri_stem_w/2.0, tri_out_r)
    theta1 = -atan2(xy1[1], xy1[0]);
    cr.arc(0,0, tri_out_r, theta0, theta1);

    cr.line_to(tri_stem_w/2.0, -xy0[1]);

    cr.fill();
    
    cr.pop_group_to_source();
    cr.paint();
    
  return;

########################################################
# get_mask_top_boundary(   - calculate where the top edge boundary
#                            of the mask is given
#                  y0   - the y position of the slot (bottom edge)
#                  theta - and the rotation angle in radians
#               ) - returns the array that gives [x1,y1], [x2,y2] that
#                   defines the line of the top edge of the mask
########################################################

def get_mask_top_boundary(y0, theta):

  x1 = tri_stem_w/2.0;
  y1 = tri_stem_w/2.0*tan(theta) + y0/cos(theta);

  x2 = cos(theta)**2*sqrt((tri_out_r**2 - y0**2)/cos(theta)**2) - y0*sin(theta);
  y2 = sqrt(tri_out_r**2 - x2**2);

  return [[x1, y1], [x2, y2]];
  
  return;

########################################################
# draw_slots_right_down(   - draws the slots on the lower right
#               cr   - to this context
#               )
########################################################

def draw_slots_right_down(cr):
  with cr:
    cr.push_group();
    
    # start drawing slots at 10 deg
    cr.rotate(tri_angle);

    spacing = (tri_stem_w + tri_w);    

    udbds = 0;
    if ( up_down_boundary_stem ):
      udbds = tri_stem_w * (1.0 - up_down_boundary_stem_ratio);

    # find the position of this start and last slot
    if ( equalize_area ):
      half_point = getHalfAreaPoint(tri_in_r, tri_out_r);
      ylast = half_point - udbds;
    else:
      y = -tri_w/2.0;
      while y < tri_out_r:
        if ( y < ((tri_out_r + tri_in_r)/2.0 - tri_w)) :
          ylast = y;
        y += spacing;
      ylast -= udbds;

    y = -tri_w/2.0;
    while y < tri_out_r:
#      if (y < ((tri_out_r + tri_in_r)/2.0)) :
      cr.rectangle(-tri_outb_r, -y, 2*tri_outb_r, -tri_w);
      y += spacing;
    
    cr.stroke();
    cr.rotate(-tri_angle); # unrotate

    # make the mask

    cr.set_operator(cairo.OPERATOR_DEST_IN);
    cr.set_source_rgba(0,0,0,1);

    [xy0, xy1] = get_mask_top_boundary(ylast, tri_angle);

    cr.move_to(xy0[0], -xy0[1]);
    cr.line_to(xy1[0], -xy1[1]);

    theta0 = -atan2(xy1[1], xy1[0]);
    theta1 = -(atan2(tri_stem_w/2.0, tri_out_r) + pi/6.0);
    cr.arc(0,0, tri_out_r, theta0, theta1);

    theta = atan2(tri_stem_w/2.0, tri_in_r) + pi/6.0;
    cr.line_to(tri_in_r*cos(theta), -tri_in_r*sin(theta));

    theta0 = -(atan2(tri_stem_w/2.0, tri_in_r) + pi/6);
    theta1 = -pi/2 + atan2(tri_stem_w/2.0, tri_in_r);
    cr.arc_negative(0,0, tri_in_r, theta0, theta1);
    
    cr.line_to(tri_stem_w/2.0, -xy0[1]);    

    cr.fill();

    # boundaries
    cr.set_operator(cairo.OPERATOR_OVER);

    if ( up_down_boundary_stem ):
      cr.move_to(xy0[0], -xy0[1]);
      cr.line_to(xy1[0], -xy1[1]);
    else:
      cr.move_to(xy1[0], -xy1[1]);
 
    theta0 = -atan2(xy1[1], xy1[0]);
    theta1 = -(atan2(tri_stem_w/2.0, tri_out_r) + pi/6.0);
    cr.arc(0,0, tri_out_r, theta0, theta1);

    theta = atan2(tri_stem_w/2.0, tri_in_r) + pi/6.0;
    cr.line_to(tri_in_r*cos(theta), -tri_in_r*sin(theta));

    theta0 = -(atan2(tri_stem_w/2.0, tri_in_r) + pi/6);
    theta1 = -pi/2 + atan2(tri_stem_w/2.0, tri_in_r);
    cr.arc_negative(0,0, tri_in_r, theta0, theta1);

    cr.line_to(tri_stem_w/2.0, -xy0[1]);
    
    cr.stroke();
    
    # erase the outlines that are not required in the mask
    tri_fw=tri_stem_w;
    cr.set_operator(cairo.OPERATOR_OVER);
    cr.set_source_rgb(1,1,1);
    cr.rotate(tri_angle);

    y = tri_w/2.0;
    while y < tri_out_r :
      cr.rectangle(-tri_outb_r, -y, 2*tri_outb_r, -tri_fw);
      y += spacing;
    

    cr.fill();
    cr.rotate(-tri_angle);

    #
    if ( not up_down_boundary_stem ):
      cr.set_operator(cairo.OPERATOR_XOR);
      cr.set_source_rgba(0,0,0,1);
      [xy0, xy1] = get_mask_top_boundary(ylast, tri_angle);
      cr.move_to(xy0[0], -xy0[1]);
      cr.line_to(xy1[0], -xy1[1]);
      cr.set_line_width(3);    
      cr.stroke();
      
      cr.set_operator(cairo.OPERATOR_XOR);    
      cr.set_source_rgba(0,0,0,1);
      [xy0, xy1] = get_mask_top_boundary(ylast, tri_angle);
      cr.move_to(xy0[0], -xy0[1]);
      cr.line_to(xy1[0], -xy1[1]);
      cr.set_line_width(3);
      cr.stroke();
    
    cr.set_line_width(1);

    
    # make the mask again

    cr.set_operator(cairo.OPERATOR_DEST_IN);
    cr.set_source_rgba(0,0,0,1);
    
    [xy0, xy1] = get_mask_top_boundary(ylast, tri_angle);
      
    cr.move_to(xy0[0], -xy0[1]);
    cr.line_to(xy1[0], -xy1[1]);

    theta0 = -atan2(xy1[1], xy1[0]);
    theta1 = -(atan2(tri_stem_w/2.0, tri_out_r) + pi/6.0);
    cr.arc(0,0, tri_out_r, theta0, theta1);

    theta = atan2(tri_stem_w/2.0, tri_in_r) + pi/6.0;
    cr.line_to(tri_in_r*cos(theta), -tri_in_r*sin(theta));

    theta0 = -(atan2(tri_stem_w/2.0, tri_in_r) + pi/6);
    theta1 = -pi/2 + atan2(tri_stem_w/2.0, tri_in_r);
    cr.arc_negative(0,0, tri_in_r, theta0, theta1);

    cr.line_to(tri_stem_w/2.0, -xy0[1]);
    

    cr.fill();    

    cr.rotate(-tri_angle);    # unrotate

    cr.pop_group_to_source();
    cr.paint();
    
  return;

########################################################
# draw_mounting_holes(   - draws the mounting holes of the mask
#               cr   - to this context
#               )
########################################################

def draw_mounting_holes(cr):
  with cr:
    cr.push_group();
    
    cr.set_line_width(2);    
    cr.set_operator(cairo.OPERATOR_OVER);
    cr.set_source_rgb(0, 0, 0)  # black
    cr.arc(0,-(tri_out_r+(tri_outb_r - tri_out_r)/2.0), tri_mount_hole_r, 0,2*pi);
    cr.stroke();
    
    cr.pop_group_to_source();
    cr.paint();

  return;

########################################################
# draw_inner_boundary( - draws the inner boundary of the mask
#               cr   - to this context
#               )
########################################################

def draw_inner_boundary(cr):
  with cr:
    cr.push_group();

    cr.set_line_width(2);    
    cr.set_operator(cairo.OPERATOR_OVER);
    cr.set_source_rgb(0, 0, 0)  # black

    notch_sz = tri_stem_w/2.0;

    # draw rectangular notches
    # top notch
    theta = asin(notch_sz/(2.0*tri_inb_r));
    cr.move_to(tri_inb_r*sin(theta), -tri_inb_r*cos(theta));
    cr.line_to(tri_inb_r*sin(theta), -(tri_inb_r*cos(theta)+notch_sz));

    cr.line_to(-notch_sz/2.0, -(tri_inb_r*cos(theta)+notch_sz));
    cr.line_to(-tri_inb_r*sin(theta), -tri_inb_r*cos(theta));
    cr.stroke();

    cr.arc(0,0, tri_inb_r, -(pi/2-theta), pi/6.0 - theta);
    cr.stroke();

    # notch on right
    cr.rotate(2*pi/3.0);
    cr.move_to(tri_inb_r*sin(theta), -tri_inb_r*cos(theta));
    cr.line_to(tri_inb_r*sin(theta), -(tri_inb_r*cos(theta)+notch_sz));

    cr.line_to(-notch_sz/2.0, -(tri_inb_r*cos(theta)+notch_sz));
    cr.line_to(-tri_inb_r*sin(theta), -tri_inb_r*cos(theta));
    cr.stroke();

    cr.arc(0,0, tri_inb_r, -(pi/2-theta), pi/6.0-theta);
    cr.stroke();

    # notch on left
    cr.rotate(2*pi/3.0);
    cr.move_to(tri_inb_r*sin(theta), -tri_inb_r*cos(theta));
    cr.line_to(tri_inb_r*sin(theta), -(tri_inb_r*cos(theta)+notch_sz));

    cr.line_to(-notch_sz/2.0, -(tri_inb_r*cos(theta)+notch_sz));
    cr.line_to(-tri_inb_r*sin(theta), -tri_inb_r*cos(theta));
    cr.stroke();

    cr.arc(0,0, tri_inb_r, -(pi/2-theta), pi/6.0-theta);
    cr.stroke();        
    
    cr.pop_group_to_source();
    cr.paint();

  return;

########################################################
# A function that calculates the boundary line starting point 
# so that the areas of right upper slits and lower slits are
# equal (06/13/2017 by Satoru Takagi)
# A description of this equation can be found in areaEqualize.pdf.
# This function uses the Bisection Method to obtain an approximate
# solution of the nonlinear equation for this matter.
########################################################
def getHalfAreaPoint(rInner, rOuter):
  theta = getTheta(rInner, rOuter);
  point = getL(theta,rInner, rOuter);
  return ( point );

def getTheta(ri,ro):
  tu = pi / 3.0;
  td = 0.0;
  # Bisection Method : assume that it converged in 30 iterations...
  for i in range(0, 30): 
    tc = (tu + td)/2.0;
    difu = getPointDif(tu , ri , ro );
    difc = getPointDif(tc , ri , ro );
    difd = getPointDif(td , ri , ro );
    
    if ( difu * difc < 0 ):
      tu = tu;
      td = tc;
    else :
      tu = tc;
      td = td;
  return ( tc );

def getPointDif(theta,ri,ro):
  ans = theta - sin(theta) * cos(theta) + sin(theta) * sin(theta) * tan( 10.0 * pi / 180.0 ) - ( pi / 6.0 ) * ( 1.0 - ( ri * ri ) / ( ro * ro ) ) ;
  return ( ans );

def getL(theta,ri,ro):
  ans = ro * ( cos(theta) - sin(theta) * tan( 10.0 * pi / 180.0 ) );
  return ( ans );

########################################################
# main entry point
########################################################

########################################################
# User interface to get relevant parameters
########################################################

# clear screen
os.system("cls" if os.name == "nt" else "clear");

# then get the user input
focal_length = input("Enter focal length of the telescope in mm = ");
print "focal length = ", focal_length, " mm"
focal_length = focal_length/25.4*INCH2PIXELS; # convert to inches

fixed_stem = raw_input("Do you use fixed stem width? (y/N):");
if ( fixed_stem == "y" ) :
    w_stem_ratio = 0;
    print "fixed stem width:",tri_stem_w/INCH2PIXELS,"in";
else:
    set_stem_ratio = raw_input("Do you set slit:stem ratio? (y/N):");
    if ( set_stem_ratio == "y" ) :
        w_stem_ratio = input("Enter slit:stem ratio 1:");
    else:
        w_stem_ratio = 1;
    print "slit:stem = 1:",w_stem_ratio;

equalize_area_input = raw_input("Do you equalize areas of right upper/lower region? (y/N):");
if ( equalize_area_input == "y" ) :
  equalize_area = True;

boundary_stem_input = raw_input("Do you build boundary stem? (y/N):");
if ( boundary_stem_input == "y" ) :
  up_down_boundary_stem = True;

spacing = focal_length/BAHTINOV_FACTOR;
if ( w_stem_ratio == 0 ):
    if ( spacing - tri_stem_w > tri_stem_w * 0.5 ) :
        tri_w = spacing - tri_stem_w
    else:
        tri_w = spacing / 3;
        tri_stem_w = 2 * spacing / 3;
else:
    tri_w = spacing / ( w_stem_ratio + 1 );
    tri_stem_w = w_stem_ratio * spacing / ( w_stem_ratio + 1 );

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
surface = cairo.PDFSurface('tribahtinov.pdf', PAPER_MAX_X, PAPER_MAX_Y);
cr = cairo.Context(surface)
with cr:
    cr.set_source_rgba(1, 1, 1,0)  # transparent
    cr.paint()
# Restore the default source which is black.

# set up the surface area and the origin
cr.translate(PAPER_MAX_X/2.0, PAPER_MAX_Y/2.0);
cr.set_line_width(3);

#
# Draw the slots
#
draw_slots_left(cr);
draw_slots_right_up(cr);
draw_slots_right_down(cr);
draw_mounting_holes(cr);

cr.rotate(2*pi/3.0);
draw_slots_left(cr);
draw_slots_right_up(cr);
draw_slots_right_down(cr);
draw_mounting_holes(cr);

cr.rotate(2*pi/3.0);
draw_slots_left(cr);
draw_slots_right_up(cr);
draw_slots_right_down(cr);
draw_mounting_holes(cr);

# rotate back to zero position
cr.rotate(2*pi/3.0);

#
# Draw the inner and outer boundaries of the mask
#
cr.set_operator(cairo.OPERATOR_OVER);
cr.set_source_rgb(0, 0, 0)  # black
cr.arc(0,0, tri_outb_r, 0,2*pi);
cr.stroke();
#cr.arc(0,0, tri_inb_r, 0,2*pi);
#cr.stroke();
draw_inner_boundary(cr);

#
# Now put the entire surface onto a white background
#
cr.set_operator(cairo.OPERATOR_DEST_OVER);
cr.set_source_rgb(1,1,1);
cr.paint();

#
# Also draw out a png file
#
surface.write_to_png('tribahtinov.png')
#
# and an svg file
#
svg_surface = cairo.SVGSurface('tribahtinov.svg', PAPER_MAX_X, PAPER_MAX_Y);
cr_svg = cairo.Context(svg_surface);
cr_svg.set_source_surface(surface, 0, 0);
cr_svg.paint();

