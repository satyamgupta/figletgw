"""
figletgw

Usage:
  figlet [-f | --font <font_name>] <text>
  figlet -h | --help
  figlet --version
  figlet -l | --list-font

Options:
  -h --help                         Show this screen.
  --version                         Show version.
  -l --list-font                  List supported fonts
  -f --font                       Font to be used for formatting (default='small')

Examples:
  figletgw -f colossal "hello"
  figlet -l

Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/satyam-gupta/figletgw
"""


from inspect import getmembers, isclass
from docopt import docopt
import socket, sys, re

from . import __version__ as VERSION

def call_figlet(param):

    port = 70
    host = 'gopher.floodgap.com'

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    sock.send('fun/figletgw\t' +param+ '\r\n')
    result = ""

    while 1:
        buf = sock.recv(2048)
        if not len(buf):
          break
        result += buf

    return result


def main():
    """Main CLI entrypoint."""
    import commands
    options = docopt(__doc__, version=VERSION)

    if(options['--list-font']):
      
        result = call_figlet("test")
        fonts = re.findall(r'(?<=font=)\w+',result)
        print ' '.join(fonts)

    elif(options['<text>']):
      
        param = options['<text>']+"|font="
        
        if(options['--font']):
            param += options['<font_name>']
        else:
            param += "small"

        result = call_figlet(param)

        if("Here is the result" in result):
            print result[117:]
        else:
            print result