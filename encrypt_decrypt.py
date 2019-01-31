#!/usr/bin/env/ python

import pyAesCrypt
import os
from getpass import getpass
import argparse

# os.chdir('/Users/urieldabby/Downloads/temp')


def encrypt(filename):
    # encryption/decryption buffer size - 64K
    bufferSize = 64 * 1024
    password = getpass()
    # encrypt
    pyAesCrypt.encryptFile(filename, "%s.aes" % filename, password, bufferSize)
    print("\nFile Encrypted\n")
    if input("Delete source file? [Y/N]").upper() == 'Y':
        os.remove(filename)
        print("Source file deleted")


def decrypt(filename):
    # encryption/decryption buffer size - 64K
    bufferSize = 64 * 1024
    password = getpass()
    try:
        # decrypt
        pyAesCrypt.decryptFile("%s.aes" % filename, filename, password, bufferSize)
        print("\nFile Decrypted\n")
    except:
        print("\nWrong Password\n")


parser = argparse.ArgumentParser(description="File Encryption/Decryption Program")


parser.add_argument("-e", "--encrypt", nargs=1, metavar = "source", default=None, help="Encrypt File")
parser.add_argument("-d", "--decrypt", nargs=1, metavar = "source", default=None, help="Decrypt File")

args = parser.parse_args()


if args.encrypt != None:
    filename = args.encrypt[0]
    encrypt(filename)

if args.decrypt != None:
    filename = args.decrypt[0]
    decrypt(filename)
