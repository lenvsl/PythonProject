import pandas as pd
import numpy as np
import mysql.connector
import matplotlib.pyplot as plt

#Import CSV Files into Python using Pandas
df1 = pd.read_csv(r'C:\Users\vasil\Desktop\tour_occ_ninat_1_Data.csv')
df2 = pd.read_csv(r'C:\Users\vasil\Desktop\tour_occ_arnat_1_Data.csv')


#Nights spent at tourist accommodation establishments (df1)


#GREECE Total 2010-2013

#Select these columns.
df1 = df1[["GEO", "TIME", "C_RESID", "Value"]]

#Select country "Greece".
country_gr = df1[df1['GEO'].str.count('Greece')>0]
#print(country_gr)

#Select "Total".
country_gr.set_index("C_RESID", inplace = True)
res = country_gr.loc["Total"]
#print(res)

#Select years: 2010, 2011, 2012, 2013.
res.set_index(["TIME"], inplace = True)
time = res.loc["2010":"2013"]
#print(time)

#Remove ',' and ':'
time = time.apply(lambda x: x.str.replace(',',''))
time = time.apply(lambda x: x.str.replace(':','0'))
#print(time)

#Separate the years.
a = time.loc['2010']
#print(a)
b = time.loc['2011']
#print(b)
c = time.loc['2012']
#print(c)
d = time.loc['2013']
#print(d)


#ITALY Total 2010-2013

#Select country "Italy".
country_it = df1[df1['GEO'].str.count('Italy')>0]
#print(country_it)

#Select "Total".
country_it.set_index("C_RESID", inplace = True)
ttl = country_it.loc["Total"]
#print(ttl)

#Select years: 2010, 2011, 2012, 2013.
ttl.set_index(["TIME"], inplace = True)
tm = ttl.loc["2010":"2013"]
#print(tm)

#Remove ',' and ':'
tm = tm.apply(lambda x: x.str.replace(',',''))
tm = tm.apply(lambda x: x.str.replace(':','0'))
#print(tm)

ten = tm.loc['2010']
#print(ten)
elev = tm.loc['2011']
#print(elev)
twelv = tm.loc['2012']
#print(twelv)
thrt = tm.loc['2013']
#print(thrt)


#Nights spent by non-residents at tourist accommodation establishments (df1)


#GREECE Foreign country 2010-2013

frgn_c = country_gr.loc["Foreign country"]
#print(frgn_c)

frgn_c.set_index(["TIME"], inplace = True)
time_fr = frgn_c.loc["2010":"2013"]
#print(time_fr)

time_fr = time_fr.apply(lambda x: x.str.replace(',',''))
time_fr = time_fr.apply(lambda x: x.str.replace(':','0'))
#print(time_fr)

a_fr = time_fr.loc['2010']
#print(a_fr)
b_fr = time_fr.loc['2011']
#print(b_fr)
c_fr = time_fr.loc['2012']
#print(c_fr)
d_fr = time_fr.loc['2013']
#print(d_fr)


#ITALY Foreign country 2010-2013

frgn_it = country_it.loc["Foreign country"]
#print(frgn_it)

frgn_it.set_index(["TIME"], inplace = True)
tm_fr = frgn_it.loc["2010":"2013"]
#print(tm_fr)

tm_fr = tm_fr.apply(lambda x: x.str.replace(',',''))
tm_fr = tm_fr.apply(lambda x: x.str.replace(':','0'))
#print(tm_fr)

ten_fr = tm_fr.loc['2010']
#print(ten_fr)
elev_fr = tm_fr.loc['2011']
#print(elev_fr)
twelv_fr = tm_fr.loc['2012']
#print(twelv_fr)
thrt_fr = tm_fr.loc['2013']
#print(thrt_fr)

#Εξαγωγή αρχείων σε CSV
#time.to_csv (r'C:\Users\vasil\Desktop\Nights_GREECE_Total_2010_2013.csv', header=True)
#tm.to_csv (r'C:\Users\vasil\Desktop\Nights_ITALY_Total_2010_2013.csv', header=True)
#time_fr.to_csv (r'C:\Users\vasil\Desktop\Nights_GREECE_ForeignCountry_2010_2013.csv', header=True)
#tm_fr.to_csv (r'C:\Users\vasil\Desktop\Nights_ITALY_ForeignCountry_2010_2013.csv', header=True)


