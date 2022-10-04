from ast import In
from unicodedata import decimal
import gi
from locale import atof, format_string
gi.require_version('Gtk', '3.0')


from gi.repository import Gtk as Gtk
from decimal import Decimal, InvalidOperation

# locale.setlocale(locale.LC_ALL, locale="German")

# RADIXCHAR = locale.localeconv()['decimal_point']

class Main:
    
    
    '''Whole window class'''
    def __init__(self):
        '''Inits elements on main window'''
        gladeFile = 'lab1var1.glade'
        self.builder = Gtk.Builder()
        self.builder.add_from_file(gladeFile)
        
        button = self.builder.get_object('calculate_button')
        button.connect('clicked', self.convert)
        
        window = self.builder.get_object('main_window')
        window.connect('delete-event', Gtk.main_quit)
        
        window.show()
    
    
    def convert(self, widget):
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
            format_string("%.2f", (fareng - 32) * 5 / 9)
        )
   
   
     
main = Main()
Gtk.main()
