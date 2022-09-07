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
        gladeFile = 'main1.glade'
        self.builder = Gtk.Builder()
        self.builder.add_from_file(gladeFile)
        
        button = self.builder.get_object('calculate_button')
        button.connect('clicked', self.convert)
        
        window = self.builder.get_object('main_window')
        window.connect('delete-event', Gtk.main_quit)
        
        window.show()
    
    
    def convert(self, widget):
        '''Define converter function from Far to Cel'''
        input1 = self.builder.get_object('far_deg').get_text()

        # Check input data 
        try:
            fareng = Decimal(input1.replace(',','.'))
        except InvalidOperation:
            pass
        
        # Insert calculated value into Celcius Entry
        celc = self.builder.get_object('cel_deg').set_text(
                ("%.2f" % ((fareng - 32) * 5 / 9))
                .replace('.', ',')
            )
        
if __name__ == '__main__':
    main = Main()
    Gtk.main()
