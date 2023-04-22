import os
import shutil
import tkinter
from tkinter import *
from tkinter import filedialog
import zipfile

dictionary = {
    'introduction': 'Inserisci il PATH \'EPS-JPG\' da comprimere',
    'completed': 'Conversione completata con successo',
    'select-folder': 'Seleziona cartella',
    'find': 'Cerca',
    'generate': 'Genera'
}

class AutoZipArchive:

    def __init__(self, root):
        
        print('First module\'s name: {}'.format(__name__)) 
        
        # Titolo finestra
        root.title('Zipper')
        #  Favicon
        # root.iconbitmap('icon.ico')
        root.iconbitmap('img/icon.ico')
        self.root = root

        # Centratura della finestra rispetto allo schermo
        window_width = root.winfo_reqwidth()
        window_height = root.winfo_reqheight()

        # Ottiene la dimensione della finestra e dello schermo
        position_right = int(root.winfo_screenwidth()/2 - window_width/2)
        position_down = int(root.winfo_screenheight()/2 - 300)

        root.geometry("+{}+{}".format(position_right, position_down))

        self.intro_label = Label(root, text=dictionary['introduction'])
        self.intro_label.grid(row=0, padx=40, pady=10, columnspan=2)
        self.search_button()
        self.generate_button()
        
    #  ============================================================
    # Search folder and select it
    def search_button(self):
        self.search_button = Button(root, text=dictionary['find'], command=self.find_folder)
        self.search_button.grid(row=2, column=0, padx=40, pady=10)


    def find_folder(self):
        self.final_path = filedialog.askdirectory(title='Select a folder')
        self.path_label = Label(root, text=self.final_path).grid(row=1, padx=40, pady=10, columnspan=2)
        return self.final_path

    #  ============================================================
    #  Zip all EPS and JPG files in folder
    def generate_button(self):
        self.search_button = Button(root, text=dictionary['generate'], command=self.zip_file)
        self.search_button.grid(row=2, column=1, padx=40, pady=10)


    def zip_file(self):
        # 1 - Lista dei file nella cartella
        for _, _, files in os.walk(self.final_path):

            # Elimina il file .DS_Store
            if '.DS_Store' in files > 0:
                os.remove('.DS_Store')
                print('File Removed!')

            # Ordinamento dei file per nome
            files.sort()

            # Estrazione di un elemento per coppia
            files_odd = files[1::2]

            # Copia dei file all'esterno
            for file in files:
                shutil.copyfile(self.final_path + '/' + file, './' + file)

            # 2 - Ottenere  il nome dei file un'unica volta per coppia
            for file in files_odd:
                files_name = file.replace('.jpg', '')

                # 3 - Crea un archivio per ogni voce presente nella lista dei numeri dispari
                archive = zipfile.ZipFile(files_name + '.zip', 'w')
                print(archive)

                # 4 - Aggiungere i file all'archivio
                archive.write(files_name + '.eps', compress_type=zipfile.ZIP_DEFLATED)
                archive.write(files_name + '.jpg', compress_type=zipfile.ZIP_DEFLATED)
                archive.close()

                # Cancellazione dei file copiati
                os.remove(files_name + '.eps')
                os.remove(files_name + '.jpg')

                #  Sposta i file ZIP direttamente sul desktop
                shutil.move(files_name + '.zip', 'C:/Users/' + os.getlogin() + '/Desktop')
        
        

#  -------------------------------------
#   Initialization
#  -------------------------------------
if (__name__ == '__main__'):
    # Creazione finestra
    root = tkinter.Tk()
    # cp = AutoZipArchive(root)
    AutoZipArchive(root)
    # Loop
    root.mainloop()

