import MySQLdb
from codes_to_km import GreatCircleDistance

class FindMatches:

    def __init__(self, id):
        self.id = id

    def PotentialMatches(self):

        db = MySQLdb.connect(host='dylan9012.mysql.pythonanywhere-services.com',
                             user='dylan9012',
                             password='destiny1',
                             db='dylan9012$default',
                             )

        cur = db.cursor()

        db.set_character_set('utf8')
        cur.execute('SET NAMES utf8;')
        cur.execute('SET CHARACTER SET utf8;')
        cur.execute('SET character_set_connection=utf8;')

        # print('SELECT Location, Max_distance, Needs_or_specialty, UserID FROM Account WHERE UserID = '+ str(id) +';')
        cur.execute('SELECT Location, Max_distance, Needs_or_specialty, UserID FROM Account WHERE UserID = ' + str(id) + ';')
        r = cur.fetchall()
        UserValues = list(r[0])
        print(UserValues)

        cur.execute('SELECT Location, max_distance, Needs_or_specialty, UserID, age, gender FROM Account WHERE Needs_or_specialty = "' + UserValues[2] + '";')
        s = cur.fetchall()
        potentials1 = [list(i) for i in s]

        for k in potentials1:
            if k[3] == int(id):
                potentials1.remove(k)
                break
            else:
                pass

        print(potentials1)

        '''
        for i in potentials1:
            i.append(GreatCircleDistance(UserValues[0], i[0]))
        
        print(potentials1)
        '''

        potentials1[0].append(0)
        potentials1[1].append(3)

        print(potentials1)

        finalmatches = []

        for q in potentials1:
            if q[6] < UserValues[1]:
                finalmatches.append(q)

        print(finalmatches)

        db.close()

if __name__ == "__main__":
    pass