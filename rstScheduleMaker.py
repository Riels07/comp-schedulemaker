import csv

dict = {
    '101': 'Exploring the Internet',
    '102': 'Web Design and Multimedia Publishing',
    '104': 'Computer Animation',
    '111': 'History of Computing',
    '120': 'Introduction to Computer Applications',
    '125': 'Visual Information Processing',
    '150': 'Introduction to Computing',
    '163': 'Discrete Structures',
    '170': 'Introduction to Object-Oriented Programming',
    '171': 'Scripting Languages',
    '215': 'Object-Oriented Programming with Mathematics',
    '250': 'Introduction to Scientific and Technical Communication',
    '251': 'Introduction to Database Systems',
    '264': 'Introduction to Computer Systems',
    '271': 'Data Structures',
    '300': 'Data Warehousing and Data Mining',
    '305': 'Database Administration',
    '309': 'Numerical Methods',
    '312': 'Free/Open Source Computing',
    '313': 'Intermediate Object-Oriented Development',
    '314': 'Problem Solving Strategies',
    '315': 'Problem Solving Strategies',
    '316': 'Ethics and Computers',
    '317': 'Social, Legal, and Ethical Issues in Computing',
    '319': 'Introduction to Unix',
    '320': 'Software Systems Analysis',
    '330': 'Software Engineering',
    '331': 'Cryptography',
    '332': 'Design Patterns and Object Oriented Design',
    '333': 'Formal Methods in Software Engineering',
    '336': 'Markup Languages',
    '337': 'Introduction to Concurrency',
    '338': 'Server-Based Software Development',
    '339': 'Distributed Systems',
    '340': 'Computer Forensics',
    '343': 'Introduction to Computer Networks',
    '346': 'Introduction to Telecommunications',
    '347': 'Intrusion Detection and Computer Forensics',
    '348': 'Network Security',
    '349': 'Wireless Networks and Security',
    '351': 'Network Management',
    '353': 'Database Programming',
    '355': 'Introduction to Data Mining and Knowledge Discover',
    '360': 'Computer Organization',
    '363': 'Design and Analysis of Computer Alogirthms',
    '364': 'High-Performance Computing',
    '366': 'Microcomputer Design and Interfacing',
    '370': 'Software Quality, Metrics, and Testing',
    '372': 'Programming Languages',
    '373': 'Objects, Frameworks, and Patterns',
    '374': 'Introduction to Operating Systems',
    '376': 'Formal Languages and Automata',
    '378': 'Artificial Intelligence',
    '380': 'Introduction to Computer Graphics',
    '381': 'Bioinformatics',
    '382': 'Introduction to Compilers',
    '383': 'Computational Bioinformatics',
    '388': 'Topics in Computer Science',
    '390': 'Broadening Participation in STEM(Computing, Math & Science)',
    '391': 'Internship in Computer Science',
    '398': 'Independent Study',
    '399': 'Research Seminar',
    '410': 'Operating Systems',
    '411': 'Computer Systems Administration',
    '412': 'Free/Open Source Computing',
    '413': 'Intermediate Object-Oriented Development',
    '417': 'Social, Legal, and Ethical Issues in Computing',
    '420': 'Software Systems Analysis',
    '421': 'Mathematical Modeling and Simulation',
    '422': 'Software Development for Wireless/Mobile Devices',
    '423': 'Combinatorial Mathematics',
    '424': 'Client-Side Web Design',
    '431': 'Cryptography',
    '433': 'Web Services Programming',
    '434': 'Enterprise Software Development',
    '436': 'Markup Languages',
    '437': 'Concurrent Programming',
    '439': 'Distributed Systems',
    '441': 'Human-Computer Interface Design',
    '442': 'Server-Side Software Development',
    '443': 'Computer Networks',
    '446': 'Telecommunications',
    '447': 'Intrusion Detection and Computer Forensics',
    '448': 'Network Security',
    '449': 'Wireless Networks and Security',
    '450': 'Microprogramming & Microprocessing',
    '453': 'Database Programming',
    '460': 'Algorithms and Complexity',
    '462': 'Computer Architecture',
    '464': 'High-Performance Computing',
    '471': 'Programming Languages',
    '473': 'Object-Oriented Programming',
    '474': 'Software Engineering',
    '475': 'System Standards and Requirements',
    '476': 'Formal Language and Automata',
    '477': 'IT Project Management',
    '480': 'Computer Graphics',
    '484': 'Artificial Intelligence',
    '488': 'Topics in Computer Science',
    '490': 'Independent Project',
    '499': 'Internship',
    '605': 'Master of Science Study',
    '???': 'DEFAULT'
    }

