# Structure to store device information using a class
class Device:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.config = "Default Config"
        self.status = 1  # 1: Online, 0: Offline

# List to store devices
devices = []

# Function to add a new device
def add_device(id, name):
    if len(devices) >= 100:  # MAX_DEVICES = 100
        print("Device limit reached.")
        return
    new_device = Device(id, name)
    devices.append(new_device)
    print(f"Device {name} added successfully.")

# Function to update device configuration
def update_config(id, config):
    for device in devices:
        if device.id == id:
            device.config = config
            print(f"Configuration updated for device {id}.")
            return
    print(f"Device with ID {id} not found.")

# Function to display all devices
def display_devices():
    print("\nDevice List:")
    print("ID\tName\t\tStatus\t\tConfig")
    for device in devices:
        status = "Online" if device.status else "Offline"
        print(f"{device.id}\t{device.name}\t\t{status}\t\t{device.config}")

# Function to set device status
def set_device_status(id, status):
    for device in devices:
        if device.id == id:
            device.status = status
            print(f"Device {id} is now {'Online' if status else 'Offline'}.")
            return
    print(f"Device with ID {id} not found.")

# Main function for the menu
def main():
    while True:
        print("\nAutomated Device Configuration and Management System")
        print("1. Add Device")
        print("2. Update Device Configuration")
        print("3. Display All Devices")
        print("4. Set Device Status")
        print("5. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            try:
                id = int(input("Enter Device ID: "))
                name = input("Enter Device Name: ")
                add_device(id, name)
            except ValueError:
                print("Invalid input. Device ID must be a number.")
        elif choice == 2:
            try:
                id = int(input("Enter Device ID: "))
                config = input("Enter New Configuration: ")
                update_config(id, config)
            except ValueError:
                print("Invalid input.")
        elif choice == 3:
            display_devices()
        elif choice == 4:
            try:
                id = int(input("Enter Device ID: "))
                status = int(input("Enter Status (1 for Online, 0 for Offline): "))
                if status in [0, 1]:
                    set_device_status(id, status)
                else:
                    print("Invalid status. Use 1 for Online or 0 for Offline.")
            except ValueError:
                print("Invalid input.")
        elif choice == 5:
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
