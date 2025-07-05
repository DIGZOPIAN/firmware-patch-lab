import asyncio
from bleak import BleakClient
import sys

# ✅ Digzopian BLE target for X-Bot (or Nordic UART BLE clone)
TARGET_MAC = "M0:RO:BO:T9:E4:B4"  # ⚠️ Replace this with your actual MAC from LightBlue

# ✅ BLE Write UUID discovered from LightBlue connection
CHAR_UUID = "6E400001-B5A3-F393-E0A9-E50E24DCCA9E"

async def send_firmware_patch(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()

    async with BleakClient(TARGET_MAC) as client:
        print("✅ Connected to", TARGET_MAC)
        for chunk in [data[i:i+20] for i in range(0, len(data), 20)]:
            await client.write_gatt_char(CHAR_UUID, chunk)
        print("✅ Patch upload complete.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 ota_writer.py patched_file.bin")
        sys.exit(1)

    asyncio.run(send_firmware_patch(sys.argv[1]))
