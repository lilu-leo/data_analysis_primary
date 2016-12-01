import unicodecsv
#enrollments = []
with open('enrollments.csv', 'rb') as f:
    reader = unicodecsv.DictReader(f)
    enrollments = list(reader)
   # for row in reader:
    #    enrollments.append(row)
            
print enrollments[0]
