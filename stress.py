import os,subprocess
import logging
# Logging configuration
#logging.basicConfig( filename="/root/stress_test.log", level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S" )
def memory_stress_test():
    print("Starting Memory Stress Test...")
    # Running memory stress test with stress-ng
    #subprocess.run(['stress-ng', '--vm', '2', '--vm-bytes', '80%'])
    os.system("stress-ng --vm 1 --vm-bytes 80% -t 60s ")
    print("Memory Stress Test Completed.")

def disk_stress_test():
    print("Starting Disk Stress Test...")
    # Running disk stress test with stress-ng
    #subprocess.run(['stress-ng', '--hdd', '2', '--hdd-bytes', '80%'])
    os.system("stress-ng --iomix 4 --iomix-bytes 90% --timeout 100s ")
    #os.system("stress-ng --hdd 4 --hdd-bytes 90% --timeout 100s ")
    print("Disk Stress Test Completed.")
def network_stress_test():
    print("Starting Network Stress Test...")
    # Assuming iperf3 server is running on vm_2 with IP 192.168.29.49
    result = subprocess.run(['iperf3', '-c', '192.168.1.5', '-t', '30'], capture_output=True, text=True)
    print(result.stdout)
    #os.system("stress-ng --net 4 --net-bytes  80M --timeout 60s")
    print("Network Stress Test Completed.")

def cpu_stress_test():
    print("Starting CPU Stress Test...")
    # Running CPU stress test with stress-ng
    #subprocess.run(['stress-ng', '--cpu', '2', '--timeout', '60'])
    os.system("stress-ng --cpu 4 --cpu-load 80 -t 60s")
    print("CPU Stress Test Completed.")

def mysql_stress_test():
    # Running sysbench for MySQL stress testing
    # Adjust the parameters as needed
    print("Starting MySQL Stress Test...")
    process = subprocess.Popen([
        'sysbench',
        '--test=/usr/share/sysbench/oltp_read_only.lua',
        '--mysql-db=test',
        '--mysql-user=stress',
        '--mysql-password=password',
        '--max-time=60',
        '--max-requests=0',
        '--threads=2',
        'run'
    ])
    #return process
    print("MySQL Stress Test Completed.")
def function():
    logging.info("Starting MySQL Stress Test...")

    # Replace 'your_vm2_ip' with the actual IP address of vm_2
    vm2_ip = '192.168.1.5'  # Example IP address for vm_2

    # Running sysbench for MySQL stress testing
    process = subprocess.Popen([
        'sysbench',
        '--test=/usr/share/sysbench/oltp_read_only.lua',
        '--mysql-db=random',
        '--mysql-user=stress',
        '--mysql-password=password',  # Replace with actual password
        f'--mysql-host={vm2_ip}',          # Specify the MySQL host
        '--max-time=30',
        '--max-requests=0',
        '--threads=2',
        'run'
    ])
    process.wait()  # Wait for MySQL stress test to complete
    logging.info("MySQL Stress Test Completed.")

def main():
    while True:
        print("\nSelect an option for stress testing:")
        print("1. Memory Stress Testing")
        print("2. Disk Stress Testing")
        print("3. Network Stress Testing")
        print("4. CPU Stress Testing")
        print("5. MySQL Stress Testing")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            memory_stress_test()
        elif choice == "2":
            disk_stress_test()
        elif choice == "3":
            network_stress_test()
        elif choice == "4":
            cpu_stress_test()
        elif choice == "5":
            function()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
        logging.basicConfig( filename="/root/stress_test.log", level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

if __name__=="__main__":
    main()
