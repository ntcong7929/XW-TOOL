# Thư viện chuẩn
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


def clear_screen():
    os.system("cls" if platform.system() == "Windows" else "clear")


try:
    from faker import Faker
    from requests import session
    from colorama import Fore, Style
    import pystyle
except ImportError:
    os.system("pip install faker requests colorama bs4 pystyle")
    os.system("pip3 install requests pysocks")
    print("__Vui Lòng Chạy Lại Tool__")
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

def generate_key_and_url(ip_address):
    ngay = int(datetime.now().day)
    key1 = str(ngay * 27 + 27)
    ip_numbers = "".join(filter(str.isdigit, ip_address))
    key = f"NTC{key1}{ip_numbers}"
    expiration_date = datetime.now() + timedelta(hours=12)
    url = f"https://hohiepvn.x10.mx/key/van-thang-vip.php?key={key}"
    return url, key, expiration_date
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
                return

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


try:
    from colorama import Fore, Style, init

    init(autoreset=True)
    COLORAMA_AVAILABLE = True
except ImportError:
    COLORAMA_AVAILABLE = False

    class Fore:
        WHITE = RED = GREEN = YELLOW = BLUE = CYAN = MAGENTA = ""

    class Style:
        NORMAL = BRIGHT = RESET_ALL = ""


ATHLETES = {
    1: "Bậc thầy tấn công",
    2: "Quyền sắt",
    3: "Thợ lặn sâu",
    4: "Cơn lốc sân cỏ",
    5: "Hiệp sĩ phi nhanh",
    6: "Vua home run",
}

CONFIG_FILE = "xworld_config.json"
ANALYSIS_FILE = "phan_tich.json"
STATS_FILE = "thong_ke.json"
KEY_FILE="ip_key_cdtd.json"

