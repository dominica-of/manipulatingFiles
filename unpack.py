#!/usr/bin/env bash

from fileinput import filename
import os
import argparse
import sys
from pip import main


def get_file_type(filename):
    with open(filename, "rb") as f:
        header = f.read(4)
    if header == b"PK\x03\x04":
        return ".zip"
    elif header == b"\x42\x5A\x68":
        return ".bz2"
    elif header == b"\x1F\x8B\x08":
        return ".gz"
    elif header == b"\x1F\x9D":
        return ".z"
    else:
        return None


def unpack_file(filename):
    filetype = get_file_type(filename)
    if filetype == ".zip":
        os.system("unzip " + filename)
    elif filetype == ".gz":
        os.system("gunzip " + filename)
    elif filetype == ".bz2":
        os.system("bunzip2 " + filename)
    elif filetype == ".z":
        os.system("uncompress " + filename)
    else:
        return False
    return True


def unpack_recursively(filename, verbose_mode=False, recursive_mode=False):
    if recursive_mode:
        for root, dirs, files in os.walk(filename):
            for name in files:
                filename = os.path.join(root, name)
    filetype = get_file_type(filename)
    if filetype == ".zip":
        if verbose_mode:
            print("Unpacking " + filename)
        os.system("unzip " + filename)
    elif filetype == ".gz":
        if verbose_mode:
            print("Unpacking " + filename)
        os.system("gunzip " + filename)
    elif filetype == ".bz2":
        if verbose_mode:
            print("Unpacking " + filename)
        os.system("bunzip2 " + filename)
    elif filetype == ".z":
        if verbose_mode:
            print("Unpacking " + filename)
        os.system("uncompress " + filename)
    else:
        if verbose_mode:
            print("Ignoring " + filename)
        


def main():
    parser = argparse.ArgumentParser(description="Unpack multiple packed files.")
    parser.add_argument("-v", "--verbose", action="store_true",
    help="echo each file decompressed & warn for each file that was not decompressed")
    parser.add_argument("-r", "--recursive", action="store_true",
    help="will traverse contents of folders recursively, performing unpack on each")
    parser.add_argument("filename", nargs="+", help="input file name")
    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    for filename in args.filename:
        if os.path.isdir(filename):
            unpack_recursively(filename, args.verbose, args.recursive)
    else:
        if unpack_file(filename):
            if args.verbose:
                print("Unpacking " + filename)
            
        else:
            if args.verbose:
                print("Ignoring " + filename)
            

__name__=="__main__"
main()

