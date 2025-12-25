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

def get_top_processes(limit=5):
    processes = []

    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            info = proc.info

            if info['cpu_percent'] is None or info['memory_percent'] is None:
                continue

            processes.append(info)

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    processes.sort(key=lambda p: p['cpu_percent'], reverse=True)
    return processes[:limit]


def display_stats(stats):
    print("\nSystem Statistics")
    print("-" * 25)
    for key, value in stats.items():
        print(f"{key}: {value}")

def display_processes(processes):
    print("\nTop Running Processes (by CPU)")
    print("-" * 55)
    print(f"{'PID':<8}{'Name':<25}{'CPU %':<10}{'MEM %'}")

    for p in processes:
        print(
            f"{p['pid']:<8}"
            f"{p['name'][:24]:<25}"
            f"{p['cpu_percent']:<10}"
            f"{round(p['memory_percent'], 2)}"
        )

def save_report(stats, processes):
    filename = "system_report.txt"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(filename, "a") as f:
        f.write(f"\nSystem Report - {timestamp}\n")
        f.write("-" * 40 + "\n")

        for key, value in stats.items():
            f.write(f"{key}: {value}\n")

        f.write("\nTop Processes (by CPU)\n")
        for p in processes:
            f.write(
                f"PID {p['pid']} | {p['name']} | "
                f"CPU {p['cpu_percent']}% | "
                f"MEM {round(p['memory_percent'], 2)}%\n"
            )

    print(f"\n[+] Report updated: {filename}")

if __name__ == "__main__":
    stats = get_system_stats()
    processes = get_top_processes()

    display_stats(stats)
    display_processes(processes)
    save_report(stats, processes)
