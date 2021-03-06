import sys, webbrowser, os

class FileWriter:
    def __init__(self, ):
        self._file = open('index.html', 'w')
        self._tpl = """<html>
    <head>
        <style>
        body {
            text-align: center;
        }
        pre {
            font-family: monospace;
            font-size: 11px;
            overflow: hidden;
            white-space: pre;
            word-wrap: normal;
            line-height: .75;
            letter-spacing: 0;
            background: %s;
            display: inline-block;
            margin: 40px auto;
            border: 10px solid #fff;
            box-shadow: 0 0 1px 0 rgba(0, 0, 0), 0 28px 16px -26px rgba(0, 0, 0);
        }
    </style>
</head><body><pre>"""

    def write(self, string, bg_color = "FFF"):
        self._file.write(self._tpl % (bg_color))
        self._file.write(string)
        self._file.write('</pre></body></html>')
        self._file.close()
        webbrowser.open('file://' + os.path.realpath('index.html'))
