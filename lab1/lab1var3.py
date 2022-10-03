from ast import In
import string
from unicodedata import decimal
import gi

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
        far_input = self.builder.get_object('far_deg').get_text()

        # Check input data 
        try:
            if far_input.find('.') != -1:
                raise InvalidOperation
            fareng = Decimal(far_input.replace(',','.'))
            
        except InvalidOperation:
            self.builder.get_object('error_label').set_visible(True)
            self.builder.get_object('cel_deg').set_text('')
            return
        
        # Insert calculated value into Celcius Entry
        self.builder.get_object('error_label').set_visible(False)
        self.builder.get_object('cel_deg').set_text(
            ("%.2f" % ((fareng - 32) * 5 / 9))
            .replace('.', ',')
        )
        
    def convert_to_fareng(self, widget):
        '''Define converter function from Cel to Far'''
        cel_input = self.builder.get_object('cel_deg').get_text()

        # Check input data 
        try:
            if cel_input.find('.') != -1:
                raise InvalidOperation
            cel = Decimal(cel_input.replace(',','.'))
            
        except InvalidOperation:
            self.builder.get_object('error_label').set_visible(True)
            self.builder.get_object('far_deg').set_text('')
            return
        
        # Insert calculated value into Celcius Entry
        self.builder.get_object('error_label').set_visible(False)
        self.builder.get_object('far_deg').set_text(
            ("%.2f" % (cel * 9 / 5 + 32))
            .replace('.', ',')
        )
   
main = Main()
Gtk.main()
