import time, pyautogui
import PySimpleGUI as sg
import multiprocessing
from psgtray import SystemTray


def KeepUI():
    sg.theme('Dark')
    layout = [
        [sg.Text('NonBlocker is active now.\nYou can hide it, and it will continue running.\nClose it to disable it.')],
        [sg.Button('Hide')]
    ]
    systray_menu = ['',['Hide','Show Window','Exit']]
    #window = sg.Window('Keep-Me-Up', layout)
    window = sg.Window('NonBlocker', icon='idea.ico').Layout(layout)
    tray = SystemTray(systray_menu,single_click_events=False,window=window,icon='idea.ico')
    tray.show_message('System Tray','System tray icon started')

    p2 = multiprocessing.Process(target=dontsleep)
    p2.start()

    while True:
        event, values = window.read()
        #print(event)
        #print(values)
        if event == tray.key:
            #Условине на список сделано потому, что при первом нажатие на кнопку возвращется список, вместо словаря, при повторном нажатие возвращается словарь
            if isinstance(event,list):
                event = values[0]
            else: event = values[event]
            #print(f'event={event}')
        if event in (sg.WIN_CLOSED,'Exit'):  # if user closes window or clicks cancel
            if p2.is_alive():
                p2.terminate()
            break
        elif event == 'Hide':
            window.hide()
            tray.show_icon()
        elif event in ('Show Window',sg.EVENT_SYSTEM_TRAY_ICON_DOUBLE_CLICKED):
            window.un_hide()
            window.bring_to_front()
    tray.close()
    window.close()

def dontsleep():
    while True:
        pyautogui.press('volumedown')
        time.sleep(1)
        pyautogui.press('volumeup')
        time.sleep(300)


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=KeepUI)
    p1.start()