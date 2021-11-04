print("Enter Marks Between 0 to 100 Obtained in 5 Subjects: ")
Math = int(input("Enter Marks Obtained in Math: "))
Eng = int(input("Enter Marks Obtained in English: "))
Bio = int(input("Enter Marks Obtained in Biology: "))
Sci = int(input("Enter Marks Obtained in 65: "))
Phy = int(input("Enter Marks Obtained in Physics: "))

tot = Math+Eng+Bio+Sci+Phy
avg = tot/5
percentage = (tot / 500.0) * 100

if avg>=91 and avg<=100:
    print("Your Grade is A* ", "Total Marks:", avg, " Overall: %", percentage)
elif avg>=81 and avg<91:
    print("Your Grade is A ", "Total Marks:", avg, " Overall: %", percentage)
elif avg>=71 and avg<81:
    print("Your Grade is B ", "Total Marks:", avg, " Overall: %", percentage)
elif avg>=61 and avg<71:
    print("Your Grade is C ", "Total Marks:", avg, " Overall: %", percentage)
elif avg>=51 and avg<61:
    print("Your Grade is D ", "Total Marks:", avg, " Overall: %", percentage)
elif avg>=41 and avg<51:
    print("Your Grade is E ", "Total Marks:", avg, " Overall: %", percentage)
elif avg>=33 and avg<41:
    print("Your Grade is F ", "Total Marks:", avg, " Overall: %", percentage)
elif avg>=0 and avg<33:
    print("Your Grade is G ", "Total Marks:", avg, " Overall: %", percentage, 
    "\nWhat the hell is this? Stop playing games!!!")
else:
    print("Invalid Input!")