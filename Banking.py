import mysql.connector as mysql
import hashlib

class bankk:

    def __init__(Self):
        print(" Hello to  Bank ")

    def insert(self):

        db = mysql.connect(host = "localhost" , user = "root" ,passwd="" , database = "bank")
        myscursor = db.cursor()
        myscursor.execute("SELECT * FROM bank ") 

        rr = myscursor.fetchone()

        if not rr:

            pre_hash = 0

            S_name = input(" Enter your name :- ")
            sender_acccount = int(input(" Enter  your account no. :- "))
            R_name = input(" Enter Receiver name :- ")
            reciver_account = int(input(" Enter Reciver account no. :- "))

            if sender_acccount == reciver_account :
                raise Exception(".... You can't do the self transcation !!!!!!")

            amount = int(input(" Enter the amount :- "))

            res = (pre_hash , S_name , sender_acccount , R_name , reciver_account , amount)

            crt = hashlib.sha256(str(res).encode("utf-8")).hexdigest()

            #print(crt)

            db1 = mysql.connect(host = "localhost" , user = "root" ,passwd="" , database = "bank")
            myscursor1 = db1.cursor()
            myscursor1.execute("INSERT INTO bank(pre_hash , Sender_account  ,  Reciver_accunt  , Amount , curr_hash , S_name , R_name) values (%s , %s ,%s ,%s ,%s)", 
                            (
                                pre_hash,
                                sender_acccount,
                                reciver_account,
                                amount,
                                crt,
                                S_name,
                                R_name,
                            )
                            )

            db1.commit()
            db1.close()
            print("The transection done ...................")

        else:
                db2 = mysql.connect(host = "localhost" , user = "root" ,passwd="" , database = "bank")
                myscursor2 = db2.cursor()
                myscursor2.execute("SELECT curr_hash FROM bank ORDER BY ID LIMIT 1")
                rrr = myscursor2.fetchone() 

                data = rrr[0]

                S_name = input(" Enter your name :- ")
                sender_acccount1 = int(input(" Enter  your account no. "))
                R_name = input(" Enter Receiver name :- ")
                reciver_account1 = int(input(" Enter Reciver account no. "))

                if sender_acccount1 == reciver_account1 :
                    raise Exception(".... You can't do the self transcation !!!!!!")

                amount1 = int(input(" Enter the amount :- "))

                ress = (data , S_name ,  sender_acccount1 , reciver_account1 , amount1)

                crtt = hashlib.sha256(str(ress).encode("utf-8")).hexdigest()

                db3 = mysql.connect(host = "localhost" , user = "root" ,passwd="" , database = "bank")
                myscursor3 = db3.cursor()
                myscursor3.execute("INSERT INTO bank(pre_hash ,  Sender_account  , Reciver_accunt  , Amount , curr_hash , S_name , R_name) values (%s , %s ,%s ,%s ,%s)", 
                                (
                                    data,
                                    sender_acccount1,
                                    reciver_account1,
                                    amount1,
                                    crtt,
                                    S_name,
                                    R_name,
                                )
                                )

                db3.commit()
                db3.close()
                print("The transection done ...................")


b = bankk()
b.insert()



