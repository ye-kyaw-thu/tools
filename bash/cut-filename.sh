#!/bin/bash

# for cutting path, full filename without path, filename without extension, file extension only
# written by Ye Kyaw Thu, Waseda University, Tokyo, Japan
# How to use: ./cut-filename.sh /home/lar/tool/bash/4github/filename/hello-word.c -p

usage_help()
{
    echo "usage: cut-filename <filename> [ -p | -np | -f | -e ]";
    echo "here,";
    echo "-p or --path for printing path only";
    echo "-np or --no-path for printing filename without path";
    echo "-f or --filename for filename without extension";
    echo "-e or --extension for file extension without name";
}


if [ "$#" -eq 2 ]
   then

      inputFilename=$1

      pathOnly="${inputFilename%/*}"
      filenameWithoutPath=$(basename "$inputFilename")
      filenameWithoutExtension="${inputFilename%.*}"
      extensionOnly="${inputFilename##*.}"



   while [ "$2" != "" ]; do
      case $2 in
         -p | --path )           shift
                                 echo $pathOnly;
                                 ;;
         -np | --no-path )       echo $filenameWithoutPath;
                                 ;;
         -f | --filename )       echo $filenameWithoutExtension;
                                 exit
                                 ;;
         -e | --extension )      echo $extensionOnly;
                                 exit
                                 ;;
          * )                    usage_help
                                 exit 1
      esac
      shift
   done
else
   usage_help
   exit 1
fi

