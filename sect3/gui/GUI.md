# GUIL
- UI = User Interface
- GUI - Graphical User Interface - this is a UI which uses graphics to interact with the user. This can be buttons, menus, images, and more. The GUI for manu programs differs in layout and exact function.
***   
### Tkinter:
- GUI is a system of interactive visual components for computer software. It displays objects that convey information and represent actions that can be taken bu the user.
* Some popular python GUIs (Tkinter, Kivy, Python Gt, wxPython, etc)
* Tkinter is the inbuilt python module that is used to create GUI applications. It is one of the most comonly used Modules for creating GUI apps in python as it is simple and easy to work with.
* IDLE is a default IDE for python which comes with python installation. It is fully coded in Tkinter.
#### Steps to create an app in Tkinter:
* inporting the module - tkinter 
* create the main window
* add any number of widegts to the main window
* apply the event trigger on the widgets 
***   
### Intro to Widgets:
- with visual components, a GUI comprises various elements such as Buttons, Text(called Labels), Images, Menus, etc.
- tkinter gives us these common GUI elements which we can use to build out the Interface
- In simple words, a Widget is an element of the GUI that displays information or provides a way for the user to interact with the OS Therefore widgets are the elements of GUI apps that provide various controls such as Labels, Buttons, ComboBoxes, CheckBoxes, MenuBars, RadioButtons, etc to users to interact with the app
* How are the represented in Python?
    * In Tkinter, Widgets are represented as objects, that is, instances of classes that represent them such as the Button class for the button widet, Frame class for the frame widget and so on 
    * So each separate widget is a Python objects
    * When creating a widget - you must pass its parent(the parent container that will hold the widget) as a param to the widget creation function 
    #### Frequently used widget classes:
    * Label - is used to provide a single-line caption for other widgets. It is     
        basically used to store text and even images
    * Button - is used to add buttons to your app. These buttons can perform various 
        actions when clicked
    * Entry - is just like the Python input() funciton, but more GUI in nature. It is 
        used to accept single-line input from the user 
    * Text - text entry widget that allows multiline text entry 
    * Frame - is used as a container widget to organize other widgets 
    * ComboBox - conatains a down arrow to select from the list of avaliable options. 
        (dropdown list)
    * Checkbutton - is used to display a number of options as checkboxes. The user 
        can select multiple options at a time.
    * Radiobutton - is used to display a number of options as radio buttons. The user 
        can select only one option at a time 
    * PanedWindow - is a container widget that may contain any number of panes, 
        arranged horizontally or vertically
    * Canvas - is used to draw shapes, such as lines, ovals, polygons, and rectangles 
        in your app.
    * tkMessageBox - not a widget its a complete python module. used to display 
        message (dialog) boxes in our apps 
    * for more [Click-Here](docs.python.org/3/library/tkinter.html#module-tkinter)