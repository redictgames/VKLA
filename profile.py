#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import vk_api
import auth

vk = auth.auth(auth.result[0],auth.result[1])

class Profile:
	relation = {1: "Не женат/Не замужем", 2: "Есть друг/Есть подруга", 3: "Помолвлен/Помолвлена", 4: "Женат/Замужем", 5:"Все сложно", 6:"В активном поиске", 7:"Влюблён/Влюблена", 0: "Не указано"}
	'''Класс отвечающий за профиль'''
	def getProfileInfo(ids):
		try:
			info = vk.method('users.get', {"user_id": ids, "fields": "sex", "fields": "online"})

			return "".join(info[0]["first_name"] + " " + info[0]["last_name"] + " " + "\ Онлайн: " + str(info[0]["online"]) + "\ ID: " + str(info[0]["id"]))
		except UnicodeEncodeError:
			pass

	def getProfileName(ids):
		try:
			info = vk.method('users.get', {"user_id": ids})

			return "".join(info[0]["first_name"] + " " + info[0]["last_name"])
		except UnicodeEncodeError:
			pass

	def getcurrentProfile():
		info = vk.method('account.getProfileInfo')
		relation = {1: "Не женат/Не замужем", 2: "Есть друг/Есть подруга", 3: "Помолвлен/Помолвлена", 4: "Женат/Замужем", 5:"Все сложно", 6:"В активном поиске", 7:"Влюблён/Влюблена", 0: "Не указано"}
		return(''.join(info['first_name'] + " " + info['last_name'] + " \ ID: " + info['screen_name'] + "\nСтрана: " + info['country']['title'] + " \ " + "Дата рождения: " + info['bdate'] + "\nСемейное положение: " + relation[info['relation']]))