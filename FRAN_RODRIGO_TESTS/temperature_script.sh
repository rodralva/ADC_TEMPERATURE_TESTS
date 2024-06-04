#!/bin/bash

# Check if file argument is passed
if [ -z "$1" ]
  then
    echo "Error: No output file specified."
    exit 1
fi

if [ -z "$2" ]
  then
    echo "Error: No output file(2) specified."
    exit 1
fi


# Function to execute commands and log output to file
log_output() {
  # Run the first Python command and capture output
  output1=$(python ProbeSelect.py 1 && python TempC-F.py)
  echo "$output1" >> "$1"
  #safety
  sleep 2

  # Run the second Python command and capture output
  output2=$(python ProbeSelect.py 2 && python TempC-F.py)
  echo "$output2" >> "$2"
  #safety
  sleep 2

  # Run the second Python command and capture output
  output3=$(python ProbeSelect.py 3 && python TempC-F.py)
  echo "$output3" >> "$3"
  #safety
  sleep 2

  # Run the second Python command and capture output
  output4=$(python ProbeSelect.py 4 && python TempC-F.py)
  echo "$output4" >> "$4"
}

# Loop until a key is pressed
while true; do
  # Call the log_output function
  log_output "$1" "$2" "$3" "$4"
  
  # Wait for 10 seconds before running the commands again
  sleep 10
  
done

