"""Needs a doc-string.
"""
from __future__ import division, absolute_import, print_function

import sys
import argparse

from frankenstein import FrankFitter, FourierBesselFitter
from frankenstein.quote import print_quote

def help():
    pass

def parse_parameters():
    return {}

def load_uvdata(params):    
    pass

def perform_fit(params):
    pass

def output_results(params):
    pass

def main():

    # Maybe some ASCII art?
    print("The world was to me a secret which I desired to devine.\n"
          "     - Mary Shelley, Frankenstein\n")

    params = parse_parameters()

    uv = load_uvdata(params)

    # Print a quote for people to read while the fit is being done?
    print("Peforming fit. Here's a quote to read while you wait...")
    print_quote()
    
    perform_fit(params)
    
    output_results(params)
    
    print("\n\n\nIT'S ALIVE\n\n")



if __name__ == "__main__":
    main()
