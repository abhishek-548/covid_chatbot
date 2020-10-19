import requests
from datetime import datetime
hour = datetime.now()
import webbrowser
url = "https://kidshealth.org/en/parents/coronavirus-stop-spread.html"
# top border
for _ in range(40):
    print(" ",end=" ")
print("........")
print("")
#middle content
for _ in range(40):
    print(" ",end=" ")
print("CODEFORCES BOT!..")
#bottom border
for _ in range(40):
    print(" ",end=" ")
print("........")
#Content
grt=""
print("Welcome to codeforces bot")
print("")
h = hour.hour
if h<12:
    grt="Good Morning!"
elif h>=12 and h<17:
    grt="Good Afternoon!"
else:
    grt="Good Evening!"
name=input("Enter your sweet name : ")
print("")
print("Hi {} {} ,Iam your covid chatbot I hope you are healthy \nI can help you in providing the covid-19 statistics across world and in India and provide precautions for it ".format(grt,name))
print("")

#main
resp = requests.get("https://api.apify.com/v2/key-value-stores/toDWvRj1JpTXiM8FF/records/LATEST?disableRedirect=true")
resp1 = requests.get("https://coronavirus-19-api.herokuapp.com/countries")

print("1.) Covid-19 statistics Around the world\n2.)Covid-19 statistics In India\n3.)Covid-19 precautions\n4.)End the chat")
print("")

