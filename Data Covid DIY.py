import numpy as np
import pandas as pd
import requests
import json
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

resp_diy = requests.get('https://data.covid19.go.id/public/api/prov_detail_DAERAH_ISTIMEWA_YOGYAKARTA.json')
cov_diy_raw = resp_diy.json()

cov_diy = pd.DataFrame(cov_diy_raw['list_perkembangan'])
print('Info cov_diy:\n', cov_diy.info())
print('\nLima data teratas cov_diy:\n', cov_diy.head())

cov_diy_tidy = (cov_diy.drop(columns = [item for item in cov_diy.columns
                                            if item.startswith('AKUMULASI') or
                                            item.startswith('DIRAWAT')
                                           ])
                 .rename(columns=str.lower)
                 .rename(columns={'kasus':'kasus_baru'})
                 )

cov_diy_tidy['tanggal'] = pd.to_datetime(cov_diy_tidy['tanggal'] * 1e6, unit='ns')

print("Data lima teratas", cov_diy_tidy.head())

#Visualisasi Jumlah Penambahan Kasus Covid
plt.clf()
fig, ax = plt.subplots(figsize=(10,5))
ax.bar(data=cov_diy_tidy, x='tanggal', height='kasus_baru', color='salmon')
fig.suptitle("Kasus Harian Positif COVID-19 di Daerah Istimewa Yogyakarta", 
             y=1.00, fontsize=16, fontweight='bold', ha='center')
ax.set_title("Terjadi pelonjakan kasus di awal bulan Agustus",
             fontsize=10)
ax.set_xlabel('')
ax.set_ylabel("Jumlah kasus")
ax.text(1, -0.3, "Sumber data: covid.19.go.id", color='blue',
        ha='right', transform=ax.transAxes)
ax.set_xticklabels(ax.get_xticks(), rotation=90)


ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))

plt.grid(axis='y')
plt.tight_layout()
fig.autofmt_xdate()
plt.show()

#Visualisasi Jumlah Penambahan Kasus Sembuh
plt.clf()
fig, ax = plt.subplots(figsize=(10,5))
ax.bar(data=cov_diy_tidy, x='tanggal', height='sembuh', color="olivedrab")
ax.set_title("Kasus Harian Sembuh Dari COVID-19	di Daerah Istimewa Yogyakarta",
             fontsize=19)
ax.set_xlabel('')
ax.set_ylabel("Jumlah kasus")
ax.text(1, -0.3, "Sumber data: covid.19.go.id", color='blue',
        ha='right', transform=ax.transAxes)
ax.set_xticklabels(ax.get_xticks(), rotation=90)

ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))

plt.grid(axis='y')
plt.tight_layout()
plt.show()

resp_diy = requests.get('https://data.covid19.go.id/public/api/prov_detail_JAWA_BARAT.json')
cov_diy_raw = resp_diy.json()
cov_diy = pd.DataFrame(cov_diy_raw['list_perkembangan'])

cov_diy_tidy = (cov_diy.drop(columns=[item for item in cov_diy.columns
if item.startswith('AKUMULASI')
or item.startswith('DIRAWAT')])
.rename(columns=str.lower)
.rename(columns={'kasus': 'kasus_baru'})
)
cov_diy_tidy['tanggal'] = pd.to_datetime(cov_diy_tidy['tanggal']*1e6, unit='ns')


#Visualisasi Jumlah Penambahan Kasus Meninggal
plt.clf()
fig, ax = plt.subplots(figsize=(10,5))
ax.bar(data=cov_diy_tidy, x='tanggal', height='meninggal', color='slategrey')
ax.set_title('Kasus Harian Meninggal Dari COVID-19 di Daerah Istimewa Yogyakarta',
fontsize=19)
ax.set_xlabel('')
ax.set_ylabel('Jumlah kasus')
ax.text(1, -0.3, 'Sumber data: covid.19.go.id', color='blue',
ha='right', transform=ax.transAxes)
ax.set_xticklabels(ax.get_xticks(), rotation=45)

ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))

plt.grid(axis='y')
plt.tight_layout()
plt.show()

# Kode sudah diadaptasi dan disempurnakan dari tutorial DQ Lab

