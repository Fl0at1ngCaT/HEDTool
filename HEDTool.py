import sys
from argparse import*
from pyfiglet import figlet_format
from colorama import Fore, Style
from modules.HED_Fun import*


logo = figlet_format("H E D", font="poison")
logo1 = figlet_format("TOOL", font="poison")
print(Style.BRIGHT + Fore.MAGENTA + logo + Style.NORMAL + Fore.BLUE + logo1)

parser = ArgumentParser(add_help=True)
parser.add_argument("-x", "--hex")
parser.add_argument("-t", "--text")
parser.add_argument("-e", "--encode", action="store_true", help="base64 encoding")
parser.add_argument("-d", "--decode", action="store_true", help="base64 decoding")
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true", help="Print Verbose")
group.add_argument("-q","--quiet", action="store_true", help="Print Quiet")
args = parser.parse_args()

def Help():
    print(Fore.CYAN + "\n\nExample: python HEDTool.py -h\n\t python HEDTool.py -x md5 -t Hello\n\t python HEDTool.py -e -t Hello\n\t python HEDTool.py -d -t SGVsbG8=")
    print(Fore.YELLOW + "\nIf you want to include spaces in your -t input, use double quote or single quote\n")
    print(Fore.CYAN + "Example: python HEDTool.py -x sha1 -t 'Hello World'")

if args.verbose:
    if args.hex:
        hash = Hash(args.text, args.hex)
        print(Fore.YELLOW + "Your Input: " + Fore.CYAN + args.text + "\t" + Fore.YELLOW + "Length: " + Fore.CYAN + str(len(args.text)))
        print(Fore.YELLOW + "Hash: " + Fore.CYAN + hash + "\t" + Fore.YELLOW + "Length: " + Fore.CYAN + str(len(hash)))
        print(Fore.YELLOW + "Hash type: " + Fore.CYAN + args.hex)

    if args.encode:
        encoded = Encode(args.text)
        print(Fore.YELLOW + "Your Input: " + Fore.CYAN + args.text + "\t" + Fore.YELLOW + "Length: " + Fore.CYAN + str(len(args.text)))
        print(Fore.YELLOW + "Encoded String: " + Fore.CYAN + encoded + "\t" + Fore.YELLOW + " Length: " + Fore.CYAN + str(len(encoded)))
        print(Fore.YELLOW + "Encoding type: " + Fore.CYAN + "base64")

    if args.decode:
        decoded = Decode(args.text)
        print(Fore.YELLOW + "Your Input: " + Fore.CYAN + args.text + "\t" + Fore.YELLOW + "Length: " + Fore.CYAN + str(len(args.text)))
        print(Fore.YELLOW + "Decoded String: " + Fore.CYAN + decoded + "\t" + Fore.YELLOW + " Length: " + Fore.CYAN + str(len(decoded)))
        print(Fore.YELLOW + "Decoding type: " + Fore.CYAN + "base64")
elif args.quiet:
    if args.hex:
        hash = Hash(args.text, args.hex)
        print(Fore.CYAN + hash)

    if args.encode:
        encoded = Encode(args.text)
        print(Fore.CYAN + encoded)

    if args.decode:
        decoded = Decode(args.text)
        print(Fore.CYAN + decoded)
else:
    if args.hex:
        hash = Hash(args.text, args.hex)
        print(Fore.YELLOW + "Hash: " + Fore.CYAN + hash)

    if args.encode:
        encoded = Encode(args.text)
        print(Fore.YELLOW + "Encoded String: " + Fore.CYAN + encoded)
        print(sys.argv[:])

    if args.decode:
        decoded = Decode(args.text)
        print(Fore.YELLOW + "Decoded String: " + Fore.CYAN + decoded)

if len(sys.argv[1:]) < 2:
    Help()