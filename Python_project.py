class station:
    def __init__(self,name):
        self.name=name
        self.readings=[]
        self.max_valid= 800
        self.safe_smoke=180
    def greet(self):
        print("Hi",self.name)
    def add_readings(self,value):
        self.readings.append(value)
        print(self.readings)
    def check(self,reading):
        if reading>self.max_valid:
            return "Bad"
        else:
            return"Good"
    def run(self):
        for r in self.readings:
            print(r,self.state(r))
    def act(self,reading):
        if reading>self.safe_smoke:
            return"Alarm"
        else:
            return"Safe"
    def state(self,reading):
        if self.check(reading)=="Bad":
            return "Rejected"
        else:
            return self.act(reading)
    

my_station = station("Remas' Station")
my_station.greet()
my_station.add_readings(100)
my_station.add_readings(300)
my_station.add_readings(600)
my_station.add_readings(900)
my_station.run()