#!/usr/bin/env python3

import platform
import subprocess
import socket
import time
import os

def get_uptime():
    """Return system uptime in seconds."""
    try:
        with open("/proc/uptime", "r") as f:
            uptime_seconds = float(f.readline().split()[0])
        return uptime_seconds
    except Exception as e:
        return f"Error getting uptime: {e}"

def format_uptime(seconds):
    """Format seconds into days, hours, minutes."""
    days = int(seconds // 86400)
    hours = int((seconds % 86400) // 3600)
    minutes = int((seconds % 3600) // 60)
    return f"{days}d {hours}h {minutes}m"

def get_os_version():
    """Return OS version from /etc/os-release or platform module."""
    try:
        if os.path.exists("/etc/os-release"):
            with open("/etc/os-release") as f:
                data = f.read()
            return data
        else:
            return platform.platform()
    except Exception as e:
        return f"Error getting OS version: {e}"

def check_port(host, port, timeout=2):
    """Check if a TCP port is open."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0
    except Exception:
        return False

def main():
    print("==== SYSTEM CHECK REPORT ====\n")

    # Uptime
    uptime_seconds = get_uptime()
    if isinstance(uptime_seconds, float):
        print(f"Uptime: {format_uptime(uptime_seconds)}")
    else:
        print(uptime_seconds)

    print("\n=== OS Version ===")
    print(get_os_version())

    # Port checks
    print("\n=== Port Checks ===")
    host = "127.0.0.1"

    ssh_open = check_port(host, 22)
    http_open = check_port(host, 80)

    print(f"SSH (22): {'OPEN' if ssh_open else 'CLOSED'}")
    print(f"HTTP (80): {'OPEN' if http_open else 'CLOSED'}")

if __name__ == "__main__":
    main()
