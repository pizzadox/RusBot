class BotState():
    State = "start" #состоние. пока строкой, но надо это обьявлять по другому
    width=0; height =0 # перенести в стуктура данных конкретного пользователя
    construction_id = 0 #orders.db construction id
    def __init__(self):
        self.State = ""
    def __init__(self,width:int,heigh:int,construction_id:int):
        self.width = width; self.height = heigh; self.construction_id = construction_id
    def __init__(self,width:int,height:int,construction_id:int,State:str):
        self.width = width
        self.height = height
        self.construction_id = construction_id
        self.State = State
    def __repr__(self):
        ans = "%d, " % self.width + "%d, " % self.height + '%d, "'%self.construction_id + self.State + '"'
        return ans

from collections import UserDict
import sqlite3
class cbStates(UserDict):
    conn=""
    def __init__(self):
        super().__init__()
        #open db
        self.conn = sqlite3.connect("bstates.db", check_same_thread=False)
        #self.bd  = conn.cursor();ans = []
        aa = self.conn.execute('SELECT user_id, width, height, construction_id, State  FROM users ' )
        ans = aa.fetchall()
        for a in ans:
            id = int(a[0])
            width =int( a[1])
            height  = int(a[2])
            constr_id = int(a[3])
            State = a[4]
            print ("load from bd id %d"%id)
            self.data[id] = BotState(width, height, constr_id, State)

    def save(self,id=0):
        if not id: #сохраняем весь словарь
            self.conn.execute('DELETE FROM users') # очищаем таблицу !!
            self.conn.commit()
            for id in bStates.keys():
                b = bStates[id]
                aa = self.conn.execute('INSERT INTO users (user_id, width, height, construction_id, State) VALUES (' +"%d,"%id + b.__repr__() +')')
                self.conn.commit()

    def __del__(self):
        self.save()
        self.conn.close()
