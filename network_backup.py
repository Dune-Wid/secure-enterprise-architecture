from netmiko import ConnectHandler
import datetime

# --- Secure HQ Network Device Inventory ---
# Using the management IPs from VLAN 10 (IT Admin)
devices = [
    {
        'device_type': 'cisco_ios',
        'host': '10.0.10.1', # HQ-EDGE Router
        'username': 'admin',
        'password': 'CyberSec2026!',
        'secret': 'CyberSec2026!',
    },
    {
        'device_type': 'cisco_ios',
        'host': '10.0.10.2', # SW-CORE (Assuming .2 IP)
        'username': 'admin',
        'password': 'CyberSec2026!',
        'secret': 'CyberSec2026!',
    },
    {
        'device_type': 'cisco_ios',
        'host': '10.0.10.3', # SW-ACCESS (Assuming .3 IP)
        'username': 'admin',
        'password': 'CyberSec2026!',
        'secret': 'CyberSec2026!',
    }
]

def backup_configs():
    print("Initiating Secure HQ Network Backup Protocol...\n")
    date_stamp = datetime.datetime.now().strftime("%Y-%m-%d")

    for device in devices:
        try:
            print(f"[*] Connecting to {device['host']} via SSHv2...")
            # Establish SSH connection
            net_connect = ConnectHandler(**device)
            net_connect.enable()
            
            # Pull the running configuration
            output = net_connect.send_command('show run')
            
            # Save to a text file
            filename = f"backup_{device['host']}_{date_stamp}.txt"
            with open(filename, 'w') as backup_file:
                backup_file.write(output)
                
            print(f"[+] Success: Configuration saved to {filename}\n")
            net_connect.disconnect()
            
        except Exception as e:
            print(f"[-] Failed to connect to {device['host']}: {e}\n")

if __name__ == "__main__":
    backup_configs()