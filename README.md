# projet_OPT_mixenergy
The production of nuclear energy is fixed in france, but if there is more renewable energy, we can use less fossil fuel or gas, and so on. So if we can predict wind power production, the calculation of 
gas use will be decided.  
## objectives
It is known that the energy mix in France can be basically divided into clean energy and fossil energy. We want to minimise the use of fossil fuels while maintaining the energy supply.  
## potential customer
RTE (the electricity transmission system operator, responsible in particular for high-voltage lines, as well as for balancing the network - ensuring in real time that there is as much 
electricity needed as is available on the network)
## solution
We have six months of hourly power generation data for the two wind parks in Saint Nazaire and six months of weather data for the Saint Nazaire area.I plan to start by using machine learning to predict the
amount of electricity that will be generated in the Saint Nazaire area for the next hour or three.This is then extended to predict the next hour or three hours of wind power generation for the whole of France.
And on the RTE official website, they predicted the energy consumption for the whole of France for the next 15 minutes. Since nuclear energy generation is fixed every day, ignoring solar energy use, when we predict 
wind energy acquisition, we can get the hourly planned fossil fuel use

## dataset
### Collection of data  
source:https://www.services-rte.com/fr/visualisez-les-donnees-publiees-par-rte/production-realisee-par-groupe.html  
Since the site does not consolidate data, it can only be downloaded one day at a time, one park at a time. So I wrote a code to make it download one month at a time, and then integrated it into a CSV file  

source: https://www.visualcrossing.com/weather/weather-data-services  
RTE Predicted consumption： https://www.rte-france.com/eco2mix/la-consommation-delectricite-en-france#
