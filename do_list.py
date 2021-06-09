import logging
import instruments
import time 

logging.basicConfig(level=logging.DEBUG,\
					format=' %(asctime)s - %(levelname)s - %(message)s')

ip = input("Введите ip: ")

# Проверка путей, копирование и выполнение скрипта
try:
    if instruments.ipcheck(ip):
        if instruments.check_list_dir(ip):
            logging.debug(f"Копирование на {ip} прошло успешно")
            if instruments.do_bat(ip):
                logging.debug("Скрипт Выполнен")
                while not instruments.check_files(ip):
                    time.sleep(2)
                    logging.debug(f"Ожидаются результаты")
                instruments.read_files(ip)
            else:
                logging.debug("Скрипт Невыполнен")
        else:
            logging.debug("Что-то с копированием пошло не так")
    else:
        logging.debug(f"Хост - {ip} недоступен")
except:
    logging.debug("Непредвидимая ошибка\n\
				   Возможно хост недоступен или проблемы с доступом")
