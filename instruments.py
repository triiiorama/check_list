import subprocess
import os
import shutil


def ipcheck(ip):
    """Пингер"""
    result = subprocess.run(f"ping {ip} -n 2",
                    shell=True, stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE)
    if result.returncode == 0:
        return True
    else:
        return False 


def check_list_dir(ip):
    """Проверка наличия папки и батника"""
    dir_path = r"\\{}\c$\check_list".format(ip)
    bat_file = r".\batman\check.bat"
    file_path = r"\\{}\c$\check_list\check.bat".format(ip)
    
    if os.path.exists(dir_path):
        shutil.copy(bat_file, dir_path)
        return True
    elif not os.path.exists(dir_path):
        os.mkdir(dir_path)
        shutil.copy(bat_file, dir_path)
        return True
    else:
        return False
    
    
def do_bat(ip):
    """Выполнить батник"""
    result = subprocess.run(r"wmic /node:{} process call create 'cmd /c \\{}\c$\check_list\check.bat'".format(ip, ip),
                    shell=True, stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE)
    if result.returncode == 0:
        return True
    else:
        return False
    
    
def check_files(ip):
    """Проверка наличия файлов"""
    dir_path = r"\\{}\c$\check_list".format(ip)
    cpu_used = dir_path + r"\used_cpu.txt"
    ram_used = dir_path + r"\used_ram.txt"
    ram_total = dir_path + r"\total_ram.txt"
    hdd_used = dir_path + r"\hdd_used_C"
    hdd_total = dir_path + r"\hdd_total_C"
    if os.path.exists(cpu_used)\
       and os.path.exists(ram_used)\
       and os.path.exists(ram_total)\
       and os.path.exists(hdd_used)\
       and os.path.exists(hdd_total):
        return True
    else:
        return False
    
def hdd_list(ip):
    pass
    
def read_files(ip):
    """Чтение файлов и загон их в переменные"""
    dir_path = r"\\{}\c$\check_list".format(ip)
    cpu_used = dir_path + r"\used_cpu.txt"
    ram_used = dir_path + r"\used_ram.txt"
    ram_total = dir_path + r"\total_ram.txt"
    hdd_used = dir_path + r"\hdd_used_C"
    hdd_total = dir_path + r"\hdd_total_C"
    
    # cpu_used
    if os.path.exists(cpu_used):
        with open(cpu_used, "r") as cpu_used:
            cpu_used = str(cpu_used.read().strip())
    else:
        print("cpu_used - Беда!")
    
    # ram_used
    if os.path.exists(ram_used):
        with open(ram_used, "r") as ram_used:
            ram_used = ram_used.read().strip()
            ram_used = str(int(ram_used) // 1000 // 1000)
    else:
        print("ram_used - Беда!")

    # ram_total
    if os.path.exists(ram_total):
        with open(ram_total, "r") as ram_total:
            ram_total = ram_total.read().strip()
            ram_total = str(int(ram_total) // 1000 // 1000)
    else:
        print("ram_total - Беда!")
        
    # hdd_used
    if os.path.exists(hdd_used):
        with open(hdd_used, "r") as hdd_used:
            hdd_used = str(hdd_used.read().strip())
    else:
        print("hdd_used - Беда!")
        
    # hdd_total
    if os.path.exists(hdd_total):
        with open(hdd_total, "r") as hdd_total:
            hdd_total = str(hdd_total.read().strip())
    else:
        print("hdd_total - Беда!")


    print(f"CPU {cpu_used}%, RAM {ram_used}/{ram_total} Gb, HDD C:{hdd_used}/{hdd_total} Gb")


# print(ipcheck("192.168.1.11"))
