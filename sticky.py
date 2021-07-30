#!/usr/bin/python3

import sys

import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Sticky")
        self.set_default_size(200, 100)

        self.box = Gtk.VBox(spacing=6)
        self.add(self.box)

        self.label = Gtk.Label()
        sys.argv.pop(0)
        self.label.set_text(" ".join(sys.argv))
        self.box.pack_start(self.label, True, True, 0)

        self.button = Gtk.Button(label="Close")
        self.button.connect("clicked", self.on_button_clicked)
        self.button.set_property("width-request", 85)
        self.button.set_property("height-request", 15)
        self.add(self.button)
        self.box.pack_start(self.button, False, False, 0)

    def on_button_clicked(self, widget):
        self.destroy()

win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()

Gtk.main()
