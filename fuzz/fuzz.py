#!/usr/local/bin/python3
import atheris
import sys
from pathvalidate import sanitize_filename, sanitize_filepath, validate_filename, is_valid_filename
from pathvalidate.error import ValidationError

@atheris.instrument_func
def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    
    if len(data) < 1:
        return

    option = fdp.ConsumeBytes(1)[0]
    in_string = fdp.ConsumeUnicodeNoSurrogates(len(data))

    if option % 4 == 0:
        sanitize_filename(in_string)
    elif option % 4 == 1:
        is_valid_filename(in_string)
    elif option % 4 == 2:
        try:
            sanitize_filepath(in_string)
        except ValidationError:
            pass
    elif option % 4 == 3:
        try:
            validate_filename(in_string)
        except ValidationError:
            pass


atheris.instrument_all()
atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()