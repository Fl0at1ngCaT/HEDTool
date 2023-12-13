# HEDTool
Simple CLI Tool for hashing, base64 encoding and decoding using python.

![HEDTool](https://github.com/Fl0at1ngCaT/HEDTool/blob/main/resourses/HEDTool.png?raw=true "HEDTool")

## Installation

        git clone https://github.com/Fl0at1ngCaT/HEDTool.git

        cd HEDTool

        pip install -r requirements.txt


## Usage

        Python HEDTool.py [-h] [-x HEX] [-t TEXT] [-e] [-d] [-v | -q]

### options:

        -h, --help            show this help message and exit

        -x HEX, --hex HEX     hash type

        -t TEXT, --text TEXT  your text input

        -e, --encode          base64 encoding

        -d, --decode          base64 decoding

        -v, --verbose         Print Verbose

        -q, --quiet           Print Quiet



### Example: 

         python HEDTool.py -h

         python HEDTool.py -x md5 -t Hello

         python HEDTool.py -e -t Hello

         python HEDTool.py -d -t SGVsbG8=




If you want to include spaces in your -t input, use double quote or single quote

### Example: 

        python HEDTool.py -x sha1 -t 'Hello World'
