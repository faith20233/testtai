import sys
import os
import struct

def pack_files(stub_file, binder_file, output_file):
    # Open files
    with open(stub_file, 'rb') as f:
        stub_data = f.read()
    with open(binder_file, 'rb') as f:
        binder_data = f.read()

    # Calculate offsets
    stub_offset = len(binder_data) + 4
    binder_offset = 4

    # Pack header
    header = struct.pack('<II', stub_offset, binder_offset)

    # Pack data
    data = binder_data + header + stub_data

    # Write output file
    with open(output_file, 'wb') as f:
        f.write(data)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Usage: python custom-packer.py <stub-file> <binder-file> <output-file>')
        sys.exit(1)

    stub_file = sys.argv[1]
    binder_file = sys.argv[2]
    output_file = sys.argv[3]

    pack_files(stub_file, binder_file, output_file)