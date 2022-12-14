# Prints a total number of <string>  appearances in the input file
import sys
import argparse
import logging

logging.basicConfig()

def parse_args(args):
    parser = argparse.ArgumentParser(description='Count a number of lines with <string> in it')
    parser.add_argument('--input-file', '-i', required=True)
    parser.add_argument('--string', '-s', help="String to search", default='hello')
    return parser.parse_args(args)

def main(args):
    config = parse_args(args)
    log = logging.getLogger(__name__)
    log.setLevel(logging.DEBUG)
    log.info('Config <%s>', config)
    with open(config.input_file,'r') as f:
        return sum([line.count(config.string) for line in f])


if __name__=='__main__':
    print(main(sys.argv[1:]))
