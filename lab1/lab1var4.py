from ast import In
import string
from unicodedata import decimal
import gi
from locale import atof, format_string

gi.require_version('Gtk', '3.0')


from gi.repository import Gtk as Gtk
from decimal import Decimal, InvalidOperation
# Сделать вариант с таблицей 

class Main:
    
    
    '''Whole window class'''
    def __init__(self):
        '''Inits elements on main window'''
        gladeFile = 'lab1var4.glade'
        self.builder = Gtk.Builder()
        self.builder.add_from_file(gladeFile)

        window = self.builder.get_object('main_window')
        window.connect('delete-event', Gtk.main_quit)
        self.f_handler_id = self.builder.get_object('far_deg').connect('changed', self.convert_from_far)
        self.c_handler_id = self.builder.get_object('cel_deg').connect('changed', self.convert_from_cel)
        self.k_handler_id = self.builder.get_object('kelv_deg').connect('changed', self.convert_from_kelv)
        
        window.show()
    
    
    def convert_from_far(self, widget):
        '''Define converter function from Far to Cel'''
        # Check input data 
        try:
            fareng = atof(self.builder.get_object('far_deg').get_text())
        except ValueError:
            self.builder.get_object('error_label').set_visible(True)
            self.builder.get_object('cel_deg').set_text('')
            self.builder.get_object('kelv_deg').set_text('')
            return

        self.builder.get_object('cel_deg').disconnect(self.c_handler_id)
        self.builder.get_object('kelv_deg').disconnect(self.k_handler_id)
        # Insert calculated value into Celcius Entry
        self.builder.get_object('error_label').set_visible(False)
        self.builder.get_object('cel_deg').set_text(
            format_string("%.2f", (fareng - 32) * 0.555)
        )

        self.builder.get_object('kelv_deg').set_text(
            format_string("%.2f", (fareng - 32) * 0.555 + 273.15)
        )

        self.c_handler_id = self.builder.get_object('cel_deg').connect('changed', self.convert_from_cel)
        self.k_handler_id = self.builder.get_object('kelv_deg').connect('changed', self.convert_from_kelv)
        
        
        
    def convert_from_cel(self, widget):
        '''Define converter function from Cel to Far'''
        # Check input data 
        try:
            cel = atof(self.builder.get_object('cel_deg').get_text())
        except ValueError:
            self.builder.get_object('error_label').set_visible(True)
            self.builder.get_object('far_deg').set_text('')
            self.builder.get_object('kelv_deg').set_text('')
            return
        
        self.builder.get_object('far_deg').disconnect(self.f_handler_id)
        self.builder.get_object('kelv_deg').disconnect(self.k_handler_id)
        # Insert calculated value into Celcius Entry
        self.builder.get_object('error_label').set_visible(False)
        self.builder.get_object('far_deg').set_text(
            format_string("%.2f", (cel * 1.8 + 32))
        )
        
        self.builder.get_object('kelv_deg').set_text(
            format_string("%.2f", cel + 273.15)
        )

        self.f_handler_id = self.builder.get_object('far_deg').connect('changed', self.convert_from_far)
        self.k_handler_id = self.builder.get_object('kelv_deg').connect('changed', self.convert_from_kelv)
        
        
    def convert_from_kelv(self, widget):
        '''Define converter function from Cel to Far'''
        # Check input data 
        try:
            kelv = atof(self.builder.get_object('kelv_deg').get_text())
        except ValueError:
            self.builder.get_object('error_label').set_visible(True)
            self.builder.get_object('cel_deg').set_text('')
            self.builder.get_object('far_deg').set_text('')
            return
        self.builder.get_object('cel_deg').disconnect(self.c_handler_id)
        self.builder.get_object('far_deg').disconnect(self.f_handler_id)

        # Insert calculated value into Celcius Entry
        self.builder.get_object('error_label').set_visible(False)
        self.builder.get_object('far_deg').set_text(
            format_string("%.2f", kelv * 1.8 + 32)
        )

        self.builder.get_object('cel_deg').set_text(
            format_string("%.2f", kelv + 273.15)
        )

        self.f_handler_id = self.builder.get_object('far_deg').connect('changed', self.convert_from_far)
        self.c_handler_id = self.builder.get_object('cel_deg').connect('changed', self.convert_from_cel)
   
main = Main()
Gtk.main()