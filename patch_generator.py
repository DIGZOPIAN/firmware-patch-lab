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

    # PATCH MAP — X-Bot M365 Clone
    patch_map = {
        0x01A3: 0x2D,  # Eco Mode Speed: 45 km/h
        0x01A4: 0x2D,  # Sport Mode Speed: 45 km/h
        0x01B2: 0x01,  # Cruise Control Enabled
        0x01D8: 0xA0   # Torque Curve Boost
    }

    patch_firmware(sys.argv[1], sys.argv[2], patch_map)
    print("✅ Firmware patched and saved to", sys.argv[2])
