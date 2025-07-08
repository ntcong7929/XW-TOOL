import base64
import hashlib
import json
import math
import os
import platform
import random
import re
import socket
import statistics
import subprocess
import sys
import threading
import time
from collections import Counter, defaultdict, deque
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta
from datetime import datetime as dt
from time import sleep
import requests
from bs4 import BeautifulSoup
try:
    from colorama import Fore, Style, init
    from faker import Faker
    import pystyle
    init(autoreset=True)
    COLORAMA_AVAILABLE = True
except ImportError:
    os.system("pip install faker requests colorama bs4 pystyle")
    fancy_print('Vui lòng chạy lại tool sau khi cài đặt!', Colors.NEON_RED, delay=1)
    sys.exit()
# Tạo hoặc đọc khóa mã hóa bằng base64
secret_key = base64.urlsafe_b64encode(os.urandom(32))


# Mã hóa và giải mã dữ liệu bằng base64
def encrypt_data(data):
    return base64.b64encode(data.encode()).decode()


def decrypt_data(encrypted_data):
    return base64.b64decode(encrypted_data.encode()).decode()


# Màu sắc cho hiển thị
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;39m"
end = "\033[0m"


def banner():
    os.system("cls" if os.name == "nt" else "clear")
    neon = [
        "\033[38;5;51m░██████╗████████╗░██████╗░░██████╗░██╗░░░░░\033[0m",
        "\033[38;5;51m██╔════╝╚══██╔══╝██╔═══██╗██╔═══██╗██║░░░░░\033[0m",
        "\033[38;5;51m██║░░░░░░░░██║░░░██║░░░██║██║░░░██║██║░░░░░\033[0m",
        "\033[38;5;51m██║░░░░░░░░██║░░░██║░░░██║██║░░░██║██║░░░░░\033[0m",
        "\033[38;5;51m╚██████╗░░░██║░░░╚██████╔╝╚██████╔╝███████╗\033[0m",
        "\033[38;5;51m ╚═════╝░░░╚═╝░░░░╚═════╝░░╚═════╝░╚══════╝\033[0m",
    ]
    for line in neon:
        print(line)
        time.sleep(0.07)
    print("\033[38;5;199m" + "═" * 50 + "\033[0m")
    print("\033[38;5;46m" + "🌟 XWORLD - CHẠY ĐUA TỐC ĐỘ 🌟".center(50) + "\033[0m")
    print("\033[38;5;199m" + "═" * 50 + "\033[0m")
    print("\033[38;5;226mYouTube: https://www.youtube.com/@Tool-Xworld\033[0m")
    print("\033[38;5;226mTelegram: https://t.me/+RL_zVyZjvx1hZjc1\033[0m")
    print("\033[38;5;226mAdmin: Thành Công | Zalo: 0842010239\033[0m")
    print("\033[38;5;199m" + "═" * 50 + "\033[0m")


def get_ip_address():
    try:
        response = requests.get("https://api.ipify.org?format=json")
        ip_data = response.json()
        ip_address = ip_data["ip"]
        return ip_address
    except Exception as e:
        print(f"Lỗi khi lấy địa chỉ IP: {e}")
        return None


def display_ip_address(ip_address):
    if ip_address:
        banner()
        print(f"\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;31mĐịa chỉ IP : {ip_address}")
    else:
        print("Không thể lấy địa chỉ IP của thiết bị.")


def luu_thong_tin_ip(ip, key, expiration_date):
    data = {ip: {"key": key, "expiration_date": expiration_date.isoformat()}}
    encrypted_data = encrypt_data(json.dumps(data))

    with open(KEY_FILE, "w") as file:
        file.write(encrypted_data)


def tai_thong_tin_ip():
    try:
        with open(KEY_FILE, "r") as file:
            encrypted_data = file.read()
        data = json.loads(decrypt_data(encrypted_data))
        return data
    except FileNotFoundError:
        return None


def kiem_tra_ip(ip):
    data = tai_thong_tin_ip()
    if data and ip in data:
        expiration_date = datetime.fromisoformat(data[ip]["expiration_date"])
        if expiration_date > datetime.now():
            return data[ip]["key"]
    return None


def generate_key_and_url(ip_address):
    ngay = int(datetime.now().day)
    key1 = str(ngay * 27 + 27)
    ip_numbers = "".join(filter(str.isdigit, ip_address))
    key = f"NTC{key1}{ip_numbers}"
    expiration_date = datetime.now() + timedelta(hours=12)
    url = f"https://hohiepvn.x10.mx/key/van-thang-vip.php?key={key}"
    return url, key, expiration_date


def da_qua_gio_moi():
    now = datetime.now()
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(
        hours=12
    )
    return now >= midnight


