'''
1. Load the course names, ch, and grade
2. Calculate CGPA 
3. Calculate SGPA 
'''

transcript = dict()
gradepoints = dict()

def set_gradepoints(filename="Marking.txt"):
	grades = open(filename)
	for line in grades:
		line = line.split(":")
		gradepoints[line[0].strip()] = float(line[1].strip())

	grades.close()

def load_grades(filename="Grades.txt"):
	gradebook = open(filename)
	current_semester = ""
	for line in gradebook:
		if "Semester:" in line:
			current_semester = line.strip()
		elif line.strip() != "":
			line = str(line).split(":")
			transcript[line[0].strip()] = list()			
			transcript[line[0].strip()].append(line[1].strip()) #Course Grade
			transcript[line[0].strip()].append(int(line[2])) #Course Credits 
			transcript[line[0].strip()].append(current_semester[10:]) #Course Semester. 
			#The slicing is to remove "Semester:"

	gradebook.close()

def SGPA(semester):
	semester = semester.strip().lower()

	total_credits = 0
	gpa = float()
	
	for course in transcript:
		course_semester = transcript[course][2].strip().lower()
		if semester == course_semester:
			total_credits += transcript[course][1]
			course_gradepoints = gradepoints[transcript[course][0]]
			gpa += course_gradepoints * transcript[course][1]

	gpa /= total_credits
	gpa *= 1000 #3 decimal places
	gpa = int(gpa)
	gpa /= 1000 #3 decimal places

	return gpa

def CGPA():
	total_credits = 0
	gpa = float()
	
	for course in transcript:
		total_credits += transcript[course][1]
		course_gradepoints = gradepoints[transcript[course][0]]
		gpa += course_gradepoints * transcript[course][1]

	gpa /= total_credits
	gpa *= 1000 #3 decimal places
	gpa = int(gpa)
	gpa /= 1000 #3 decimal places

	return gpa

if __name__ == '__main__':
	set_gradepoints()
	load_grades()
	print(CGPA())