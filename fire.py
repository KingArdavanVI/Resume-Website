import subprocess

def block_ip_windows(ip):
    rule_name = f"Block_{ip}"
    cmd = f'netsh advfirewall firewall add rule name="{rule_name}" dir=in action=block remoteip={ip}'
    subprocess.run(cmd, shell=True)
    print(f"[+] Blocked IP: {ip}")


def unblock_ip_windows(ip):
    rule_name = f"Block_{ip}"
    cmd = f'netsh advfirewall firewall delete rule name="{rule_name}"'
    subprocess.run(cmd, shell=True)
    print(f"[-] Unblocked IP: {ip}")

block_ip_windows("192.168.1.100")