# Replace one string to another in the input file and save it to output file
import sys
import argparse
import logging

logging.basicConfig()

def parse_args(args):
    parser = argparse.ArgumentParser(description='Replace string in file')
    parser.add_argument('--input-file', '-i', required=True)
    parser.add_argument('--output-file', '-o', required=True)
    parser.add_argument('--search', '-s', default='hello')
    parser.add_argument('--replace', '-r', default='goodbye')
    parser.add_argument('--delete', '-d', action='store_true', help="Delete the input file")
    return parser.parse_args(args)

def main(args):
    config = parse_args(args)
    log = logging.getLogger(__name__)
    log.setLevel(logging.DEBUG)
    log.info('Config <%s>', config)
    if config.input_file == config.output_file:
        raise ValueError('Input and output files should be different')
    out = open(config.output_file,'w')
    with open(config.input_file,'r') as f:
        out.writelines([line.replace(config.search,config.replace) for line in f])
    out.close()
    log.debug('File %s created', config.output_file)
    if config.delete:
        import os
        os.remove(config.input_file)
        log.debug('File %s deleted', config.input_file)


if __name__=='__main__':
    main(sys.argv[1:])
