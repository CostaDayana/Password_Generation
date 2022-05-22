import random
import PySimpleGUI as sg
from PySimpleGUI import (Push,VSeparator,Column)

import os

class PassGen:

    def __init__(self):
        
        sg.theme('LightGrey1')
        layout_direita=[
            [sg.Text('Site/Software:',size=(12,1)),sg.Input(key='site',size=(38,1))],
            [Push()],
            [sg.Text('E-Mail/Usuário:',size=(12,1)),sg.Input(key='usuario',size=(38,1))],
            [Push()],
            [sg.Text('Quantidade de Caracters',size=(20,1)),
             sg.Combo(values=list(
                range(30)),key='total_chars',default_value=1,size=(3,1))],
            [Push()],
            [sg.Output(size=(52,5))],
            [Push()],
            [Push(),sg.Button('Gerar Senha'),Push()]
        ]
        layout_esquerda=[
            [sg.Image(filename='img/kindpng_244948.png')]
        ]
        layout=[
            [Column(layout_esquerda),VSeparator(),Column(layout_direita)]
            ]

        self.window = sg.Window('Password Generation', layout=layout)

    def Iniciar(self):
        while True:
            evento, valores = self.window.read()
            if evento == sg.WINDOW_CLOSED:
                break
            if evento == 'Gerar Senha':
                nova_senha = self.gerar_senha(valores)
                print(nova_senha)
                self.salvar_senhas(nova_senha,valores)

    def gerar_senha(self, valores):
       char_list='ABDCEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%¨&*()_+'
       chars= random.choices(char_list,k=int(valores['total_chars']))
       new_pass=''.join(chars)
       
       return new_pass

    def salvar_senhas(self,nova_senha,valores):
        with open('senhas.txt','a',newline='') as arquivo: 
            arquivo.write(f"site: {valores['site']}, usuario: {valores['usuario']}, senha: {nova_senha} \n")

        print('Arquivo Salvo')

gen = PassGen()

gen.Iniciar()