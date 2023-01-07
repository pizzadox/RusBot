# Определяем переменные конструкции
# Следуюие данные берем у клиента
height = 1000
width = 900
rama_profile_h = 6000
shtapik_profile_h = 6000
# Определяем фурнитуру для конструкции
suhar_rama = 1
suhar_mini = 1
podkladka_pod_steklo = 1
vent_zaglyshka = 1
# Формула расчета для Конструкции ОКНО глухое
rama_l = height * 2
rama_h = width * 2
shtapik_l = rama_l - 52
shtapik_h = rama_h - 52
suhar_rama = suhar_rama * 4
suhar_mini = suhar_mini * 4
podkladka_pod_steklo = podkladka_pod_steklo * 4
vent_zaglyshka = vent_zaglyshka * 2
# Считаем необходимые матриалы
rama_profile = (rama_l + rama_h) / rama_profile_h
shtapik_profile = (shtapik_l + shtapik_h) / shtapik_profile_h
# Выводим расчет
print('Расчет материалов :')
print(' - Рамный профиль ( 121010 ): ', rama_profile, 'профиля длинной :', rama_profile_h)
print(' - Штапик ( 125060 ): ', shtapik_profile, 'профиля длинной :', shtapik_profile_h)
print(' - Сухарь угловой ( 721014 ): ', suhar_rama, 'шт.')
print(' - Сухарь установочный ( 723020 ): ', suhar_mini, 'шт.')
print(' - Заглушка вентиляционная ( 727180 ): ', vent_zaglyshka, 'шт.')
print(' - Подкладка под стекло ( 727010 ): ', podkladka_pod_steklo, 'шт.')
