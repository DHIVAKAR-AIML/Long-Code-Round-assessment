import uuid
class movie:
    def __init__(self):
        self.title1 = {'love today':"001" , 'hi naan':'002' ,'dude' :'003' , 'ddd' : '004'}
        self.title = {'001':'001 love today - 21-01-2026 - 01:00 - vr mall' , '002':'002 hi naan - 23-01-2026 - 09:00 - vmax' , '003' : '003 dude - 22-01-2026 - 05:00 - Dmax' , '004':'004 ddd - 04-06-2026 - 07:00v - dmzx'}
        self.lang = {'001':'tamil' ,'002':'telugu' ,'003' :'tamil' ,'004' : 'english' }
        self.date = {'001':"21-01-2026",'002':"23-01-2026",'003':"22-01-2026" , '004' : '04-06-2006'}


    def getshowtimes(self,title , lan , dat):
        print("avaliable")
        print("movie_id | movie name | date time | location")
        if title in self.title1:
            self.id = self.title1[title]
            print(self.title[self.id])

        for i in self.lang:
            self.lang1 = self.lang[i]
            if lan == self.lang1:
                print(self.title[i])

        for i in self.date:
            self.date1 = self.date[i]
            if dat == self.date1:
                print(self.title[i])

class seat:
    def __init__(self):
        self.seat_id = None
        self.catagory = None
        self.status = None
        self.no_of_seat = {'001' : 52 , '002' : 76 , '003' : 67 , '004' : 98}

    def lock(self,movie_id):
        self.seat = []
        self.sseat = [self.x for self.x in range(1,self.no_of_seat[movie_id])]
        if self.no_of_seat[movie_id] <= 0:
            return 
        self.many = int(input("\nhow many seat u want to book"))
        print(f'avaliable seat are \n{self.sseat}')
        if self.many < self.no_of_seat[movie_id]:
            for i in range(self.many):
                  self.seat.append(input(f"\ntotal {self.no_of_seat[movie_id]} seat are avaliable , plz enter ur seat no:"))
        print("pay to confirm your seats")
        if e.booking(movie_id , self.many):
            print("booked sucessfully")
            self.eticket = str(uuid.uuid4())[:8].upper()
            print(f'\nur ticket will sent to ur mail shortly\n ur eticket id: {self.eticket}')

        else:
            print("\ntime out plz try again")

class booking:
    def __init__(self):
        self.total = 0
        self.amount = {'001' : 500 , '002' : 600 , '003' : 900 , '004' : 890}
    def booking(self,movie_id ,many):
        self.total = self.amount[movie_id] * many
        print(f'{self.amount[movie_id]} per seat')
        self.confim = input(f'pay : {self.total}\n paid : yes or no\n').lower()
        if self.confim == 'yes':
            return True
        return False

d = movie()
e = booking()
f = seat()



search = input("seacrch with date or language or title:").lower()
if search == 'date':
   date = input("\nenter date: ")
   d.getshowtimes(None , None , date)
elif search == 'title':
    title = input("\nenter time: ")
    d.getshowtimes(title , None , None)
elif search == 'language':
    lan = input("\nlanguage: ")
    d.getshowtimes(None , lan , None)

select_id = input("\nenter the movie id u want to book seat:")
f.lock(select_id)
















        