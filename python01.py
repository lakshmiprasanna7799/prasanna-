from scapy.all import *
import psutil
from collections import defaultdict
import os
from threading import Thread
import pandas as pd

all_mac={iface.mac for iface in ifaces.value()}
connection2pid={}
pid2traffic =defaultdict
global_df=None
is_program_running=True
def get_size(bytes):
		for unit in {'','K','M','G','T','P'}:
			if bytes<1024:
				return f"{bytes:.2f}(unit)B"
			bytes /=1024
		