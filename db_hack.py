import random
from datacenter.models import Chastisement
from datacenter.models import Schoolkid
from datacenter.models import Mark
from datacenter.models import Commendation
from datacenter.models import Lesson


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


def fix_marks(child="Фролов Иван Григорьевич"):
	Mark.objects.filter(schoolkid__full_name=child, points__in=[2,3]).update(points=5)


def remove_chastisements(child="Фролов Иван Григорьевич"):
	Chastisement.objects.filter(schoolkid__full_name=child).delete()


def create_commendation(subject_title, child="Фролов Иван Григорьевич"):
	commendation = random.choice(COMMENDATIONS)
	schoolkid = Schoolkid.objects.get(full_name=child)
	lession = Lesson.objects.filter(year_of_study=6, group_letter="А", subject__title=subject_title.capitalize()).order_by("?").first()
	Commendation.objects.create(text=commendation, created=lession.date, schoolkid=schoolkid, subject=lession.subject, teacher=lession.teacher)


