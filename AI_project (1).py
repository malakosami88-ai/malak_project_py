class companion:
    def __init__(self,name):
        self.name= name
        self.readings=[]
        self.examples={45:"Normal",52:"Normal",48:"Normal",95:"Unusual",88:"Unusual"}
    def classify(self,reading):
        closest=min(self.examples,key=lambda x:abs(x-reading))
        return self.examples[closest]
test = [(55, "unusual"), (91, "Unusual"), (47, "Normal"),(100, "Unusual"), (55, "Normal")]
my_companion=companion("Mr Bigo")
sum=0
for Q,A in test:
    if my_companion.classify(Q)==A:
        sum+=1
    else:
        print("The question:",Q)
        print("The wrong answer:",my_companion.classify(Q))
        print("Right answer:",A)
accuracy =sum/len(test)*100
print("Accuracy=",accuracy,"%")
value =80
result= my_companion.classify(value)
print(result)
if result =="Unusual":
    my_companion.readings.append(value)
print(my_companion.readings)
