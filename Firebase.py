import pyrebase
import time

firebaseConfig={"apiKey": "AIzaSyCVKuxaKPCSvtaHYN9EBq2d7-FxjfnRHKI",
    "authDomain": "wave-6f068.firebaseapp.com",
   "databaseURL": "https://wave-6f068-default-rtdb.firebaseio.com",
    "projectId": "wave-6f068",
    "storageBucket": "wave-6f068.appspot.com",
    "messagingSenderId": "69361873480",
    "appId": "1:69361873480:web:fca94b005074dca1239e7d",
    "measurementId": "G-Y0ZZBRPYF4"}
firebase=pyrebase.initialize_app(firebaseConfig)
db=firebase.database()
list1=[]
list2=[]
list3=[]
list4=[]
period=2021255000




while True:


    #period=2021255000

    for t1 in range(60):
        t=60-t1

        db.child("Time").child("Time").set(str(t))
        #time.sleep(0.5)
        if t==55:
            Users = db.child("Users").get()
            #print(Users.val())
            a=Users.val()
            print("===================================================================")

            for i in a:

                if a[i]["predict"]=="1":

                        price=a[i]["price"]
                        list1.append(int(price))


                #for i in a:

                if a[i]["predict"]=="2":

                        price=a[i]["price"]
                        list2.append(int(price))






            print(list1)
            print(list2)

            total=0
            total1=0



            for ele in range(0, len(list1)):
                  total = total + list1[ele]



            for ele1 in range(0, len(list2)):
                  total1 = total1 + list2[ele1]


            all=total+total1
            print(all)



            '''if total>total1 and total>total2:
                db.child("Result").child(period).set(str("2"))
                print("Price on 1 is high",total)
            if total1>total and total1>total2:
                db.child("Result").child(period).set(str("3"))
                print("price on 2 is high ",total1)
            if total2>total and total2>total1:
                db.child("Result").child(period).set(str("1"))
                print("price on 3 is high",total2)
                print("now")'''
            smallest = 0
            smallest1 = 0


            if total < total1 :
                smallest = total
                print("1")
                db.child("Result").child(period).set(str(1))
                for z in a:
                    #list4=[]
                    if a[z]["predict"] == "1":
                        contract= a[z]["price"]
                        intcontract=int(contract)
                        print(contract)

                        list4.append(int(z))
                        print(list4)
                for element in list4:
                   print("vbg")
                   #wallet=a[element]["wallet"]
                   wallet=db.child("Users").child(element).child("wallet").get().val()
                   intwallet=int(wallet)

                   intcontract=2*intcontract
                   newwallet=intcontract+intwallet
                   db.child("Users").child(element).child("wallet").set(str(newwallet))




            else:
                print("2")
                db.child("Result").child(period).set(str(2))
                for x in a:
                    #list4=[]
                    if a[x]["predict"] == "2":
                        contract= a[x]["price"]
                        intcontract=int(contract)
                        print(contract)

                        list4.append(int(x))
                        print(list4)
                for element in list4:
                    #wallet=a[element]["wallet"]
                    wallet=db.child("Users").child(element).child("wallet").get().val()
                    intwallet=int(wallet)

                    intcontract=2*intcontract
                    newwallet=intcontract+intwallet
                    db.child("Users").child(element).child("wallet").set(str(newwallet))







            #print(smallest, "less price on 3")
            #with open("prize1.csv","w") as f:
             #   f.write(f"{period},{all},{total},{total1},{total2},{total+total1-2*total2}")
            period=period+1
            list1.clear()
            list2.clear()

            list4.clear()
            print("===========================================================================")












