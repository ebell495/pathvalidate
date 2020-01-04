#!/usr/bin/env python3

import click

from pathvalidate.click import validate_filename_arg, validate_filepath_arg


@click.command()
@click.option("--filename", callback=validate_filename_arg)
@click.option("--filepath", callback=validate_filepath_arg)
def cli(filename, filepath):
    if filename:
        click.echo("filename: {}".format(filename))
    if filepath:
        click.echo("filepath: {}".format(filepath))


if __name__ == "__main__":
    cli()
