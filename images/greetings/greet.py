# Creates a file with "hello <name>" content
import sys
import argparse
import logging

logging.basicConfig()

def parse_args(args):
    parser = argparse.ArgumentParser(description='Create a greeting file')
    parser.add_argument('--names', '-n', help="Names to greet, comma separated", required=True)
    parser.add_argument('--output-file', '-o', required=True)
    parser.add_argument('--greeting', '-g', default="hello")
    return parser.parse_args(args)

def main(args):
    config = parse_args(args)
    log = logging.getLogger(__name__)
    log.setLevel(logging.DEBUG)
    log.info('Config <%s>', config)
    out = open(config.output_file,'w')
    out.writelines([f"{config.greeting} {name}\n" for name in config.names.split(',')])
    out.close()
    log.debug('File %s created', config.output_file)


if __name__=='__main__':
    main(sys.argv[1:])
