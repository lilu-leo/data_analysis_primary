import unicodecsv

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
