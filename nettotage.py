import pandas as pd

#Charger les données 
stations = pd.read_csv("Data/Citycycle_stations.csv")
trajets = pd.read_csv("Data/Citycycle_trajets.csv")

#Valeurs manquantes dans trajets dans les colonnes 
#print(stations.info())
#temperature_c	760 − 744
#type_abonnement	760 − 745

#Voir si il y'a des doublons 
print(trajets.duplicated().sum())
#0 doublons dans stations
#60 doublons dans trajets 

trajets = trajets.drop_duplicates()
print(len(trajets))

print(trajets["trajet_id"].duplicated().sum())