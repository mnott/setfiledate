#!/usr/bin/env python

#
# Change the modification date of a bunch of files, but not the time.
#

import os
import sys
import click
import datetime
from datetime import date

@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.option('--d',  help='The new modification date.', default=date.today(), show_default=True)
@click.argument('files', nargs=-1)

def cli(d, files):
  """This script changes the modification date of files, but not the time."""
  datem = datetime.datetime.strptime(d, "%Y-%m-%d")

  for filename in files:
    old_date = datetime.datetime.fromtimestamp(os.path.getctime(filename))
    new_date = datetime.datetime(datem.year, datem.month, datem.day, old_date.hour, old_date.minute, old_date.second)
    os.system('SetFile -d "{}" {}'.format(new_date.strftime('%m/%d/%Y %H:%M:%S'), filename))
    os.system('SetFile -m "{}" {}'.format(new_date.strftime('%m/%d/%Y %H:%M:%S'), filename))

#
# Main loop.
#
if __name__=='__main__':
  if len(sys.argv) == 1:
      cli.main(['--help'])
  else:
      cli()
