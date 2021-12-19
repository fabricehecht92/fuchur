# fuchur
A simple script to add bookmarks to a textfile - I use it to save things when using tor

usage:

  python3 fuchur https://website.com /path/to/textfile/bookmarks.txt

to find the right bookmark just use:

  cat bookmarks.txt | grep <searchterm>
  
Note: Some website seem to block the request from the script. There is currently no fix.
