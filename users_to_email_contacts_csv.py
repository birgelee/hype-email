#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import subprocess
import json
import datetime
import time
import random
import os

def parse_args():
    parser = argparse.ArgumentParser()
    # This is a CAIDA AS topology.
    parser.add_argument("-u", "--users_csv",
                        default="./hype-email-list.csv")
    return parser.parse_args()

#def get_current_human_time():
#	value = datetime.datetime.fromtimestamp(time.time())
#	return value.astimezone(datetime.timezone.utc).strftime('UTC %Y-%m-%d %H:%M:%S')
#
#
#def run_cmd(cmdAndArgsList):
#	#print(cmdAndArgsList)
#	retryCount = 1
#	out = b''
#	err = b''
#	for i in range(retryCount):
#		p = subprocess.Popen(cmdAndArgsList, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#		out, err = p.communicate()
#		if err == b'':
#			return out.decode('utf-8')
#		elif "kex_exchange_identification" in err.decode('utf-8'): # Just try again in this case.
#			continue
#		else:
#			# Assume this is an ssh connection error.
#			print(f"[{get_current_human_time()}] stderr: \"{err.decode('utf-8')}\" from cmd {cmdAndArgsList}") # This could go to stderr or stdio.
#			return out.decode('utf-8')
#		#pass
#		#raise IOError(f"Non-empty error: {err.decode('utf-8')}")
#	print(f"[{get_current_human_time()}] Max retries ({retryCount}) reached. stderr: \"{err.decode('utf-8')}\" from cmd {cmdAndArgsList}") # This could go to stderr or stdio.
#	return out.decode('utf-8')



def main(args):
	print(f"emailAddress,unsubscribeAll,attributesData,topicPreferences.News")
	for line in open(args.users_csv):
		sline = line.strip()
		if sline == "":
			continue
		print(f"{sline},false,,OPT_IN")




if __name__ == '__main__':
    main(parse_args())