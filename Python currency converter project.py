'''Name:-Sachin Kumar
Section:K22PK
roll No.86'''
#WELCOME TO OUR CURRECNY CONVERTER:-
def display_menu():
  print("1. Convert INR to Afghan Afghani(AFN)")
  print("2. Convert INR to Albanian Lek (ALL)")
  print("3. Convert INR to Australian Dollar(AUD)")
  print("4. Convert INR to Bahamian Dollar(BSD)")
  print("5. Convert INR to Bangladeshi Taka(BDT)")
  print("6. Convert INR to Bhutan currency(BTN)")
  print("7. Convert INR to Brazilian Real(BRL)")
  print("8. Convert INR to Canadian Dollar(CAD)")
  print("9. Convert INR to Chinese Yuan(CNY)")
  print("10. Convert INR to Euro(EUR)")
  print("11. Convert INR to Egyptian Pound(EGP)")
  print("12. Convert INR to Hong Kong Dollar(HKD)")
  print("13. Convert INR to Indonesian Rupiah(IDR)")
  print("14. Convert INR to Japenese Yen(JPY)")
  print("15. Convert INR to Mauritian Rupee(MUR)")
  print("16. Convert INR to Nepalese Rupee(NPR)")
  print("17. Convert INR to New Zealand Dollar(NZD)")
  print("18. Convert INR to Pakistani Rupee(PKR)")
  print("19. Convert INR to Phillipine peso(PHP)")
  print("20. Convert INR to Russian Ruble(RUB)")
  print("21. Convert INR to United Arab Emirates Dirham(AED)")
  print("22. Convert INR to United States Dollar(USD)")
  print("23. Convert INR to Swiss Franc(CHF)")
  print("24. Convert INR to West African CFA franc(XOF)")


def INR_to_AFN(value):
  return value*1.07
def INR_to_ALL(value):
  return value*1.38
def INR_to_AUD(value):
  return value*0.018
def INR_to_BSD(value):
  return value*0.012
def INR_to_BDT(value):
  return value*1.30
def INR_to_BTN(value):
  return value*1.00
def INR_to_BRL(value):
  return value*0.066
def INR_to_CAD(value):
  return value*0.016
def INR_to_CNY(value):
  return value*0.088
def INR_to_EUR(value):
  return value*0.012
def INR_to_EGP(value):
  return value*0.30
def INR_to_HKD(value):
  return value*0.096
def INR_to_IDR(value):
  return value*192.99
def INR_to_JPY(value):
  return value*1.70
def INR_to_MUR(value):
  return value*0.54
def INR_to_NPR(value):
  return value*1.60
def INR_to_NZD(value):
  return value*0.020
def INR_to_PKR(value):
  return value*2.75
def INR_to_PHP(value):
  return value*0.69
def INR_to_RUB(value):
  return value*0.75
def INR_to_AED(value):
  return value*0.045
def INR_to_USD(value):
  return value*0.012
def INR_to_CHF(value):
  return value*0.012
def INR_to_XOF(value):
  return value*7.75
while True:
  display_menu()
  choice=int(input())
  if choice==5:
    print("Bye!")
    break
  else:
    amount=float(input("Enter an amount in Indian Rupees: "))
    if choice==1:
      print(amount,"INR",INR_to_AFN(amount),"AFN")
    elif choice==2:
      print(amount,"INR",INR_to_ALL(amount),"ALL")
    elif choice==3:
      print(amount,"INR",INR_to_AUD(amount),"AUD")
    elif choice==4:
      print(amount,"INR",INR_to_BSD(amount),"BSD")
    elif choice==5:
      print(amount,"INR",INR_to_BDT(amount),"BDT")
    elif choice==6:
      print(amount,"INR",INR_to_BTN(amount),"BTN")
    elif choice==7:
      print(amount,"INR",INR_to_BRL(amount),"BRL")
    elif choice==8:
      print(amount,"INR",INR_to_CAD(amount),"CAD")
    elif choice==9:
      print(amount,"INR",INR_to_CNY(amount),"CNY")
    elif choice==10:
      print(amount,"INR",INR_to_EUR(amount),"EUR")
    elif choice==11:
      print(amount,"INR",INR_to_EGP(amount),"EGP")
    elif choice==12:
      print(amount,"INR",INR_to_HKD(amount),"HKD")
    elif choice==13:
      print(amount,"INR",INR_to_IDR(amount),"IDR")
    elif choice==14:
      print(amount,"INR",INR_to_JPY(amount),"JPY")
    elif choice==15:
      print(amount,"INR",INR_to_MUR(amount),"MUR")
    elif choice==16:
      print(amount,"INR",INR_to_NPR(amount),"NPR")
    elif choice==17:
      print(amount,"INR",INR_to_NZD(amount),"NZD")
    elif choice==18:
      print(amount,"INR",INR_to_PKR(amount),"PKR")
    elif choice==19:
      print(amount,"INR",INR_to_PHP(amount),"PHP")
    elif choice==20:
      print(amount,"INR",INR_to_RUB(amount),"RUB")
    elif choice==21:
      print(amount,"INR",INR_to_AED(amount),"AED")
    elif choice==22:
      print(amount,"INR",INR_to_USD(amount),"USD")
    elif choice==23:
      print(amount,"INR",INR_to_CHF(amount),"CHF")
    elif choice==24:
      print(amount,"INR",INR_to_XOF(amount),"XOF")
    else:
        print("PLEASE ENTER GIVEN CHOICES")
