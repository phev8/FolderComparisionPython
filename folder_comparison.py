__author__ = 'Peter Hevesi'

from os import listdir, walk
from os.path import isfile, isdir, join

source = input("\n\tChoose source directory: ").strip()
dest = input("\tChoose destination directory: ").strip()


print( "\tComparing structure of ", source," and ", dest )


source_list = []
dest_list = []

def scan_dir( path, itemlist, parent="" ):
    current_dir_items =  listdir(path)
    for item in current_dir_items:
        if isdir(join(path, item)):
            itemlist = scan_dir( join(path, item), itemlist, join(parent, item))
        else:
            itemlist.append( join(parent, item))
    return itemlist

source_list = scan_dir( source, source_list)
dest_list = scan_dir( dest, dest_list)

print("\t-------- Missing in destination folder : --------")
any_diff = False
for f in source_list:
    if f not in dest_list:
        print('\t', f, " is missing in destination.")
        any_diff = True

print("\n\n\t-------- Missing in source folder : --------")
for f in dest_list:
    if f not in source_list:
        print('\t', f, " is missing in source.")
        any_diff = True

if not any_diff:
    print("\tNo difference between source and destination.")

print("\t--------------------------------")

