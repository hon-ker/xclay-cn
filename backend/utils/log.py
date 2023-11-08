#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__clay__'

import logging
import sys

from colorama import init, Fore, Back, Style

import config

# 设置scapy的日志等级
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

# 初始化 Colorama，以支持终端颜色
init(autoreset=True)

# 创建 logger 对象
logger = logging.getLogger()
logger.setLevel(config.LOGGING_LEVEL.upper())

# 创建文件处理程序
file_handler = logging.FileHandler(config.LOGGING_FILE)
# 定义日志格式
file_formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


# log文件通过logger模块实现，终端打印自定义实现
class SimpleLog(object):

    def __init__(self, logger):
        self.logger = logger

    def debug(self, *args):
        if config.LOGGING_LEVEL.upper() == "DEBUG":
            string = " ".join(map(str, list(args)))
            colored_string = f"{Fore.BLACK}{Style.BRIGHT}[!] {string}"
            sys.stdout.write(colored_string + "\n")
            self.logger.debug(string)

    def info(self, *args):
        string = " ".join(map(str, list(args)))
        colored_string = f"{Fore.GREEN}{Style.BRIGHT}[+] {string}"
        sys.stdout.write(colored_string + "\n")
        self.logger.info(string)

    def succes(self, *args):
        string = " ".join(map(str, list(args)))
        colored_string = f"{Fore.CYAN}{Style.BRIGHT}[#] {string}"
        sys.stdout.write(colored_string + "\n")
        self.logger.warning(string)

    def error(self, *args):
        string = " ".join(map(str, list(args)))
        colored_string = f"{Fore.RED}{Style.BRIGHT}[-] {string}"
        sys.stdout.write(colored_string + "\n")
        self.logger.error(string)

    def write_debug(self, *args):
        string = " ".join(map(str, list(args)))
        self.logger.debug(string)

    def write_info(self, *args):
        string = " ".join(map(str, list(args)))
        self.logger.info(string)

    def write_warning(self, *args):
        string = " ".join(map(str, list(args)))
        self.logger.warning(string)

    def write_error(self, *args):
        string = " ".join(map(str, list(args)))
        self.logger.error(string)


# 创建 SimpleLog 实例
log = SimpleLog(logger)

if __name__ == "__main__":
    log.debug("text信息")
    log.info(12138, "new")
    log.succes("success成功")
    log.error("error信息")
    log.info(1, 2, 3, 4, 5, 6)
