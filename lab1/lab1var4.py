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
        gladeFile = 'lab1var4.glade'
        self.builder = Gtk.Builder()
        self.builder.add_from_file(gladeFile)

        window = self.builder.get_object('main_window')
        window.connect('delete-event', Gtk.main_quit)
        # TODO переплетение коннектов. Мб определить другой сигнал 
        self.f_handler_id = self.builder.get_object('far_deg').connect('changed', self.convert_from_far)
        self.c_handler_id = self.builder.get_object('cel_deg').connect('changed', self.convert_from_cel)
        self.k_handler_id = self.builder.get_object('kelv_deg').connect('changed', self.convert_from_kelv)
        # self.builder.get_object('far_deg').editing_done(self.convert_from_far)
        
        window.show()
    
    
    def convert_from_far(self, widget):
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
            self.builder.get_object('kelv_deg').set_text('')
            return

        self.builder.get_object('cel_deg').disconnect(self.c_handler_id)
        self.builder.get_object('kelv_deg').disconnect(self.k_handler_id)
        # Insert calculated value into Celcius Entry
        self.builder.get_object('error_label').set_visible(False)
        self.builder.get_object('cel_deg').set_text(
            ("%.2f" % ((fareng - Decimal(32)) * Decimal(0.555)))
            .replace('.', ',')
        )

        self.builder.get_object('kelv_deg').set_text(
            ("%.2f" % ((fareng - Decimal(32)) * Decimal(0.555 + 273.15)))
            .replace('.', ',')
        )

        self.c_handler_id = self.builder.get_object('cel_deg').connect('changed', self.convert_from_cel)
        self.k_handler_id = self.builder.get_object('kelv_deg').connect('changed', self.convert_from_kelv)
        
        
        
    def convert_from_cel(self, widget):
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
            self.builder.get_object('kelv_deg').set_text('')
            return
        
        self.builder.get_object('far_deg').disconnect(self.f_handler_id)
        self.builder.get_object('kelv_deg').disconnect(self.k_handler_id)
        # Insert calculated value into Celcius Entry
        self.builder.get_object('error_label').set_visible(False)
        self.builder.get_object('far_deg').set_text(
            ("%.2f" % (cel * Decimal(1.8) + Decimal(32)))
            .replace('.', ',')
        )
        
        self.builder.get_object('kelv_deg').set_text(
            ("%.2f" % (cel + Decimal(273.15))).replace('.', ',')
        )

        self.f_handler_id = self.builder.get_object('far_deg').connect('changed', self.convert_from_far)
        self.k_handler_id = self.builder.get_object('kelv_deg').connect('changed', self.convert_from_kelv)
        
        
    def convert_from_kelv(self, widget):
        '''Define converter function from Cel to Far'''
        kelv_input = self.builder.get_object('kelv_deg').get_text()
        # Check input data 
        try:
            if kelv_input.find('.') != -1:
                raise InvalidOperation
            kelv = Decimal(kelv_input.replace(',','.'))
        except InvalidOperation:
            self.builder.get_object('error_label').set_visible(True)
            self.builder.get_object('cel_deg').set_text('')
            self.builder.get_object('far_deg').set_text('')
            return
        self.builder.get_object('cel_deg').disconnect(self.c_handler_id)
        self.builder.get_object('far_deg').disconnect(self.f_handler_id)

        # Insert calculated value into Celcius Entry
        self.builder.get_object('error_label').set_visible(False)
        self.builder.get_object('far_deg').set_text(
            ("%.2f" % (kelv * Decimal(1.8) + Decimal(32)))
            .replace('.', ',')
        )

        self.builder.get_object('cel_deg').set_text(
            ("%.2f" % (kelv + Decimal(273.15)))
            .replace('.', ',')
        )

        self.f_handler_id = self.builder.get_object('far_deg').connect('changed', self.convert_from_far)
        self.c_handler_id = self.builder.get_object('cel_deg').connect('changed', self.convert_from_cel)
   
main = Main()
Gtk.main()