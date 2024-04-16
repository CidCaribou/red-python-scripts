# Discover access points
discover_access_points = subprocess.Popen(["sudo", "airodump-ng", "--band", "a", "-w", "file", "--write-interval", "1", "--output-format", "csv", hacknic + "mon"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# Loop that shows the wireless access points and their clients.
try:
    while True:
        # Clear the screen before displaying networks and clients.
        subprocess.call("clear", shell=True)
        for file_name in os.listdir():
            # Look for CSV files to read network information.
            if ".csv" in file_name:
                with open(file_name) as csv_h:
                    csv_reader = csv.reader(csv_h)
                    clients_displayed = set()  # To avoid displaying clients multiple times
                    for row in csv_reader:
                        # Skip header rows
                        if "BSSID" in row:
                            continue
                        # Display network information
                        print(f"Network: {row[13]} (BSSID: {row[0]}, Channel: {row[3]})")
                        # Display associated clients
                        if row[0] not in clients_displayed:  # Avoid displaying clients for the same network multiple times
                            clients_displayed.add(row[0])
                            print("Clients:")
                            print("No |\tMAC Address       |\tClient Name")
                            print("___|\t_________________|\t____________________________")
                            client_count = 0
                            for client_row in csv_reader:
                                # Skip header rows and clients not associated with the current network
                                if "BSSID" in client_row or client_row[0] != row[0]:
                                    continue
                                client_count += 1
                                print(f"{client_count}\t{client_row[0]}\t{client_row[5]}")
                            break  # Stop reading the CSV file after displaying clients for the current network
        # Wait for user input
        print("\nSelect a client to target (enter the corresponding number) or press Ctrl+C to exit:")
        choice = input()
        # Perform actions based on user input
        # (e.g., perform deauthentication attack on the selected client)
        # Add your code here based on user choice
except KeyboardInterrupt:
    print("\nReady to make choice.")
