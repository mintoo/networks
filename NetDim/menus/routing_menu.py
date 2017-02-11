# NetDim
# Copyright (C) 2016 Antoine Fourmy (antoine.fourmy@gmail.com)
# Released under the GNU General Public License GPLv3

import tkinter as tk
from os.path import join
from objects.objects import *
from tkinter import ttk
from PIL import ImageTk
from pythonic_tkinter.preconfigured_widgets import *
from collections import OrderedDict

class RoutingMenu(ScrolledFrame):
    
    def __init__(self, notebook, master):
        super().__init__(notebook, width=200, height=600, borderwidth=1, relief='solid')
        self.ms = master
        self.ntw = self.ms.cs.ntw
        font = ('Helvetica', 8, 'bold')  
        
        # label frame for object creation
        lf_refresh = Labelframe(self.infr)
        lf_refresh.text = 'Refresh actions'
        lf_refresh.grid(0, 0, sticky='nsew')
        
        img_path = join(self.ms.path_icon, 'refresh.png')
        img_pil = ImageTk.Image.open(img_path).resize((128, 128))
        self.img_refresh = ImageTk.PhotoImage(img_pil)
        
        button_routing = TKButton(self.infr)
        button_routing.command = self.ms.refresh
        button_routing.config(image=self.img_refresh, relief='flat')
        button_routing.config(width=150, height=150)
        button_routing.grid(0, 0, sticky='ew', in_=lf_refresh)
        
        self.actions = (
                        'Creation of all virtual connections',
                        'Names / addresses interface allocation',
                        'Update AS topology',
                        'Creation of all ARP / MAC tables',
                        'Creation of all routing tables',
                        'Path finding procedure (traffic flows)',
                        'Redraw the graph',
                        'Refresh the display (including labels)'
                        )
        
        self.action_booleans = []
        for id, action in enumerate(self.actions, 1):
            action_bool = tk.BooleanVar()
            action_bool.set(True)
            self.action_booleans.append(action_bool)
            img = tk.PhotoImage(width=1, height=1)
            button = Checkbutton(self.infr, variable=action_bool)
            button.text = action
            button.grid(id, 0, in_=lf_refresh)
        