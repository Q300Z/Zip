import os
import shutil
import time
from time import gmtime, strftime

start = time.time()

# La ou se trouve vos mangas NON zipé, oublié pas les "/" pas d'anti slash !
path = ""
# La ou se trouverons vos mangas zipé, oublié pas les "/" pas d'anti slash !
out = ""

nbchapg = 0
nbmangag = 0


def archive(path, out, nbchapg, nbmangag):
    list = os.listdir(path)  # Liste les Sites
    # print(list)
    i = 0
    while i < 2:
        for x in list:
            if "desktop.ini" in x:
                list.remove(x)
            elif ".nomedia" in x:
                list.remove(x)
        i = i + 1

    nbsite = len(list)  # Nb site
    a = 0
    for site in list:
        sitepath = path + "/" + site

        outsite = out + "/" + site
        if os.path.exists(outsite):  # Vérifie les présences du dossiers dans les Archives
            #print("Le dossiers existe déjà : " + outsite)
            a = a + 1
        else:  # ... sinon le créer
            os.mkdir(outsite)
        listmanga = os.listdir(sitepath)  # Liste les Mangas
        nbmanga = len(listmanga)  # Nb mangas
        nbmangag = nbmanga + nbmangag

        for manga in listmanga:
            mangapath = sitepath + "/" + manga

            outmanga = outsite + "/" + manga
            # Vérifie les présences du dossiers dans les Archives
            if os.path.exists(outmanga):
                #print("Le dossiers existe déjà : " + outmanga)
                a = a + 1
            else:  # ... sinon le créer
                os.mkdir(outmanga)

            listchap = os.listdir(mangapath)  # Liste les Chapitres
            nbchap = len(listchap)  # Nb chap
            nbchapg = nbchap + nbchapg

            for chap in listchap:
                chappath = mangapath + "/" + chap
                outchap = outmanga + "/" + chap
                # Vérifie les présences de l'archive
                if os.path.exists(outchap + ".zip"):
                    #print("L'archive existe déjà : " + outchap + ".zip")
                    a = a + 1
                else:  # ... sinon la créer
                    # Archive les chapitres
                    shutil.make_archive(outchap, 'zip', chappath)
                    print("Archivage : " + manga + " | chapitre : " + chap)
    print("Nombre de site : " + str(nbsite) + " | Nombre de manga : " +
          str(nbmangag) + " | Nombre de chapitre : " + str(nbchapg))


archive(path, out, nbchapg, nbmangag)

end = time.time()
elapsed = end - start
print("Temps d'excution : " + strftime("%H:%M:%S", gmtime(elapsed)))
