list = ["1", "2", "3", "4", "5", "6", "156"]
even = []
odd = []
outlier = []
for i in list:
    if int(i) > 100:
        outlier.append(i)
    elif int(i)%2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Even Numbers: ", even)
print("Odd Numbers: ", odd)
print("Outliers: ", outlier)