class GameStats:
    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.current_streak = 0
        self.max_win_streak = 0
        self.max_loss_streak = 0
        self.history = []
        self.load_stats()

    def load_stats(self):
        try:
            with open(STATS_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.wins = data.get("wins", 0)
                self.losses = data.get("losses", 0)
                self.current_streak = data.get("current_streak", 0)
                self.max_win_streak = data.get("max_win_streak", 0)
                self.max_loss_streak = data.get("max_loss_streak", 0)
                self.history = data.get("history", [])
        except:
            pass

    def save_stats(self):
        try:
            data = {
                "wins": self.wins,
                "losses": self.losses,
                "current_streak": self.current_streak,
                "max_win_streak": self.max_win_streak,
                "max_loss_streak": self.max_loss_streak,
                "history": self.history[-100:],
                "last_updated": dt.now().isoformat(),
            }
            with open(STATS_FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            fancy_print(f"⚠️ Lỗi lưu thống kê: {e}", Fore.YELLOW)

    def add_result(self, is_win, round_id, bot_choice, actual_result):
        if is_win:
            self.wins += 1
            if self.current_streak >= 0:
                self.current_streak += 1
            else:
                self.current_streak = 1
            self.max_win_streak = max(self.max_win_streak, self.current_streak)
        else:
            self.losses += 1
            if self.current_streak <= 0:
                self.current_streak -= 1
            else:
                self.current_streak = -1
            self.max_loss_streak = max(self.max_loss_streak, abs(self.current_streak))
        self.history.append(
            {
                "timestamp": dt.now().isoformat(),
                "round_id": round_id,
                "bot_choice": bot_choice,
                "actual_result": actual_result,
                "result": "win" if is_win else "loss",
            }
        )

        self.save_stats()

    def get_win_rate(self):
        total = self.wins + self.losses
        if total == 0:
            return 0
        return (self.wins / total) * 100

    def display_stats(self):
        total = self.wins + self.losses
        win_rate = self.get_win_rate()
        print(f"\n\033[38;5;51m📈 GAME STATISTICS DASHBOARD\033[0m")
        print(f"\033[38;5;39m{'═' * 50}\033[0m")
        stat_items = [
            ("🏆 Victories", self.wins, "\033[38;5;46m"),
            ("💀 Defeats", self.losses, "\033[38;5;196m"),
            ("🎯 Total Games", total, "\033[38;5;51m"),
            ("📊 Win Rate", f"{win_rate:.1f}%", "\033[38;5;226m"),
            ("🔥 Current Streak", abs(self.current_streak), "\033[38;5;214m"),
            (
                "⚡ Max Streak",
                max(self.max_win_streak, self.max_loss_streak),
                "\033[38;5;135m",
            ),
        ]
        for label, value, color in stat_items:
            print(f"{label:<18}: {color}{str(value):>15}\033[0m")
            time.sleep(0.1)


def load_config():
    fancy_print("╔" + "═" * 45 + "╗", Fore.CYAN, Style.BRIGHT)
    fancy_print("║" + " " * 45 + "║", Fore.CYAN, Style.BRIGHT)
    fancy_print(
        "║" + "🏃‍♂️ XWORLD CHẠY ĐUA TỐC ĐỘ 🏃‍♂️".center(43) + "║", Fore.CYAN, Style.BRIGHT
    )
    fancy_print("║" + " " * 45 + "║", Fore.CYAN, Style.BRIGHT)
    fancy_print("╠" + "═" * 45 + "╣", Fore.CYAN, Style.BRIGHT)
    fancy_print(
        "║ Hướng dẫn lấy link:                         ║", Fore.CYAN, Style.BRIGHT
    )
    fancy_print(
        "║ 1. Vào https://xworld.io/vi-VN              ║", Fore.CYAN, Style.BRIGHT
    )
    fancy_print(
        "║ 2. Đăng nhập tài khoản                      ║", Fore.CYAN, Style.BRIGHT
    )
    fancy_print(
        "║ 3. Tìm và nhấn Chạy đua tốc độ              ║", Fore.CYAN, Style.BRIGHT
    )
    fancy_print(
        "║ 4. Nhấn 'Lập tức truy cập'                  ║", Fore.CYAN, Style.BRIGHT
    )
    fancy_print(
        "║ 5. Copy link và paste vào đây               ║", Fore.CYAN, Style.BRIGHT
    )
    fancy_print("╚" + "═" * 45 + "╝", Fore.CYAN, Style.BRIGHT)

    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            config = json.load(f)
            fancy_print("✅ Đã tìm thấy cấu hình lưu trước!", Fore.GREEN, Style.BRIGHT)
            use_saved = input("Sử dụng cấu hình cũ? (y/n): ").lower()
            if use_saved == "y":
                return config
    except:
        pass

    link = input("\n🔗 NHẬP LINK CỦA BẠN: ")

    try:
        parts = link.split("&")
        user_id = parts[0].split("userId=")[1]
        user_secret_key = parts[1].split("secretKey=")[1]

        fancy_print(f"✅ User ID: {user_id}", Fore.GREEN, Style.BRIGHT)
        fancy_print(
            f"✅ Secret Key: {user_secret_key[:20]}...", Fore.GREEN, Style.BRIGHT
        )

        config = {
            "user_id": user_id,
            "user_secret_key": user_secret_key,
        }

        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=2, ensure_ascii=False)

        return config
    except Exception as e:
        fancy_print(f"❌ Lỗi phân tích link: {e}", Fore.RED, Style.BRIGHT)
        return None


def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def fancy_print(text, color=Fore.WHITE, style=Style.NORMAL, end="\n"):
    if COLORAMA_AVAILABLE:
        print(f"{style}{color}{text}{Style.RESET_ALL}", end=end)
    else:
        print(text, end=end)


def display_header():
    now = dt.now()
    print("\033[38;5;51m" + "═" * 50 + "\033[0m")
    print("\033[38;5;199m" + "🏃‍♂️ XWORLD CHẠY ĐUA TỐC ĐỘ 🏃‍♂️".center(50) + "\033[0m")
    print("\033[38;5;51m" + "═" * 50 + "\033[0m")
    print(f"\033[38;5;226mThời gian: {now.strftime('%H:%M:%S %d/%m/%Y')}\033[0m")
    print("\033[38;5;51m" + "═" * 50 + "\033[0m")


def safe_api_call(url, headers, params=None, json_data=None, max_retries=3):
    for attempt in range(max_retries):
        try:
            if json_data:
                response = requests.post(
                    url, headers=headers, json=json_data, timeout=15
                )
            else:
                response = requests.get(url, headers=headers, params=params, timeout=15)

            if response.status_code == 200:
                return response.json()
            else:
                fancy_print(
                    f"⚠️ API lỗi {response.status_code} (lần {attempt + 1})", Fore.YELLOW
                )

        except requests.exceptions.Timeout:
            fancy_print(f"⚠️ Timeout lần {attempt + 1}/{max_retries}", Fore.YELLOW)
        except Exception as e:
            fancy_print(f"⚠️ Lỗi API lần {attempt + 1}/{max_retries}: {e}", Fore.YELLOW)

        if attempt < max_retries - 1:
            time.sleep(2**attempt)

    return None


def get_wallet_info(headers):
    user_id = headers["user-id"]
    json_data = {"user_id": int(user_id), "source": "home"}

    data = safe_api_call(
        "https://wallet.3games.io/api/wallet/user_asset", headers, json_data=json_data
    )

    if data and data.get("data"):
        assets = data["data"].get("user_asset", {})
        return {
            "BUILD": assets.get("BUILD", 0),
            "WORLD": assets.get("WORLD", 0),
            "USDT": assets.get("USDT", 0),
        }
    return None


def display_wallet(wallet_info):
    if not wallet_info:
        print("\033[38;5;196m❌ Không thể lấy thông tin ví\033[0m")
        return
    print("\n\033[38;5;214m💰 SỐ DƯ TÀI SẢN\033[0m")
    print("\033[38;5;226m" + "═" * 30 + "\033[0m")
    print(f"\033[38;5;255mBUILD: \033[38;5;39m{wallet_info['BUILD']:<19,.2f}\033[0m")
    print(f"\033[38;5;255mWORLD: \033[38;5;46m{wallet_info['WORLD']:<19,.2f}\033[0m")
    print(f"\033[38;5;255mUSDT : \033[38;5;226m{wallet_info['USDT']:<19,.2f}\033[0m")
    print("\033[38;5;226m" + "═" * 30 + "\033[0m")


def get_recent_data(headers, count=100):
    params = {"asset": "BUILD"}

    if count == 10:
        url = "https://api.sprintrun.win/sprint/recent_10_issues"
    else:
        url = "https://api.sprintrun.win/sprint/recent_100_issues"

    data = safe_api_call(url, headers, params=params)
    return data


def calculate_anti_martingale_patterns(recent_results):
    patterns = {}

    for window_size in [3, 5, 7, 10]:
        if len(recent_results) >= window_size:
            recent_window = recent_results[-window_size:]

            appearance_count = Counter(recent_window)

            for athlete_id in range(1, 7):
                if athlete_id not in patterns:
                    patterns[athlete_id] = {}

                patterns[athlete_id][f"absent_{window_size}"] = appearance_count.get(
                    athlete_id, 0
                )
                patterns[athlete_id][f"pressure_{window_size}"] = (
                    window_size - appearance_count.get(athlete_id, 0)
                )

    return patterns


def calculate_heat_index(recent_results, total_wins):
    heat_scores = {}

    for athlete_id in range(1, 7):
        base_score = total_wins.get(athlete_id, 0)

        recent_10 = (
            recent_results[-10:] if len(recent_results) >= 10 else recent_results
        )
        recent_wins = recent_10.count(athlete_id)

        recent_5 = recent_results[-5:] if len(recent_results) >= 5 else recent_results
        super_recent_wins = recent_5.count(athlete_id)

        last_win_distance = 0
        for i, result in enumerate(reversed(recent_results)):
            if result == athlete_id:
                last_win_distance = i
                break
        else:
            last_win_distance = len(recent_results)

        heat_scores[athlete_id] = {
            "base_score": base_score,
            "recent_10_wins": recent_wins,
            "recent_5_wins": super_recent_wins,
            "last_win_distance": last_win_distance,
            "pressure_score": min(last_win_distance * 2, 20),
            "cooling_factor": max(0, super_recent_wins - 1) * 3,
        }

    return heat_scores


def advanced_prediction_algorithm(analysis_data, recent_results):
    if not analysis_data or not recent_results:
        return None

    total_wins = analysis_data.get("win_counts", {})

    anti_martingale = calculate_anti_martingale_patterns(recent_results)
    heat_index = calculate_heat_index(recent_results, total_wins)

    prediction_scores = {}

    for athlete_id in range(1, 7):
        heat_data = heat_index.get(athlete_id, {})
        pattern_data = anti_martingale.get(athlete_id, {})

        base_score = heat_data.get("base_score", 0) * 0.2
        pressure_score = heat_data.get("pressure_score", 0) * 0.4
        pattern_score = (
            pattern_data.get("pressure_10", 0) + pattern_data.get("pressure_7", 0)
        ) * 0.25
        random_score = random.uniform(0, 15) * 0.15
        cooling_penalty = heat_data.get("cooling_factor", 0)

        total_score = (
            base_score + pressure_score + pattern_score + random_score - cooling_penalty
        )

        prediction_scores[athlete_id] = {
            "total_score": total_score,
            "base_score": base_score,
            "pressure_score": pressure_score,
            "pattern_score": pattern_score,
            "random_score": random_score,
            "cooling_penalty": cooling_penalty,
            "last_win_distance": heat_data.get("last_win_distance", 0),
            "recent_wins": heat_data.get("recent_5_wins", 0),
        }

    sorted_predictions = sorted(
        prediction_scores.items(), key=lambda x: x[1]["total_score"], reverse=True
    )

    least_likely_id, least_scores = sorted_predictions[-1]
    least_likely_info = {
        "id": least_likely_id,
        "name": ATHLETES[least_likely_id],
        "prediction_score": least_scores["total_score"],
        "reason": "Điểm dự đoán thấp nhất",
        "total_wins": total_wins.get(least_likely_id, 0),
        "cooling_penalty": least_scores["cooling_penalty"],
    }

    return least_likely_info


def analyze_performance_data(data):
    if not data or not data.get("data"):
        return None, []

    analysis = {
        "win_counts": {},
        "win_rates": {},
        "recent_performance": {},
        "trend_analysis": {},
        "consistency_score": {},
    }

    recent_results = []

    if "athlete_2_win_times" in data["data"]:
        win_data = data["data"]["athlete_2_win_times"]

        for athlete_id in range(1, 7):
            key = str(athlete_id)
            wins = int(win_data.get(key, 0))
            analysis["win_counts"][athlete_id] = wins
            analysis["win_rates"][athlete_id] = (wins / 100) * 100

    if "recent_issues" in data["data"]:
        for issue in data["data"]["recent_issues"]:
            if "winner_athlete_id" in issue:
                recent_results.append(int(issue["winner_athlete_id"]))

    if not recent_results and analysis["win_counts"]:
        simulated_results = []
        for athlete_id in range(1, 7):
            wins = analysis["win_counts"][athlete_id]
            simulated_results.extend([athlete_id] * wins)

        random.shuffle(simulated_results)
        recent_results = simulated_results[-50:]

    return analysis, recent_results


def display_analysis_results(least_likely):
    fancy_print("\n" + "╔" + "═" * 45 + "╗", Fore.GREEN, Style.BRIGHT)
    fancy_print(
        "║" + "💤 ÍT KHẢ NĂNG VỀ NHẤT 💤".center(43) + "║", Fore.GREEN, Style.BRIGHT
    )
    fancy_print("╚" + "═" * 45 + "╝", Fore.GREEN, Style.BRIGHT)

    fancy_print(f"\n❌ {least_likely['name']}", Fore.GREEN, Style.BRIGHT)
    return least_likely["id"]


def display_strategy_tips():
    print(f"\n\033[38;5;51m{'═'*45}\033[0m")
    print(f"\033[38;5;51m{'💡 CHIẾN LƯỢC CHƠI 💡'.center(45)}\033[0m")
    print(f"\033[38;5;51m{'═'*45}\033[0m")
    tips = [
        "🎯 Tránh chọn người ít khả năng",
        "💰 Quản lý vốn thông minh",
        "📊 Theo dõi & điều chỉnh",
        "❗ Tuyệt đối không all-in",
    ]
    for tip in tips:
        print(f"   {tip}")


def save_analysis_to_file(analysis, least_likely, recent_results):
    try:
        result = {
            "timestamp": dt.now().isoformat(),
            "analysis": analysis,
            "recent_results": recent_results[-20:],
            "predictions": {"least_likely": least_likely},
        }

        with open(ANALYSIS_FILE, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)

        fancy_print(f"✅ Đã lưu kết quả phân tích vào {ANALYSIS_FILE}", Fore.GREEN)
    except Exception as e:
        fancy_print(f"⚠️ Lỗi lưu file: {e}", Fore.YELLOW)


def get_current_round_info(headers):
    try:
        data = safe_api_call(
            "https://api.sprintrun.win/sprint/recent_10_issues", headers
        )
        if data and data.get("data") and data["data"].get("recent_10"):
            current_round = data["data"]["recent_10"][0]
            return int(current_round["issue_id"] + 1)
    except Exception as e:
        fancy_print(f"⚠️ Lỗi lấy thông tin kỳ: {e}", Fore.YELLOW)
    return None


def check_result_and_update_stats(headers, round_id, bot_choice, stats):
    fancy_print(f"\n🔍 Đang chờ kết quả kỳ {round_id}...", Fore.CYAN)
    fancy_print(f"🤖 Bot chọn: {ATHLETES[bot_choice]}", Fore.YELLOW)

    max_wait_time = 300
    start_time = time.time()

    while time.time() - start_time < max_wait_time:
        try:
            data = safe_api_call(
                "https://api.sprintrun.win/sprint/recent_10_issues", headers
            )

            if data and data.get("data") and data["data"].get("recent_10"):
                latest_round = data["data"]["recent_10"][0]

                if (
                    int(latest_round["issue_id"]) == round_id
                    and "result" in latest_round
                ):
                    winner = int(latest_round["result"][0])
                    is_win = winner != bot_choice

                    fancy_print("\n" + "═" * 50, Fore.CYAN, Style.BRIGHT)
                    fancy_print(f"🏆 KỲ {round_id} - KẾT QUẢ", Fore.CYAN, Style.BRIGHT)
                    fancy_print("═" * 50, Fore.CYAN, Style.BRIGHT)
                    fancy_print(
                        f"🥇 Người thắng: {ATHLETES[winner]}", Fore.GREEN, Style.BRIGHT
                    )
                    fancy_print(
                        f"🤖 Bot chọn: {ATHLETES[bot_choice]}",
                        Fore.YELLOW,
                        Style.BRIGHT,
                    )

                    if is_win:
                        fancy_print("✅ KẾT QUẢ: THẮNG!", Fore.GREEN, Style.BRIGHT)
                    else:
                        fancy_print("❌ KẾT QUẢ: THUA!", Fore.RED, Style.BRIGHT)

                    fancy_print("═" * 50, Fore.CYAN, Style.BRIGHT)

                    stats.add_result(is_win, round_id, bot_choice, winner)
                    stats.display_stats()

                    return True

        except Exception as e:
            fancy_print(f"⚠️ Lỗi kiểm tra kết quả: {e}", Fore.YELLOW)

        time.sleep(5)

    fancy_print("⏰ Hết thời gian chờ kết quả!", Fore.RED, Style.BRIGHT)
    return False


def main():
    clear_screen()
    config = load_config()
    if not config:
        fancy_print("❌ Không thể tải cấu hình!", Fore.RED, Style.BRIGHT)
        input("Nhấn Enter để thoát...")
        return

    stats = GameStats()

    while True:
        try:
            headers = {
                "accept": "*/*",
                "accept-language": "vi,en;q=0.9",
                "cache-control": "no-cache",
                "country-code": "vn",
                "origin": "https://xworld.info",
                "pragma": "no-cache",
                "priority": "u=1, i",
                "referer": "https://xworld.info/",
                "sec-ch-ua": '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
                "sec-ch-ua-mobile": "?1",
                "sec-ch-ua-platform": '"Android"',
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "cross-site",
                "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36",
                "user-id": config["user_id"],
                "user-login": "login_v2",
                "user-secret-key": config["user_secret_key"],
                "xb-language": "vi-VN",
            }

            clear_screen()
            display_header()

            fancy_print("🔄 Đang lấy thông tin tài khoản...", Fore.CYAN)
            wallet_info = get_wallet_info(headers)
            display_wallet(wallet_info)

            stats.display_stats()

            fancy_print("\n🔄 Đang phân tích dữ liệu...", Fore.CYAN)
            time.sleep(1)

            data = get_recent_data(headers, 100)
            if not data:
                fancy_print("❌ Không thể lấy dữ liệu!", Fore.RED, Style.BRIGHT)
                input("Nhấn Enter để thử lại...")
                continue

            fancy_print("🧠 Đang áp dụng thuật toán...", Fore.CYAN)
            analysis, recent_results = analyze_performance_data(data)

            if not analysis:
                fancy_print("❌ Không thể phân tích!", Fore.RED, Style.BRIGHT)
                input("Nhấn Enter để thử lại...")
                continue

            fancy_print("🎯 Đang tính toán dự đoán...", Fore.CYAN)
            time.sleep(1)

            least_likely = advanced_prediction_algorithm(analysis, recent_results)

            clear_screen()
            display_header()
            bot_choice = display_analysis_results(least_likely)
            display_strategy_tips()

            round_id = get_current_round_info(headers)
            if not round_id:
                fancy_print("❌ Không thể lấy thông tin kỳ!", Fore.RED, Style.BRIGHT)
                input("Nhấn Enter để thử lại...")
                continue

            fancy_print(
                f"\n🎮 Dự đoán sẵn sàng cho kỳ {round_id}!", Fore.GREEN, Style.BRIGHT
            )

            check_result_and_update_stats(headers, round_id, bot_choice, stats)

            save_analysis_to_file(analysis, least_likely, recent_results)

        except KeyboardInterrupt:
            fancy_print("\n\n⚠️ Đã dừng chương trình!", Fore.YELLOW, Style.BRIGHT)
            stats.save_stats()
            break
        except Exception as e:
            fancy_print(f"\n❌ Lỗi nghiêm trọng: {e}", Fore.RED, Style.BRIGHT)
            fancy_print("📧 Vui lòng báo lỗi cho developer", Fore.YELLOW)
            input("Nhấn Enter để thử lại...")


while True:
    init()
    # key()
    try:
        main()
    except KeyboardInterrupt:
        print(
            "\n\033[1;97m[\033[1;91m<>\033[1;97m] \033[1;31mCảm ơn bạn đã dùng Tool !!!"
        )
        sys.exit()
