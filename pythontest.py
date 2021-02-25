"""val =100
print (val)

#value = input("Enter value: ")

#if value > 95 :
   #print ("student is good")
#elif value < 35:
	#print ("student fail")
#else:
	#print ("student moderate")


list1=['mouth','tongue','teeth','jaw']
print list1
print list1[2:3]
print list1[3:]
list1.append('nose')
for x in list1:
	print x
print list1


dict1 = {'Name' : 'Williams','Age' : 47 ,'Country' : 'Newzland' , 'Occupetion' : 'Cricket'}
dict2= {'Battingtype' : 'Right-hand', 'Bowling': 'None'}
dict3 = {'Name' : 'Kohli','Age' : 39 ,'Country' : 'India' , 'Occupetion' : 'Cricket'}

dict4=dict2.copy()

seq = ('name', 'age', 'sex')
dict = dict.fromkeys(seq)
print "New Dictionary : %s" %  str(dict)

dict = dict.fromkeys(seq, 10)
print "New Dictionary : %s" %  str(dict)

print "Compare %d" % cmp (dict1 , dict2)
print "Value %d" % cmp (dict2 , dict3)

print "Length of dictonary %d" % len(dict1)
print "String %s" % str(dict1)
print "Type %s" % type(dict1)
print "Copy of dictonary %s" % str(dict4)

print "Value : %s" %  dict1.get('Age')
print "Value : %s" %  dict2.get('Education', "Never")

print "Has key : %s" % dict1.has_key('Name')
print "Has key : %s" % dict1.has_key('SEX')

print "Items : %s" % dict2.items()
print "KEYS : %s" % dict3.keys()
dict2.update(dict3)
print "UPDaTE : %s" % dict2

import time;

localtime = time.localtime(time.time())
print "Local current time :", localtime

localtime = time.asctime (time.localtime(time.time()))
print "Local current time :", localtime


import calendar

cal =calendar.month(2021,2)
print cal


var1 = 'Hello World!'
print "Updated String :- ", var1[:6] + 'Python'"""

from string import maketrans 
import time
import calendar

string1= u"7895636"

print string1


print string1.isdecimal()

string2= "merry weds someone who is not her neighbour"

print string2.zfill(45)
print len(string2)
print string2.upper()

str3= "dogs"
str4="1234"
transtab = maketrans(str3 , str4)
print string2.translate(transtab,'ne')
print string2.title()

string5 = "UPPER CASE"
string6="lower case"

print string5.swapcase()
print string6.swapcase()
print string5.strip('P')
print string2.split('Merry',1)

string7= "this is string example....wow!!!"
string8= "is"

print string7.rindex(string8)
print string7.index(string8)

str = "this is string example....wow!!! this is really string"
print str.replace("is", "was")
print str.replace("is", "was", 1)

s = "**";
seq = ("a", "b", "c"); # This is sequence of strings.
print s.join( seq )

print string2.islower()

#ticks=time.time()
#print ticks

localtime = time.localtime(time.time())
print localtime
localtime1 = time.asctime(time.localtime(time.time()))
print localtime1
print "time.altzone %d " % time.altzone

def procedure():
	time.sleep(2)

"""t0 = time.clock()
procedure()
print time.clock()

t0 = time.time()
procedure()
print "Wall time", time.time() - t0"""

print "time.ctime() : %s" % time.ctime(2)
print "time.gmtime() : %s" % time.gmtime()
print "time.localtime() : %s" % time.localtime()

t = (2009, 3, 17, 17, 5, 38, 1, 28, 0)
secs = time.mktime( t )
print "time.mktime(t) : %f" %  secs
print "asctime(localtime(secs)): %s" % time.asctime(time.localtime(secs))

print "Start : %s" % time.ctime()
time.sleep( 0 )
print "End : %s" % time.ctime()

t = (2009, 11, 19, 1, 3, 56, 2, 48, 0)
t = time.mktime(t)
print time.strftime("%B %d %Y %H:%M:%S", time.gmtime(t))

"""year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
print calendar.isleap(year)
print calendar.calendar(year,w=2,l=1,c=6)
print calendar.firstweekday()
print calendar.leapdays(1992,2021)
print calendar.month(year,month,w=2,l=1)
print calendar.monthcalendar(year,month)
print calendar.monthrange(year,month)"""


def calling_fun(s):
	print s
	return

calling_fun(2)
calling_fun(5)

def calling_ref(g):
	g=9
	print "Old new", g
	return
g=10
calling_ref(g)
print "new value",g






#print calendar.setfirstweekday(6)
#print calendar.prcal(year,w=2,l=1,c=6)
#print calendar.prmonth(year,month,w=2,l=1)


"""if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))"""

  