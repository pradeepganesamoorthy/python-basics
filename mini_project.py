jack = { "name":"Jack Frost",
         "assignment" : [80, 50, 40, 20],
         "test" : [75, 75],
         "lab" : [78.20, 77.20]
       }

james = { "name":"James Potter",
          "assignment" : [82, 56, 44, 30],
          "test" : [80, 80],
          "lab" : [67.90, 78.72]
        }

dylan = { "name" : "Dylan Rhodes",
          "assignment" : [77, 82, 23, 39],
          "test" : [78, 77],
          "lab" : [80, 80]
        }
         
jess = { "name" : "Jessica Stone",
         "assignment" : [67, 55, 77, 21],
         "test" : [40, 50],
         "lab" : [69, 44.56]
       }


tom = { "name" : "Tom Hanks",
        "assignment" : [29, 89, 60, 56],
        "test" : [65, 56],
        "lab" : [50, 40.6]
      } 


def calculate_avg(ls=[]):
	return sum(ls) / len(ls)

def percentage_cal(assign,test,lab):
	return (0.1*assign + 0.7*test + 0.2*lab)

def grade_predict(score=0):
	if score>=90: 
		return "A"
	elif score>=80:
		return "B"
	elif score>=70:
		return "C"
	elif score>=50:
		return "D"
	elif score>=40:
		return "E"





jack_assignment_total = calculate_avg(jack.get("assignment"))
jack_test_total = calculate_avg(jack.get("test"))
jack_lab_total =calculate_avg(jack.get("lab"))
jack_total_score = percentage_cal(jack_assignment_total,jack_test_total,jack_lab_total)

james_assignment_total = calculate_avg(james.get("assignment"))
james_test_total = calculate_avg(james.get("test"))
james_lab_total =calculate_avg(james.get("lab"))
james_total_score = percentage_cal(james_assignment_total,james_test_total,james_lab_total)

dylan_assignment_total = calculate_avg(dylan.get("assignment"))
dylan_test_total = calculate_avg(dylan.get("test"))
dylan_lab_total =calculate_avg(dylan.get("lab"))
dylan_total_score = percentage_cal(dylan_assignment_total,dylan_test_total,dylan_lab_total)

jess_assignment_total = calculate_avg(jess.get("assignment"))
jess_test_total = calculate_avg(jess.get("test"))
jess_lab_total =calculate_avg(jess.get("lab"))
jess_total_score = percentage_cal(jess_assignment_total,jess_test_total,jess_lab_total)

tom_assignment_total = calculate_avg(tom.get("assignment"))
tom_test_total = calculate_avg(tom.get("test"))
tom_lab_total =calculate_avg(tom.get("lab"))
tom_total_score = percentage_cal(tom_assignment_total,tom_test_total,tom_lab_total)

name_list=[jack,james,dylan,jess,tom]
score_list=[jack_total_score,james_total_score,dylan_total_score,jess_total_score,tom_total_score]

for (i,k) in zip(name_list,score_list):
	print (i["name"])
	print ("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
	print ("Average mark of %s is: %s" %(i["name"],k))
	print ("Grade of %s is: %s" %(i["name"],grade_predict(k)))
	print ("\n")