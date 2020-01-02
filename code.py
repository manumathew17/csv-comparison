import csv
count=0
starting_point=int(input("enter starting row"))
ending_point=int(input("enter ending row"))
with open(r"fille.csv")as f:
    data=csv.reader(f)
    for row in  data:
         if int(row[31])>=starting_point and int(row[31])<=ending_point:
             with open(r"average.csv") as f3:
                data2=csv.reader(f3)
                for i in data2:
                     
                     
                         if(row[3]==i[0]):
                             p1=row[0]
                             p2=row[1]
                             p29=row[2]
                             p3=row[3]
                             p4=row[4]
                             p5=row[5]
                             p6=i[0]
                             p7=i[1]
                             p8=i[2]
                             p9=i[3]
                             p10=i[4]
                             p11=i[5]
                             p12=i[6]
                             p13=i[7]
                             p14=i[8]
                             p15=i[9]
                             p16=i[10]
                             p17=i[11]
                             p18=i[12]
                             p19=i[13]
                             p20=i[14]
                             p21=i[15]
                             p22=i[16]
                             p23=i[17]
                             p24=i[18]
                             p25=i[19]
                             p26=i[20]
                             p27=i[21]
                             p28=i[22]
                             p29=i[23]
                             p30=i[24]
                             p31=i[25]
                             count=count+1
                             print(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p17,p18,p19,p20,p21,p22,p23,p24,p25)
                             with open(r"output8.csv","a",newline='' ) as f3:
                                 wtr = csv.writer(f3)
                                 wtr.writerows([[p1,p2,p29,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20,p21,p22,p23,p24,p25,p26,p27,p28,p29,p30,p31]])
print(count)
