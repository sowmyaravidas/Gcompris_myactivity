#  gcompris - smya.py
#
# Copyright (C) 2003, 2008 Bruno Coudoin
#
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, see <http://www.gnu.org/licenses/>.
#
# smya activity.
import gtk
import gtk.gdk
import gcompris
import gcompris.utils
import gcompris.skin
import gcompris.bonus
import gcompris.sound
import gobject
import goocanvas
import pango
import cairo
import math



from gcompris import gcompris_gettext as _

class Gcompris_smya:
  """The practice activity"""


  def __init__(self, gcomprisBoard):
    print "smya init"

        # Save the gcomprisBoard, it defines everything we need
    # to know from the core
    self.gcomprisBoard = gcomprisBoard

    # Needed to get key_press
    gcomprisBoard.disable_im_context = True
    self.rootitem = None 

  def start(self):
    print "smya start"
    self.gcomprisBoard.level=1
    self.gcomprisBoard.maxlevel = 2
    self.gcomprisBoard.sublevel = 1
    self.gcomprisBoard.number_of_sublevel=1
    # Set the buttons we want in the bar
    # gcompris.bar_set(gcompris.BAR_LEVEL)
    #gcompris.bar_set_level(self.gcomprisBoard)
    self.backroot = goocanvas.Group(parent = \
        self.gcomprisBoard.canvas.get_root_item())
    gcompris.bar_set(gcompris.BAR_LEVEL)
    gcompris.bar_set_level(self.gcomprisBoard)

    # Set a background image
    #    gcompris.set_default_background(self.gcomprisBoard.canvas.get_root_item())


    # Create our rootitem. We put each canvas item in it so at the end we
    # only have to kill it. The canvas deletes all the items it contains
    # automaticaly.
    
    self.rootitem = goocanvas.Group(parent = self.gcomprisBoard.canvas.get_root_item())
    #svghandle = gcompris.utils.load_svg("/smya/index.jpeg")
    




    pic = goocanvas.Image(
      parent = self.rootitem,
      pixbuf = gcompris.utils.load_pixmap("smya/index.jpeg"),
      x = 475,
      y = 225,
      width = 160,
      height = 160)
  
    pic.connect("button_press_event", self.pic_event) 
    
    
    txt = goocanvas.Text(
      parent = self.rootitem,
      x=400.0,
      y=100.0,
      text=("Welcome dear children\n"
            "This is a trial \n"
            "Click on any object to change the background color"),
      fill_color="white",
      anchor = gtk.ANCHOR_CENTER,
      alignment = pango.ALIGN_CENTER
      )
  
    txt.connect("button_press_event", self.txt_event)    
    
      #GooCanvasItem *ellipse = goo_canvas_ellipse_new (mygroup, 100.0, 100.0, 50.0, 30.0,
       #                                                "stroke-color", "red",
      #"line-width", 5.0,
      #                                              "fill-color", "blue",
       #                                             NULL);

    el = goocanvas.Ellipse(
      parent=self.rootitem,
      center_x=100,
      center_y=100,
      radius_x=50,
      radius_y=30,
      stroke_color="red",
      fill_color="blue",
      line_width=5.0) 

    el.connect("button_press_event", self.el_event)

    rec = goocanvas.Rect(
      parent=self.rootitem,
      x=650,
      y=70,
      height=100,
      width=100,
      stroke_color="black",
      fill_color="green",
      line_width=5.0)
   
    rec.connect("button_press_event", self.rec_event)

    
    path = goocanvas.Path(
      parent=self.rootitem,
      data="M 10 240 L 170 240", 
      stroke_color="orange")
     
    path.connect("button_press_event", self.path_event)   

    item = goocanvas.Rect(
      parent = self.backroot,
      x = 0,
      y = 0,
      width = gcompris.BOARD_WIDTH,
      height = 900,
      fill_color = "pink"
      )
      

  def el_event (self, el, target, event):
    if event.type == gtk.gdk.BUTTON_PRESS:
        item = goocanvas.Rect(
        parent = self.backroot,
        x = 0,
        y = 0,
        width = gcompris.BOARD_WIDTH,
        height = 900,
        fill_color = "yellow"
        )

  def rec_event (self, rec, target, event):
    if event.type == gtk.gdk.BUTTON_PRESS:
        item = goocanvas.Rect(
        parent = self.backroot,
        x = 0,
        y = 0,
        width = gcompris.BOARD_WIDTH,
        height = 900,
        fill_color = "green"
        )

  def path_event (self, path, target, event):
    if event.type == gtk.gdk.BUTTON_PRESS:
        item = goocanvas.Rect(
        parent = self.backroot,
        x = 0,
        y = 0,
        width = gcompris.BOARD_WIDTH,
        height = 900,
        fill_color = "red"
        )

  def pic_event (self, pic, target, event):
      if event.type == gtk.gdk.BUTTON_PRESS:
          item = goocanvas.Rect(
          parent = self.backroot,
          x = 0,
          y = 0,
          width = gcompris.BOARD_WIDTH,
          height = 900,
          fill_color = "blue"
          )


  def txt_event (self, txt, target, event):
    if event.type == gtk.gdk.BUTTON_PRESS:
        item = goocanvas.Rect(
        parent = self.backroot,
        x = 0,
        y = 0,
        width = gcompris.BOARD_WIDTH,
        height = 900,
        fill_color = "white"
        )


  def item_event (self, item, target, event):
    if event.type == gtk.gdk.BUTTON_PRESS:
        item = goocanvas.Rect(
        parent = self.backroot,
        x = 0,
        y = 0,
        width = gcompris.BOARD_WIDTH,
        height = 900,
        fill_color = "pink"
        )


  def end(self):
    print "smya end"
    # Remove the root item removes all the others inside it
    self.rootitem.remove()
    self.backroot.remove()
    self.backroot = None
    self.rootitem = None



  def ok(self):
    print("smya ok.")


  def repeat(self):
    print("smya repeat.")


  #mandatory but unused yet
  def config_stop(self):
    pass

  # Configuration function.
  def config_start(self, profile):
    print("smya config_start.")

  def key_press(self, keyval, commit_str, preedit_str):
    utf8char = gtk.gdk.keyval_to_unicode(keyval)
    strn = u'%c' % utf8char

    print("Gcompris_smya key press keyval=%i %s" % (keyval, strn))

  def pause(self, pause):
    print("smya pause. %i" % pause)

  def set_level(self,level):
    self.gcomprisBoard.level = level
    self.gcomprisBoard.sublevel = 1
    gcompris.bar_set_level(self.gcomprisBoard)
    self.display_level(self.gcomprisBoard.level)



   


