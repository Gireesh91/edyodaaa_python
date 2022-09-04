from select import select
from user_main import *
from events import *
class user_profile():

    user_details = []
    events = []

    def show(self,choice):

        if choice == 1:
            print("*****************ADD USER DETAILS*******************")
            name = input("Enter the name of user :")
            userName = input("Enter the UserName of user : ")
            userPassword = input("Enter password :")
            print("Register as Member or Organiser :")
            print("1.Organiser \n2.Member")
            cho = int(input("your choice : "))
            if(cho ==1):
                user_obj = User(name,userName,userPassword,"ORGANISER")
                self.user_details.append(user_obj)
            if(cho ==2):
                user_obj = User(name,userName,userPassword,"MEMBER")
                self.user_details.append(user_obj)         
            print("Successfully Registered")
        if choice == 2:
            print("****** login to the Application*****")
            userName = input("Enter username")
            password = input("Enter password")
            for user in self.user_details:
                if user.userName == userName and user.password == password:
                    if(user.userType == "MEMBER"):
                        print("successfully loged in as Member")
                        self.memberWork()
                    if(user.userType == 'ORGANISER'):
                        print("successfully loged in as Organiser")
                        self.organiserWork()
                else:
                    print("entered username : "+ userName)
                    print("entered password : "+ password)
                    print("Login Failed")
                    return

    def memberWork(self):
        print("****** select a choice *******")
        print("1.Show events \n2.Register for an event")
        ch = int(input("your choice"))
        if(ch ==1):
            self.showAllEventsToMember()
        if(ch ==2):
            pass
        return

    def showAllEventsToMember(self):
        for event in self.events:
            print("EventId : "+event.get_eventId()+"\n"+"eventName : "+event.get_name()+"\n"+"startDate : "+event.get_startDate()+"\n"+"startTime : "+event.get_startTime()+"\n"+"endDate : "+event.get_endDate()+"\n"+"endTime : "+event.get_endTime()+"\n"+"seatAvailabe : "+event.get_seatAvailble()+"\n"+"registeredUserIds : "+str(event.get_registeredUserIds()))

    def organiserWork(self):
        print("****** select a choice *******")
        while True:
            print("1.create event : \n2.Show all events : \n3.View event details : \n4.Update event : \n5.Delete event \n6.logout : ")
            selected = int(input("Enter the choice : "))
            if(selected == 1 ):
                self.createEvent()
            if(selected == 2 ):
                self.showAllEvents()
            if(selected == 3 ):
                self.showEventDetails()
            if(selected == 4 ):
                self.updateEvent()
            if(selected == 5 ):
                self.deleteEvent()
            if(selected == 6 ):
                print("Loged out successfully")
                return

    def showAllEvents(self):
        username = input("Enter userName : ")
        for event in self.events:
            if(event.get_organiser() == username):
                print("EventId : "+event.get_eventId()+ "    " + "eventName : "+event.get_name())
        return

    def showEventDetails(self):
        eventId = input("Enter eventId : ")
        for event in self.events:
            if(event.get_eventId() == eventId):
                print("EventId : "+event.get_eventId()+"\n"+"eventName : "+event.get_name()+"\n"+"startDate : "+event.get_startDate()+"\n"+"startTime : "+event.get_startTime()+"\n"+"endDate : "+event.get_endDate()+"\n"+"endTime : "+event.get_endTime()+"\n"+"seatAvailabe : "+event.get_seatAvailble()+"\n"+"registeredUserIds : "+str(event.get_registeredUserIds()))
        return

    def updateEvent(self):
        print("To update the event Provide information")
        eventId = input("Enter eventId : ")
        name = input("Enter new Name : ")
        startD = input("Enter new start date : ")
        startT = input("Enter new Start time : ")
        endD = input("Enter new end Date : ")
        endT = input("Enter new end Time : ")
        for event in self.events:
            if(event.get_eventId() == eventId):
                event.set_name(name)
                event.set_startDate(startD)
                event.set_startTime(startT)
                event.set_endDate(endD)
                event.set_endTime(endT)
        print("updated successufully")
        return

    def deleteEvent(self):
        eventId = input("Enter evnetId")
        for event in self.events:
            if(event.get_eventId() == eventId):
                self.events.remove(event)
        print("deleted successfully")
        return

    def createEvent(self):
        print("******** Please Create an Event ********")
        eventName = input("Enter Event name :")
        organizer = input("Enter userName : ")
        startdate = input("Enter Event startDate : ")
        starttime = input("Enter Event startTime : ")
        enddate = input("Enter Event endDate : ")
        endtime = input("Enter Event endTime")
        totalSeats = input("Enter Total seats : ")
        eventId = eventName+"_"+ organizer
        registeredUserIds = []
        event_obj = Event(eventId, eventName, organizer, startdate, starttime, enddate, endtime, totalSeats, registeredUserIds)
        self.events.append(event_obj)
        print("Successfully event created with eventId : "+eventId)
        return















while True:
    print("Enter the choice from the following : \n1.Add User : \n2.Login To the Application : \n3.Exit")
    choice = int(input("Enter the choice : "))
    if(choice != 1 and choice != 2):
        break
    user_profile_obj = user_profile()
    user_profile_obj.show(choice)