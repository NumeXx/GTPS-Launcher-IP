# Coded BY NumeX
# iDea By Jesen

from PySimpleGUI.PySimpleGUI import Tree, execute_editor
import pkg_resources, subprocess, sys

required = {'pysimplegui'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if missing:
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)
    print("installing module...")
    
import PySimpleGUI as sg
import webbrowser

addRed = False
def launch():
    global addRed
    ip = values['ip']
    try:
        with open("'C:\\Windows\\System32\\drivers\\etc\\hosts', 'r'") as f:
            if f"{ip} growtopia1.com" in f.read():
                sg.popup(f"{ip} Already in host", title='!Error')
            else:
                addRed = True;
            f.close()
        
        if addRed:
            with open('C:\\Windows\\System32\\drivers\\etc\\hosts', 'a') as f:
                f.write(f'\r\n{ip} growtopia1.com\n{ip} growtopia2.com')
            sg.popup(f"{ip} Added to host", title="Success")
            f.close()

    except:
        sg.popup("Windows hosts failed... Trying linux version (Maybe wine?)")
        try:
            with open('\\etc\\hosts', 'r+') as f:
                if f"{ip} growtopia1.com" in f.read():
                    sg.popup(f"{ip} Already in host", title='!Error')
                else:
                    addRed = True;
                f.close()
            
            if addRed:
                with open('\\etc\\hosts', 'a') as f:
                    f.write(f'\r\n{ip} growtopia1.com\n{ip} growtopia2.com')
                sg.popup(f"{ip} Added to host", title="Success")
                f.close()
        except:
            sg.popup('Unknown error while modifying hosts file??\nTry run as administrator', title='!Error')

def about():
    layoutabout = [[sg.Text("This app made by NumeX#1790")],
                [sg.Button("Link App"), sg.Button("Youtube"), sg.Button("Discord")],
                [sg.Button("Close")]]
    windowabout = sg.Window("About", layoutabout)
    eventa, valuesa = windowabout.read()
    if eventa == "Link App":
        webbrowser.open("https://github.com/NumeXx/GTPS-Launcher-IP")
        windowabout.close()

    elif eventa == "Youtube":
        webbrowser.open('https://www.youtube.com/channel/UCDXi6rK5MBvpQ-o4Gn5pJhg')
        windowabout.close()

    elif eventa == "Discord":
        webbrowser.open("https://discord.gg/HDuBhZmTBA")
        webbrowser.close()

    elif eventa == "Close":
        windowabout.close()

sg.theme("BrownBlue")

layout = [[sg.Text("Ip :"), sg.Input(key="ip", size=(50))], 
        [sg.Button("Start Launch Programm", size=(50))],
        [sg.Text("")],
        [sg.Button("About", button_color="orange"), sg.Button("Quit", button_color="red")]]

window = sg.Window("GTPS Launcher", layout)

while True:
    event, values = window.read()
    if event in (None,  "Quit"):
        break

    elif event == "Start Launch Programm":
        if values["ip"] == "":
            sg.popup("Please input ip!", title="Error!")
        else:
            launch()
    
    elif event == "About":
        about()

window.close()