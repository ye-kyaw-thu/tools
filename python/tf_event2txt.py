"""
Created on Fri, 15 Dec 2023

@author: Ye Kyaw Thu, Visiting Professor, LST, NECTEC, Thailand

How to Run:
$ python ./tf_event2txt.py --help
$ time python ./tf_event2txt.py --input ./events.out.tfevents.1702602561.lst-gpu-3090.18783.0 --output ./log.txt
"""

import argparse
import sys
import tensorflow as tf
from tensorflow.core.util import event_pb2
from tensorflow.python.lib.io import tf_record

def read_tf_events_file(file_path, output_file=None):
    for serialized_example in tf_record.tf_record_iterator(file_path):
        event = event_pb2.Event.FromString(serialized_example)
        output_string = "Event: {}\n".format(event)
        if event.WhichOneof('what') == 'summary':
            for value in event.summary.value:
                output_string += "Summary Value: {}\n".format(value)

        if output_file:
            with open(output_file, 'a') as f:
                f.write(output_string)
        else:
            print(output_string)

def main():
    parser = argparse.ArgumentParser(description="Read TensorFlow event files.")
    parser.add_argument("-i", "--input", type=str, help="Input TensorFlow event file. If not provided, reads from stdin.")
    parser.add_argument("-o", "--output", type=str, help="Output file to write the results. If not provided, prints to stdout.")
    args = parser.parse_args()

    if args.input:
        read_tf_events_file(args.input, args.output)
    else:
        # Read from stdin
        for line in sys.stdin:
            read_tf_events_file(line.strip(), args.output)

if __name__ == "__main__":
    main()