#Arrivals at tourist accommodation establishments (df2)


#GREECE Total 2010-2013

df2 = df2[["GEO", "TIME", "C_RESID", "Value"]]

arr_countr = df2[df2['GEO'].str.count('Greece')>0]
#print(arr_countr)

arr_countr.set_index("C_RESID", inplace = True)
t = arr_countr.loc["Total"]
#print(t)

t.set_index(["TIME"], inplace = True)
year = t.loc["2010":"2013"]
#print(year)

year = year.apply(lambda x: x.str.replace(',',''))
year = year.apply(lambda x: x.str.replace(':','0'))
#print(year)

dd = year.loc['2010']
#print(dd)
ee = year.loc['2011']
#print(ee)
ff = year.loc['2012']
#print(ff)
gg = year.loc['2013']
#print(gg)


#ITALY Total 2010-2013

itt = df2[df2['GEO'].str.count('Italy')>0]
#print(itt)

itt.set_index("C_RESID", inplace = True)
frr = itt.loc["Total"]
#print(frr)

frr.set_index(["TIME"], inplace = True)
tmm = frr.loc["2010":"2013"]
#print(tmm)

tmm = tmm.apply(lambda x: x.str.replace(',',''))
tmm = tmm.apply(lambda x: x.str.replace(':','0'))
#print(tmm)

tenn = tmm.loc['2010']
#print(tenn)
elevv = tmm.loc['2011']
#print(elevv)
twelvv = tmm.loc['2012']
#print(twelvv)
thrtt = tmm.loc['2013']
#print(thrtt)


#Arrivals of non-residents at tourist accommodation establishments (df2)


#GREECE Foreign country 2010-2013

arr_fr = arr_countr.loc["Foreign country"]
#print(arr_fr)

arr_fr.set_index(["TIME"], inplace = True)
year_fr = arr_fr.loc["2010":"2013"]
#print(year_fr)

year_fr = year_fr.apply(lambda x: x.str.replace(',',''))
year_fr = year_fr.apply(lambda x: x.str.replace(':','0'))
#print(year_fr)

dd_fr = year_fr.loc['2010']
#print(dd_fr)
ee_fr = year_fr.loc['2011']
#print(ee_fr)
ff_fr = year_fr.loc['2012']
#print(ff_fr)
gg_fr = year_fr.loc['2013']
#print(gg_fr)


#ITALY Foreign country 2010-2013

itt_fr = itt.loc["Foreign country"]
#print(itt_fr)

itt_fr.set_index(["TIME"], inplace = True)
tmm_fr = itt_fr.loc["2010":"2013"]
#print(tmm_fr)

tmm_fr = tmm_fr.apply(lambda x: x.str.replace(',',''))
tmm_fr = tmm_fr.apply(lambda x: x.str.replace(':','0'))
#print(time)

tenn_fr = tmm_fr.loc['2010']
#print(ttenn_fr)
elevv_fr = tmm_fr.loc['2011']
#print(elevv_fr)
twelvv_fr = tmm_fr.loc['2012']
#print(twelvv_fr)
thrtt_fr = tmm_fr.loc['2013']
#print(thrtt_fr)

#Εξαγωγή αρχείων σε CSV
#year.to_csv (r'C:\Users\vasil\Desktop\Arrivals_GREECE_Total_2010_2013.csv', header=True)
#tmm.to_csv (r'C:\Users\vasil\Desktop\Arrivals_ITALY_Total_2010_2013.csv', header=True)
#year_fr.to_csv (r'C:\Users\vasil\Desktop\Arrivals_GREECE_ForeignCountry_2010_2013.csv', header=True)
#tmm_fr.to_csv (r'C:\Users\vasil\Desktop\Arrivals_ITALY_ForeignCountry_2010_2013.csv', header=True)


