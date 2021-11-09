import argparse

from . import detect, test, train, tune
from .models import export


parser = argparse.ArgumentParser(prog='python -m yolor_mimsolutions')
subparsers = parser.add_subparsers()
test.configure_argparser(subparsers.add_parser('test'))
train.configure_argparser(subparsers.add_parser('train'))
tune.configure_argparser(subparsers.add_parser('tune'))
detect.configure_argparser(subparsers.add_parser('detect'))
export.configure_argparser(subparsers.add_parser('export'))
args = parser.parse_args()
args.main_function(args)
