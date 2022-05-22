import PySimpleGUI as sg
from PySimpleGUI import (Push,Button,Image,Column,HSeparator,Window,VSeparator,Text,theme,Frame)

import random

sg.theme('DarkPurple1')
layout=[
    [sg.T('Site/Software',size=(10,1)),
    sg.Input(key='site',size=(20,1))],
    [ sg.T('E-Mail/Usuário',size=(10,1)),sg.Input(key='usuario',size=(20,1)),
    sg.T('Quantidade de Caracters',size=(10,1)),sg.Combo(values=list(
    range(30)),key='total_chars',default_value=1,size=(3,1))],
    [sg.Output(size=(32,5))],
    [sg.Button('Gerar Senha')]
]

window = Window('Password Generation',layout=layout)

window.read()

window.close()