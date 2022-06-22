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
***    
### Geometry: 
* We know that a widtget is an element of the GUI that displays information or gives a way for the user to interact with the OS and a window is a container in which all other gui elements, widgets, are placed.
* But creating a new widget doesn't mean that is will appear on the screen. To make them appear on the screen, we need to place them on the window and orrgainize them accordingly
* Therefore, before we actually move ahead lets cover Gemotery
***   
#### Geometry Management:
* the layout of the application in tkinter is controlled by the geometry managers. it helps us to plce and orgainze various widgets in the window
* therefore, to display it, we need to call spcial geomtery management method
* all tkinter widgets have access to a specific geomerty management methods, which have the purpose of organizing widgets throughout the parent widget area.
* The following are 3 methods for that: pack() grid() place() 
***   
- pack() - geometry manager organizes widgets in blocks before placing them in the 
    parent widget. It places the widgets in the given order as they are created.
    * it computes a rectangluar area called a parcel thats's just tall and wide enough to hold the widget and fills the remaining area in the window tih blank space
    * it centers the widget in the parcel unless a defferent location is specified
    * widget.pack( pack_options )
        * Here the widget is the GUI widget that you want to place in the parent container
        * pack() is called on the widget that we wish to place 
        * this method takes various optional options(params) that help us to manipulate the wdget while using the pack manager
    * Pack Method Options: 
        * expand - takes a boolean value. When set to true, the widget expands to fill and space in the widgets parent
        * fill - determines whether the widget fills any extra space allocated to it by the packer, or keeps its own minimal dimenisons. It can have the following calues: NONE (default), X(fill only horizontally), Y (fill only vertically), or BOTH (horizontally and vertically)
        * side - determines on which side of the parent widget should the new parent widget be placed. Possible values: TOP(default), BOTTOM, LEFT, RIGHT
***   
- grid() - orgainzes widgets in a table-like structure in the parent widget, 
    basically it puts widgets in a 2-D table.
    * the parent container is split into a number of rows and columns, and each cell in the resulting table can hold a widget
    * it is one of the most generally used geometry managers in tkinter and we can use the grid() to implement the grid geometry
    * widget.grid( grid_options )
        * Here widget is the GUI widget that you want to place in the parent conatiner
        * grid() is called on the widget that we wish to place
        this method takes various optional options(params)that helps manipulate the widget when using grid manager
    * Grid Method Options:
        * row - is the row to put the widget in. the default i the first row that is still empty
        * column - is the column to put the widget in default is 0 (leftmost column)
        * rowspan - specifies how manu row the widget occupies default is 1
        * columnspan - spacifies how manu columns the widget occupies default is 1
        * sticky - it helps to center the widget in the cell. It can have the values ilke N, E, S, W, NE, NW, SE, SW which are the compass diesctions indicating the sides and corners of the cell to which the widget sticks
***   
- place() - orgainzes widgets by placing them in a spcific position in the parent 
    widget. It is the simplest form of the three general geometry managers provided in tkinter 
    * it allows you to explicity set the position and size of a window, either in absolute terms, or relative to another window 
    * widget.place( place_options )
    * Place Method Options:
        * height, width - specifies the height and width in pixels
        * x,y - spcifies the horizontal and vertical offset in pixels 
        * relx, rely - specifies the horizontal and vertical offset as a float between 0.0 and 1.0 basically as a fraction of the height and width of the parent widget
        * relheight, relwidth - specifies the horizontal and vertical offset as a float between 0.0 and 1.0 basically as a fraction of the height and width of the parent widget 
        * bordermode - it has two possible values that hekos to manipulate the border INSIDE (default) to indicate that other options refer to the parent's inside (ignoring the parent's border) or OUTSIDE otherwise
***   
### tkMessageBox: 
- yet another GUI tool in Tkinter that is used to display various types of popup and dialog boxes.
- but unlike other gui tools which are widgets, tkMessageBox is a module
- in Py3 we cannot use tkMessageBox for py3 we have messagebox (same thing)
* from tkinter import messagebox
***   
##### SYNTAX #####
messagebox.functionName(title, message, options)
* here functionName is the name of the appropriate message box function. Each   
    function creates and displays a different kind of message box
* title - is the text to be displayed in the title bar of a message box 
* message - it is the text to be displayed as a message 
* options - these are the alternative choices that you may use to tailor a standard message box. Some of the options you can use are default and parent. The default option is used to specify the default button, such as ABORT, RETRY, IGNORE in the message box. The parent option is used to specify the window on top of which the message box is to be displayed.
***   
##### messagebox Functions:
- there are different functions that help us to create and display various message 
    boxes:
    * showinfo()
    * showwarning()
    * showerror()
    * askquestion()
    * askokcancel()
    * askyesno()
    * askretrycancel()
- these functions work just like their name suggest
***   
### Making Interavive Apps:
##### Event and Event Handling:
* When we create a GUI in tkinter, we make a call to the mainloop() method, this 
    method internally starts the event loop
* An event loop is responsible for the event handling and it continusously wait for 
    events to happen
* During the event loop, your app checks if an event has occured. If so, then some  
    code can be executed in response 
* In simple words, an event is any action that occurs during the event loop that
    might trigger some beehavior in the app, such as when a key or mouse button is pressed
* When an event occurs, an event object is emitted, which means that an instance of a 
    class representing the event is instansiated
* tkinter provides a mechanism to let the programmer deal with events. For each 
    widget, it's possible to bind functions to an event
* if the defined event occurs in the eidget, we can call the respective handler 
    function on the event object
* the handler functions are the funcitons that has the logic of what to do if an eent 
    has occured 
* bind() function or command option to make GUI interactive
***   
##### bind() function:
* whenever an event occurs, we can call the event handler function using the bind() 
    funciton provided by the tkinter module 
* the bind funciton bounds the event and executes the function whenever the event 
    occurs 
* ##### SYNTAX #####
widget.bind(event, handler)
***   
##### Events in Python: 
There are various types of events in tkinter that we can target using the bind method:
<!-- <Button>: specifies that the mouse button is pressed with the mouse pointer over the
     widget. The left mouse button is defined by the event <Button-1> the middle button by <Button-2> and the rightmost button by <Button-3>
<ButtonRelease>: spcifies that the button is released. to specify the left middle or 
    right mouse button use <ButtonRelease-1>(-2-3) respectively
<Double-Button>: is similar to the Button-event, but here the button is 
    double-clicked same way to specify 1,2,3
<FocusIn>: specifies that the keyboard focus was moved to this widget, or to a child 
    of this widget
<FocusOut>: specifies that the keyboard focus was moved from this widget to another 
    widget 
<Key>: specifies that the user pressed any key </Key> -->
***   
##### command option: 
-we know, generally, all the widgets provide us with the command option that calls a 
    method whenever the user interacts or changes the state of the widget 
##### SYNTAX ##### 
objName = Widget(command = function_name)
