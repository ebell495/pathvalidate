#!/usr/local/bin/python3
import atheris
import sys
from pathvalidate import sanitize_filename, sanitize_filepath, validate_filename, is_valid_filename

@atheris.instrument_func
def TestOneInput(data):
    barray = bytearray(data)
    if len(barray) > 0:
        opt = barray[0]
        del barray[0]
        if opt % 2 == 0:
            sanitize_filename(str(barray))
        elif opt % 2 == 1:
            is_valid_filename(str(barray))
    else:
        sanitize_filename(str(barray))

atheris.instrument_all()
atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()