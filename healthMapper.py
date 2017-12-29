'''''''''''''''
Health Mapper 
October 2017
'''''''''''''''

import folium
import pandas as pd
import branca
#North and South = latitude, East and West = longitude
categories = ['Age', 
            'Sex',
            'Diabetes Diagnosis', 'Cardiovascular Disease Diagnosis',
            'Water Accessiblity', 'Clinic Accessiblity',
            'Alcohol Use', 'Tobacco Use', 'Health Insurance',
            'Member of progresando con solidaridad', 
            '# of People Living in the House', 'Number of those people at or under the age of 5',
            'Floor','Roof','Type of House', 'Latrine Accessibility'
            ]
#Actual Coordinates of Constanza
#C_COORDINATES = [18.9115, -70.71]

#Average of Coordinates of Constanza Health Data
C_COORDINATES = [18.9045441, -70.76437349]

#Reading in CSV file into pandas table
health_data = pd.read_csv('constanza_health.csv')

# Number of Data points_for speed purposes
MAX_RECORDS = 100
 
# create empty map zoomed in on Constanza
constanzaMap = folium.Map(location = C_COORDINATES, 
							tiles = 'OpenStreet Map', 
							zoom_start = 16,
							min_lat=17, max_lat=19, 
							min_lon=-71, max_lon=-69
                            #min_lat=-90, max_lat=90, min_lon=-180, max_lon=180
							)


#FOR LOOP: add a marker for every record in the CSV file
for each in health_data[0:MAX_RECORDS].iterrows():
    #FUNCTION: Generates HTML code for Pop-Up
    def simpHTML(x, each):
        html = '<h4>' + str(x) + '</h4>' + '<p>' + str(each[1][x]) + '</p>'
        return html
    html = ''
    i = 0
    #FOR LOOP: Goes Through Health Categories List and appends it to html code
    for item in range(len(categories)):
        x = simpHTML(categories[i], each)
        i += 1
        html += x
    iframe = branca.element.IFrame(html=html, width=150, height=300)
    popup = folium.Popup(iframe, max_width=500)

    #Creates actual marker based on CSV GPS coordinates and Health Categories List Names
    folium.Marker(
        #latitude and longitude GPS-Coordinates
    	location = [each[1]['Latitude'],each[1]['Longitude']],
    	popup = popup 
        ).add_to(constanzaMap)
 
#display(map)
constanzaMap.save('constanza_health_map.html')