#Converting specific Dataframe column to list
#NIGHTS

#GREECE Total 2010-2013
list1 = a["Value"].values.tolist()
list2 = b["Value"].values.tolist()
list3 = c["Value"].values.tolist()
list4 = d["Value"].values.tolist()
print('\nLISTS:\n')
print("Nights spent at tourist accommodation establishments (Greece):")
print("Converting Values GreeceTotal2010: to list:", list1)
print("Converting Values GreeceTotal2011: to list:", list2)
print("Converting Values GreeceTotal2012: to list:", list3)
print("Converting Values GreeceTotal2013: to list:", list4)
print("\nΑΘΡΟΙΣΜΑΤΑ:")
x1 = 0
for i in list1:
    x1 = x1 + float(i)
print(x1)

x2 = 0
for i in list2:
    x2 = x2 + float(i)
print(x2)

x3 = 0
for i in list3:
    x3 = x3 + float(i)
print(x3)

x4 = 0
for i in list4:
    x4 = x4 + float(i)
print(x4)

#GREECE Foreign country 2010-2013
list_1 = a_fr["Value"].values.tolist()
list_2 = b_fr["Value"].values.tolist()
list_3 = c_fr["Value"].values.tolist()
list_4 = d_fr["Value"].values.tolist()
print("\nNights spent by non-residents at tourist accommodation establishments (Greece):")
print("Converting Values GreeceForeign2010: to list:", list_1)
print("Converting Values GreeceForeign2011: to list:", list_2)
print("Converting Values GreeceForeign2012: to list:", list_3)
print("Converting Values GreeceForeign2013: to list:", list_4)
print("\nΑΘΡΟΙΣΜΑΤΑ:")
x_1 = 0
for i in list_1:
    x_1 = x_1 + float(i)
print(x_1)

x_2 = 0
for i in list_2:
    x_2 = x_2 + float(i)
print(x_2)

x_3 = 0
for i in list_3:
    x_3 = x_3 + float(i)
print(x_3)

x_4 = 0
for i in list_4:
    x_4 = x_4 + float(i)
print(x_4)

#ITALY Total 2010-2013
lista = ten["Value"].values.tolist()
listb = elev["Value"].values.tolist()
listc = twelv["Value"].values.tolist()
listd = thrt["Value"].values.tolist()
print("\nNights spent at tourist accommodation establishments (Italy):")
print("Converting Values ItalyTotal2010: to list:", lista)
print("Converting Values ItalyTotal2011: to list:", listb)
print("Converting Values ItalyTotal2012: to list:", listc)
print("Converting Values ItalyTotal2013: to list:", listd)
print("\nΑΘΡΟΙΣΜΑΤΑ:")
xa = 0
for i in lista:
    xa = xa + float(i)
print(xa)

xb = 0
for i in listb:
    xb = xb + float(i)
print(xb)

xc = 0
for i in listc:
    xc = xc + float(i)
print(xc)

xd = 0
for i in listd:
    xd = xd + float(i)
print(xd)

#ITALY Foreign country 2010-2013
list_a = ten_fr["Value"].values.tolist()
list_b = elev_fr["Value"].values.tolist()
list_c = twelv_fr["Value"].values.tolist()
list_d = thrt_fr["Value"].values.tolist()
print("\nNights spent by non-residents at tourist accommodation establishments (Italy):")
print("Converting Values ItalyForeign2010: to list:", list_a)
print("Converting Values ItalyForeign2011: to list:", list_b)
print("Converting Values ItalyForeign2012: to list:", list_c)
print("Converting Values ItalyForeign2013: to list:", list_d)
print("\nΑΘΡΟΙΣΜΑΤΑ:")
x_a = 0
for i in list_a:
    x_a = x_a + float(i)
print(x_a)

x_b = 0
for i in list_b:
    x_b = x_b + float(i)
print(x_b)

x_c = 0
for i in list_c:
    x_c = x_c + float(i)
print(x_c)

x_d = 0
for i in list_d:
    x_d = x_d + float(i)
print(x_d)


