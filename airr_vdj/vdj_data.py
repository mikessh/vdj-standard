"""
Parse V(D)J assignment results and produce AIRR standard data format.
"""

# Python packages
import sys
import argparse
import json

from Bio import SeqIO

from .version import __version__, __copyright__

def getArgParser():
	"""Command line arguments for vdj_data"""
	parser = argparse.ArgumentParser();
	parser.description='Parse V(D)J assignment results and produce AIRR standard data format. VERSION '+__version__
	parser.add_argument('-v', '--version', action='version', version='VERSION '+__version__+' '+__copyright__)
	return parser

def main():
	"""Parse V(D)J assignment results and produce AIRR standard data format"""
	parser = getArgParser()
	args = parser.parse_args()

	if (not args):
		args.print_help()
		sys.exit()
