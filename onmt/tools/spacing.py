from pykospacing import Spacing
spacing = Spacing()
import sys
import codecs
import io
import argparse



# hack for python2/3 compatibility
from io import open
argparse.open = open

def create_parser():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="kospacing")

    parser.add_argument(
        '--input', '-i', type=argparse.FileType('r'), default=sys.stdin,
        metavar='PATH',
        help="Input file (default: standard input).")
    parser.add_argument(
        '--output', '-o', type=argparse.FileType('w'), default=sys.stdout,
        metavar='PATH',
        help="Output file (default: standard output)")

    return parser

def spacing_text(sentence):
    return spacing(sentence)
    
    
    
if __name__ == '__main__':

    parser = create_parser()
    args = parser.parse_args()

    # read/write files as UTF-8
    args.input = open(args.input.name, 'r', encoding='utf-8')
    args.output = open(args.output.name, 'w', encoding='utf-8')

    while True:
        src = args.input.readline()
        if not src: break
        args.output.write(spacing_text(src.replace(" ", "")).strip())
        args.output.write('\n')
        
    args.input.close()
    args.output.close()