#ARRIVALS


#GREECE Total 2010-2013
list11 = dd["Value"].values.tolist()
list22 = ee["Value"].values.tolist()
list33 = ff["Value"].values.tolist()
list44 = gg["Value"].values.tolist()
print("\nArrivals at tourist accommodation establishments (Greece):")
print("Converting Values GreeceTotal2010: to list:", list11)
print("Converting Values GreeceTotal2011: to list:", list22)
print("Converting Values GreeceTotal2012: to list:", list33)
print("Converting Values GreeceTotal2013: to list:", list44)
print("\nΑΘΡΟΙΣΜΑΤΑ:")
x11 = 0
for i in list11:
    x11 = x11 + float(i)
print(x11)

x22 = 0
for i in list22:
    x22 = x22 + float(i)
print(x22)

x33 = 0
for i in list33:
    x33 = x33 + float(i)
print(x33)

x44 = 0
for i in list44:
    x44 = x44 + float(i)
print(x44)

#GREECE Foreign country 2010-2013
list_11 = dd_fr["Value"].values.tolist()
list_22 = ee_fr["Value"].values.tolist()
list_33 = ff_fr["Value"].values.tolist()
list_44 = gg_fr["Value"].values.tolist()
print("\nArrivals of non-residents at tourist accommodation establishments (Greece):")
print("Converting Values GreeceForeign2010: to list:", list_11)
print("Converting Values GreeceForeign2011: to list:", list_22)
print("Converting Values GreeceForeign2012: to list:", list_33)
print("Converting Values GreeceForeign2013: to list:", list_44)
print("\nΑΘΡΟΙΣΜΑΤΑ:")
x_11 = 0
for i in list_11:
    x_11 = x_11 + float(i)
print(x_11)

x_22 = 0
for i in list_22:
    x_22 = x_22 + float(i)
print(x_22)

x_33 = 0
for i in list_33:
    x_33 = x_33 + float(i)
print(x_33)

x_44 = 0
for i in list_44:
    x_44 = x_44 + float(i)
print(x_44)

#ITALY Total 2010-2013
listaa = tenn["Value"].values.tolist()
listbb = elevv["Value"].values.tolist()
listcc = twelvv["Value"].values.tolist()
listdd = thrtt["Value"].values.tolist()
print("\nArrivals at tourist accommodation establishments (Italy):")
print("Converting Values ItalyTotal2010: to list:", listaa)
print("Converting Values ItalyTotal2011: to list:", listbb)
print("Converting Values ItalyTotal2012: to list:", listcc)
print("Converting Values ItalyTotal2013: to list:", listdd)
print("\nΑΘΡΟΙΣΜΑΤΑ:")
xaa = 0
for i in listaa:
    xaa = xaa + float(i)
print(xaa)

xbb = 0
for i in listbb:
    xbb = xbb + float(i)
print(xbb)

xcc = 0
for i in listcc:
    xcc = xcc + float(i)
print(xcc)

xdd = 0
for i in listdd:
    xdd = xdd + float(i)
print(xdd)

#ITALY Foreign country 2010-2013
list_aa = tenn_fr["Value"].values.tolist()
list_bb = elevv_fr["Value"].values.tolist()
list_cc = twelvv_fr["Value"].values.tolist()
list_dd = thrtt_fr["Value"].values.tolist()
print("\nArrivals of non-residents at tourist accommodation establishments (Italy):")
print("Converting Values ItalyForeign2010: to list:", list_aa)
print("Converting Values ItalyForeign2011: to list:", list_bb)
print("Converting Values ItalyForeign2012: to list:", list_cc)
print("Converting Values ItalyForeign2013: to list:", list_dd)
print("\nΑΘΡΟΙΣΜΑΤΑ:")
x_aa = 0
for i in list_aa:
    x_aa = x_aa + float(i)
print(x_aa)

x_bb = 0
for i in list_bb:
    x_bb = x_bb + float(i)
print(x_bb)

x_cc = 0
for i in list_cc:
    x_cc = x_cc + float(i)
print(x_cc)

