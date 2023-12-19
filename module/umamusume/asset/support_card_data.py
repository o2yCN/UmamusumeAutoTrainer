from difflib import SequenceMatcher
import json
import os.path

from bot.recog.ocr import find_similar_text
from module.umamusume.define import *
from bot.base.resource import Template

class SupportCardData:
	id: int
	fullname: str
	name: str
	title: str
	character: str
	template : Template
	skill_list : list[str]
	card_type: SupportCardType

	def __init__(self):
		self.template = None

SUPPORT_CARD_NAME_TO_INDEX: dict[str, int] = {}
SUPPORT_CARD_NAME: list[str] = []

SUPPORT_CARD_MAP: dict[int, SupportCardData] = {}
UMAMUSUME_SUPPORT_CARD_TEMPLATE_PATH = "/umamusume/support_card/head"

def get_card_type(type_id:int) -> SupportCardType:
	if type_id == 0:
		return SupportCardType.SUPPORT_CARD_TYPE_SPEED
	elif type_id == 1:
		return SupportCardType.SUPPORT_CARD_TYPE_STAMINA
	elif type_id == 2:
		return SupportCardType.SUPPORT_CARD_TYPE_POWER
	elif type_id == 3:
		return SupportCardType.SUPPORT_CARD_TYPE_WILL
	elif type_id == 4:
		return SupportCardType.SUPPORT_CARD_TYPE_INTELLIGENCE
	elif type_id == 5:
		return SupportCardType.SUPPORT_CARD_TYPE_FRIEND
	elif type_id == 6:
		return SupportCardType.SUPPORT_CARD_TYPE_GROUP
	else:
		return SupportCardType.SUPPORT_CARD_TYPE_UNKNOWN

def split_full_name (fullname:str) -> (str,str):
	title = fullname.split(']')[0].strip('[')
	character = fullname.split(']')[1]
	return character,title

def load_support_card_database():
	skill_map = {}
	fullname_map = {}
	with open('resource/umamusume/data/text_data.json', 'r', encoding="utf-8") as file:
		json_data = json.load(file)
		skill_map = json_data["47"]
		fullname_map = json_data["75"]

	with open('resource/umamusume/data/cardDB.json', 'r', encoding="utf-8") as file:
		json_data = json.load(file)
		for card_id in json_data:
			data = json_data[card_id]
			support_card_id = int(data["cardId"])
			fullname = data["fullName"]
			if str(support_card_id) in fullname_map:
				fullname = fullname_map[str(support_card_id)]

			character,title = split_full_name(fullname)

			support_card_data = SupportCardData()
			support_card_data.id = support_card_id
			support_card_data.fullname = fullname
			support_card_data.name = data["cardName"]
			support_card_data.title = title
			support_card_data.character = character

			path = "resource" + UMAMUSUME_SUPPORT_CARD_TEMPLATE_PATH + "/" + str(support_card_id)+".png"
			if os.path.isfile(path):
				support_card_data.template = Template(str(support_card_id), UMAMUSUME_SUPPORT_CARD_TEMPLATE_PATH)
			
			support_card_data.skill_list = []
			for skill_id in data["cardSkill"]["skillList"]:
				if str(skill_id) in skill_map:
					support_card_data.skill_list.append(skill_map[str(skill_id)])
			
			support_card_data.card_type = get_card_type(int(data["cardType"]))

			SUPPORT_CARD_MAP[support_card_id] = support_card_data
			SUPPORT_CARD_NAME_TO_INDEX[fullname] = support_card_id
			SUPPORT_CARD_NAME.append(fullname)

def find_similar_support_card_id(character:str,title:str) -> int:
	fullname = make_full_name(character,title)
	if fullname in SUPPORT_CARD_NAME_TO_INDEX:
		return SUPPORT_CARD_NAME_TO_INDEX[fullname]
	else:
		card_name = find_similar_text(fullname, SUPPORT_CARD_NAME,0.8)
		if card_name != "":
			return SUPPORT_CARD_NAME_TO_INDEX[card_name]
		else:
			for cardid in SUPPORT_CARD_MAP:
				card = SUPPORT_CARD_MAP[cardid]
				if SequenceMatcher(None,card.title,title).ratio() > 0.8:
					return cardid
			
			return 0

def get_support_card_data(support_card_id:int) -> SupportCardData:
	if support_card_id in SUPPORT_CARD_MAP:
		return SUPPORT_CARD_MAP[support_card_id]
	else:
		return None
	
def make_full_name(character:str,title:str) -> str:
	title = title.strip('[').strip(']')
	return '['+title+']'+character

def load_support_card_data(character:str,title:str) -> SupportCardData or None:
	support_card_id = find_similar_support_card_id(character,title)
	if support_card_id != 0:
		return get_support_card_data(support_card_id)
	else:
		return None

load_support_card_database()