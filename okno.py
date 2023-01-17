# from echo_bot import height, width
import sqlite3

# Делам выборку из бд - какие считать окна
def window(c_id = 0, g_id=0):
    """  *Выбирает окна по id конструкции, id группы, либо просто показывает все доступные
    возращает(name, description, img_name, construction_id), либо их список """
    conn = sqlite3.connect("orders.db")
    window = conn.cursor();ans = []
    if ( not  c_id) and (not g_id): # пока только список всех конструкций
        for row in window.execute("SELECT name, description, img, id FROM constructions"):
            ans.append(row)
        conn.close()
    return ans
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
window_filling = [filling_l, filling_h]
# Считаем необходимые материалы
rama_profile = (rama_l + rama_h) / rama_profile_h
shtapik_profile = (shtapik_l + shtapik_h) / shtapik_profile_h

# Окно одностворчатое



def answer(width, height):
    # Определяем фурнитуру для конструкции
    suhar_rama = 1; suhar_mini = 1; podkladka_pod_steklo = 1; vent_zaglyshka = 1
    #расчёт
    rama_l = height * 2; rama_h = width * 2
    shtapik_l = width - 52; shtapik_h = height - 98
    suhar_rama = suhar_rama * 4
    suhar_mini = suhar_mini * 4
    podkladka_pod_steklo = podkladka_pod_steklo * 4
    vent_zaglyshka = vent_zaglyshka * 2
    uplotnitel_1 = height * 2 + width * 2 - 328
    uplotnitel_2 = height * 2 + width * 2 - 288
    filling_h = width - 66
    filling_l = height - 66
    window_filling = [filling_l, filling_h]
    rama_profile = (rama_l + rama_h) / rama_profile_h
    shtapik_profile = (shtapik_l + shtapik_h) / shtapik_profile_h
    # собираем текст ответа
    ans =  'Расчет материалов :\n'
    ans += '- Профиль :\n'
    ans += ' - Рамный профиль ( 121010 ): ' + "%.2f " % rama_profile  + 'профиля длинной : ' + "%.0f " % rama_profile_h
    ans += '\n - Штапик ( 125060 ): ' + "%.2f" % shtapik_profile + ' профиля длинной :' + "%.0f " % shtapik_profile_h
    ans += '\n - Комплектующие :\n'
    ans += ' - Сухарь угловой ( 721014 ): ' + "%.0f " % suhar_rama + 'шт.\n'
    ans += ' - Сухарь установочный ( 723020 ): ' + " %.0f "  % suhar_mini +  'шт.\n'
    ans += ' - Заглушка вентиляционная ( 727180 ): ' +  "%.0f " % vent_zaglyshka + 'шт.\n'
    ans += ' - Подкладка под стекло ( 727010 ): ' + "%.0f " % podkladka_pod_steklo + 'шт.\n'
    ans += '- Резина :\n'
    ans += ' - Уплонитель ( 521010 ): ' + "%.0f мм \n" % uplotnitel_1
    ans += ' - Уплонитель ( 522020 ): ' + "%.0f мм \n" % uplotnitel_2
    ans += '- Стекло :\n'
    ans += ' - Заполнение ( 6мм ): '+ " %.0f * " % filling_l + "%.0f мм \n" % filling_h
    ans += "%.0f *" % window_filling[0] + "%.0f \n" % window_filling[1]
    return ans

#if __name__ == '__main__':
    print (answer(width,height))