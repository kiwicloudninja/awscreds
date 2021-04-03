#!/usr/bin/python3

import sys
import pyperclip
import configparser
from os.path import expanduser, isfile

def compare_credentials(old, new):
	credential_name = new.sections()[0]
	for key in new[credential_name]:
		if old[credential_name][key] != new[credential_name][key]:
			return False
	return True

def update_credentials():
	# get pasteboard contents and check they have credentials
	new_section = pyperclip.paste()
	if 'aws_access_key_id' not in new_section:
		sys.exit("No valid credential found on the clipboard")

	# create a new config item, and determine it's name
	new_config = configparser.ConfigParser()
	new_config.read_string(new_section)
	new_item = new_config.sections()[0]

	# if an existing credentials file exists, read it
	aws_creds_name = expanduser("~") + '/.aws/credentials'
	config = configparser.ConfigParser()
	if isfile(aws_creds_name):
		config.read(aws_creds_name)

		# exit if the old credential is up to date
		if new_item in config and compare_credentials(config, new_config):
			sys.exit(new_item + " is still current")

		config.remove_section(new_item)

	# add the new credential
	config.read_string(new_section)

	# write the credentials file
	with open(aws_creds_name, 'w') as config_file:
		config.write(config_file)

	print("Updated " + new_item + " in " + aws_creds_name + "\r\n")

if (__name__ == '__main__'):
	update_credentials()
