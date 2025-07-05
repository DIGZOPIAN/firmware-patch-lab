
FROM gitpod/workspace-full

RUN sudo apt update &&     sudo apt install -y openjdk-17-jdk python3-pip unzip bluetooth bluez libglib2.0-dev &&     pip3 install flask pybluez
