# Importing Required Modules :-

import PySimpleGUI as sg
import os
from html.parser import HTMLParser
from bs4 import BeautifulSoup
import re

# ---------------------------------------------------------------------------------------------------------------------------------
#                                                     NEEDS OF BUILD FUNCTION
# ---------------------------------------------------------------------------------------------------------------------------------

def Code_Beautifier(document):  # Organises the text of HTML Document.
    soup=BeautifulSoup(document, 'html.parser')
    _return = soup.prettify()
    return _return

def Link_Handler(IN):  # Automatically handles link address with relative address (Converts them to Individual File Addresses).
    match = re.findall(r'<a href="(.*?)"', IN)
    OUT=IN
    for link in match:
        new_link=(get_file_name(link))[1]
        OUT = OUT.replace(link, "/"+new_link)
    return OUT

def get_file_name(Path):  # Returns a tuple with File name without extension as first element and file name with extension as second from the full path of the file.
    _return_with_extension = ""
    for i in range(1, len(Path) + 1):
        if Path[-i] == "/":
            break
        else:
            _return_with_extension = Path[-i] + _return_with_extension
    _return = ""
    for j in range(0, len(_return_with_extension)):
        if _return_with_extension[j] == ".":
            break
        else:
            _return += _return_with_extension[j]
    final = (_return, _return_with_extension)
    return final


def func_creator(FileName, Code):  # Returns the function as string, needed by pyramid module for HTML page.
    unhandled_beautified_code =  Code_Beautifier(Code)
    completely_handled_code = Link_Handler(unhandled_beautified_code)
    _return = "def " + FileName + "(request):" + "\n" + \
              "  " + "return Response(\"\"\"" + completely_handled_code + "\"\"\")" + "\n" + "\n"
    return _return


def route_adder(IN):  # Returns two lines needed by pyramid for creating a view and adding path/route of file.
    _return = ""
    for i in range(0, len(IN)):
        File_Details = get_file_name(IN[i])
        Individual_Files = "        config.add_route(\'" + File_Details[0] + "\',\'/" + File_Details[
            1] + "\')\n" + "        config.add_view(" + File_Details[0] + ", route_name = \'" + File_Details[
                               0] + "\')\n"
        _return += Individual_Files
    return _return

def Home_Page(Path, Port):  # Returns the line of code needed for automatically opening an HTML page usually homepage/inital starting point.
    file_details = get_file_name(Path)
    _return ="webbrowser.open"+ "(\'http://localhost:" + Port + "/" + file_details[1] + "\', new=1)"
    return _return

def build(Input_List, Output_Directory, port, On_Start_File):  # Main Script for build process that automatically creates a folder with the output file/ build :-
    fixed_imports = """import webbrowser\nfrom wsgiref.simple_server import make_server\nfrom pyramid.config import Configurator\nfrom pyramid.response import Response"""
    Routes = route_adder(Input_List)
    final_lines = """if __name__ == '__main__':\n    with Configurator() as config:\n""" + Routes + """        app = config.make_wsgi_app()\n        """ + Home_Page(On_Start_File, port) + """\n        """ + """server = make_server('0.0.0.0', """ + port + """, app)\n        server.serve_forever()"""
    os.mkdir(Output_Directory + "/" + "Build")  # Creating a directing for storing finally built file.
    mf = open(Output_Directory + "/" + "Build" + "/" + "AppFile.py", "a")  # Creates and opens a file for final code.
    mf.write("# coding: ANSI")  # Some opening error removal by defining encoding.
    mf.write("\n")
    mf.write(fixed_imports)  # Adds lines of code containg module imports needed for pyramid program to run.
    mf.write("\n")
    mf.write("\n")
    for loc in Input_List:  # loc is the path/location to each HTML file chosen.
        f = open(loc, "r")
        data_read = f.read()  # Reads the data HTML file chosen.
        Name_of_File = get_file_name(loc)
        write_material = func_creator(Name_of_File[0], data_read)
        mf.write(write_material)  # Adds the functions by func_creator.
        mf.write("\n")
        f.close()
    mf.write(final_lines)  # Finally adds line for adding routes, views, automate the process of opening a HTML page as homepage.
    mf.close()


# ---------------------------------------------------------------------------------------------------------------------------------
#                                                GUI AND BASIC FUNCTIONS NEEDED
# ---------------------------------------------------------------------------------------------------------------------------------


def folder_checks(Location):  # Performs all checks to ensure proper file handling.
    Existence_Check = os.access(Location, os.F_OK)
    if Existence_Check:
        _return = ("""\n Checking Folder Existence... \n Does Folder exist ? True""", 'CL')
        Write_Check = os.access(Location, os.R_OK)
        if Write_Check:
            _return = ("""\n Checking Folder Existence... \n Does Folder exist ? True \n \n Checking Write Access... \n Do we have Write Permission ? True""", 'CL')
        else:
            _return = ("""\n Checking Folder Existence... \n Does Folder exist ? True \n Checking Write Access... \n Do we have Write Permission ? False \n Task Terminated.""", 'TD')
    else:
        _return = ("""\n Checking Folder Existence... \n Does Folder exist ? False \n Task Terminated.""", 'TD')
    return _return