x_dd = 0
for i in list_dd:
    x_dd = x_dd + float(i)
print(x_dd)



#MYSQL


mydb = mysql.connector.connect(user="root", password="", host='localhost')
mycursor = mydb.cursor()
mycursor.execute('DROP DATABASE IF EXISTS db')
mycursor.execute("CREATE DATABASE db")
mydb = mysql.connector.connect(user="root", password="", host='localhost', database="db")

#Nights spent at tourist accommodation establishments

#GREECE

mycursor = mydb.cursor()
mycursor.execute("DROP TABLE IF EXISTS nightsgreecetotal")
mycursor.execute("CREATE TABLE nightsgreecetotal (Time INT(4), Geo VARCHAR(255), Value FLOAT(25))")

mycursor = mydb.cursor()
sql = "INSERT INTO nightsgreecetotal (Time, Geo, Value) VALUES (%s, %s, %s)"
val = [("2010", "Greece", "186768309.98"), ("2011", "Greece", "193301650.45000002"), ("2012", "Greece", "178653208.04"), ("2013", "Greece", "197259655.98")]
mycursor.executemany(sql, val)
mydb.commit()
print('\nSQL:\n')

mycursor = mydb.cursor()
mycursor.execute("SELECT Time, Geo, Value FROM nightsgreecetotal")
myresult1 = mycursor.fetchall()
print('Nights spent at tourist accommodation establishments, for Greece:')
for y1 in myresult1:
    print(y1)


#ITALY

mycursor = mydb.cursor()
mycursor.execute("DROP TABLE IF EXISTS nightsitalytotal")
mycursor.execute("CREATE TABLE nightsitalytotal (Time INT(4), Geo VARCHAR(255), Value FLOAT(25))")

mycursor = mydb.cursor()
sql = "INSERT INTO nightsitalytotal (Time, Geo, Value) VALUES (%s, %s, %s)"
val = [("2010", "Italy", "875536869.1399999"), ("2011", "Italy", "900781257.9999999"), ("2012", "Italy", "886532073.2199999"), ("2013", "Italy", "875605147.7")]
mycursor.executemany(sql, val)
mydb.commit()
print('\n')

mycursor = mydb.cursor()
mycursor.execute("SELECT Time, Geo, Value FROM nightsitalytotal")
myresult2 = mycursor.fetchall()
print('Nights spent at tourist accommodation establishments, for Italy:')
for y2 in myresult2:
    print(y2)


#Nights spent by non-residents at tourist accommodation establishments

#GREECE

mycursor = mydb.cursor()
mycursor.execute("DROP TABLE IF EXISTS nightsgreeceforeign")
mycursor.execute("CREATE TABLE nightsgreeceforeign (Time INT(4), Geo VARCHAR(255), Value FLOAT(25))")

mycursor = mydb.cursor()
sql = "INSERT INTO nightsgreeceforeign (Time, Geo, Value) VALUES (%s, %s, %s)"
val = [("2010", "Greece", "127236365.27"), ("2011", "Greece", "140205446.8"), ("2012", "Greece", "132623672.95"), ("2013", "Greece", "149919791.54000002")]
mycursor.executemany(sql, val)
mydb.commit()
print('\n')

mycursor = mydb.cursor()
mycursor.execute("SELECT Time, Geo, Value FROM nightsgreeceforeign")
myresult3 = mycursor.fetchall()
print('Nights spent by non-residents at tourist accommodation establishments, for Greece:')
for y3 in myresult3:
    print(y3)

#ITALY

mycursor = mydb.cursor()
mycursor.execute("DROP TABLE IF EXISTS nightsitalyforeign")
mycursor.execute("CREATE TABLE nightsitalyforeign (Time INT(4), Geo VARCHAR(255), Value FLOAT(25))")

mycursor = mydb.cursor()
sql = "INSERT INTO nightsitalyforeign (Time, Geo, Value) VALUES (%s, %s, %s)"
val = [("2010", "Italy", "384056026.07000005"), ("2011", "Italy", "409408234.85999995"), ("2012", "Italy", "419084682.7"), ("2013", "Italy", "428049914.8")]
mycursor.executemany(sql, val)
mydb.commit()
print('\n')

