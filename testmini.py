var = [{ "name":"Jack Frost",
         "assignment" : [80, 50, 40, 20],
         "test" : [75, 75],
         "lab" : [78.20, 77.20]
       },{ "name":"James Potter",
          "assignment" : [82.0, 56.0, 44.0, 30.0],
          "test" : [80, 80],
          "lab" : [67.90, 78.72]
        },{ "name" : "Dylan Rhodes",
          "assignment" : [77, 82, 23, 39],
          "test" : [78, 77],
          "lab" : [80, 80]
        },{ "name" : "Jessica Stone",
         "assignment" : [67, 55, 77, 21],
         "test" : [40, 50],
         "lab" : [69, 44.56]
       },{ "name" : "Tom Hanks",
        "assignment" : [29, 89, 60, 56],
        "test" : [65, 56],
        "lab" : [50, 40.6]
      }]

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

def main(st_rec_l=[]):
    for index, r in enumerate(var):        
        assign = calculate_avg(var[index]["assignment"]) 
        test = calculate_avg(var[index]["test"])
        lab = calculate_avg(var[index]["lab"])
        total_percent = percentage_cal(assign,test,lab)
        st_grade = grade_predict(total_percent)  
             
        print (var[index]["name"])
        print ("****************************")
        print ("Average of %s is: %s" %(var[index]["name"],total_percent))
        print ("Grade level of %s is : %s" %(var[index]["name"],st_grade)) 
        print ("\n")

main()