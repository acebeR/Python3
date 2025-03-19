#Abstração

from pathlib import Path
LOG_FILE = Path(__file__).parent / 'log.txt'
class Log:
    def _log(self,msg):
        raise NotImplementedError('Implemente o método log')
    
    def log_error(self,msg):
        self._log(f'Error: {msg}')
    
    def log_success(self,msg):
        self._log(f'Success: {msg}')

class LogFileMixin(Log):
    def _log(self,msg):
        msg_format = f'{msg}({self.__class__.__name__})' 
        print('Salvando no arquivo log!', msg_format)
        with open(LOG_FILE,'a') as arquivo:
            arquivo.write(msg_format)
            arquivo.write('\n')

    
class LogPrintMixin(Log):
    def _log(self,msg):
        print(f'{msg} {self.__class__.__name__}')

if __name__ == '__main__':
    print(LOG_FILE)