mycursor = mydb.cursor()
mycursor.execute("SELECT Time, Geo, Value FROM nightsitalyforeign")
myresult4 = mycursor.fetchall()
print('Nights spent by non-residents at tourist accommodation establishments, for Italy:')
for y4 in myresult4:
    print(y4)


#Arrivals at tourist accommodation establishments

#GREECE

mycursor = mydb.cursor()
mycursor.execute("DROP TABLE IF EXISTS arrivalsgreecetotal")
mycursor.execute("CREATE TABLE arrivalsgreecetotal (Time INT(4), Geo VARCHAR(255), Value FLOAT(25))")

mycursor = mydb.cursor()
sql = "INSERT INTO arrivalsgreecetotal (Time, Geo, Value) VALUES (%s, %s, %s)"
val = [("2010", "Greece", "44508442.70999999"), ("2011", "Greece", "45359471.43000001"), ("2012", "Greece", "40134783.7"), ("2013", "Greece", "44336865.70999999")]
mycursor.executemany(sql, val)
mydb.commit()
print('\n')

mycursor = mydb.cursor()
mycursor.execute("SELECT Time, Geo, Value FROM arrivalsgreecetotal")
myresult11 = mycursor.fetchall()
print('Arrivals at tourist accommodation establishments, for Greece:')
for y11 in myresult11:
    print(y11)

#ITALY

mycursor = mydb.cursor()
mycursor.execute("DROP TABLE IF EXISTS arrivalsitalytotal")
mycursor.execute("CREATE TABLE arrivalsitalytotal (Time INT(4), Geo VARCHAR(255), Value FLOAT(25))")

mycursor = mydb.cursor()
sql = "INSERT INTO arrivalsitalytotal (Time, Geo, Value) VALUES (%s, %s, %s)"
val = [("2010", "Italy", "217067400.35999998"), ("2011", "Italy", "228115866.20999998"), ("2012", "Italy", "228554692.75"), ("2013", "Italy", "228948354.6")]
mycursor.executemany(sql, val)
mydb.commit()
print('\n')

mycursor = mydb.cursor()
mycursor.execute("SELECT Time, Geo, Value FROM arrivalsitalytotal")
myresult22 = mycursor.fetchall()
print('Arrivals at tourist accommodation establishments, for Italy:')
for y22 in myresult22:
    print(y22)


#Arrivals of non-residents at tourist accommodation establishments

#GREECE

mycursor = mydb.cursor()
mycursor.execute("DROP TABLE IF EXISTS arrivalsgreeceforeign")
mycursor.execute("CREATE TABLE arrivalsgreeceforeign (Time INT(4), Geo VARCHAR(255), Value FLOAT(25))")

mycursor = mydb.cursor()
sql = "INSERT INTO arrivalsgreeceforeign (Time, Geo, Value) VALUES (%s, %s, %s)"
val = [("2010", "Greece", "23980309.040000003"), ("2011", "Greece", "26674961.509999998"), ("2012", "Greece", "24447526.86"), ("2013", "Greece", "27758142.39")]
mycursor.executemany(sql, val)
mydb.commit()
print('\n')

mycursor = mydb.cursor()
mycursor.execute("SELECT Time, Geo, Value FROM arrivalsgreeceforeign")
myresult33 = mycursor.fetchall()
print('Arrivals of non-residents at tourist accommodation establishments, for Greece:')
for y33 in myresult33:
    print(y33)

#ITALY

mycursor = mydb.cursor()
mycursor.execute("DROP TABLE IF EXISTS arrivalsitalyforeign")
mycursor.execute("CREATE TABLE arrivalsitalyforeign (Time INT(4), Geo VARCHAR(255), Value FLOAT(25))")

mycursor = mydb.cursor()
sql = "INSERT INTO arrivalsitalyforeign (Time, Geo, Value) VALUES (%s, %s, %s)"
val = [("2010", "Italy", "96362622.68999998"), ("2011", "Italy", "104398833.64"), ("2012", "Italy", "107348223.40999998"), ("2013", "Italy", "110800540.9")]
mycursor.executemany(sql, val)
mydb.commit()
print('\n')