while True:
  var=int(input("which statistics you want to choose  : "))
  #In world 
  if var==1:
    country=input("Enter the country you want : ")
    details=int(input("Do you want to know any particular details or whole info : \n1.)Total Info\n2.)Particular info  "))
    if details == 1:
      for i in range(len(resp1.json())):
        if resp1.json()[i].get("country")==country:
          print("Total number of active cases in {} is {}".format(country,resp1.json()[i].get("cases")))
          print("Total number of new active cases in {} is {}".format(country,resp1.json()[i].get("todayCases")))
          print("Total number of recovered cases in {} is {}".format(country,resp1.json()[i].get("recovered")))
          print("Total number of deaths in {} is {}".format(country,resp1.json()[i].get("deaths")))
          print("Total number of new deaths in {} is {}".format(country,resp1.json()[i].get("todayDeaths")))
    elif details == 2:
      print('which info you want : \n1.)Total no.of active cases\n2.)Total no.of new active cases\n3.)Total no.of recovered cases\n4.)Total no.of deaths\n5.)Total no.of new deaths')
      countdetail=int(input("Enter your choice : "))
      if countdetail==1:
        for i in range(len(resp1.json())):
            if resp1.json()[i].get("country")==country:
              print("Total no.of active cases in {} is : {}".format(country,resp1.json()[i].get("cases")))
      if countdetail==2:
        for i in range(len(resp1.json())):
            if resp1.json()[i].get("country")==country:
              print("Total no.of new active cases in {} is : {}".format(country,resp1.json()[i].get("todayCases")))
      if countdetail==3:
        for i in range(len(resp1.json())):
            if resp1.json()[i].get("country")==country:
              print("Total no.of recovered cases in {} is : {}".format(country,resp1.json()[i].get("recovered")))
      if countdetail==4:
        for i in range(len(resp1.json())):
            if resp1.json()[i].get("country")==country:
              print("Total no.of deaths in {} is : {}".format(country,resp1.json()[i].get("deaths")))
      if countdetail==4:
        for i in range(len(resp1.json())):
            if resp1.json()[i].get("country")==country:
              print("Total no.of new deaths in {} is : {}".format(country,resp1.json()[i].get("todayDeaths")))

  
  if var==2:
    state=input("Do you want to know covid-19 statistics about any particular state or whole India?  ")
    if state=="India":
      det=int(input("Do you want to know any particular details or whole info : \n1.)Total Info\n2.)Particular info  "))
      if det==1:
				#Total no.active cases
        print("Total number of active cases in India : ",resp.json().get("activeCases"))
				#total no.of actibe cases new
        print("Total number of new active cases in India : ",resp.json().get("activeCasesNew"))
				#total recovered
        print("Total number of recovered cases in India : ",resp.json().get("recovered"))
				#total recovered new
        print("Total number of new recovered cases in India : ",resp.json().get("recoveredNew"))
				#total no.of deaths
        print("Total number of deaths cases in India : ",resp.json().get("deaths"))
      if det==2:
        print('which info you want : \n1.)Total no.of active cases\n2.)Total no.of new active cases\n3.)Total no.of recovered cases\n4.)Total no.of new recovered cases\n5.)Total no.ofdeaths')
        particinfo=int(input("Choose your particular info : "))
        if particinfo==1:
          print("Total no.of active cases : ",resp.json().get("activeCases"))
        if particinfo==2:
          print("Total no.of new active cases : ",resp.json().get("activeCasesNew"))
        if particinfo==3:
          print("Total no.of recovered cases : ",resp.json().get("recovered"))
        if particinfo==4:
          print("Total no.of new recovered cases : ",resp.json().get("recoveredNew"))
        if particinfo==5:
          print("Total no.of recovered cases : ",resp.json().get("deaths"))
    else:
      detail=int(input("Do you want to know any particular details or whole info : \n1.)Total Info\n2.)Particular info  "))
      if detail==1:
        for i in range(len(resp.json().get("regionData"))):
          if resp.json().get("regionData")[i].get("region")==state:
						#total infectedcases in state
            print("Total no.of Infected cases in {}  is : {}".format(state,resp.json().get("regionData")[i].get("totalInfected")))
						#total infectedcasesnew
            print("Total no.of New Infected cases in {}  is : {}".format(state,resp.json().get("regionData")[i].get("newInfected")))
						#total recovered cases
            print("Total no.of recovered cases in {}  is : {}".format(state,resp.json().get("regionData")[i].get("recovered")))
						#total new recovered cases
            print("Total no.of new recovered cases in {}  is : {}".format(state,resp.json().get("regionData")[i].get("newRecovered")))
						#total no.of detahs
            print("Total no.of deaths in {}  is : {}".format(state,resp.json().get("regionData")[i].get("deceased")))
      else:
        print('which info you want : \n1.)Total no.of active cases\n2.)Total no.of new active cases\n3.)Total no.of recovered cases\n4.)Total no.of new recovered cases\n5.)Total no.ofdeaths')
        particinfo1=int(input("Choose your particular info : "))
        if particinfo1==1:
          for i in range(len(resp.json().get("regionData"))):
            if resp.json().get("regionData")[i].get("region")==state:
              print("Total no.of active cases in {} is : {}".format(state,resp.json().get
              ("regionData")[i].get("totalInfected")))
        if particinfo1==2:
          for i in range(len(resp.json().get("regionData"))):
            if resp.json().get("regionData")[i].get("region")==state:
              print("Total no.of new active cases in {} is : {}".format(state,resp.json().get("regionData")[i].get("newInfected")))
        if particinfo1==3:
          for i in range(len(resp.json().get("regionData"))):
            if resp.json().get("regionData")[i].get("region")==state:
              print("Total no.of active cases in {} is : {}".format(state,resp.json().get("regionData")[i].get("recovered")))
        if particinfo1==4:
          for i in range(len(resp.json().get("regionData"))):
            if resp.json().get("regionData")[i].get("region")==state:
              print("Total no.of new active cases in {} is : {}".format(state,resp.json().get("regionData")[i].get("newRecovered")))
        if particinfo1==5:
          for i in range(len(resp.json().get("regionData"))):
            if resp.json().get("regionData")[i].get("region")==state:
              print("Total no.of new active cases in {} is : {}".format(state,resp.json().get("regionData")[i].get("deceased")))
  if var==3:
    webbrowser.open(url, new=2)
  if var==4:
    print("Thanks for using our chatbot\n<<<<<<<<Stay Home Stay Safe>>>>>>>>")
    exit()