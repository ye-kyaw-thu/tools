#!/bin/bash

for fd in */ ; do

   cd ./$fd;
   echo "Making spectrogram for $(pwd)";

   for file in *mono*.wav;do
      outfile="${file%.*}.png"
      sox "$file" -n spectrogram -r -o "$outfile"
   done

   #mogrify -strip -quality 80% -sampling-factor 4:4:4 -format jpg spectrograms/*.png
   mogrify -strip -quality 80% -sampling-factor 4:4:4 -format jpg ./*.png;

   rm *.png;
   cd ..;

done
