import pandas as pd
from csv import DictWriter

my_netflix= pd.read_csv('ViewingActivity.csv')  
netflix_kaggle = pd.read_csv("netflix_titles.csv")
netflix_combined = pd.read_csv("Kaggle_combined.csv")

# loop over entries in kaggle title to see if connection is in my_netflix
for i, entry in netflix_kaggle.iterrows():
    title = entry['title']
    show_type = entry['type']
    
    print(title)
    print("---- Start ----")
    
#use boolean found to only add once
    found = False
    for y, my_entry in my_netflix.iterrows():
        
        my_title = my_entry['Title']
        #if a show is found, only use part before :
        if(show_type == "TV Show"):
            my_title = my_title.split(':')[0]
        
      #if found not yet True add data to columns
        if title == my_title and not found:
            #open new csv and add
             f_object = open('Kaggle_combined.csv', 'a', encoding="utf-8")
             print("Title found in my title!" + my_title)
             field_names = ['Profile Name','Start Time', 'Duration', 'Title_N', 'Device Type', 'Bookmark', 'Latest Bookmark', 'Country_N', 'Type', 'Title_kg', 'Cast', 'Date Added', 'Release Year', 'Rating', 'Listed In', 'Description']
             row = {'Profile Name': my_entry['Profile Name'],
               'Start Time': my_entry['Start Time'],
               'Duration': my_entry['Duration'],
               'Title_N': my_entry['Title'].replace("’","'"),
               'Device Type': my_entry['Device Type'] ,
               'Bookmark': my_entry['Bookmark'],
               'Latest Bookmark': my_entry['Latest Bookmark'],
               'Country_N': my_entry['Country'],
               'Type':entry['type'],
               'Title_kg': entry['title'],
               'Cast': entry['cast'],
               'Date Added': entry['date_added'],
               'Rating': entry['rating'],
               'Listed In': entry['listed_in'],
               'Description': entry['description'],
               }            
             
             dictwriter_object = DictWriter(f_object, fieldnames=field_names)
             dictwriter_object.writerow(row)
            #close csv
             f_object.close()
             found = True
    print("---- End ----") # to read in the console