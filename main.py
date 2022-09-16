# Libraries

import tkinter as tk
from tkinter import ttk

import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

from infobulle import CreateToolTip
from interactive_map import interactive_map

# Constantes

PV = [1500, 1350, 1250, 1150, 1050]
PV1 = ["PACA", "Occitanie", "Corse"]
PV2 = ["Nouvelle Aquitaine"]
PV3 = ["Auvergne Rhône Alpes", "Pays de la Loire"]
PV4 = ["Bretagne", "Normandie", "Centre Val de Loire",
       "Bourgogne Franche Comté"]
PV5 = ["Hauts de France", "Ile de France", "Grand Est"]

listOrientations = ["Est", "Sud-Est", "Sud", "Sud-Ouest", "Ouest"]
listInclinaisons = ["0°", "30°", "60°", "90°"]
f_c = [[1.00, 1.00, 1.00, 1.00, 1.00],
       [0.93, 1.09, 1.15, 1.09, 0.93],
       [0.87, 1.06, 1.13, 1.06, 0.87],
       [0.79, 0.99, 1.06, 0.99, 0.79],
       [0.59, 0.74, 0.77, 0.74, 0.59]]

listMateriaux = ["silicium monocristallin", "silicium polycristallin",
                 "silicium amorphe (couche mince)", "autres couches minces",
                 "diséléniure de cuivre-gallium-indium",
                 "tellure de cadmium"]
K_cr_min = [0.12, 0.10, 0.04, 0.0035, 0.105, 0.095]
K_cr_max = [0.18, 0.16, 0.08, 0.0035, 0.105, 0.095]

listVentilations = ["modules non ventilés",
                    "modules ventilés ou faiblement ventilés",
                    "modules très ventilés ou à ventilation forcée"]
list_f_perf = [0.70, 0.75, 0.80]

listMois = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet',
            'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
listPourcentage = [4.66, 6.05, 9.1, 10.27, 10.41, 10.95, 11.55, 10.93, 9.65,
                   7.31, 4.96, 4.16]

list_conso = [377, 332, 268, 173, 106, 105, 111, 111, 119, 167, 305, 400]
list_conso = [i/sum(list_conso) for i in list_conso]
conso_moyenne_menage_100m2 = 9350
list_conso = [i * conso_moyenne_menage_100m2 for i in list_conso]

# Tkinter

root = tk.Tk()
root.title("Calculer la production d'énergie solaire")
# Defining dimensions
root.geometry("400x300")
# Resizable not allowed
root.resizable(0, 0)
# windows only (remove the minimize/maximize button)
root.attributes('-toolwindow', True)


frame = ttk.Frame(root)


def change_position():
    global region
    region = interactive_map()
    region_box["text"] = region


# Région:
ttk.Label(frame, text='Région:').grid(column=0, row=0, sticky=tk.W)
region_box = ttk.Button(frame, text='Sélectionner position',
                        command=change_position)
region_box.grid(column=1, row=0, sticky=tk.W)

# Orientation:
ttk.Label(frame, text='Orientation du toit:').grid(column=0, row=1, sticky=tk.W)
orientation_box = ttk.Combobox(frame, values=listOrientations, width=25)
orientation_box.grid(column=1, row=1, sticky=tk.W)

# Inclinaison:
ttk.Label(frame, text='Inclinaison du toit:').grid(column=0, row=2, sticky=tk.W)
inclinaison_box = ttk.Combobox(frame, values=listInclinaisons, width=25)
inclinaison_box.grid(column=1, row=2, sticky=tk.W)

# Surface:
ttk.Label(frame, text='Surface de panneaux (en m2):').grid(
    column=0, row=3, sticky=tk.W)
surface_box = ttk.Entry(frame, width=8)
surface_box.grid(column=1, row=3, sticky=tk.W)

# Matériaux:
ttk.Label(frame, text='Materiaux des panneaux:').grid(column=0, row=4, sticky=tk.W)
materiaux_box = ttk.Combobox(frame, values=listMateriaux, width=25)
materiaux_box.grid(column=1, row=4, sticky=tk.W)

