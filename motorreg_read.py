# -*- coding: utf-8 -*-
"""
Script til samling af parset XML-data fra Motorregisteret

Created on Thu Mar 11 14:59:57 2021

@author: Sebastian Dyrby Johansen
"""

# Importing packages.
import json
import pandas as pd
import numpy as np
import datetime

begin_time = datetime.datetime.now()

dat1 = []
dat2 = []

for idx in range(1,109):
    output = 'D:/xml_streaming/output_' + str(idx*100000) + '.json'
    with open(output) as json_file:
        cars = json.load(json_file)
        for car in cars:
            
            if 'regNr' in car.keys():
                dat1.append(car['regNr'])
            else:
                dat1.append(np.nan)
            
            if 'synDato' in car.keys():
                dat2.append(car['synDato'])
            else:
                dat2.append(np.nan)

output = 'D:/xml_streaming/output_final.json'
with open(output) as json_file:
    cars = json.load(json_file)
    for car in cars:
        
        if 'regNr' in car.keys():
            dat1.append(car['regNr'])
        else:
            dat1.append(np.nan)
            
        if 'synDato' in car.keys():
            dat2.append(car['synDato'])
        else:
            dat2.append(np.nan)
        
print("Append for-loops for synDato færdigt, tid:")
print(datetime.datetime.now()-begin_time)

begin_time = datetime.datetime.now()

dats = {'regNr': dat1, 'synDato': dat2}

print('Dats er samlet, tid:')
print(datetime.datetime.now()-begin_time)
begin_time = datetime.datetime.now()

df = pd.DataFrame(dats)
print(df[1:11])

print('DataFrame sat op, tid:')
print(datetime.datetime.now()-begin_time)

begin_time = datetime.datetime.now()
df.to_csv("C:/Users/SDJO/OneDrive - COWI/SPECIALE/Data/Motorregisteret/df_synDato.csv", sep=";", index=False)
print("Gemt som csv, tid:")
print(datetime.datetime.now()-begin_time)

#%%

begin_time = datetime.datetime.now()

for idx in range(1,22):
    locals()["dat" + str(idx)] = []

for idx in range(1,1086):
    output = 'D:/xml_streaming/output_' + str(idx*10000) + '.json'
    with open(output) as json_file:
        cars = json.load(json_file)
        for car in cars:
            
            if 'regNr' in car.keys():
                dat1.append(car['regNr'])
            else:
                dat1.append(np.nan)
            
            if 'foersteRegDato' in car.keys():
                dat2.append(car['foersteRegDato'])
            else:
                dat2.append(np.nan)
                
            if 'regStatus' in car.keys():
                dat3.append(car['regStatus'])
            else:
                dat3.append(np.nan)
            
            if 'regStatusDato' in car.keys():
                dat4.append(car['regStatusDato'])
            else:
                dat4.append(np.nan)
            
            if 'maerke' in car.keys():
                dat5.append(car['maerke'])
            else:
                dat5.append(np.nan)
            
            if 'model' in car.keys():
                dat6.append(car['model'])
            else:
                dat6.append(np.nan)
            
            if 'variant' in car.keys():
                dat7.append(car['variant'])
            else:
                dat7.append(np.nan)
            
            if 'artNavn' in car.keys():
                dat8.append(car['artNavn'])
            else:
                dat8.append(np.nan)
            
            if 'anvNavn' in car.keys():
                dat9.append(car['anvNavn'])
            else:
                dat9.append(np.nan)
            
            if 'totalVaegt' in car.keys():
                dat10.append(car['totalVaegt'])
            else:
                dat10.append(np.nan)
            
            if 'kmPerLiter' in car.keys():
                dat11.append(car['kmPerLiter'])
            else:
                dat11.append(np.nan)
                
            if 'drivkraft' in car.keys():
                dat12.append(car['drivkraft'])
            else:
                dat12.append(np.nan)
                
            if 'synKmStand' in car.keys():
                dat13.append(car['synKmStand'])
            else:
                dat13.append(np.nan)
            
            if 'oplStatus' in car.keys():
                dat14.append(car['oplStatus'])
            else:
                dat14.append(np.nan)
    
            if 'oplStatusDato' in car.keys():
                dat15.append(car['oplStatusDato'])
            else:
                dat15.append(np.nan)
            
            if 'ident' in car.keys():
                dat16.append(car['ident'])
            else:
                dat16.append(np.nan)
            
            if 'stelNr' in car.keys():
                dat17.append(car['stelNr'])
            else:
                dat17.append(np.nan)
            
            if 'siddepladser' in car.keys():
                dat18.append(car['siddepladser'])
            else:
                dat18.append(np.nan)
    
            if 'slagVol' in car.keys():
                dat19.append(car['slagVol'])
            else:
                dat19.append(np.nan)
                
            if 'stoersteEffekt' in car.keys():
                dat20.append(car['stoersteEffekt'])
            else:
                dat20.append(np.nan)
                
            if 'antCylinder' in car.keys():
                dat21.append(car['antCylinder'])
            else:
                dat21.append(np.nan)

