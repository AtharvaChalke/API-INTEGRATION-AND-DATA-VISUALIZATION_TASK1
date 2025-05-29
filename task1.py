import json
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

API_KEY="Not disclosing my API"       #Not revealing api key as it s confidential and not to be shared to others
city_name='Mumbai'   #hardcoded Mumbai as user input was case sensitive to API
def get_weather():
    API_URL=f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"
    try:
      response = requests.get(API_URL)     #it will try the GET request to API
      response.raise_for_status()          #raises exception to http error like 404 or 500s
      return response.json()              
    except Exception as e:                 #exception handeling if in case the api failed to fetch city's data
      print("Error Happened")
      return None

def processes(Weatherdata):
    if Weatherdata is None:
        print("No Plot available Check")
        return
    main_data=Weatherdata['main']  #fetching weather's parameters for selected city
    #weather = data['main']['weather']
    dataVisual=pd.DataFrame({'Metric':['Temperature in Celsius','Humidity %','MinTemperature','MaxTempreature','feels_Like'],
                             'Value':[main_data['temp'],main_data['humidity'],main_data['temp_min'],main_data['temp_max'],main_data['feels_like']]})
    plt.figure(figsize=(10,6))
    sns.barplot(x='Metric',y='Value',data=dataVisual,palette=['Green','Gray','blue','red','violet','cyan'],width=0.6,label="Temperature in Celsius",edgecolor="black")
    plt.title(f"Temperature Forecast Data for {city_name}") #use to give title to plot
    plt.xlabel("Weather Forecast Parameters")               #labels x-axis parameter
    plt.ylabel('Tempreature Value')                         #labels y-axis parameter
    plt.legend()                                            #shows legend for plot
    plt.show()                                              #shows plot

if __name__=="__main__":
  print("Weather Visualizer Project Using Mathplotlib and seaborn")
  weather=get_weather()
  processes(weather)

#in barplot 'x' says x-axis vals and 'y' says y-axis vals
#data variable takes the data which we want to visualize 
#width defines barplot's width and label is used as legend's label
#edgecolor is use to give  barplot a neat look for example i have used black here
