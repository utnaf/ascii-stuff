import sys


class FileWriter:
    def __init__(self, file):
        self._file = None
        if file == True:
            self._file = open('index.html', 'w')
            self._file.write('<html><head></head><body><pre>')

    def write(self, string):
        if self._file != None:
            self._file.write(string)
            self._file.write('</pre></body></html>')
            self._file.close()
        else:
            sys.stdout.write(string)
            input()
