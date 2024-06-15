import matplotlib.pyplot as plt
from obspy import UTCDateTime
from obspy.clients.fdsn import Client
import cartopy.crs as ccrs

def get_earthquake_data():
    """
    Mengambil data gempa dengan magnitudo lebih dari atau sama dengan 7.3 dari USGS.
    """
    client = Client("IRIS")
    event_time = UTCDateTime("2021-12-14T03:20:00")
    catalog = client.get_events(starttime=event_time, endtime=event_time + 86400, minmagnitude=7.3)
    return catalog

def plot_earthquake_map(event):
    """
    Membuat peta lokasi gempa bumi menggunakan Cartopy (tampilan peta satelit).
    """
    lat = event.origins[0].latitude
    lon = event.origins[0].longitude

    # Membuat peta dengan tampilan peta satelit
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw={'projection': ccrs.PlateCarree()})
    ax.coastlines(resolution='10m', color='black', linewidth=1)
    ax.gridlines(draw_labels=True)

    # Menandai lokasi gempa dengan lingkaran merah
    ax.plot(lon, lat, 'ro', markersize=10, label='Gempa Magnitudo 7.3')

    # Menambahkan judul dan legenda
    plt.title('Lokasi Gempa Bumi di Laut Flores (Magnitudo ≥ 7.3)')
    plt.legend()

    # Menampilkan peta satelit
    plt.show()

if __name__ == "__main__":
    earthquake_data = get_earthquake_data()
    
    if len(earthquake_data) > 0:
        event = earthquake_data[0]
        plot_earthquake_map(event)
    else:
        print("Tidak ada data gempa bumi dengan magnitudo 7.3 di Laut Flores pada tanggal tersebut.")
