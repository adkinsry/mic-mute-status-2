#!/usr/bin/env python3
import subprocess
import threading
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, Pango, GLib, GdkPixbuf
import os

class MicOverlay(Gtk.Window):
    def __init__(self, x=50, y=50):
        super().__init__(title="Mic Status Overlay")

        # Set basic window properties:
        self.set_decorated(False)
        self.set_keep_above(True)
        self.set_accept_focus(False)
        self.set_skip_taskbar_hint(True)
        self.set_skip_pager_hint(True)
        self.set_type_hint(Gdk.WindowTypeHint.UTILITY)

        # Set transparency if desired:
        self.set_app_paintable(True)
        screen = Gdk.Screen.get_default()
        visual = screen.get_rgba_visual()
        if visual is not None and self.is_composited():
            self.set_visual(visual)

        # Set fixed position:
        self.move(x, y)

        # Add drag functionality
        self.add_events(Gdk.EventMask.BUTTON_PRESS_MASK | Gdk.EventMask.BUTTON_RELEASE_MASK | Gdk.EventMask.POINTER_MOTION_MASK)
        self.connect("button-press-event", self.on_button_press)
        self.connect("button-release-event", self.on_button_release)
        self.connect("motion-notify-event", self.on_motion_notify)

        self.dragging = False
        self.drag_offset_x = 0
        self.drag_offset_y = 0

        # Create an Image widget
        self.image = Gtk.Image()
        self.add(self.image)

        self.show_all()

        # Initial update
        self.update_mute_status()

        # Start a background thread to listen for changes via pactl subscribe
        self.listener_thread = threading.Thread(target=self.listen_for_changes, daemon=True)
        self.listener_thread.start()

    def on_button_press(self, widget, event):
        if event.button == 1:  # Left mouse button
            self.dragging = True
            self.drag_offset_x = event.x
            self.drag_offset_y = event.y
            return True

    def on_button_release(self, widget, event):
        if event.button == 1:
            self.dragging = False
            return True

    def on_motion_notify(self, widget, event):
        if self.dragging:
            self.move(event.x_root - self.drag_offset_x, event.y_root - self.drag_offset_y)
            return True

    def update_mute_status(self):
        # Logic to update the mute status and change the image accordingly
        pass

    def listen_for_changes(self):
        # Logic to listen for changes in microphone status
        pass

if __name__ == "__main__":
    overlay = MicOverlay()
    Gtk.main()