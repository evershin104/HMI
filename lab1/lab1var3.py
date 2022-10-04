from ast import In
from unicodedata import decimal
import gi
from locale import atof, format_string


gi.require_version('Gtk', '3.0')


from gi.repository import Gtk as Gtk
from decimal import Decimal, InvalidOperation


class Main:
    
    
    '''Whole window class'''
    def __init__(self):
        '''Inits elements on main window'''
        gladeFile = 'lab1var3.glade'
        self.builder = Gtk.Builder()
        self.builder.add_from_file(gladeFile)

        window = self.builder.get_object('main_window')
        window.connect('delete-event', Gtk.main_quit)
        
        self.builder.get_object('far_deg').connect('changed', self.convert_to_celsius)
        self.builder.get_object('cel_deg').connect('changed', self.convert_to_fareng)
        
        window.show()
    
    
    def convert_to_celsius(self, widget):
        '''Define converter function from Far to Cel'''
        # Check input data 
        try:
            fareng = atof(self.builder.get_object('far_deg').get_text())
        except ValueError:
            self.builder.get_object('error_label').set_visible(True)
            self.builder.get_object('cel_deg').set_text('')
            return
        
        # Insert calculated value into Celcius Entry
        self.builder.get_object('error_label').set_visible(False)
        self.builder.get_object('cel_deg').set_text(
            format_string("%.2f", ((fareng - 32) * 5 / 9))
        )
        
    def convert_to_fareng(self, widget):
        '''Define converter function from Cel to Far'''
        # Check input data 
        try:
            cel = atof(self.builder.get_object('cel_deg').get_text())
        except ValueError:
            self.builder.get_object('error_label').set_visible(True)
            self.builder.get_object('far_deg').set_text('')
            return
        
        # Insert calculated value into Celcius Entry
        self.builder.get_object('error_label').set_visible(False)
        self.builder.get_object('far_deg').set_text(
            format_string("%.2f", (cel * 9 / 5 + 32))
        )
   
main = Main()
Gtk.main()
