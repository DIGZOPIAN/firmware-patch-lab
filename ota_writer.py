import asyncio
from bleak import BleakClient
import sys

# ⛔ Replace this with your real BLE MAC address
TARGET_MAC = "XX:XX:XX:XX:XX:XX"

# ⛔ Replace this with your real writable GATT characteristic UUID
CHAR_UUID = "0000fff2-0000-1000-8000-00805f9b34fb"

async def send_firmware_patch(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()

    async with BleakClient(TARGET_MAC) as client:
        print("Connected to", TARGET_MAC)
        for chunk in [data[i:i+20] for i in range(0, len(data), 20)]:
            await client.write_gatt_char(CHAR_UUID, chunk)
        print("Patch upload complete.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 ota_writer.py patched.bin")
        sys.exit(1)

    asyncio.run(send_firmware_patch(sys.argv[1]))
