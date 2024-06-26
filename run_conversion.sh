#!/bin/bash

# Check if the input file and output file are provided
if [ $# -ne 2 ]; then
  echo "Usage: $0 <input_file> <output_file>"
  exit 1
fi

# Run the Python script with the provided input and output files
python3 convert_nala_to_yay.py "$1" "$2"
