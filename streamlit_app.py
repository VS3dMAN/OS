import streamlit as st

# Structure to store device information using a class
class Device:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.config = "Default Config"
        self.status = 1  # 1: Online, 0: Offline

# Initialize session state for devices
if "devices" not in st.session_state:
    st.session_state.devices = []

# Function to add a new device
def add_device(id, name):
    if len(st.session_state.devices) >= 100:  # MAX_DEVICES = 100
        st.error("Device limit reached.")
        return
    new_device = Device(id, name)
    st.session_state.devices.append(new_device)
    st.success(f"Device {name} added successfully.")

# Function to update device configuration
def update_config(id, config):
    for device in st.session_state.devices:
        if device.id == id:
            device.config = config
            st.success(f"Configuration updated for device {id}.")
            return
    st.error(f"Device with ID {id} not found.")

# Function to display all devices
def display_devices():
    if not st.session_state.devices:
        st.warning("No devices to display.")
        return

    data = [{
        "ID": device.id,
        "Name": device.name,
        "Status": "Online" if device.status else "Offline",
        "Config": device.config
    } for device in st.session_state.devices]
    st.table(data)

# Function to set device status
def set_device_status(id, status):
    for device in st.session_state.devices:
        if device.id == id:
            device.status = status
            st.success(f"Device {id} is now {'Online' if status else 'Offline'}.")
            return
    st.error(f"Device with ID {id} not found.")

# Streamlit UI
st.title("Automated Device Configuration and Management System")

menu = ["Add Device", "Update Configuration", "Display Devices", "Set Device Status"]
choice = st.sidebar.selectbox("Select Action", menu)

if choice == "Add Device":
    st.subheader("Add a New Device")
    id = st.number_input("Enter Device ID", min_value=1, step=1)
    name = st.text_input("Enter Device Name")
    if st.button("Add Device"):
        if name:
            add_device(id, name)
        else:
            st.error("Device name cannot be empty.")

elif choice == "Update Configuration":
    st.subheader("Update Device Configuration")
    id = st.number_input("Enter Device ID", min_value=1, step=1)
    config = st.text_input("Enter New Configuration")
    if st.button("Update Configuration"):
        if config:
            update_config(id, config)
        else:
            st.error("Configuration cannot be empty.")

elif choice == "Display Devices":
    st.subheader("Device List")
    display_devices()

elif choice == "Set Device Status":
    st.subheader("Set Device Status")
    id = st.number_input("Enter Device ID", min_value=1, step=1)
    status = st.radio("Select Status", [1, 0], format_func=lambda x: "Online" if x == 1 else "Offline")
    if st.button("Set Status"):
        set_device_status(id, status)
