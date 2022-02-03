# Bird
Official repository for the Bird Programming Language.
## Installation
### Windows
To install on Windows, download the exe from [here](https://github.com/mathstar13/Bird/releases/tag/v1.2.0).
### Linux
To install on Linux, download bird-1.2.0-linux.tar.gz from [here](https://github.com/mathstar13/Bird/releases/tag/v1.2.0).
After downloading, unzip it using the following commands:
```
mkdir tmp
tar -xzvf bird-1.2.0-linux.tar.gz tmp/
cd tmp
```
Then run the installer using `sudo sh bird.sh`.
### MacOS and anything else
*Notice: I don't know if the linux method will work here. Try that before this. If it does, please let me know!*

*To use Bird on these operating systems, you must have at least Python 3.6 installed.*

1. Download the source code from [this link](https://github.com/mathstar13/Bird/releases/tag/v1.2.0) and extract it.
2. Create a file called bddir.txt in your home directory.
3. Inside the file, insert the full path to the folder called `Bird` from the extracted source code.
## Usage
### Windows and Linux
On Windows and Linux, the installer automatically adds the directory to PATH, so all you have to do is run `bird [filename]` from any directory.
### MacOS and anything else
To run Bird files on these operating systems, run `python console.py [filename]` or `python3 console.py [filename]`.
