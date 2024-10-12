import random
import base64
import time
import os

def generate_china():
    return f"223.6.6.{random.randint(1, 255)}"

def generate_germany():
    return f"5.0.0.{random.randint(1, 255)}"

def generate_sweden():
    return f"46.70.{random.randint(1, 255)}.{random.randint(1, 255)}"

def generate_saudi_arabia():
    return f"62.0.{random.randint(1, 255)}.{random.randint(1, 255)}"

def generate_denmark():
    return f"91.148.{random.randint(1, 255)}.{random.randint(1, 255)}"

def generate_bahrain():
    return f"94.72.{random.randint(1, 255)}.{random.randint(1, 255)}"

def generate_egypt():
    return f"2.50.{random.randint(1, 255)}.{random.randint(1, 255)}"

def generate_turkey():
    return f"46.0.{random.randint(1, 255)}.{random.randint(1, 255)}"

def generate_dubai():
    return f"2.48.{random.randint(1, 255)}.{random.randint(1, 255)}"

def generate_usa():
    return f"67.230.{random.randint(1, 255)}.{random.randint(1, 255)}"

def generate_japan():
    x = random.randint(1, 255)
    y = random.randint(1, 255)
    return f"1.0.0.{y}"

def generate_england():
    x = random.randint(1, 255)
    y = random.randint(1, 255)
    return f"109.169.{x}.{y}"

def generate_singapore():
    x = random.randint(1, 255)
    y = random.randint(1, 255)
    return f"152.75.{x}.{y}"

def generate_wireguard_config(country_ip, address, private_key, public_key, dns="8.8.8.8", mtu="1420"):
    allowed_ips = "0.0.0.0/0"
    config = f"""
[Interface]
PrivateKey = {private_key}
Address = {address}
DNS = {dns}
MTU = {mtu}

[Peer]
PublicKey = {public_key}
AllowedIPs = {allowed_ips}
"""
    return config

def print_with_delay(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    header = r"""
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜⬜⬜⬜⬜⬜⬜⬜⬜🟥🟥
🟥🟥⬜⬛⬜⬜⬛⬛⬛⬛⬜🟥🟥
🟥🟥⬜⬛⬜⬜⬛⬜⬜⬜⬜🟥🟥
🟥🟥⬜⬛⬜⬜⬛⬜⬜⬜⬜🟥🟥
🟥🟥⬜⬛⬛⬛⬛⬛⬛⬛⬜🟥🟥
🟥🟥⬜⬜⬜⬜⬛⬜⬜⬛⬜🟥🟥
🟥🟥⬜⬜⬜⬜⬛⬜⬜⬛⬜🟥🟥
🟥🟥⬜⬛⬛⬛⬛⬜⬜⬛⬜🟥🟥
🟥🟥⬜⬜⬜⬜⬜⬜⬜⬜⬜🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
"""
    print_with_delay(header)

def main():
    print_header()
    print("Do you want to use WIREGUARD 🐉or DNS_IPV4?")
    choice = input("Enter 'WIREGUARD' or 'DNS_IPV4': ").strip().lower()

    if choice not in ['wireguard', 'dns_ipv4']:
        print("Invalid choice")
        return

    if choice == 'dns_ipv4':
        dns_suffix = "regular_dns"

        print("Select your SIM card:")
        print("1 == Irancell")
        print("2 == MCI")
        sim_card_choice = input("Enter 1 or 2: ")

        if sim_card_choice == "1":
            base_ip = "78.157.42.100"
        elif sim_card_choice == "2":
            base_ip = "10.202.10.10"
        else:
            print("Invalid choice for SIM card")
            return

        print("\nSelect your country:")
        print(f"1 == China 🇨🇳")
        print(f"2 == Germany 🇩🇪")
        print(f"3 == Sweden 🇸🇪")
        print(f"4 == Saudi Arabia 🇸🇦")
        print(f"5 == Turkey 🇹🇷")
        print(f"6 == Denmark 🇩🇰")
        print(f"7 == Bahrain 🇧🇭")
        print(f"8 == Egypt 🇪🇬")
        print(f"9 == Dubai 🇦🇪")
        print(f"10 == United States 🇺🇸")
        print(f"11 == Japan 🇯🇵")
        print(f"12 == England 🏴")
        print(f"13 == Singapore 🇸🇬")

        country_choice = input("Enter 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, or 13: ")

        if country_choice == "1":
            ip = generate_china()
        elif country_choice == "2":
            ip = generate_germany()
        elif country_choice == "3":
            ip = generate_sweden()
        elif country_choice == "4":
            ip = generate_saudi_arabia()
        elif country_choice == "5":
            ip = generate_turkey()
        elif country_choice == "6":
            ip = generate_denmark()
        elif country_choice == "7":
            ip = generate_bahrain()
        elif country_choice == "8":
            ip = generate_egypt()
        elif country_choice == "9":
            ip = generate_dubai()
        elif country_choice == "10":
            ip = generate_usa()
        elif country_choice == "11":
            ip = generate_japan()
        elif country_choice == "12":
            ip = generate_england()
        elif country_choice == "13":
            ip = generate_singapore()
        else:
            print("Invalid choice for country")
            return

        clear_screen()
        print("\nGenerated IPs:")
        print_with_delay(base_ip)
        print_with_delay(ip)
        print_with_delay("\nThis DNS is for single user. If you give it to someone, its speed will decrease")
        print_with_delay(dns_suffix)

    elif choice == 'wireguard':
        print("\nSelect your country for WireGuard configuration:")
        print(f"1 == China 🇨🇳")
        print(f"2 == Germany 🇩🇪")
        print(f"3 == Sweden 🇸🇪")
        print(f"4 == Saudi Arabia 🇸🇦")
        print(f"5 == Turkey 🇹🇷")
        print(f"6 == Denmark 🇩🇰")
        print(f"7 == Bahrain 🇧🇭")
        print(f"8 == Egypt 🇪🇬")
        print(f"9 == Dubai 🇦🇪")
        print(f"10 == United States 🇺🇸")
        print(f"11 == Japan 🇯🇵")
        print(f"12 == England 🏴")
        print(f"13 == Singapore 🇸🇬")

        country_choice = input("Enter 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, or 13: ")

        if country_choice == "1":
            ip = generate_china()
        elif country_choice == "2":
            ip = generate_germany()
        elif country_choice == "3":
            ip = generate_sweden()
        elif country_choice == "4":
            ip = generate_saudi_arabia()
        elif country_choice == "5":
            ip = generate_turkey()
        elif country_choice == "6":
            ip = generate_denmark()
        elif country_choice == "7":
            ip = generate_bahrain()
        elif country_choice == "8":
            ip = generate_egypt()
        elif country_choice == "9":
            ip = generate_dubai()
        elif country_choice == "10":
            ip = generate_usa()
        elif country_choice == "11":
            ip = generate_japan()
        elif country_choice == "12":
            ip = generate_england()
        elif country_choice == "13":
            ip = generate_singapore()
        else:
            print("Invalid choice for country")
            return

        name = input("What name do you want to give to this configuration? ")

        private_key = base64.b64encode(os.urandom(32)).decode('utf-8')
        public_key = base64.b64encode(os.urandom(32)).decode('utf-8')
        address = f"{random.randint(2, 254)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}/24"

        clear_screen()
        wireguard_config = generate_wireguard_config(ip, address, private_key, public_key)

        print(f"\nGenerated WireGuard Configuration ({name}):")
        print_with_delay(wireguard_config)

if __name__ == "__main__":
    main()