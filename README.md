# setfiledate

Set the date, but not the time, of a bunch of files.

This comes in handy if you have set the date on your camera wrongly. The script maintains the creation time, which can still be off, but at least should maintain the creation order.

Usage:

```
./setfiledate.py 2022-01-15 *jpg
```

The script was copied from [Basti](https://bastibe.de/2015-10-03-changing-file-creation-dates.html). Credits go to Basti, I've just added the CLI wrapper.

