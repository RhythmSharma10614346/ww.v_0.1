from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._rows = 0 # number of rows in the grid
        self._cols=1#number of columns in the grid
        @property
        def cols (self):
            return self._cols
        @cols.setter
        def cols (self , value ):
            if isinstance(value,(int)):
                self._cols = int(value)#set the new column count and update the layout
                self.update_layout()
                @property
                def rows (self):
                    return self._rows
                @rows.setter
                def rows (self , value ):
                    if isinstance(value,(int)) :
                        self._rows = int(value )# set the new row count and update the layout
                        self.update_layout()
                        def addWidgetToRowCol(rowNumber:int,colNumber:int,*args,**kvArgs)->None:#function to add widgets to
                            def addWidget(self,*args,**kwargs):
                                for i in range((self._rows*2)-3):
                                    for j in range ((self._cols)*4-5):
                                        widget =Label(size=(68/7),pos =(j+i%2*(9),(i//2)*(10)))
                                        self.add_widget(widget)
                                        def update_layout(self,*args,**kwargs):
                                            pass
                                        class MainApp(App):
                                            def build(self):
                                                root =MyGrid()
                                                return root
                                            if __name__ == '__main__':
                                                MainApp().run()
                                                