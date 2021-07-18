import re
import os
from tools.receptor import Receptor

class Commander(Receptor):
    def __init__(self):
        self.__command = self.listen()

    def __command_parser(self, voice_command):
        cmds = [
            {
                'titulo': 'printscreen',
                'description': 'Realizando print da tela',
                'regex': 'print*',
                'sh_action': 'xfce4-screenshooter -f -s . '
            },
            {
                'titulo': 'atualizar',
                'description': 'Realizando atualização do sistema',
                'regex': 'atual*',
                'sh_action': 'sudo apt-get update && sudo apt-get upgrade'
            }     
        ]
        
        for cmd in cmds:
            valid_cmd = re.search(cmd['regex'], voice_command)
            if (valid_cmd):
                return cmd
    
    def exec_command(self):
        command = self.__command 
        cmd = self.__command_parser(command)

        if (cmd):
            self._speak(cmd['description'])
            os.system(cmd['sh_action'])
        else:
            self._speak(f'Erro: o comando {command} não foi encontrado.')
            exit()