mycursor = mydb.cursor()
mycursor.execute("SELECT Time, Geo, Value FROM arrivalsitalyforeign")
myresult44 = mycursor.fetchall()
print('Arrivals of non-residents at tourist accommodation establishments, for Italy:')
for y44 in myresult44:
    print(y44)


#Matplot


#NIGHTS Greece-Italy Total

# width of the bars
barWidth = 0.4

# Choose the height of the blue bars
bars1 = [x1, x2, x3, x4]

# Choose the height of the cyan bars
bars2 = [xa, xb, xc, xd]

# Choose the height of the error bars (bars1)
yer1 = [0.5, 0.4, 0.5, 0.4]

# Choose the height of the error bars (bars2)
yer2 = [1, 0.7, 1, 0.7]

# The x position of bars
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]

# Create blue bars
plt.bar(r1, bars1, width=barWidth, color='darkblue', edgecolor='black', yerr=yer1, capsize=7, label='Greece')

# Create cyan bars
plt.bar(r2, bars2, width=barWidth, color='seagreen', edgecolor='black', yerr=yer2, capsize=7, label='Italy')

# general layout
plt.xticks([r + barWidth for r in range(len(bars1))], ['2010', '2011', '2012', '2013'])
plt.title('Nights spent at tourist accommodation establishments')
plt.ylabel('Value')
plt.xlabel('Time')
plt.legend()

# Show graphic
plt.show()

#NIGHTS Greece-Italy Foreign

bars_1 = [x_1, x_2, x_3, x_4]
bars_2 = [x_a, x_b, x_c, x_d]

r_1 = np.arange(len(bars_1))
r_2 = [x + barWidth for x in r_1]

plt.bar(r_1, bars_1, width=barWidth, color='darkblue', edgecolor='black', yerr=yer1, capsize=7, label='Greece')
plt.bar(r_2, bars_2, width=barWidth, color='seagreen', edgecolor='black', yerr=yer2, capsize=7, label='Italy')

plt.xticks([r + barWidth for r in range(len(bars_1))], ['2010', '2011', '2012', '2013'])
plt.title('Nights spent by non-residents at tourist accommodation establishments')
plt.ylabel('Value')
plt.xlabel('Time')
plt.legend()

plt.show()


#ARRIVALS Greece-Italy Total

bars11 = [x11, x22, x33, x44]
bars22 = [xaa, xbb, xcc, xdd]

r11 = np.arange(len(bars11))
r22 = [x + barWidth for x in r11]

plt.bar(r11, bars11, width=barWidth, color='darkblue', edgecolor='black', yerr=yer1, capsize=7, label='Greece')
plt.bar(r22, bars22, width=barWidth, color='seagreen', edgecolor='black', yerr=yer2, capsize=7, label='Italy')

plt.xticks([r + barWidth for r in range(len(bars11))], ['2010', '2011', '2012', '2013'])
plt.title('Arrivals at tourist accommodation establishments')
plt.ylabel('Value')
plt.xlabel('Time')
plt.legend()
plt.show()

#ARRIVALS Greece-Italy Foreign

bars_11 = [x_11, x_22, x_33, x_44]
bars_22 = [x_aa, x_bb, x_cc, x_dd]

r_11 = np.arange(len(bars_11))
r_22 = [x + barWidth for x in r_11]

plt.bar(r_11, bars_11, width=barWidth, color='darkblue', edgecolor='black', yerr=yer1, capsize=7, label='Greece')
plt.bar(r_22, bars_22, width=barWidth, color='seagreen', edgecolor='black', yerr=yer2, capsize=7, label='Italy')

plt.xticks([r + barWidth for r in range(len(bars_11))], ['2010', '2011', '2012', '2013'])
plt.title('Arrivals of non-residents at tourist accommodation establishments')
plt.ylabel('Value')
plt.xlabel('Time')
plt.legend()
plt.show()