def get_shortened_link_phu(url):
    try:
        token = "66e82f69e4b6f63fe227f33e"
        api_url = f"https://link4m.co/api-shorten/v2?api={token}&url={url}"

        response = requests.get(api_url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return {
                "status": "error",
                "message": "Không thể kết nối đến dịch vụ rút gọn URL.",
            }
    except Exception as e:
        return {"status": "error", "message": f"Lỗi khi rút gọn URL: {e}"}

class Colors:
    NEON_BLUE = "\033[38;5;39m"
    NEON_CYAN = "\033[38;5;51m"
    NEON_GREEN = "\033[38;5;46m"
    NEON_PINK = "\033[38;5;199m"
    NEON_PURPLE = "\033[38;5;135m"
    NEON_YELLOW = "\033[38;5;226m"
    NEON_ORANGE = "\033[38;5;214m"
    NEON_RED = "\033[38;5;196m"
    NEON_WHITE = "\033[38;5;255m"
    NEON_MAGENTA = "\033[38;5;201m"
    
    GRADIENT_BLUE = ["\033[38;5;17m", "\033[38;5;18m", "\033[38;5;19m", "\033[38;5;20m", "\033[38;5;21m"]
    GRADIENT_PURPLE = ["\033[38;5;54m", "\033[38;5;55m", "\033[38;5;56m", "\033[38;5;57m", "\033[38;5;93m"]
    GRADIENT_GREEN = ["\033[38;5;22m", "\033[38;5;28m", "\033[38;5;34m", "\033[38;5;40m", "\033[38;5;46m"]
    GRADIENT_RAINBOW = ["\033[38;5;196m", "\033[38;5;214m", "\033[38;5;226m", "\033[38;5;46m", "\033[38;5;51m", "\033[38;5;201m"]
    
    RESET = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"

# Constants
ROOM_NAMES = [
    " ",
    "Nhà kho",
    "Phòng họp",
    "Phòng giám đốc",
    "Phòng trò chuyện",
    "Phòng giám sát",
    "Văn phòng",
    "Phòng tài vụ",
    "Phòng nhân sự"
]
CONFIG_FILE = "xworld_config.json"
DATA_FILE = "dulieu.txt"
STATS_FILE = "thongke.json"
KEY_FILE = "ip_key_vth.json"

def clear_screen():
    os.system('cls' if platform.system() == "Windows" else 'clear')

def fancy_print(text, color=Fore.WHITE, style=Style.NORMAL, end='\n', delay=0):
    if COLORAMA_AVAILABLE:
        print(f"{style}{color}{text}{Style.RESET_ALL}", end=end)
    else:
        print(text, end=end)
    if delay > 0:
        time.sleep(delay)

def gradient_text(text, colors):
    if not colors:
        return text
    result = ""
    text_len = len(text)
    color_len = len(colors)
    for i, char in enumerate(text):
        color_index = int((i / text_len) * (color_len - 1))
        result += colors[color_index] + char
    return result + Colors.RESET

def typewriter_effect(text, color=Fore.WHITE, delay=0.02):
    for char in text:
        print(f"{color}{char}{Style.RESET_ALL}", end='', flush=True)
        time.sleep(delay)
    print()

def display_animated_banner():
    clear_screen()
    banner_text = """
░██████╗████████╗░██████╗░░██████╗░██╗░░░░░
██╔════╝╚══██╔══╝██╔═══██╗██╔═══██╗██║░░░░░
██║░░░░░░░░██║░░░██║░░░██║██║░░░██║██║░░░░░
██║░░░░░░░░██║░░░██║░░░██║██║░░░██║██║░░░░░
╚██████╗░░░██║░░░╚██████╔╝╚██████╔╝███████╗
 ╚═════╝░░░╚═╝░░░░╚═════╝░░╚═════╝░╚══════╝
"""
    lines = banner_text.strip().split('\n')
    for line in lines:
        gradient_line = gradient_text(line, Colors.GRADIENT_RAINBOW)
        print(gradient_line)
        time.sleep(0.15)
    
    print()
    title_text = "🌟 XWORLD - VUA THOÁT HIỂM 🌟"
    subtitle_text = "✨ Tool Vip by Thành Công ✨"
    
    print(f"{Colors.NEON_CYAN}{'═' * 50}{Colors.RESET}")
    print(f"{Colors.NEON_PINK}{title_text:^50}{Colors.RESET}")
    print(f"{Colors.NEON_GREEN}{subtitle_text:^50}{Colors.RESET}")
    print(f"{Colors.NEON_CYAN}{'═' * 50}{Colors.RESET}")
    
    time.sleep(1)
    print(f"\n{Colors.NEON_YELLOW}📞 THÔNG TIN LIÊN HỆ:{Colors.RESET}")
    print(f"{Colors.NEON_CYAN}{'═' * 50}{Colors.RESET}")
    
    contact_info = [
        ("📺 YouTube", "https://www.youtube.com/@Tool-Xworld"),
        ("📱 Telegram", "https://t.me/+RL_zVyZjvx1hZjc1"),
        ("🎵 TikTok", "https://www.tiktok.com/@cng1237929"),
        ("📞 Zalo", "0842010239"),
        ("👉 Admin", "Thành Công")
    ]
    
    for icon_name, info in contact_info:
        print(f"{Colors.NEON_WHITE}{icon_name:<10}: {Colors.NEON_CYAN}{info}{Colors.RESET}")
        time.sleep(0.1)
    
    print(f"{Colors.NEON_CYAN}{'═' * 50}{Colors.RESET}")
    print(f"{Colors.NEON_PURPLE}⚡ Phiên bản: {Colors.NEON_YELLOW}V2.0 Pro{Colors.RESET}")
    print(f"{Colors.NEON_PURPLE}🚀 Trạng thái: {Colors.NEON_GREEN}Hoạt động{Colors.RESET}")
    
    time.sleep(2)

def display_modern_header():
    current_time = datetime.now().strftime("%H:%M:%S")
    current_date = datetime.now().strftime("%d/%m/%Y")
    
    print(f"\n{Colors.NEON_PINK}🎮 DASHBOARD{Colors.RESET}")
    print(f"{Colors.NEON_BLUE}🚀 Vua Thoát Hiểm Assistant{Colors.RESET}")
    print(f"{Colors.NEON_CYAN}{'═' * 50}{Colors.RESET}")
    
    print(f"{Colors.NEON_GREEN}⏰ Thời gian: {Colors.NEON_YELLOW}{current_time}{Colors.RESET} | {Colors.NEON_GREEN}📅 Ngày: {Colors.NEON_YELLOW}{current_date}{Colors.RESET}")
    print(f"{Colors.NEON_GREEN}🌐 IP Address: {Colors.NEON_YELLOW}192.168.1.100{Colors.RESET} | {Colors.NEON_GREEN}🔑 Status: {Colors.NEON_GREEN}Active{Colors.RESET}")
    
    print(f"{Colors.NEON_CYAN}{'═' * 50}{Colors.RESET}")

def display_loading_animation():
    print(f"\n{Colors.NEON_YELLOW}⚡ INITIALIZING SYSTEM ⚡{Colors.RESET}")
    print(f"{Colors.NEON_CYAN}{'═' * 50}{Colors.RESET}")
    bar_length = 40
    for i in range(bar_length + 1):
        percent = (i / bar_length) * 100
        filled = "█" * i
        empty = "░" * (bar_length - i)
        
        print(f"\r{Colors.NEON_CYAN}[{Colors.NEON_GREEN}{filled}{Colors.NEON_WHITE}{empty}{Colors.NEON_CYAN}] {Colors.NEON_YELLOW}{percent:.1f}%{Colors.RESET}", end="", flush=True)
        time.sleep(0.05)
    
    print(f"\n{Colors.NEON_GREEN}✅ System initialized successfully!{Colors.RESET}")
    time.sleep(1)

# Key Management
def get_ip_address():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        ip_data = response.json()
        ip_address = ip_data['ip']
        return ip_address
    except Exception as e:
        fancy_print(f"❌ Lỗi khi lấy địa chỉ IP: {e}", Colors.NEON_RED, delay=1)
        return None

def luu_thong_tin_ip(ip, key, expiration_date):
    data = {ip: {"key": key, "expiration_date": expiration_date.isoformat()}}
    encrypted_data = encrypt_data(json.dumps(data))
    with open(KEY_FILE, "w") as file:
        file.write(encrypted_data)

def tai_thong_tin_ip():
    try:
        with open(KEY_FILE, "r") as file:
            encrypted_data = file.read()
        data = json.loads(decrypt_data(encrypted_data))
        return data
    except FileNotFoundError:
        return None
def kiem_tra_ip(ip):
    data = tai_thong_tin_ip()
    if data and ip in data:
        expiration_date = datetime.fromisoformat(data[ip]["expiration_date"])
        if expiration_date > datetime.now():
            return data[ip]["key"]
    return None


def get_shortened_link_phu(url):
    try:
        token = "66e82f69e4b6f63fe227f33e"
        api_url = f"https://link4m.co/api-shorten/v2?api={token}&url={url}"
        response = requests.get(api_url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return {"status": "error", "message": "Không thể kết nối đến dịch vụ rút gọn URL."}
    except Exception as e:
        return {"status": "error", "message": f"Lỗi khi rút gọn URL: {e}"}

def key_vip():
	def get_raw_info():
	    system = platform.system()

	    info_parts = []

	    if system == "Windows":
	        try:
	            # Volume serial
	            vol = subprocess.check_output("vol C:", shell=True).decode(errors="ignore")
	            info_parts.append(vol.strip())
	        except:
	            pass

	        try:
	            # Machine GUID từ registry
	            reg = subprocess.check_output('reg query HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Cryptography /v MachineGuid', shell=True)
	            info_parts.append(reg.decode(errors="ignore").strip())
	        except:
	            pass

	        try:
	            info_parts.append(platform.node())  # Tên máy
	        except:
	            pass

	    elif system == "Linux":
	        if "ANDROID_ROOT" in os.environ:
	            try:
	                android_id = subprocess.check_output("settings get secure android_id", shell=True).decode().strip()
	                info_parts.append(android_id)
	            except:
	                pass

	            try:
	                with open("/proc/cpuinfo", "r") as f:
	                    for line in f:
	                        if "Serial" in line or "Hardware" in line:
	                            info_parts.append(line.strip().split(":")[-1].strip())
	            except:
	                pass

	            try:
	                info_parts.append(platform.node())
	            except:
	                pass
	        else:
	            try:
	                info_parts.append(platform.node())
	            except:
	                pass

	    return "-".join(info_parts)

	def get_device_id():
	    raw = get_raw_info()
	    if not raw:
	        return "UNKNOWN_DEVICE"
	    hashed = hashlib.sha256(raw.encode()).hexdigest()
	    return f"DEVICE-{hashed[:16]}"
	def date_now():
	    hom_nay = datetime.now()
	    return hom_nay.strftime("%d/%m/%Y")
	device_id=get_device_id()
	ngay=date_now()
	print("\033[38;5;46m" + f"Mã thiết bị : {device_id}".center(50) + "\033[0m")
	print("\033[38;5;46m" + "Để mua key vip vui lòng nhắn tin cho admin".center(50) + "\033[0m")
	key_input=input("\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;34mNhập Key: ")
	try:
		res=requests.get('https://raw.githubusercontent.com/ntcong7929/KEY/refs/heads/main/key.txt')
		key=res.text
		list_key=key.strip().split('\n')
		for i in list_key:
			if str(key_input) == str(i.split('|')[1]):
				print('KEY ĐÚNG MỜI BẠN VÀO TOOL...')
				time.sleep(1)
				return True
		return False
	except Exception as e:
		print("\033[1;35mCó lỗi, vui lòng báo admin\033[1;36m:",e)
def display_ip_address(ip_address):
    if ip_address:
        display_animated_banner()
        print(f"\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;31mĐịa chỉ IP : {ip_address}")
    else:
        print("Không thể lấy địa chỉ IP của thiết bị.")
def key():
    ip_address = get_ip_address()
    display_ip_address(ip_address)

    if ip_address:
        existing_key = kiem_tra_ip(ip_address)
        if existing_key:
            print(
                f"\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;35mTool còn hạn, mời bạn dùng tool..."
            )
            clear_screen()
            time.sleep(2)
        else:
            if da_qua_gio_moi():
                print("\033[1;33mQuá giờ sử dụng tool !!!")

            url, key, expiration_date = generate_key_and_url(ip_address)

            with ThreadPoolExecutor(max_workers=2) as executor:
                print(
                    "\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;32mNhập 1 Để Lấy Key \033[1;33m( Free )"
                )
                print(
                    "\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;32mNhập 2 Để Nhập Key Vip\033[1;33m ( VIP )"
                )

                while True:
                    try:
                        choice = input(
                            "\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;34mNhập lựa chọn: "
                        )
                        print(
                            "\033[97m════════════════════════════════════════════════"
                        )
                        if choice == "1":
                            yeumoney_future = executor.submit(
                                get_shortened_link_phu, url
                            )
                            yeumoney_data = yeumoney_future.result()
                            if yeumoney_data and yeumoney_data.get("status") == "error":
                                print(yeumoney_data.get("message"))
                                return
                            else:
                                link_key_yeumoney = yeumoney_data.get("shortenedUrl")
                                print(
                                    "\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;35mLink Để Vượt Key Là \033[1;36m:",
                                    link_key_yeumoney,
                                )

                            while True:
                                keynhap = input(
                                    "\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;33mKey Đã Vượt Là: \033[1;32m"
                                )
                                if keynhap == key:
                                    print("Key Đúng Mời Bạn Dùng Tool")
                                    clear_screen()
                                    sleep(2)
                                    luu_thong_tin_ip(
                                        ip_address, keynhap, expiration_date
                                    )
                                    return
                                else:
                                    print(
                                    	"\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;35mKey Sai Vui Lòng Vượt Lại Link \033[1;36m:",
                                        link_key_yeumoney,
                                    )
                        elif choice=='2':
                        	status=key_vip()
                        	if status==True:
                        		print('MỜI BẠN DÙNG TOOL VUI VẺ 😊')
                        		clear_screen()
                        		return
                        	else:
                        		print("KEY SAI HOẶC KHÔNG TỒN TẠI!")
                        		print('THOÁT TOOL...')
                        		exit(1)
                    except ValueError:
                        print("Vui lòng nhập số hợp lệ.")
                    except KeyboardInterrupt:
                        print(
                            "\n\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;31mCảm ơn bạn đã dùng Tool !!!"
                        )
                        sys.exit()

# Configuration and Stats
def load_config():
    print(f"{Colors.NEON_CYAN}{'═' * 50}{Colors.RESET}")
    print(f"{Colors.NEON_PINK}📋 HƯỚNG DẪN LẤY LINK{Colors.RESET}")
    print(f"{Colors.NEON_CYAN}{'═' * 50}{Colors.RESET}")
    instructions = [
        "1. Vào https://xworld.io/vi-VN",
        "2. Đăng nhập tài khoản",
        "3. Vào Vua Thoát Hiểm, nhấn 'Lập tức truy cập'",
        "4. Copy link và nhập vào đây"
    ]
    for instr in instructions:
        print(f"{Colors.NEON_GREEN} {instr}{Colors.RESET}")
        time.sleep(0.1)
    print(f"{Colors.NEON_CYAN}{'═' * 50}{Colors.RESET}")
    link = input(f"{Colors.NEON_YELLOW}🔗 NHẬP LINK CỦA BẠN: {Colors.RESET}")
    try:
        a = link.split('&')
        user_id = a[0].split('userId=')[1]
        user_secret_key = a[1].split('secretKey=')[1]
    except:
        fancy_print("❌ Link không hợp lệ!", Colors.NEON_RED, delay=1)
        sys.exit(1)
    
    default_config = {
        "user_id": user_id,
        "user_secret_key": user_secret_key,
        "risk_level": 0.1,
        "analysis_depth": 50,
        "lucky_factor": 0.2
    }
    
    try:
        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
            config = json.load(f)
            return {**default_config, **config}
    except:
        with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
            json.dump(default_config, f, indent=2, ensure_ascii=False)
        return default_config

def save_stats(stats):
    try:
        with open(STATS_FILE, 'w', encoding='utf-8') as f:
            json.dump(stats, f, indent=2, ensure_ascii=False)
    except Exception as e:
        fancy_print(f"❌ Lỗi lưu thống kê: {e}", Colors.NEON_RED, delay=1)

def load_stats():
    try:
        with open(STATS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return {"wins": 0, "loses": 0, "total_games": 0, "win_streak": 0, "max_streak": 0}

# API Calls
def safe_api_call(url, headers, params=None, json_data=None, max_retries=3):
    for attempt in range(max_retries):
        try:
            if json_data:
                response = requests.post(url, headers=headers, json=json_data, timeout=15)
            else:
                response = requests.get(url, headers=headers, params=params, timeout=15)
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 401:
                fancy_print(f"❌ Lỗi xác thực lần {attempt + 1}/{max_retries}", Colors.NEON_RED, delay=1)
                return None
            else:
                fancy_print(f"⚠️ API error {response.status_code} lần {attempt + 1}", Colors.NEON_YELLOW, delay=1)
        except requests.exceptions.Timeout:
            fancy_print(f"⚠️ Timeout lần {attempt + 1}/{max_retries}", Colors.NEON_YELLOW, delay=1)
        except Exception as e:
            fancy_print(f"❌ Lỗi API lần {attempt + 1}/{max_retries}: {e}", Colors.NEON_RED, delay=1)
        time.sleep(2 ** attempt)
    return None

def display_wallet_balance(headers):
    json_data = {'user_id': int(headers['user-id']), 'source': 'home'}
    response = safe_api_call('https://wallet.3games.io/api/wallet/user_asset', headers, json_data=json_data)
    if response:
        assets = response.get("data", {}).get("user_asset", {})
        build = assets.get("BUILD", 0)
        world = assets.get("WORLD", 0)
        usdt = assets.get("USDT", 0)
        print(f"\n{Colors.NEON_ORANGE}💰 SỐ DƯ{Colors.RESET}")
        print(f"{Colors.NEON_YELLOW}{'═' * 30}{Colors.RESET}")
        assets_list = [
            ("BUILD", build, Colors.NEON_BLUE, ""),
            ("WORLD", world, Colors.NEON_GREEN, ""),
            ("USDT", usdt, Colors.NEON_YELLOW, "")
        ]
        for asset, amount, color, icon in assets_list:
            print(f"{icon} {Colors.NEON_WHITE}{asset:<8}: {color}{amount:>15,.2f}{Colors.RESET}")
            time.sleep(0.2)
        print(f"{Colors.NEON_YELLOW}{'═' * 30}{Colors.RESET}")
        return True
    return False

def get_top10_data(headers):
    params = {'asset': 'BUILD'}
    response = safe_api_call('https://api.escapemaster.net/escape_game/recent_10_issues', headers, params=params)
    if not response or not response.get('data'):
        return [], []
    issue_ids = [i['issue_id'] for i in response['data']]
    killed_rooms = [int(i['killed_room_id']) for i in response['data']]
    return issue_ids, killed_rooms

def get_top100_data(headers):
    params = {'asset': 'BUILD'}
    res = safe_api_call('https://api.escapemaster.net/escape_game/recent_100_issues', headers, params=params)
    if not res or not res.get('data') or not res['data'].get('room_id_2_killed_times'):
        return [], []
    room_data = res['data']['room_id_2_killed_times']
    rooms = [int(i) for i in room_data.keys()]
    kill_counts = [room_data[str(i)] for i in rooms]
    return rooms, kill_counts

def load_historical_data():
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            killed_rooms = [int(line.split('Sát thủ chọn phòng [')[1].split(']')[0]) for line in lines[-50:]]
            return killed_rooms, lines[-50:]
    except:
        return [], []

# Room Selection Algorithms
def algorithm_fibonacci(data, config):
    killed_rooms = data['killed_rooms'][:20]
    fib = [1, 1, 2, 3, 5, 8]
    scores = {i: 1.0 for i in range(1, 9)}
    for i, room in enumerate(killed_rooms):
        if i < len(fib):
            penalty = fib[i] / sum(fib) * 0.5
            scores[room] -= penalty
    return {k: max(0.1, v) for k, v in scores.items()}

def algorithm_martingale(data, config):
    historical_data = data['historical_data']
    scores = {i: 1.0 for i in range(1, 9)}
    streak = 0
    for line in historical_data[-10:]:
        if 'Thắng' in line:
            streak += 1
        else:
            streak = 0
    for room in range(1, 9):
        if streak > 2:
            scores[room] -= streak * 0.1
        else:
            scores[room] += streak * 0.05
    return {k: max(0.1, v) for k, v in scores.items()}

def algorithm_pattern_recognition(data, config):
    killed_rooms = data['killed_rooms'][:5]
    patterns = {}
    for i in range(len(killed_rooms) - 3):
        pattern = tuple(killed_rooms[i:i+3])
        patterns[pattern] = patterns.get(pattern, 0) + 1
    scores = {i: 1.0 for i in range(1, 9)}
    for pattern, count in patterns.items():
        if pattern[-1] in scores:
            scores[pattern[-1]] -= count * 0.3
    return {k: max(0.1, v) for k, v in scores.items()}

def algorithm_hot_cold(data, config):
    room_frequency = Counter(data['killed_rooms'][:20])
    scores = {i: 1.0 for i in range(1, 9)}
    max_freq = max(room_frequency.values(), default=1)
    for room, count in room_frequency.items():
        scores[room] -= (count / max_freq) * 0.5
    for room in range(1, 9):
        if room not in room_frequency:
            scores[room] += 0.3
    return {k: max(0.1, v) for k, v in scores.items()}

def algorithm_zigzag(data, config):
    killed_rooms = data['killed_rooms'][:10]
    scores = {i: 1.0 for i in range(1, 9)}
    for i in range(1, len(killed_rooms)):
        if killed_rooms[i] != killed_rooms[i-1]:
            scores[killed_rooms[i]] -= 0.2
        else:
            scores[killed_rooms[i]] -= 0.4
    return {k: max(0.1, v) for k, v in scores.items()}

def algorithm_weighted_average(data, config):
    killed_rooms = data['killed_rooms'][:20]
    scores = {i: 1.0 for i in range(1, 9)}
    for i, room in enumerate(killed_rooms):
        weight = 1 / (i + 1)
        scores[room] -= weight * 0.5
    return {k: max(0.1, v) for k, v in scores.items()}

def algorithm_anti_pattern(data, config):
    killed_rooms = data['killed_rooms'][:5]
    pattern_freq = Counter(tuple(killed_rooms[i:i+3]) for i in range(len(killed_rooms)-2))
    scores = {i: 1.0 for i in range(1, 9)}
    for pattern, count in pattern_freq.items():
        last_room = pattern[-1]
        scores[last_room] -= count * 0.4
    return {k: max(0.1, v) for k, v in scores.items()}

def algorithm_machine_learning(data, config):
    historical_data = data['historical_data']
    scores = {i: 1.0 for i in range(1, 9)}
    for line in historical_data[-50:]:
        try:
            room = int(line.split('Bot chọn phòng [')[1].split(']')[0])
            result = line.split('KẾT QUẢ: ')[1].strip()
            if result == 'Thắng':
                scores[room] += 0.1
            else:
                scores[room] -= 0.1
        except:
            continue
    return {k: max(0.1, v) for k, v in scores.items()}

def select_algorithm_by_last_result(last_result):
    algorithms = [
        algorithm_fibonacci,
        algorithm_martingale,
        algorithm_pattern_recognition,
        algorithm_hot_cold,
        algorithm_zigzag,
        algorithm_weighted_average,
        algorithm_anti_pattern,
        algorithm_machine_learning
    ]
    if last_result is None or last_result < 1 or last_result > 8:
        return random.choice(algorithms)
    return algorithms[last_result - 1]

# Room Selection Logic
def calculate_room_safety_scores(top10_data, top100_data, config, historical_data):
    issue_ids, killed_rooms = top10_data
    rooms_100, kill_counts_100 = top100_data
    data = {
        'killed_rooms': killed_rooms,
        'historical_data': historical_data
    }
    algorithms = [
        algorithm_fibonacci,
        algorithm_martingale,
        algorithm_pattern_recognition,
        algorithm_hot_cold,
        algorithm_zigzag,
        algorithm_weighted_average,
        algorithm_anti_pattern,
        algorithm_machine_learning
    ]
    combined_scores = {i: 0.0 for i in range(1, 9)}
    for algo in algorithms:
        scores = algo(data, config)
        for room, score in scores.items():
            combined_scores[room] += score / len(algorithms)
    
    if rooms_100:
        max_kills = max(kill_counts_100, default=1)
        for room in range(1, 9):
            if room in rooms_100:
                room_index = rooms_100.index(room)
                kill_count = kill_counts_100[room_index]
                combined_scores[room] -= (kill_count / max_kills) * 0.2
            else:
                combined_scores[room] += 0.1
    
    return {k: max(0.1, min(1.0, v)) for k, v in combined_scores.items()}

def smart_room_selection(safety_scores, config, last_room=None, last_result=None):
    min_safe_score = 0.6
    safe_rooms = {room: score for room, score in safety_scores.items() if score >= min_safe_score}
    if not safe_rooms:
        safe_rooms = {k: v for k, v in safety_scores.items() if k != last_room}
        if not safe_rooms:
            safe_rooms = safety_scores
    weighted_choices = []
    for room, score in safe_rooms.items():
        weight = score + (random.random() * config['lucky_factor'])
        weighted_choices.append((room, weight))
    if random.random() < config['risk_level']:
        return random.choice([room for room, _ in weighted_choices])
    return max(weighted_choices, key=lambda x: x[1])[0]

def display_analysis_results(safety_scores, selected_room, current_issue):
    safety_score = max(safety_scores.values())
    print(f"\n{Colors.NEON_PINK}🤖 ROOM ANALYSIS SYSTEM{Colors.RESET}")
    print(f"{Colors.NEON_PURPLE}{'═' * 40}{Colors.RESET}")
    print(f"{Colors.NEON_CYAN}Đang phân tích dữ liệu", end="")
    for i in range(6):
        print(f"{Colors.NEON_CYAN}.", end="", flush=True)
        time.sleep(0.3)
    print(f"{Colors.NEON_GREEN} ✓ Hoàn thành!{Colors.RESET}", end="\r")
    print(' '*50, end='\r')
    
    print(f"{Colors.NEON_GREEN}🎯 Phòng được chọn: {Colors.NEON_YELLOW}#{selected_room} - {ROOM_NAMES[selected_room]}{Colors.RESET}")
    print(f"{Colors.NEON_BLUE}🧠 Độ tin cậy: {Colors.NEON_GREEN}{safety_score*100:.1f}%{Colors.RESET}")
    print(f"{Colors.NEON_ORANGE}📊 Xác suất thắng: {Colors.NEON_GREEN}{safety_score*100:.1f}%{Colors.RESET}")
    bar_length = 30
    filled_length = int(bar_length * safety_score)
    bar = "█" * filled_length + "░" * (bar_length - filled_length)
    print(f"{Colors.NEON_WHITE}Progress: {Colors.NEON_GREEN}{bar}{Colors.RESET} {Colors.NEON_YELLOW}{safety_score*100:.1f}%{Colors.RESET}")

def chon_phong_thong_minh(headers, config, last_room=None, last_result=None):
    fancy_print("🔍 Đang thu thập dữ liệu...", Colors.NEON_CYAN, delay=1)
    top10_data = get_top10_data(headers)
    top100_data = get_top100_data(headers)
    issue_ids, killed_rooms = top10_data
    
    if not issue_ids or not killed_rooms:
        fancy_print("⚠️ Không thể lấy dữ liệu, chọn phòng ngẫu nhiên", Colors.NEON_YELLOW, delay=1)
        return random.randint(1, 8), 0, [], []
    
    current_issue = issue_ids[0] + 1
    killed_rooms_history, historical_data = load_historical_data()
    
    fancy_print("📊 Đang phân tích với 8 thuật toán...", Colors.NEON_CYAN, delay=1)
    safety_scores = calculate_room_safety_scores(top10_data, top100_data, config, historical_data)
    selected_room = smart_room_selection(safety_scores, config, last_room, last_result)
    display_analysis_results(safety_scores, selected_room, current_issue)
    
    try:
        prediction_data = {
            'issue': current_issue,
            'selected_room': selected_room,
            'safety_scores': safety_scores,
            'timestamp': datetime.now().isoformat()
        }
        with open('predictions.json', 'a', encoding='utf-8') as f:
            f.write(json.dumps(prediction_data, ensure_ascii=False) + '\n')
    except:
        pass
    
    return selected_room, current_issue, top10_data, top100_data

def display_enhanced_stats():
    stats = load_stats()
    win_rate = (stats['wins'] / max(stats['total_games'], 1)) * 100
    print(f"\n{Colors.NEON_CYAN}📈 GAME STATISTICS DASHBOARD{Colors.RESET}")
    print(f"{Colors.NEON_BLUE}{'═' * 50}{Colors.RESET}")
    stat_items = [
        ("🏆 Victories", stats["wins"], Colors.NEON_GREEN),
        ("💀 Defeats", stats["loses"], Colors.NEON_RED),
        ("🎯 Total Games", stats["total_games"], Colors.NEON_CYAN),
        ("📊 Win Rate", f"{win_rate:.1f}%", Colors.NEON_YELLOW),
        ("🔥 Current Streak", stats["win_streak"], Colors.NEON_ORANGE),
        ("⚡ Max Streak ", stats["max_streak"], Colors.NEON_PURPLE),
    ]
    
    for label, value, color in stat_items:
        print(f"{label:<18}: {color}{str(value):>15}{Colors.RESET}")
        time.sleep(0.1)

def kiem_tra_kq_nang_cao(headers, ki, bot_chon, top10_data, top100_data):
    fancy_print(f"\n⏳ Đang chờ kết quả kỳ #{ki}...", Colors.NEON_YELLOW, delay=1)
    max_wait_time = 300
    wait_interval = 10
    waited_time = 0
    
    while waited_time < max_wait_time:
        top10_data_new = get_top10_data(headers)
        issue_ids, killed_rooms = top10_data_new
        if not issue_ids or not killed_rooms:
            time.sleep(wait_interval)
            waited_time += wait_interval
            continue
        if int(ki) == int(issue_ids[0]):
            killer_room = killed_rooms[0]
            result = 'Thắng' if bot_chon != killer_room else 'Thua'
            print(f"\n{Colors.NEON_PINK}🎮 GAME RESULT - ROUND #{ki}{Colors.RESET}")
            print(f"{Colors.NEON_MAGENTA}{'═' * 50}{Colors.RESET}")
            print(f"{Colors.NEON_CYAN}🆔 Game ID: {Colors.NEON_YELLOW}{ki}{Colors.RESET}")
            print(f"{Colors.NEON_RED}💀 Sát thủ chọn: {Colors.NEON_WHITE}#{killer_room} - {ROOM_NAMES[killer_room]}{Colors.RESET}")
            print(f"{Colors.NEON_BLUE}🤖 Bot chọn: {Colors.NEON_WHITE}#{bot_chon} - {ROOM_NAMES[bot_chon]}{Colors.RESET}")
            print(f"{Colors.NEON_MAGENTA}{'═' * 50}{Colors.RESET}")
            
            if result == "Thắng":
                print(f"{Colors.NEON_GREEN}🎉 VICTORY! 🎉{Colors.RESET}")
            else:
                print(f"{Colors.NEON_RED}💔 DEFEAT! BETTER LUCK NEXT TIME! 💔{Colors.RESET}")
                print(f"{Colors.NEON_ORANGE}The killer found you! 😵{Colors.RESET}")
            
            print(f"{Colors.NEON_MAGENTA}{'═' * 50}{Colors.RESET}")
            
            stats = load_stats()
            stats['total_games'] += 1
            if result == 'Thắng':
                stats['wins'] += 1
                stats['win_streak'] += 1
                stats['max_streak'] = max(stats['max_streak'], stats['win_streak'])
            else:
                stats['loses'] += 1
                stats['win_streak'] = 0
            save_stats(stats)
            
            top10_str = ",".join(map(str, top10_data[1]))
            top100_str = ",".join(map(str, top100_data[1]))
            with open(DATA_FILE, 'a', encoding='utf-8') as f:
                f.write(f'{ki} {top10_str} {top100_str} {killer_room} {bot_chon} {result}\n')
            
            time.sleep(3)
            return result, killer_room
        dots = "." * ((waited_time // 5) % 4)
        print(f"\r{Colors.NEON_YELLOW}⏳ Chờ kết quả{dots:<3} ({waited_time//60:02d}:{waited_time%60:02d}){Colors.RESET}", end='')
        time.sleep(wait_interval)
        waited_time += wait_interval
    fancy_print("\n❌ Timeout - Không thể lấy kết quả!", Colors.NEON_RED, delay=1)
    return None, None

def main():
    display_animated_banner()
    key()
    time.sleep(1)
    display_loading_animation()
    config = load_config()
    headers = {
        'accept': '*/*',
        'accept-language': 'vi,en;q=0.9',
        'cache-control': 'no-cache',
        'country-code': 'vn',
        'origin': 'https://xworld.info',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://xworld.info/',
        'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'user-id': config['user_id'],
        'user-login': 'login_v2',
        'user-secret-key': config['user_secret_key'],
        'xb-language': 'vi-VN',
    }
    
    clear_screen()
    display_animated_banner()
    if not display_wallet_balance(headers):
        fancy_print("❌ Không thể kết nối đến server. Vui lòng kiểm tra lại link!", Colors.NEON_RED, delay=1)
        input(f"{Colors.NEON_YELLOW}Nhấn Enter để thoát...{Colors.RESET}")
        return
    
    time.sleep(2)
    last_room = None
    last_result = None
    
    while True:
        try:
            clear_screen()
            display_modern_header()
            display_wallet_balance(headers)
            bot_chon, ki, top10_data, top100_data = chon_phong_thong_minh(headers, config, last_room, last_result)
            if ki == 0:
                fancy_print("❌ Không thể lấy thông tin kỳ hiện tại!", Colors.NEON_RED, delay=1)
                time.sleep(5)
                continue
            time.sleep(3)
            display_enhanced_stats()
            result, killer_room = kiem_tra_kq_nang_cao(headers, ki, bot_chon, top10_data, top100_data)
            if result:
                if result == 'Thắng':
                    fancy_print("🎉 CHÚC MỪNG! BẠN ĐÃ THẮNG!", Colors.NEON_GREEN, delay=1)
                else:
                    fancy_print("😢 Chúc bạn may mắn lần sau!", Colors.NEON_YELLOW, delay=1)
                last_result = killer_room
                last_room = bot_chon if result == 'Thua' else None
            fancy_print(f"\n⏰ Chờ 10 giây trước khi tiếp tục...", Colors.NEON_CYAN, delay=10)
        except KeyboardInterrupt:
            fancy_print("\n🌟 Cảm ơn bạn đã sử dụng XWORLD Tool! 🌟", Colors.NEON_PINK, delay=1)
            break
        except Exception as e:
            fancy_print(f"❌ Lỗi không mong muốn: {e}", Colors.NEON_RED, delay=1)
            fancy_print("🔄 Thử lại sau 5 giây...", Colors.NEON_YELLOW, delay=5)

main()
