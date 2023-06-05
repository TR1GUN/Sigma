# Итак
#
# Поскольку мы должны

# Сюда пихать список из ID радио
Radio = []
# Это срез дней что затрагиваем
Days = 3
# Параметры сбора
Params = {"unique": True}
from Action import Action

collection = Action(RadioStation_list=Radio, Scheduler=Days, Params=Params).get_tracks()