def parse_title(id):
    title = dict[id]
    return title

# decodes the tokens to the day names: MWF = Monday Wednesday Friday etc
def parse_days(days):
    decoded = []
    if days == 'See Note':
       return ['See Note']
    if "M" in days:
        decoded.append('Monday')
    if "T" in days:
        # needed so "Tr" doesn't add Tuesday and Thursday
        if (days.count("Tr") == 1 and days.count("T") == 2):
            decoded.append('Tuesday')
        # needed so "T" 
        elif (days.count("Tr") == 0 and days.count("T") == 1):
            decoded.append('Tuesday')
    if "W" in days:
        decoded.append('Wednesday')
    if "Tr" in days:
        decoded.append('Thursday')
    if "F" in days:
        decoded.append('Friday')
    if "Sa" in days:
        decoded.append('Saturday')
    if not decoded == []:
        return decoded
    else:
        return ['TBD']

# decodes the instructor names putting them in order: "Smith,Adam" = Adam Smith
def parse_instructor(instructor):
    decoded = instructor.split(',')
    if '' in decoded:
        return ['TBD']
    else:
        decoded.reverse()
        return decoded

# decodes the instructor names putting them in order: "Smith,Adam" = Adam Smith
def parse_instructor2(instructor):
    decoded = instructor.split(',')
    if '' in decoded:
        return ['TBD']
    else:
        decoded.reverse()
        decoded[0] = decoded[0] + ' '
        return decoded

# decodes the campus to its full name
def parse_campus(campus):
    if (campus.strip() == 'WTC'):
        return 'Water Tower'
    elif (campus.strip() == 'LSC'):
        return 'Lakeshore'
    elif (campus.strip() == 'ONLN'):
        return 'Online'
    elif (campus.strip() == 'HYBRID'):
        return 'Hybrid'
    else:
        return 'TBD'

# decodes the facility
def parse_facility(facility):
    if 'non-lab' in facility:
        return facility
    if '-' in facility:
       data = facility.split('-')
    else:
        data = facility.split(' ')
    if '' in data:
        return 'TBD'
    if not len(data) == 2:
        return facility
    else:
        return data[0] + ' ' + data[1]
    
# gets the start and end time of the course and returns in form start-end
def parse_time(start, end):
    if start == 'See Note':
        return start
    if start == '' or end == '':
        return 'TBD'
    else:
        data_start = start.split(' ')
        time_start = data_start[0][:len(data_start[0])-3]
        ampm_start = data_start[1]
        data_end = end.split(' ')
        time_end = data_end[0][:len(data_end[0])-3]
        ampm_end = data_end[1]
        if time_start[0] == '0':
            time_start = time_start[1:]
        if time_end[0] == '0':
            time_end = time_end[1:]
        return time_start + ' ' + ampm_start + ' - ' + time_end + ' ' + ampm_end

# Returns the session the course takes place in
def parse_session(code):
    if code == '1':
        return None
    if code == '8W1':
        return 'This course meets during the first 8 week session of the semester.'
    if code == '8W2':
        return 'This course meets during the second 8 week session of the semester.'

# Returns a note to be printed if a note is listed.
def parse_note(note):
    if not note == "":
        return note
    else:
        return None

def writeLine(rstfile, string):
    rstfile.write(string + '\n')

def skipLine(rstFile):
    rstfile.write('\n')
 