output = 'D:/xml_streaming/output_final.json'
with open(output) as json_file:
    cars = json.load(json_file)
    for car in cars:
        
        if 'regNr' in car.keys():
            dat1.append(car['regNr'])
        else:
            dat1.append(np.nan)

        if 'foersteRegDato' in car.keys():
            dat2.append(car['foersteRegDato'])
        else:
            dat2.append(np.nan)
            
        if 'regStatus' in car.keys():
            dat3.append(car['regStatus'])
        else:
            dat3.append(np.nan)
        
        if 'regStatusDato' in car.keys():
            dat4.append(car['regStatusDato'])
        else:
            dat4.append(np.nan)
        
        if 'maerke' in car.keys():
            dat5.append(car['maerke'])
        else:
            dat5.append(np.nan)
        
        if 'model' in car.keys():
            dat6.append(car['model'])
        else:
            dat6.append(np.nan)
        
        if 'variant' in car.keys():
            dat7.append(car['variant'])
        else:
            dat7.append(np.nan)
        
        if 'artNavn' in car.keys():
            dat8.append(car['artNavn'])
        else:
            dat8.append(np.nan)
        
        if 'anvNavn' in car.keys():
            dat9.append(car['anvNavn'])
        else:
            dat9.append(np.nan)
        
        if 'totalVaegt' in car.keys():
            dat10.append(car['totalVaegt'])
        else:
            dat10.append(np.nan)
        
        if 'kmPerLiter' in car.keys():
            dat11.append(car['kmPerLiter'])
        else:
            dat11.append(np.nan)
            
        if 'drivkraft' in car.keys():
            dat12.append(car['drivkraft'])
        else:
            dat12.append(np.nan)
            
        if 'synKmStand' in car.keys():
            dat13.append(car['synKmStand'])
        else:
            dat13.append(np.nan)
        
        if 'oplStatus' in car.keys():
            dat14.append(car['oplStatus'])
        else:
            dat14.append(np.nan)

        if 'oplStatusDato' in car.keys():
            dat15.append(car['oplStatusDato'])
        else:
            dat15.append(np.nan)
        
        if 'ident' in car.keys():
            dat16.append(car['ident'])
        else:
            dat16.append(np.nan)
        
        if 'stelNr' in car.keys():
            dat17.append(car['stelNr'])
        else:
            dat17.append(np.nan)
        
        if 'siddepladser' in car.keys():
            dat18.append(car['siddepladser'])
        else:
            dat18.append(np.nan)

        if 'slagVol' in car.keys():
            dat19.append(car['slagVol'])
        else:
            dat19.append(np.nan)
            
        if 'stoersteEffekt' in car.keys():
            dat20.append(car['stoersteEffekt'])
        else:
            dat20.append(np.nan)
            
        if 'antCylinder' in car.keys():
            dat21.append(car['antCylinder'])
        else:
            dat21.append(np.nan)

print("Append for-loops færdigt, tid:")
print(datetime.datetime.now()-begin_time)

#%%
begin_time = datetime.datetime.now()

dats = {'regNr': dat1, 'foersteRegDato': dat2, 'regStatus': dat3, 'regStatusDato': dat4,
         'maerke': dat5, 'model': dat6, 'variant': dat7, 'artNavn': dat8, 'anvNavn': dat9,
         'totalVaegt': dat10, 'kmPerLiter': dat11, 'drivkraft': dat12, 'synKmStand': dat13,
         'oplStatus': dat14, 'oplStatusDato': dat15, 'ident': dat16, 'stelNr': dat17,
         'siddepladser': dat18, 'slagVol': dat19, 'stoersteEffekt': dat20, 'antCylinder': dat21}

print('Dats er samlet, tid:')
print(datetime.datetime.now()-begin_time)
begin_time = datetime.datetime.now()

df = pd.DataFrame(dats)
print(df[1:11])

print('DataFrame sat op, tid:')
print(datetime.datetime.now()-begin_time)

#%%

begin_time = datetime.datetime.now()

store = pd.HDFStore('D:/xml_streaming/store.h5')

store['df'] = df  # save it

#%%
begin_time = datetime.datetime.now()

store = pd.HDFStore('D:/xml_streaming/store.h5')
store['df']  # load it

print('HDF gemt, tid:')
print(datetime.datetime.now()-begin_time)

#%%

begin_time = datetime.datetime.now()
df_tot.to_csv("C:/Users/SDJO/OneDrive - COWI/SPECIALE/Data/Motorregisteret/df_tot_incSyn.csv", sep=";", index=False)
print("Gemt som csv, tid:")
print(datetime.datetime.now()-begin_time)