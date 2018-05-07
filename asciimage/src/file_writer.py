import sys


class FileWriter:
    def __init__(self, file):
        self._file = None
        if file == True:
            self._file = open('index.html', 'w')
            self._file.write("""<html>
    <head>
        <style>
        pre {
            font-family: monospace;
            font-size: 8px;
            overflow-x: auto;
            padding: 1.25rem 1.5rem;
            white-space: pre;
            word-wrap: normal;
            line-height: .75;
            letter-spacing: 0;
            background: #aaa;
            text-align: center;
            position: fixed;
            top: 0;
            bottom: 0;
            left: 0;
            right: 0;      
        }
    </style>
</head><body><pre>""")

    def write(self, string):
        if self._file != None:
            self._file.write(string)
            self._file.write('</pre></body></html>')
            self._file.close()
        else:
            sys.stdout.write(string)
            input()
