import matplotlib.pyplot as plt
from obspy import UTCDateTime
from obspy.clients.fdsn import Client
from mpl_toolkits.basemap import Basemap

# Fungsi untuk mengambil data gempa dari USGS
def get_earthquake_data():
    client = Client("USGS")
    event_time = UTCDateTime("2023-12-13T00:00:00")
    catalog = client.get_events(starttime=event_time, endtime=event_time + 86400, minmagnitude=7.3)
    return catalog

# Fungsi untuk membuat peta
def plot_earthquake_map(event):
    lat = event.origins[0].latitude
    lon = event.origins[0].longitude

    fig, ax = plt.subplots(figsize=(10, 10))
    m = Basemap(projection='merc', llcrnrlat=-10, urcrnrlat=-5, llcrnrlon=115, urcrnrlon=122, resolution='i', ax=ax)

    m.drawcountries()
    m.drawcoastlines()
    m.drawmapboundary(fill_color='aqua')
    m.drawparallels(range(-10, -5, 1), labels=[1, 0, 0, 0])
    m.drawmeridians(range(115, 123, 1), labels=[0, 0, 0, 1])

    x, y = m(lon, lat)
    m.plot(x, y, 'ro', markersize=10, label='Gempa Magnitudo 7.3')

    plt.title('Lokasi Gempa Bumi')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    earthquake_data = get_earthquake_data()
    
    if len(earthquake_data) > 0:
        event = earthquake_data[0]
        plot_earthquake_map(event)
    else:
        print("Tidak ada data gempa bumi dengan magnitudo 7.3 di Laut Flores pada tanggal tersebut.")