def input_checks(Location):  # Preforms all checks to ensure proper folder handling.
    Existence_Check = os.access(Location, os.F_OK)
    if Existence_Check:
        _return = ("""\n Checking File Existence... \n Does file exist ? True""", 'CL')
        Read_Check = os.access(Location, os.R_OK)
        if Read_Check:
            _return = ("""\n Checking File Existence... \n Does file exist ? True \n \n Checking Read Access... \n Do we have Read Permission ? True""", 'CL')
        else:
            _return = ("""\n Checking File Existence... \n Does file exist ? True \n Checking Read Access... \n Do we have Read Permission ? False \n Task Terminated.""", 'TD')
    else:
        _return = ("""\n Checking File Existence... \n Does file exist ? False \n Task Terminated.""", 'TD')
    return _return


# ---------------------------------------------------------------------------------------------------------------------------------
#                                                   GRAPHICAL USER INTERFACE
# ---------------------------------------------------------------------------------------------------------------------------------

sg.theme("Reds")
layout1 = [  # Layout 1 for Choosing HTML Files.
    [sg.Text('Input Files Chooser :-')],
    [sg.Input(key='-IN-'), sg.FileBrowse()],
    [sg.Button('Next File'), sg.Button('Submit All'), sg.Button('QUIT')],
    [sg.Text(size=(34, 7), key='-Progress-')]
]

layout2 = [  # Layout 2 for choosing Output Folder & BUILD button.
    [sg.Text('Output Folder Chooser :-')],
    [sg.Input(key='-IN-'), sg.FolderBrowse()],
    [sg.Button('BUILD'), sg.Button('QUIT')],
    [sg.Text(size=(34, 7), key='-Progress-')]
]

window1 = sg.Window('HTML File Chooser', layout1)

OutputList = ()
while True:
    event1, values1 = window1.read()
    if event1 == sg.WIN_CLOSED or event1 == 'QUIT':
        break
    elif event1 == 'Next File':
        if values1['-IN-'] == '':
            window1['-Progress-'].update('\n Please Enter a path to the file.')
        else:
            toshow1 = input_checks(values1['-IN-'])
            if toshow1[1] == 'CL':
                OutputList += (values1['-IN-'],)
            window1['-Progress-'].update(toshow1[0])
            window1['-IN-'].update('')
    elif event1 == 'Submit All':
        if values1['-IN-'] == '':
            window1.close()
            window2 = sg.Window('Output Folder:-', layout2)
            while True:
                event2, values2 = window2.read()
                if event2 == sg.WIN_CLOSED or event2 == 'QUIT':
                    break
                elif event2 == 'BUILD':
                    if values2['-IN-'] == '':
                        window1['-Progress-'].update('\n Please Enter a path to the file.')
                    else:
                        toShow2 = folder_checks(values2['-IN-'])
                        if toShow2[1] == 'CL':
                            window2['-Progress-'].update(toShow2[0])
                            Port_Number = sg.popup_get_text('Port Checker', 'Enter the Port Number to set the server on :-')
                            Start_Page = sg.popup_get_file("Choose the file you want to automatically open as Homepage: -", title="File Chooser:-")
                            try:  # MAIN BUILD EXECUTION :-
                                build(OutputList, values2['-IN-'], Port_Number, Start_Page)
                                sg.popup("Success", "Your Build of the App was Successful.")
                            except:
                                sg.popup("Error", "Unknown Error Occurred.\nThe Build was Unsuccessful.")
                        else:
                            window2['-Progress-'].update(toShow2[0])
                elif event2 == 'QUIT':
                    window2.close()
        else:
            toshow1 = input_checks(values1['-IN-'])
            if toshow1[1] == 'CL':
                OutputList += (values1['-IN-'],)
            window1['-Progress-'].update(toshow1[0])
            window1['-IN-'].update('')
            window1.close()
            window2 = sg.Window('Output Folder:-', layout2)
            while True:
                event2, values2 = window2.read()
                if event2 == sg.WIN_CLOSED or event2 == 'QUIT':
                    break
                elif event2 == 'BUILD':
                    if values2['-IN-'] == '':
                        window1['-Progress-'].update('\n Please Enter a path to the file.')
                    else:
                        toShow2 = folder_checks(values2['-IN-'])
                        if toShow2[1] == 'CL':
                            window2['-Progress-'].update(toShow2[0])
                            Port_Number = sg.popup_get_text('Port Checker', 'Enter the Port Number to set the server on :-')
                            Start_Page = sg.popup_get_file("Choose the file you want to automatically open as Homepage: -", title="File Chooser:-")
                            build(OutputList, values2['-IN-'], Port_Number, Start_Page)
                            sg.popup("Success", "Your Build of the App was Successful.")
                            try:  # MAIN BUILD EXECUTION :-
                                build(OutputList, values2['-IN-'], Port_Number, Start_Page)
                                sg.popup("Success", "Your Build of the App was Successful.")
                            except:
                                sg.popup("Error", "Unknown Error Occurred.\nThe Build was Unsuccessful.")
                        else:
                            window2['-Progress-'].update(toShow2[0])
                elif event2 == 'QUIT':
                    window2.close()
