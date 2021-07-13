#!/usr/bin/bash

# The following script is used to rename and move .gpx file generated by Columbus P-10 Pro logger. 
# Files generated by logger has follwing naming convention by default YYYY-mm/ddHHMMSS.GPX
# This script changes them to YYYY-mm/YYYY-mm-dd_HHMMSS.GPX
# Also moves the files into an $ARCHIVE_NAME folder.

ARCHIVE_NAME="_RENAMED"

file_counter=0

function rename_files {
# $1 = folder name
    # ignore upper/lower case in the filenames
    shopt -s nocasematch 
    
    # remove last char ('/') from folder name
    date_prefix="${1::-1}"
    
    for file in "$1"* ; do
        # if it's a .gpx file
        if [[ $file == *".gpx"* ]]; then
            if [[ ! $file == *"_"* ]]; then
                # split path to file by slashes and keep the last part
                filename=${file##*/}
                # first two chars from filename are DAY, the rest is time
                day="${filename::2}" 
                timestamp="${filename:2}"
                # insert the prefix into new filename
                file_new=${1}${date_prefix}-${day}_${timestamp}
                echo "$file -> $file_new"
                mv "$file" "$file_new"
                ((file_counter+=1))
            fi
        fi
    done
}


function archive {
    mkdir -p $ARCHIVE_NAME
    echo "Archiving $1"
    # cp+rm used instead of mv to handle already existing directories
    cp -R "$1" "$ARCHIVE_NAME"
    rm -R "$1"
}


# for each folder that has a dash (yyyy-mm)
for folder in */ ; do
    if [[ $folder == *"-"* ]]; then
      # rename files within the folder so they have a full date
      rename_files "$folder"
    fi
done

# read used so the terminal won't close after exectuion is complete
echo "Reanming completed. $file_counter files processed."

read -p "Do you wish to move the files into archive ($ARCHIVE_NAME)? [y/n]" -n 1 -r
echo
# move the folders into archive, if user agrees
if [[ $REPLY =~ ^[Yy]$ ]]; then
    for folder in */ ; do
        if [[ $folder == *"-"* ]]; then
          archive "$folder"
        fi
    done
fi



