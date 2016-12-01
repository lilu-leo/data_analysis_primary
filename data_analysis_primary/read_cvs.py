import unicodecsv
from datetime import datetime as dt
def read_cvs(file_name):
    with open(file_name, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader) 

enrollments = read_cvs('enrollments.csv')
daily_engagement = read_cvs('daily_engagement.csv')
project_submissions = read_cvs('project_submissions.csv')
print enrollments[0]
print daily_engagement[0]
print project_submissions[0]

def parse_date(date):
    if date == '':
        return None
    else:
        return dt.strptime(date, '%Y-%m-%d')
                                
def parse_maybe_int(i):
    if i == '':
        return None
    else:
        return int(i)
                                                            
for enrollment in enrollments:
    enrollment['cancel_date'] = parse_date(enrollment['cancel_date'])
    enrollment['days_to_cancel'] = parse_maybe_int(enrollment['days_to_cancel'])
    enrollment['is_canceled'] = enrollment['is_canceled'] == True
    enrollment['is_udacity'] = enrollment['is_udacity'] == True
    enrollment['join_date'] = parse_date(enrollment['join_date'])

print enrollments[0]


for engagement_record in daily_engagement:
    engagement_record['lessons_completed'] = int(float(engagement_record['lessons_completed']))
    engagement_record['num_courses_visited'] = int(float(engagement_record['num_courses_visited']))
    engagement_record['projects_completed'] = int(float(engagement_record['projects_completed']))
    engagement_record['total_minutes_visited'] = int(float(engagement_record['total_minutes_visited']))
    engagement_record['utc_date'] = parse_date(engagement_record['utc_date'])

print daily_engagement[0]

