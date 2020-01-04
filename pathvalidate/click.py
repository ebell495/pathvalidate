"""
.. codeauthor:: Tsuyoshi Hombashi <tsuyoshi.hombashi@gmail.com>
"""


import click

from ._common import PathType
from ._file import sanitize_filename, sanitize_filepath, validate_filename, validate_filepath
from .error import ValidationError


def validate_filename_arg(ctx, param, value) -> str:
    if not value:
        return ""

    try:
        validate_filename(value)
    except ValidationError as e:
        raise click.BadParameter(str(e))

    return value


def validate_filepath_arg(ctx, param, value) -> str:
    if not value:
        return ""

    try:
        validate_filepath(value)
    except ValidationError as e:
        raise click.BadParameter(str(e))

    return value


def sanitize_filename_arg(ctx, param, value) -> PathType:
    if not value:
        return ""

    return sanitize_filename(value)


def sanitize_filepath_arg(ctx, param, value) -> PathType:
    if not value:
        return ""

    return sanitize_filepath(value)


def filename(ctx, param, value):
    # Deprecated
    if not value:
        return None

    try:
        validate_filename(value)
    except ValidationError as e:
        raise click.BadParameter(e)

    return sanitize_filename(value)


def filepath(ctx, param, value):
    # Deprecated
    if not value:
        return None

    try:
        validate_filepath(value)
    except ValidationError as e:
        raise click.BadParameter(e)

    return sanitize_filepath(value)
