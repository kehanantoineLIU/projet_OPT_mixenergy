# projet_OPT_mixenergy
France is heavily dependent on nuclear energy nuclear power, which will account for around 63% of total electricity production in 2022. The remaining 37% comes from other sources sources such as gas and renewable energies. and renewable energies. The aim is to increase the share of green energies in the remaining 37% of electricity electricity generation, in particular by making maximum use of wind power capacity to reduce the need for electricity generation reduce the need for gas-fired power generation. gas-fired generation.   
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
To answer this question, we set up an empirical model based on the following equation:   

![image](https://github.com/kehanantoineLIU/projet_OPT_mixenergy/assets/125217787/bd12d46f-ea39-4044-8019-322bfa8b4696)    

The equation defines the demand for electricity, with 63% coming from nuclear power and 11% from hydropower, and the remainder being met by sources such as wind and gas generation. The main objective is to meet this demand efficiently, while reducing the share of fossil fuels, particularly gas, in favor of renewable energies.   
1. The first phase of the project aims to assess wind power production for the whole of France. The initial focus is on the Saint-Nazaire offshore wind farm, with a view to generalizing the results to all onshore wind farms in France. 
2. The second phase of the project consists in accurately predicting total electricity consumption for the whole country.
country as a whole.

## data
### Collection of data  
For the prediction of wind power production, we used three different databases:
● Meteorological data includes hour-by-hour details between March 1, 2023 and September 30, 2023. These data include parameters such as wind direction and speed, wind gusts, temperature, precipitation, humidity and cloud percentage.
● Hour-by-hour wind power production data for the Saint-Nazaire wind farm for the period from March 1, 2023 to September 30, 2023. This data includes the amount of energy produced in megawatts (MW) for each hour during this period for both groups at the farm.
● Data for onshore wind farms in France, including the name of each farm, as well as the maximum power in megawatts (MW) they can produce. 

For the prediction of electricity consumption in France, a dataset containing electricity consumption data covering an hourly period from January 1, 2021 to November 1, 2023 was used.
(Data source placed at the end of the Bibliographie)

### data preparation 
Before integrating this data into our predictive models for wind energy production and electricity consumption in France, we applied several operations. These included data selection, cleaning, construction, integration and formatting. Specifically, data selection involves the removal of irrelevant columns, while cleaning addresses missing values and anomalies. Data integration combines information on wind generation, weather conditions and consumption into a new Data Frame. Finally, preparing the data for algorithm training includes structuring the training and test sets, and formatting the data to represent the total energy produced across the entire wind farm. Preparing the consumption data also involves decomposing the 'Date and Time' column to facilitate the use of a Random Forest model, enabling the model to understand the temporal relationships in electricity consumption in France.

## Algorithms & evaluation 
### model
1. To predict wind power production, we face a regression problem based on supervised learning. For this type of problem, several machine learning algorithms can be used. However, we have chosen 5 of the most common algorithms: Linear Regression, Random Forest, KNN Regression, Gradient Boosting Regressing and Support Vector Regression. 
2. For the prediction of power consumption, 2 models were chosen to capture complex capture complex, temporal and long-term relationships in time series time series: Random Forest and LSTM (Long Short-Term Memory).
### evaluation
When evaluating different models, it is essential to use a variety of measures to ensure the quality of predictions and to compare them with each other. The results of MSE, RMSE and MAE results reflect the errors between predicted and actual values, where lower values indicate better predictions. The NMAE takes into account the scale of the data, enabling a fair comparison between different datasets. The R² quantifies the extent to which variations in the predicted variable can be explained by variations in the actual variable, with a value close to 1 indicating a quality prediction.   

![image](https://github.com/kehanantoineLIU/projet_OPT_mixenergy/assets/125217787/bff1d0c5-2dfc-4b68-bf29-ea9fb59bd0c5)   

We can therefore see that Random Forest is the algorithm that best learns and best predicts wind energy production.   

![image](https://github.com/kehanantoineLIU/projet_OPT_mixenergy/assets/125217787/8290daab-7523-4f0c-b648-7737b75f36be)   

LSTM has better accuracy and performance in the case of electricity consumption prediction. of electricity consumption, which is why we have chosen this algorithm for the electricity consumption.

## applications   

![image](https://github.com/kehanantoineLIU/projet_OPT_mixenergy/assets/125217787/b67b9c71-9067-44ac-be2d-6e6d56275048)   


With the help of our two selected models, we made predictions for December 4, 2023 concerning electricity consumption and wind power generation in France. Once these two elements were found, we then calculated the other elements of the energy mix equation according to our assumptions   

![image](https://github.com/kehanantoineLIU/projet_OPT_mixenergy/assets/125217787/6dc9ced2-fab1-44e6-8b19-3a6f02491402)



## Bibliographie
[1] https://prix-elec.com/energie/production/mix-energetique   
[2]https://www.rte-france.com/actualites/bilan-electrique-2022?fbclid=IwAR158_C84WXimQtYBCu8ughPvk9rUVVkV3WoMI9zvk4zJ5rKA5rN4cjYNig (Bilan Mix 2022)   
[3]https://www.lemonde.fr/les-decodeurs/article/2022/10/06/pourquoi-le-prix-de-l-electricite-depend-de-celui-du-gaz-et-autres-questions-sur-les-factures-a-venir_6140985_4355771.html   
[4] https://www.sciencedirect.com/science/article/pii/S0960148117302550#sec6 (Rapportscientifique sur l’utilisation du Random Forest pour l’estimation de production éolienne)   
[5] https://www.rte-france.com/eco2mix/telecharger-les-indicateurs (data consommations)   
[6] https://www.visualcrossing.com/weather/weather-data-services (data meteorologiques)   
[7]https://www.services-rte.com/fr/visualisez-les-donnees-publiees-par-rte/production-realisee-par-groupe.html (data production electrique parc Saint Nazaire)   
[8] https://www.georisques.gouv.fr/donnees/bases-de-donnees/eolien-terrestre (liste of parcs eoliens terrestres)
