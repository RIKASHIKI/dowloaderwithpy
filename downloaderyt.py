import tkinter as tk
from tkinter import ttk
from module.y2mateapi.y2mate_api import Handler
#membuat objek utama tkinter
diana = tk.Tk()
diana.title("tugas uts")

# Membuat label "WELCOME"
label = ttk.Label(diana, text="WELCOME", font=('bold', 16))
label.grid(row=0, column=0, columnspan=4, sticky="n")
# Membuat label "info_label"
info_label = ttk.Label(diana, text="Nama : ahmad thahar al azhari\nnim     : 310122023672\nemail  : hariamd210@gmail.com").grid(row=1, column=0, padx=20, pady=5)
# membuat label untuk tombol agar tidak terpengaruh yang lain
proyek_labelbut = ttk.Label(diana, text="")
proyek_labelbut.grid(row=1, column=2, padx=1, pady=1)
# Membuat label "proyek_label"
proyek_label = ttk.Label(diana, text="")
proyek_label.grid(row=1, column=3, padx=1, pady=1)

#menampilkan antarmuka untuk youtube
def proyek_1():
    # menambahkan ke variabel global
    global masuk_entry
    youtubetitle = ttk.Label(proyek_label, text="YOUTUBE DOWNLOAD", font=('bolt', 14))
    youtubetitle.grid(row=0, column=3, columnspan=2, sticky='n')
    masuk_label = ttk.Label(proyek_label, text='masukkan judul atau link video')
    masuk_label.grid(row=1, column=3)
    # kotak masukkan teks
    masuk_entry = ttk.Entry(proyek_label)
    masuk_entry.grid(row=2, column=3, padx=0)
    # tombol menjalankan pencarian youtube
    masukan_pencarian = ttk.Button(proyek_label, text='cari', command=run_yt)
    masukan_pencarian.grid(row=2, column=4, padx=0)
    # tombol "Tutup Proyek"
    proyek_button1.config(text="BACK", command=Tkembali)


def proyek_2():
    tiktoktitle = ttk.Label(proyek_label, text="no project here", font=('bolt', 14))
    tiktoktitle.grid(row=0, column=3, columnspan=2, sticky='n')
    # tombol "Tutup Proyek"
    proyek_button2.config(text="BACK", command=Tkembali)

#mengembalikan tampilan proyek ke awal
def Tkembali():
    proyek_label.config(text="")
    #menghapus label yang berisi pencarian sebelumnya
    for widget in proyek_label.winfo_children():
        widget.destroy()
    # Mengaktifkan kembali tombol "YOUTUBE" dan "TIKTOK"
    proyek_button1.config(text="YOUTUBE", command=proyek_1)
    proyek_button2.config(text="TIKTOK", command=proyek_2)
    proyek_button1.grid(row=1, column=1, padx=1, pady=1)
    proyek_button2.grid(row=2, column=1, padx=1, pady=1)


#memproses pencarian youtube dan menampilkan hasil
def run_yt():
    global video_quality, video_title, video_size
    user_input = masuk_entry.get()
    if user_input:
        api = Handler(user_input)
        for video_metadata in api.run():
            video_title = video_metadata.get('title', 'judul tidak tersedia')
            video_quality = video_metadata.get('fquality', 'kualitas tidak tersedia')
            video_size = video_metadata.get('size', "ukuran tidak ditemukan")
            outputyt = ttk.Label(proyek_label, text=f"title : {video_title}\nquality : {video_quality}\nsize : {video_size}")
            outputyt.grid(row=3, column=3)
            api.auto_save()
    else:
        #mencegah error saat pertama kali dijalankan
        masuktitle = ttk.Label(proyek_label, text='masukan judul/link terlebih dahulu')
        masuktitle.grid(row=3, column=3)


#membuat tombol tampilkan proyek
proyek_button1 = ttk.Button(proyek_labelbut, text="YOUTUBE", command=proyek_1)
proyek_button2 = ttk.Button(proyek_labelbut, text="TIKTOK", command=proyek_2)
proyek_button1.grid(row=1, column=1, padx=1, pady=1)
proyek_button2.grid(row=2, column=1, padx=1, pady=1)

# Menjalankan loop utama
diana.mainloop()
