class Bus:
    def __init__(self,number,route,total_seats,row,col):
        self.number=number
        self.route=route
        self.total_seats=total_seats
        self.booked_seats=0
        self.row=row
        self.col=col
        self.seats=[]
    
        for i in range(self.row):
            row=[]
            for j in range(self.col):
                row.append('free')
            
            self.seats.append(row)
       
    
    def available_seats(self):
        return self.total_seats-self.booked_seats
        
        
    def book_seat(self,row,col):
        if self.seats[row][col]=='free':
            self.seats[row][col]='X'
            self.booked_seats +=1
            return True
        return False
 

class BusSystem:
    def __init__(self):
        self.buses=[]
        self.passengers=[]
        
    def add_bus(self,number,route,seats,admin_loged_in):
        if not admin_loged_in:
            print('only admin can add bus')
            return
        newbus=Bus(number,route,seats,5,10)
        self.buses.append(newbus)
        print(f'Bus {number} added successfully')
        
        
    def show_buses(self):
        if not self.buses:
            print('not bus available')
            return
      
        print("\n------------------------All View Bus---------------------\n")
        for bus in self.buses:
           
            print(f'Bus: {bus.number},Route: {bus.route},Available seats: {bus.available_seats()}')
            
           
    def book_ticket(self,bus_number,name,phone,):
        bus_no=None
        
        for bus in self.buses:
            if bus.number==bus_number:
                bus_no=bus
                break
        if bus_no is None:
            print('Bus not found')
            return
        passenger=Passenger(name,phone,bus_no)
        
        seats =input('Enter the seats (A1 A2 A3):').split()
        
        passenger.book_tickes(bus_number,seats)
        self.passengers.append(passenger)
   
class Admin:
    def __init__(self,username,password,system):
        self.username=username
        self.password=password
        self.loged_in=False
        self.system=system
       
        
    def add_bus(self,number,route,seats):
        self.system.add_bus(number,route,seats,self.loged_in)
      
    
    
    def login(self,username,password):
        if username==self.username:
            
            if password==self.password:
                self.loged_in=True
                print('login successful')
            else:
                print('Invalid password')
                
        else:
            print('Invalid username')
            
class Passenger:
    def __init__(self,name,phone,bus):
        self.name=name
        self.phone=phone
        self.bus=bus
     
       
        
    def book_tickes(self,bus_number,booking_seats):
        flag=0
        self.booked_tickes=[]
        if self.bus.number !=bus_number:
            print('wrong show number')
            return
        else:
            for x in booking_seats:
                r=ord(x[0])-65
                c=ord(x[1])-49
                #c=int (x[1:])-1 1 ter basi ticket kete chile ai ta use kore hobe
                
                
                if r>=self.bus.row or c>=self.bus.col or r<0 or c<0:
                    print('seat doesnot exists')
                elif self.bus.seats[r][c]!='free':
                    print(x,'in already booked')
                    
                else:
                    self.bus.seats[r][c]='X'
                    self.bus.booked_seats +=1
                    self.booked_tickes.append(x)
                    flag=1
            
            
                    
        if flag==1:
            print("\n------------------------Ticket Booked Successfully---------------------\n")
            print('Name: ',self.name)
            print('Phone: ',self.phone)
            print('Price:',500*len(self.booked_tickes),'Tk')                    
           
    

system_bus=BusSystem()
admin=Admin('admin','1234',system_bus)
def admin_menu():
    while True:
        print("\n------------------------Admin Menu---------------------\n")
        print('1. Add Bus')
        print('2.View all Buses')
        print('3.logout')
        
        option =int(input('Enter the option'))
        if option==1:
            number=input('Enter number ')
            route=input('Route: ')
            seats=int(input('total seats '))
            admin.add_bus(number,route,seats)
            
        elif option==2:
            system_bus.show_buses()
            
        elif option==3:
            admin.loged_in=False
            print('loged out')
            break
        else:
            print('Invalid option')
            
def main_menu():
    while True:
        print("\n------------------------Main Menu---------------------\n")
        print("1. Admin Login")
        print("2. Book Ticket")
        print("3. View Buses")
        print("4. Exit")
        
        option =int(input('Enter the option'))
        if option==1:
          username=input('Username : ')
          password=input('password :')
          admin.login(username,password)
          if admin.loged_in:
              admin_menu()
              
          
        elif option==2:
            name=input('Enter your name :')
            phone=input('Enter your phone :')
            bus_number=input('Enter bus number :')
            system_bus.book_ticket(bus_number,name,phone)
            
           
        elif option==3:
            system_bus.show_buses()
            
        elif option==4:
            print('Exit')
            break
        else:
            print('Invalid option')
main_menu()