# Reads the spreadsheet and saves rst file in RSTFILE.txt
def printMobile(csv_file, semester):
    
    with open(csv_file, 'r') as f:
        sem = semester.lower().split(' ')
        rstfile = open(sem[0] + sem[1] + 'mobile.inc', "w")
        dict = csv.DictReader(f, delimiter=',', quotechar='"')

        courses = 0
	newCourse = True
        firstGraduateCourse = True
        currentCourseNumber = '0'
	rstfile.write('Mobile/Single Column Format - ' + semester + ' - Schedule\n')
        rstfile.write('==================================================================\n')
        rstfile.write('\n')
        rstfile.write('The following courses will (tentatively) be held during the ' + semester + ' semester.\n')
        rstfile.write('\n')
        rstfile.write('For classroom locations and open/full status, see `LOCUS <http://www.luc.edu/locus>`_.\n')
        rstfile.write('\n')
        rstfile.write('Note: While we update this page regularly, please check `LOCUS <http://www.luc.edu/locus>`_ ' 
			+ 'for the most recent information.\n')
        rstfile.write('\n')
        rstfile.write('**In case of conflict, information on LOCUS should be considered authoritative.**\n')
        rstfile.write('\n')

        rstfile.write('QuickLinks\n')
        rstfile.write('~~~~~~~~~~~~~\n')
        rstfile.write('\n* :doc:`' + sem[0] + 'widescreen`')
        rstfile.write('\n* :ref:`undergraduate_courses_list`')
        rstfile.write('\n* :ref:`graduate_courses_list`')

        rstfile.write('\n')
        rstfile.write('\n.. _undergraduate_courses_list:')
        rstfile.write('\n')
        rstfile.write('\nUndergraduate Courses')
        rstfile.write('\n~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

        #iterates through each entry in the spreadsheet
        for line in dict:
	    if line['SUBJECT'] == 'COMP':
               courses += 1
               if line['CATALOG NUMBER'] == '388' and (line['SECTION'] == '4' or line['SECTION'] == '5'):
                   line['START TIME'] = 'See Note'
                   line['CLASS MEETING PATTERN'] = 'See Note'
	       if int(line['CATALOG NUMBER']) >= 400 and firstGraduateCourse:
                   firstGraduateCourse = False
                
                   rstfile.write('\n.. _graduate_courses_list:')
                   rstfile.write('\n')
                   rstfile.write('\nGraduate Courses')
                   rstfile.write('\n~~~~~~~~~~~~~~~~~~\n')
               #prints the title of the course
               if line['CATALOG NUMBER'] == '388' or line['CATALOG NUMBER'] == '488':
                   title = ('\nCOMP ' + line['CATALOG NUMBER'].strip() + '-' + line['SECTION'].strip()
                            + ': ' + line['COURSE TITLE'])
                   rstfile.write(title)
                   rstfile.write('\n' + '~' * (len(title) + 1))
               else:
                   title = ('\nCOMP ' + line['CATALOG NUMBER'].strip() + '-' + line['SECTION'].strip()
                         + ': ' + parse_title(line['CATALOG NUMBER']))
                   rstfile.write(title)
                   rstfile.write('\n' + '~' *(len(title) + 1))


               #prints session if not for full semester
               session = parse_session(line['SESSION'])
               if not session == None:
                   rstfile.write('\n')
                   rstfile.write('\n' + '**' +  session + '**')

            
               #prints the instructor
               rstfile.write('\n')
               rstfile.write('\nInstructor: ')
               for name in parse_instructor(line['INSTRUCTOR']):
                   rstfile.write(name.strip(' \t\n\r') + ' ')

               #prints the start - end time
               rstfile.write('\n')
               rstfile.write('\nTime: ' + parse_time(line['START TIME'].strip(), line['END TIME'].strip()))
               rstfile.write('\n')

               #prints the days of the week                
               rstfile.write('\nDay(s): ')
               for day in parse_days(line['CLASS MEETING PATTERN']):
                   rstfile.write(day + ' ')
               rstfile.write('\n')

               #prints the campus
               rstfile.write('\nCampus: ' + parse_campus(line['CLASS LOCATION'].strip()))
               rstfile.write('\n')

               #prints the note if there is a note
               note = parse_note(line['DISPLAYED SECTION NOTES'])
               if not note == None:
                   rstfile.write('\nNotes: ' + note)
                   rstfile.write('\n')
                                          
               if line['CATALOG NUMBER'] == '314' or line['CATALOG NUMBER'] == '315':
                   rstfile.write('\nCourse Description: ' +
                          ':doc:`comp314-315`')
               else:
                   rstfile.write('\nCourse Description: ' +
                          ':doc:`comp'
                          + line['CATALOG NUMBER'].strip() + '`')
                
               rstfile.write('\n')

        print ('MOBILE FORMAT COMPLETE')
        print (str(courses) + ' courses added.')

def printWidescreen(csv_file, semester):
    
    with open(csv_file, 'r') as f:
        sem = semester.lower().split(' ')
        rstfile = open(sem[0] + sem[1] + 'widescreen.inc', "w")
        dict = csv.DictReader(f, delimiter=',', quotechar='"')

        courses = 0
	newCourse = True
        firstGraduateCourse = True
        currentCourseNumber = '0'
        notes = []

	rstfile.write('Widescreen/Table Format - ' + semester + ' - Schedule\n')
        rstfile.write('=============================================================\n')
        rstfile.write('\n')
        rstfile.write('The following courses will (tentatively) be held during the ' + semester + ' semester.\n')
        rstfile.write('\n')
        rstfile.write('For classroom locations and open/full status, see `LOCUS <http://www.luc.edu/locus>`_.\n')
        rstfile.write('\n')
        rstfile.write('Note: While we update this page regularly, please check `LOCUS <http://www.luc.edu/locus>`_ ' 
			+ 'for the most recent information.\n')
        rstfile.write('\n')
        rstfile.write('**In case of conflict, information on LOCUS should be considered authoritative.**\n')
        rstfile.write('\n')

        rstfile.write('QuickLinks\n')
        rstfile.write('~~~~~~~~~~~~~\n')
        rstfile.write('\n* :doc:`' + sem[0] + 'mobile`')
        rstfile.write('\n* :ref:`undergraduate_courses_table`')
        rstfile.write('\n* :ref:`graduate_courses_table`')

        rstfile.write('\n')
        rstfile.write('\n.. _undergraduate_courses_table:')
        rstfile.write('\n')
        rstfile.write('\nUndergraduate Courses')
        rstfile.write('\n~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

        #iterates through each entry in the spreadsheet
        for line in dict:
            if line['SUBJECT'] == 'COMP':
               courses += 1
               if line['CATALOG NUMBER'] == '388' and (line['SECTION'] == '4' or line['SECTION'] == '5'):
                   line['START TIME'] = 'See Note'
                   line['CLASS MEETING PATTERN'] = 'See Note'
	       if int(line['CATALOG NUMBER']) >= 400 and firstGraduateCourse:
                   firstGraduateCourse = False
                
                   rstfile.write('\n.. _graduate_courses_table:')
                   rstfile.write('\n')
                   rstfile.write('\nGraduate Courses')
                   rstfile.write('\n~~~~~~~~~~~~~~~~~~\n')

               if currentCourseNumber == line['CATALOG NUMBER']:
                   newCourse = False
               else:
                   newCourse = True
                   currentCourseNumber = line['CATALOG NUMBER']
                   if len(notes) > 0:
                      rstfile.write('\n.. rubric:: Notes\n')
                      for note in notes:
                         rstfile.write('\n.. [#] ' + note)              
                      notes = []
                      rstfile.write('\n')

	       if newCourse:
                   newCourse = False
                
                   #prints the title of the course and sets up the table
		   if line['CATALOG NUMBER'] == '388' or line['CATALOG NUMBER'] == '488':
                       title = '\n:doc:`comp' + line['CATALOG NUMBER'].strip() + '`'
                       rstfile.write(title)
                       rstfile.write('\n' + '-' * (len(title) + 1) + '\n')
                       rstfile.write('\n.. csv-table::')
                       rstfile.write('\n    :header: "Section", "Topic", "Instructor", "Time", "Day(s)", "Campus", "Note"')
   	               rstfile.write('\n    :widths: 10, 100, 75, 75, 30, 50, 50\n\n')
                   else:
                       if line['CATALOG NUMBER'] == '314' or line['CATALOG NUMBER'] == '315':
                           title = '\n:doc:`comp314-315`\n'
                           rstfile.write(title)
                    	   rstfile.write('\n' + '-' *(len(title) + 1) +'\n')
                       else:
                           title = '\n:doc:`comp' + line['CATALOG NUMBER'].strip() + '`'
                    	   rstfile.write(title)
                    	   rstfile.write('\n' + '-' *(len(title) + 1) +'\n')
                   
                       rstfile.write('\n.. csv-table::')
                       rstfile.write('\n    :header: "Section", "Instructor", "Time", "Day(s)", "Campus", "Note"')
   	               rstfile.write('\n    :widths: 10, 175, 75, 30, 50, 50\n\n')
   
               #prints the section number
               rstfile.write('    ' + line['SECTION'].strip() + ', ')

               if line['CATALOG NUMBER'] == '388' or line['CATALOG NUMBER'] == '488':
                   rstfile.write(line['COURSE TITLE'].strip() + ', ')
               
                

               #prints the instructor

               for name in parse_instructor2(line['INSTRUCTOR']):
                   rstfile.write(name)
               rstfile.write(', ')

            
               #prints the start - end time
               rstfile.write(parse_time(line['START TIME'].strip(), line['END TIME'].strip()) + ', ')

               #prints the days of the week
               if line['CLASS MEETING PATTERN'] == '':
                   rstfile.write('TBD, ')
               else:             
                   rstfile.write(line['CLASS MEETING PATTERN'] + ', ')
                
               #prints the campus
               rstfile.write(parse_campus(line['CLASS LOCATION'].strip()) + ', ')

	       #special case for COMP 388 - Foundations
               note = line['DISPLAYED SECTION NOTES']
               if note != '':
                  notes.append(note)
                  rstfile.write('[#]_ \n')
               else: 
                  rstfile.write('N/A \n')


        print ('WIDESCREEN FORMAT COMPLETE')
        print (str(courses) + ' courses added.')


def main(csv_file, semester):
   
   printWidescreen(csv_file, semester)
   printMobile(csv_file, semester)

main(raw_input("CSV File: "), raw_input("Semester: "))


        
