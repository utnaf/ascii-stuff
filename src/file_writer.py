import sys

class FileWriter:
    def __init__(self, file):
        self._file = None
        if file != False:
            self._file = open(file, 'w')
            self._file.write('<html><head></head><body><pre>')
    
    def write(self, char):
        if self._file != None:
            self._file.write(char)
        else:
            sys.stdout.write(char)

    def cr(self):
        if self._file != None:
            self.write('<br />')
        else:
            self.write('\n')
                    

    def __del__(self):
        if self._file != None:
            self._file.write('</pre></body></html>')
            close(self._file)
