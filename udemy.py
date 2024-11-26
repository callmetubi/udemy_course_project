import pandas as pd 

data=pd.read_csv(r"C:\Users\hp15s\Desktop\udemy_course_project\file (3).csv")
print(data)

#1- WHAT ARE ALL DIFFERENT SUBJECTS FOR WHICH UDEMY IS OFFERING COURSES?
print(data.subject.unique())
#2- NUMBER OF COURSES AND MAX MIN COURSE
print(data.subject.value_counts())

print(data.columns)
#3- SHOW ALL THE COURSES COST
print(data.is_paid.value_counts())
#4- WHICH ARE FREE COST 
print(sum(data.is_paid == False))
#5- WHICH ARE TOP SELLING COURSE
print(data.sort_values('num_subscribers', ascending=False))
#6- WHICH ARE LEAST SELLING COURSE
print(data.sort_values('num_subscribers'))
#7-SHOW ALL COURSES OF GRAPHIC DESIGN WHERE THE PRICE IS BELOW 100?
print([(data.subject == 'Graphic Design') & (data.price < '100')])
#8- LIST OUT ALL THE COURSE THAT ARE ELATED WITH 'PYHTON'
data_name=data[data.course_title.str.contains('Python')]
#9-WHAT ARE COURSES THAT PUBLISHED INYEAR 2015?
print(data.dtypes)
data['published_timestamp'] = pd.to_datetime(data['published_timestamp'])
print(data['published_timestamp'])
print(data.dtypes)
data['Year']= data['published_timestamp'].dt.year
print(data.columns)
print(data[data.Year == 2015])
#10 WHAT ARE THE MX NUMBER OF SUBSCRIBERS FOR EACH LEVEL OF COURSES?
print(data.level.unique())
print(data.groupby('level')['num_subscribers'].max())
print(data.groupby('level').max())