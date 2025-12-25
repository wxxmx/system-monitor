import psutil
from datetime import datetime

def get_system_stats():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    return {
        "CPU Usage (%)": cpu,
        "Memory Usage (%)": memory.percent,
        "Disk Usage (%)": disk.percent
    }

def display_stats(stats):
    print("\nSystem Statistics")
    print("-" * 25)
    for key, value in stats.items():
        print(f"{key}: {value}")

def save_report(stats):
    filename = "system_report.txt"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(filename, "a") as f:
        f.write(f"\nSystem Report - {timestamp}\n")
        f.write("-" * 30 + "\n")
        for key, value in stats.items():
            f.write(f"{key}: {value}\n")

    print(f"\n[+] Report saved to {filename}")

if __name__ == "__main__":
    stats = get_system_stats()
    display_stats(stats)
    save_report(stats)
