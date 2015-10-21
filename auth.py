#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import vk_api
from random import random
from time import sleep
import os
import json
import getpass

WORD_CACHE = 'auth.cache'

if os.path.exists(WORD_CACHE):
	result = json.load(open(WORD_CACHE, 'rt'))
else:
	login = input("Login: ")
	password = getpass.getpass("Password: ")
	result = [login, password]
	json.dump(result, open(WORD_CACHE, 'wt'))

def auth(login,password):
	WORD_CACHE = 'auth.cache'
	data = [None,None]

	vk = vk_api.VkApi(str(result[0]),str(result[1]))

	try:
		vk.authorization()
	except vk_api.AuthorizationError as error_msg:
		print(error_msg)
		os.remove(WORD_CACHE)

	return vk