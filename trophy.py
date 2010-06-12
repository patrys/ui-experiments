#!/usr/bin/env python

import gtk
import os
import pynotify

ICON_FILE = os.path.join(os.path.dirname(__file__), 'assets', 'trophy.png')

pynotify.init('UI Experiments')
pixbuf = gtk.gdk.pixbuf_new_from_file(ICON_FILE)
notification = pynotify.Notification('You have earned a trophy.', 'Run GNOME for 1 day')
notification.set_icon_from_pixbuf(pixbuf)
notification.show()