path = r"C:\Users\mdenni\Documents\Python\my Python scripts\Photovoltaique\index_infobulle.png"
photo = tk.PhotoImage(file=path)

tooltip_materiaux = ttk.Button(frame, text='information', image=photo)
tooltip_materiaux.grid(column=2, row=4, sticky=tk.W)

info_matériaux = ("Choisir le materiau de base de votre panneau solaire : "
                  "\n Le silicium monocristallin a le meilleur rendement.")
CreateToolTip(tooltip_materiaux, info_matériaux)

# Ventilation:
ttk.Label(frame, text='Ventilation:').grid(column=0, row=5, sticky=tk.W)
ventilation_box = ttk.Combobox(frame, values=listVentilations, width=25)
ventilation_box.grid(column=1, row=5, sticky=tk.W)
tooltip_ventil = ttk.Button(frame, text='information', image=photo)
tooltip_ventil.grid(column=2, row=5, sticky=tk.W)

info_ventil = ("Choisir le type de ventilation : \n Certains panneaux "
               "solaires disposent d'une ventilation intégrée permettant "
               "d'augmenter leurs performances en réduisant leur "
               "température.\n Certains panneaux, appelés aérovoltaïques, "
               "récupèrent cette chaleur produite en l'insufflant dans la "
               "maison en période froide.")
CreateToolTip(tooltip_ventil, info_ventil)


def show_window():

    orientation = orientation_box.get()
    orientation_index = listOrientations.index(orientation)
    inclinaison = inclinaison_box.get()
    inclinaison_index = listInclinaisons.index(inclinaison)
    surface = int(surface_box.get())
    materiaux = materiaux_box.get()
    materiaux_index = listMateriaux.index(materiaux)
    ventilation = ventilation_box.get()
    ventilation_index = listVentilations.index(ventilation)

    if region in PV1:
        region_index = 0
    elif region in PV2:
        region_index = 1
    elif region in PV3:
        region_index = 2
    elif region in PV4:
        region_index = 3
    else:
        region_index = 4

    # Irradiation solaire annuelle
    E_sol = PV[region_index] * f_c[inclinaison_index][orientation_index]

    # Puissance de Crête
    P_cr_min = K_cr_min[materiaux_index] * surface
    P_cr_max = K_cr_max[materiaux_index] * surface

    # Performance du système
    f_perf = list_f_perf[ventilation_index]

    # Calcul de l'énergie fournie en kWh/an
    W_pv_min = E_sol * P_cr_min * f_perf
    W_pv_max = E_sol * P_cr_max * f_perf
    W_pv_moyen = round((W_pv_min + W_pv_max) / 2)

    """
    top = tk.Toplevel()
    top.title("Estimation de la production d'énergie solaire")
    top.geometry("600x600")
    root.resizable(0, 0)
    root.attributes('-toolwindow', True)
    """

    listProduction = [W_pv_moyen*a/100 for a in listPourcentage]

    # Afficher une figure

    plt.figure(figsize=(10, 6), dpi=80)
    ax = plt.subplot(111)
    ax.bar(listMois, listProduction, width=-0.2, color='b', align='edge')
    ax.bar(listMois, list_conso, width=0.2, color='r', align='edge')

    ax.set_title(f"Production annuelle : {W_pv_moyen} kWh - Consommation annuelle moyenne pour un ménage de 100m² bien isolé : {conso_moyenne_menage_100m2} kWh")
    ax.set_xlabel('Mois')
    ax.legend(['Production mensuelle', 'Consommation mensuelle'])
    plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%d kWh'))

    plt.show()


# Button pour calculer:
button_calculer = ttk.Button(frame, text='Calculer', command=show_window)
button_calculer.grid(column=1, row=6, sticky=tk.S)


for widget in frame.winfo_children():
    widget.grid(padx=3, pady=5)

frame.grid(column=0, row=0)


root.mainloop()
