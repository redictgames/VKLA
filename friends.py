#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import vk_api
import auth
from profile import Profile
from time import sleep

vk = auth.auth(auth.result[0],auth.result[1])


class Friends:
	'''Класс отвечающий за список друзей'''

	def getFriends(ids, method):
		if method == 'list':
			info = vk.method('friends.get', {"user_id": ids})
			for i in range(len(info['items'])):
				print(Profile.getProfileInfo(info['items'][i]))
				sleep(1)
		elif method == 'online':
			info = vk.method('friends.getOnline', {"user_id": ids})
			for i in range(len(info)):
				print(Profile.getProfileInfo(info[i]))
				sleep(1)
