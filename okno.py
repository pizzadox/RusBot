from echo_bot import ddd

# Определяем переменные конструкции
# Следуюие данные берем у клиента в файле echo_bot
height = 100
width = 200
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
shtapik_l = width - 52
shtapik_h = height - 98
suhar_rama = suhar_rama * 4
suhar_mini = suhar_mini * 4
podkladka_pod_steklo = podkladka_pod_steklo * 4
vent_zaglyshka = vent_zaglyshka * 2
uplotnitel_1 = height * 2 + width * 2 - 328
uplotnitel_2 = height * 2 + width * 2 - 288
filling_h = width - 66
filling_l = height - 66
# Считаем необходимые материалы
rama_profile = (rama_l + rama_h) / rama_profile_h
shtapik_profile = (shtapik_l + shtapik_h) / shtapik_profile_h
# Выводим расчет
print('Расчет материалов :')
print('- Профиль :')
print(' - Рамный профиль ( 121010 ): ', "%.2f" % rama_profile, 'профиля длинной :', rama_profile_h)
print(' - Штапик ( 125060 ): ', "%.2f" % shtapik_profile, 'профиля длинной :', shtapik_profile_h)
print('- Комплектующие :')
print(' - Сухарь угловой ( 721014 ): ', suhar_rama, 'шт.')
print(' - Сухарь установочный ( 723020 ): ', suhar_mini, 'шт.')
print(' - Заглушка вентиляционная ( 727180 ): ', vent_zaglyshka, 'шт.')
print(' - Подкладка под стекло ( 727010 ): ', podkladka_pod_steklo, 'шт.')
print('- Резина :')
print(' - Уплонитель ( 521010 ): ', uplotnitel_1, 'мм.')
print(' - Уплонитель ( 522020 ): ', uplotnitel_2, 'мм.')
print('- Стекло :')
print(' - Заполнение ( 6мм ): ', filling_l,'*',filling_h,  'мм')