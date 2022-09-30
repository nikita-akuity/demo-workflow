# Creates a file with "hello <name>" content
import sys
import argparse
import logging

logging.basicConfig()

def parse_args(args):
    parser = argparse.ArgumentParser(description='Create a greeting file')
    parser.add_argument('--name', '-n', action='append', help="Name to greet", required=True)
    parser.add_argument('--output-file', '-o', required=True)
    return parser.parse_args(args)

def main(args):
    config = parse_args(args)
    log = logging.getLogger(__name__)
    log.setLevel(logging.DEBUG)
    log.info('Config <%s>', config)
    out = open(config.output_file,'w')
    out.writelines([f"hello {name}\n" for name in config.name])
    out.close()
    log.debug('File %s created', config.output_file)


if __name__=='__main__':
    main(sys.argv[1:])
