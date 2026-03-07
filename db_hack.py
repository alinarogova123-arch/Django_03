import random
import sys
from datacenter.models import Chastisement
from datacenter.models import Schoolkid
from datacenter.models import Mark
from datacenter.models import Commendation
from datacenter.models import Lesson
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import MultipleObjectsReturned


COMMENDATIONS = [
	"Молодец!",
	"Отлично!",
	"Хорошо!",
	"Гораздо лучше, чем я ожидал!",
	"Ты меня приятно удивил!",
	"Великолепно!",
	"Прекрасно!",
	"Ты меня очень обрадовал!",
	"Именно этого я давно ждал от тебя!",
	"Сказано здорово – просто и ясно!",
	"Ты, как всегда, точен!",
	"Очень хороший ответ!",
	"Талантливо!",
	"Ты сегодня прыгнул выше головы!",
	"Я поражен!",
	"Уже существенно лучше!",
	"Потрясающе!",
	"Замечательно!",
	"Прекрасное начало!",
	"Так держать!",
	"Ты на верном пути!",
	"Здорово!",
	"Это как раз то, что нужно!",
	"Я тобой горжусь!",
	"С каждым разом у тебя получается всё лучше!",
	"Мы с тобой не зря поработали!",
	"Я вижу, как ты стараешься!",
	"Ты растешь над собой!",
	"Ты многое сделал, я это вижу!",
	"Теперь у тебя точно все получится!"
]


def get_schoolkid(child_name):
	try:
		schoolkid = Schoolkid.objects.get(full_name__contains=child_name)
	except ObjectDoesNotExist:
		raise ObjectDoesNotExist("Ученик с таким именем не найден")
	except MultipleObjectsReturned:
		raise MultipleObjectsReturned("С таким именем несколько учеников")
	else:
		return schoolkid


def fix_marks(child_name):
	schoolkid = get_schoolkid(child_name)	
	Mark.objects.filter(schoolkid=schoolkid, points__in=[2,3]).update(points=5)


def remove_chastisements(child_name):
	schoolkid = get_schoolkid(child_name)
	Chastisement.objects.filter(schoolkid=schoolkid).delete()


def create_commendation(child_name, subject_title):
	schoolkid = get_schoolkid(child_name)
	commendation = random.choice(COMMENDATIONS)
	lesson = Lesson.objects.filter(year_of_study=6, group_letter="А", subject__title=subject_title.capitalize()).order_by("?").first()
	try:
		Commendation.objects.create(text=commendation, created=lesson.date, schoolkid=schoolkid, subject=lesson.subject, teacher=lesson.teacher)
	except AttributeError:
		print("Такой предмет не найден")
