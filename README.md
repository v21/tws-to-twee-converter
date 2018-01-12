tws-to-twee-converter
=====================

Converts Twine .tws files to .twee files

The python script takes a file as an argument, and prints the resulting Twee file to stdout.

To use, do something like:

````
python twsimporter.py twinefile.tws > newtweefile.tw
````

Also accepts a `-twee2` option, which will include the position of each passage in `twee2` output file format:

````
python twsimporter.py twinefile.tws -twee2 > newtweefile.tw2
````
