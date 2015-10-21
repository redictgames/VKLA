#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import vk_api
import auth
from profile import Profile

vk = auth.auth(auth.result[0],auth.result[1])

class Messages:
	def Send(ids, message):
		try:
			info = vk.method("messages.send", {"user_id": ids, "message": message})
			return info
		except vk_api.vk_api.ApiError:
			print("Ошибка. Повторите попытку")
			pass 
	def Get(method):
		if method.lower() == 'dialogs':
			info = vk.method("messages.getDialogs", {"count": 5, 'rev': 1})
			for i in range(len(info['items'])):
				print(''.join(info['items'][i]['message']['title'][:2] + "..."  + " \ Отправитель: " + Profile.getProfileName([info['items'][i]['message']['user_id']]) + "\ ID: " + str(info['items'][i]['message']['user_id']) + "\ " + "".join(["Прочитано" if str(info['items'][i]['message']['read_state']) == "1" else "Не прочитано"])))

		if method.lower() == 'history':
			ids = input("Введите ID пользователя# ")
			info = vk.method("messages.getHistory", {"user_id": ids, "rev": 0, "count": 10})
			for i in reversed(range(len(info['items']))):
				print(''.join(Profile.getProfileName(info['items'][i]['from_id']) + ": " + info['items'][i]['body']) if info['items'][i]['body'] != '' or info['items'][i]['body'] else Profile.getProfileName(info['items'][i]['from_id']) + ": " + "[Сообщение с прикреплением]")