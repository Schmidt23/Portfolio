#!/bin/bash

usage() {
    echo "fixCRLF [options] path"
    echo "options:"
    echo "      -b: print basename of files in path"
    echo "      -c: cat of files in path"
    echo "      -d: unix to dos"
    echo "      -u: dos to unix"
}

print_basename() {
    echo $1 | xargs -n 1 basename  
}

print_cat() {
    cat -v $1
}

dos_to_unix() {
    sed -i $'s/^M$//' $1
}

unix_to_dos() {
    sed -i $'s/$/\r/' $1
}

while getopts 'bcduh' flag; do
    case "${flag}" in
    #add function to FUNC array
    b) FUNC+=(print_basename);;
    c) FUNC+=(print_cat);;
    d) FUNC+=(unix_to_dos);;
    u) FUNC+=(dos_to_unix);;
    h) usage
        exit 1
        ;;
    *) usage
        exit 1
        ;;
    esac
done

#set default if no option is given
if (($OPTIND == 1)); then
    FUNC+=(print_basename)
fi

shift $((OPTIND -1)) #go from options to parameters

FILES=${1:-$PWD}/*  #optional path arg, else current working directory

for f in $FILES
    do
        if [ -f "$f" ]; then
            #iterate through every function in FUNC array
            for fu in "${FUNC[@]}"; do
             $fu $f
             done
        fi
done