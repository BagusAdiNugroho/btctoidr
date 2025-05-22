def btc_to_idr(jumlah_btc, harga_per_btc_usd, kurs_usd_to_idr):
    nilai_usd = jumlah_btc * harga_per_btc_usd
    nilai_idr = nilai_usd * kurs_usd_to_idr
    return nilai_idr

# Contoh penggunaan:
jumlah_btc = 0.01065625	
harga_per_btc_usd = 1100000
kurs_usd_to_idr = 17000

rupiah = btc_to_idr(jumlah_btc, harga_per_btc_usd, kurs_usd_to_idr)
print(f"Nilai Rupiah: Rp{rupiah:,.2f}")