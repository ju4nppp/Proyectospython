from tkinter import filedialog
from tkinter import *
import pygame
import os

root = Tk() #inicia el programa
root.title('Reproductor de musica') # titulo del programa
root.geometry('500x300') # tamaño de la ventana

pygame.mixer.init() #inicializa el mixer de pygame para reproducir audio

menubar = Menu(root) # creamos un menu para el programa en la parte de arriba
root.config(menu=menubar) # Lo asignamos a la base

songs = []
current_song = ''
paused = False

songlist = Listbox(root, bg='black', fg='yellow', width=100, height=15)
songlist.pack()

def load_music():    #CARGAR LA CANCION AL REPRODUCTOR
    global current_song
    root.directory = filedialog.askdirectory()
    for song in os.listdir(root.directory):
        name, ext = os.path.splitext(song) #dividimos la cancion entre el nombre y su extension
        if ext == '.mp3':
            songs.append(song)

    for song in songs:
        songlist.insert('end', song) #inserta cada cancion al final de la lista
    songlist.selection_set(0) # selecciona la primera cancion en el tope de la lista
    current_song = songs[songlist.curselection()[0]] # esto setea que la currentsong sea la cancion al tope de la lista

def play_music():
    global current_song, paused
    if not paused:
        pygame.mixer.music.load(os.path.join(root.directory, current_song))
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.unpause()
        paused = False
def pause_music():
    global pause
    pygame.mixer.music.pause()
    paused = True
def next_music():
    global current_song, paused
    try:
        songlist.select_clear(0, END)
        songlist.selection_set(songs.index(current_song) + 1)
        current_song = songs[songlist.curselection()[0]]
        play_music()
    except:
        pass
def previous_music():
    global current_song, paused
    try:
        songlist.select_clear(0, END)
        songlist.select_set(songs.index(current_song) - 1)
        current_song = songs[songlist.curselection()[0]]
        play_music()
    except:
        pass

organise_menu = Menu(menubar, tearoff= False) #añadimos submenus
organise_menu.add_command(label='Selecciona carpeta', command= load_music ) # le ponemos etiqueta
menubar.add_cascade(label='Organizar', menu=organise_menu) #le metemos menus cascada al submenu



play_botton_images = PhotoImage(file= 'reproductor_imgs\play2.png') #Guardamos cada imagen como variable
pause_botton_images = PhotoImage(file= 'reproductor_imgs\pause2.png')
next_botton_images = PhotoImage(file= 'reproductor_imgs\mext2.png')
previous_botton_images = PhotoImage(file= 'reproductor_imgs\previous2.png')

control_frame = Frame(root) # creamos un 'marco', que nos permite meterle widgets para que se vea bien
control_frame.pack()

play_btn = Button(control_frame, image=play_botton_images, borderwidth=0, command= play_music) # añadimos cada imagen al control frame como un boton
pause_btn = Button(control_frame, image=pause_botton_images, borderwidth=0, command= pause_music)
next_btn = Button(control_frame, image=next_botton_images, borderwidth=0, command= next_music)
previous_btn = Button(control_frame, image=previous_botton_images, borderwidth = previous_music)

play_btn.grid(row = 0, column = 1, padx = 7, pady = 10) #añadimos cada boton a la grid de la ventana para orga  nizarlo
pause_btn.grid(row = 0, column = 2, padx = 7, pady = 10)
next_btn.grid(row = 0, column = 3, padx = 7, pady = 10)
previous_btn.grid(row = 0, column = 0, padx = 7, pady = 10)

root.mainloop() #corre el programa constantemente