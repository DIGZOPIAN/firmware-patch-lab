FROM ubuntu:22.04

# Avoids tzdata interactive prompt
ENV DEBIAN_FRONTEND=noninteractive

# Update + install core tools
RUN apt update && apt install -y \
    python3 \
    python3-pip \
    bluetooth \
    bluez \
    libbluetooth-dev \
    unzip \
    curl \
    git \
    sudo \
    nano \
    dbus

# Upgrade pip and install BLE + serial packages
RUN pip3 install --upgrade pip && \
    pip3 install bleak pyserial intelhex

# Optional: Add default workspace directory
WORKDIR /workspace/firmware-patch-lab
