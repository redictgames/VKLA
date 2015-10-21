#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import vk_api
from profile import Profile
from friends import Friends
from message import Messages


class Help:
	'''Класс для получение помощи по программе(т.е все методы программы)'''
	def hello():
		print('''VKApi Lightweight App v0.1a
Дорогой друг, если ты когда либо задумывался о том, как много трафика уходит на повседневные задачи во ВКонтакте,\nЭто приложение создано, чтобы сэкономить ваш трафик в нужную минуту,\nЧтобы ознакомиться со списком команд введите "help" ''')
	def help():
		print('''Profile - Выводит информацию о вашем профиле\nMessage - позволяет отправлять\nFriends - выводит ваших друзей\nMessages - выводит ваши сообщения\nПример запроса: friends <id> <method>\nТак же вы можете получить полную документацию по использованию каждой функции:\nhelp <name_of_func>''')
	def help_4_func(func):
		try:
			if func == 'profile':
				print("Profile - Выводит информацию о любом профиле профиле\nProfile <id>\nПример полного запроса:\nprofile 1")
			if func == 'messages':
				print("Messages - Позволяет читать сообщения\nmessages <method>\nМетоды: dialogs, history\nМетод dialogs - выдает список последних 5-и диалогов\nМетод history - при выполнении запрашивает ID пользователя и выводит последние 10 сообщений\nПример полного запроса:\nmessages history")
			if func == 'message':
				print("Message - Позволяет отправить сообщение\nMessage <id>\nПосле выполнения команды запрашивает текст сообщения\nПример полного запроса:\nmessage 1337")
			if func == 'friends':
				print("Friends - Показывает список ваших друзей\nFriends <id> <method>\nМетоды: list, online\nМетод list - выдает полный список друзей\nМетод online - выдает список друзей онлайн\nПример полного запроса:\nfriends 1 online")
			if func == 'help':
				Help.help()
		except:
			pass

	def Interpreter(command):
		command = command.split()
		commands = []
		for i in command:
			commands += [i]
		return commands

Help.hello()
import auth
vk = auth.auth(auth.result[0],auth.result[1])

class Executing:
	"""Класс выполнения спланированных задач"""

	def execute(command):
		if command[0].lower() == 'profile':
			try:
				print(Profile.getProfileInfo(command[1]))
			except:
				print(Profile.getcurrentProfile())
		if command[0].lower() == 'friends':
			Friends.getFriends(command[1], command[2])
		if command[0].lower() == 'help':
			try:
				Help.help_4_func(command[1])
			except:
				Help.help_4_func(func='help')

		if command[0].lower() == 'messages':
			try:
				print(Messages.Get(command[1].lower()))
			except:
				print("Ошибка запроса, попробуйте еще раз")
				pass
		if command[0].lower() == 'message':
			message = input("Write message# ")
			Messages.Send(command[1], message)


while True:
	command = input(">> ")

	command = Help.Interpreter(command)

	Executing.execute(command)

