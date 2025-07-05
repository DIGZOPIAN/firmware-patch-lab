import sys

def patch_firmware(input_file, output_file, patch_bytes):
    with open(input_file, 'rb') as f:
        data = bytearray(f.read())

    for address, value in patch_bytes.items():
        data[address] = value

    with open(output_file, 'wb') as f:
        f.write(data)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python3 patch_generator.py input.bin output.bin")
        sys.exit(1)

    # Example patch (speed limiter byte at 0x1A3 set to 0xFF)
    patch_map = { 0x01A3: 0xFF }

    patch_firmware(sys.argv[1], sys.argv[2], patch_map)
    print("Firmware patched and saved to", sys.argv[2])
