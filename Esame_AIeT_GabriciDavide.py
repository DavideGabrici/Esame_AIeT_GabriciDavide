from scipy.stats import gaussian_kde
import numpy as np
import matplotlib.pyplot as plt
import statistics as stat
import sys
from matplotlib.lines import Line2D



# caricamento dati
file_path = sys.argv[1]
dati = np.loadtxt(file_path, unpack=True)
MsuH = dati[0]
m_ini = dati[1]
M_ass = dati[4]
b_y = dati[8]
age_parent = dati[12]


# ====================================================================================================================================================================================================================================================================================================================
# DIAGRAMMA HERTZSPRUNG-RUSSELL
# ====================================================================================================================================================================================================================================================================================================================

# definizione caratteristiche del diagramma
plt.figure(figsize = (12, 8))
plt.xlim(-0.2,1)
plt.ylim(9,-4)
plt.xlabel('Colore b-y')
plt.ylabel('Magnitudine assoluta')
plt.title('Diagramma Hertzsprung-Russell')
# colori selezionati per migliorare la leggibilità
colori = ['darkred','orangered','sandybrown','gold','yellowgreen','lawngreen','forestgreen','lime','aquamarine','cyan','deepskyblue','royalblue','navy','blue','mediumslateblue','blueviolet','darkorcid','plum','purple','fuchsia','mediumvioletred','hotpink','pink']

# costruzione gruppi d'età e etichette
a = 0.65 # passi
b = 1.1 # parametro per costruzione di intervalli non costanti
for idx, j in enumerate(np.arange(0, 13, a)):
    if (j + a)**b < 14:
        gruppo = np.where((j**(b) < age_parent) & (age_parent <= (j + a)**(b)))[0]
        # limitazione a due cifre decimali nel plot della legenda
        label = '{:.2f} - {:.2f} Gyr'.format(j**(b), (j + a)**(b))
        plt.scatter(b_y[gruppo], M_ass[gruppo], marker = '.', s = 10, label = label, color = colori[idx % len(colori)], zorder = j)
  
# plot del grafico
plt.legend(loc = 'upper right', frameon = True, framealpha = 0.5)
plt.savefig('Diagramma H-R.png')
plt.show()


# ====================================================================================================================================================================================================================================================================================================================
# ISTOGRAMMI METALLICITÁ
# ====================================================================================================================================================================================================================================================================================================================

# definizione gruppi d'età
GrI = np.where(age_parent <= 1)[0]
labelI = 'Gruppo I - età minore di 1 Gyr'
GrII = np.where((1 < age_parent) & (age_parent <= 4.5))[0]
labelII = 'Gruppo II - età tra 1 e 4.5 Gyr'
GrIII = np.where(4.5 < age_parent)[0]
labelIII = 'Gruppo III - età maggiore di 4.5 Gyr'

# definizione caratteristiche dell'istogramma
plt.figure(figsize = (12, 8))
plt.xlim(-2,1)
plt.ylim(-50,1000)
plt.xlabel('Metallicità')
plt.ylabel('Conteggi')
plt.title('Distribuzione in metallicità')


# GRUPPO I ===========================================================================================================================================================================================================================================================================================================

# costruzione delle colonne
colonneI = np.linspace(-2, 1, num = 21)
istoI = np.histogram(MsuH[GrI], bins = colonneI)[0]
centro_colonneI = (colonneI[:-1] + colonneI[1:]) / 2

# costruzione istogramma
plt.step(centro_colonneI, istoI, where = 'mid', color = 'darkred', linewidth = 2, label = labelI)

# media e mediana
mediaI = stat.mean(MsuH[GrI])
medianaI = stat.median(MsuH[GrI])
plt.axvline(x = mediaI, color = 'darkred', linestyle = 'dashed', linewidth = 2, label = 'Media Gruppo I')
plt.axvline(x = medianaI, color = 'darkred', linestyle = 'dotted', linewidth = 2, label = 'Mediana Gruppo I')
print(f'Media Gruppo I: {mediaI}')
print(f'Mediana Gruppo I: {medianaI}')


# GRUPPO II ==========================================================================================================================================================================================================================================================================================================

# costruzione delle colonne
colonneII = np.linspace(-2, 1, num = 21)
istoII = np.histogram(MsuH[GrII], bins = colonneII)[0]
centro_colonneII = (colonneII[:-1] + colonneII[1:]) / 2

# costruzione istogramma
plt.step(centro_colonneII, istoII, where = 'mid', color = 'sandybrown', linewidth = 2, label = labelII, alpha = 0.6)

# media e mediana
mediaII = stat.mean(MsuH[GrII])
medianaII = stat.median(MsuH[GrII])
plt.axvline(x = mediaII, color = 'sandybrown', linestyle = 'dashed', linewidth = 2, label = 'Media Gruppo II')
plt.axvline(x = medianaII, color = 'sandybrown', linestyle = 'dotted', linewidth = 2, label = 'Mediana Gruppo II')
print(f'Media Gruppo II: {mediaII}')
print(f'Mediana Gruppo II: {medianaII}')


# GRUPPO III =========================================================================================================================================================================================================================================================================================================

# costruzione delle colonne
colonneIII = np.linspace(-2, 1, num = 21)
istoIII = np.histogram(MsuH[GrIII], bins = colonneIII)[0]
centro_colonneIII = (colonneIII[:-1] + colonneIII[1:]) / 2

# costruzione istogramma
plt.step(centro_colonneIII, istoIII, where = 'mid', color = 'navy', linewidth = 2, label = labelIII, alpha = 0.4)

# media e mediana
mediaIII = stat.mean(MsuH[GrIII])
medianaIII = stat.median(MsuH[GrIII])
plt.axvline(x = mediaIII, color = 'navy', linestyle = 'dashed', linewidth = 2, label = 'Media Gruppo III')
plt.axvline(x = medianaIII, color = 'navy', linestyle = 'dotted', linewidth = 2, label = 'Mediana Gruppo III')
print(f'Media Gruppo III: {mediaIII}')
print(f'Mediana Gruppo III: {medianaIII}')


# plot del grafico
plt.legend(loc = 'upper left', frameon = True, framealpha = 0.5)
plt.savefig('Distribuzione Metallicità.png')
plt.show()


# ====================================================================================================================================================================================================================================================================================================================
# METALLICITÁ VS MASSA
# ====================================================================================================================================================================================================================================================================================================================

# definizione caratteristiche del grafico
plt.figure(figsize = (12, 8))
plt.xlim(0,7)
plt.ylim(-2,1)
plt.xlabel('Massa iniziale')
plt.ylabel('Metallicità')
plt.title('Metallicità vs Massa')


# GRUPPO I ===========================================================================================================================================================================================================================================================================================================

# costruzione grafico
plt.scatter(m_ini[GrI], MsuH[GrI], color = 'darkred', marker = '.', s = 10, label = labelI, alpha=1) 


# GRUPPO II ==========================================================================================================================================================================================================================================================================================================

# costruzione grafico
plt.scatter(m_ini[GrII], MsuH[GrII], color = 'sandybrown', marker = '.', s = 10, label = labelII, alpha=0.6)


# GRUPPO III =========================================================================================================================================================================================================================================================================================================

# costruzione grafico
plt.scatter(m_ini[GrIII], MsuH[GrIII], color = 'navy', marker = '.', s = 10, label = labelIII, alpha=0.4)


# plot del grafico
plt.legend(loc = 'lower right', frameon = True, framealpha = 0.5)
plt.savefig('Metallicità vs Massa.png')
plt.show()


# ====================================================================================================================================================================================================================================================================================================================
# METALLICITÁ VS MASSA - PROFILO DI DENSITÁ
# ====================================================================================================================================================================================================================================================================================================================

# definizione caratteristiche del grafico
plt.figure(figsize = (12, 8))
plt.xlim(0,7)
plt.ylim(-2,1)
plt.xlabel('Massa iniziale')
plt.ylabel('Metallicità')
plt.title('Metallicità vs Massa')


# definizione dei contorni di densità
def plot_density_contours(x, y, color, label):
    xy = np.vstack([x, y])
    kde = gaussian_kde(xy)
    
    # generazione griglia di punti
    x_grid = np.linspace(min(x), max(x), 100)
    y_grid = np.linspace(min(y), max(y), 100)
    X, Y = np.meshgrid(x_grid, y_grid)
    
    # valutazione della densità sulla griglia
    Z = kde(np.vstack([X.ravel(), Y.ravel()])).reshape(X.shape)
    
    # costruzione contorni
    contour = plt.contour(X, Y, Z, colors = color, linewidths = 2)
    return contour


# GRUPPO I ===========================================================================================================================================================================================================================================================================================================

# costruzione grafico
contourI = plot_density_contours(m_ini[GrI], MsuH[GrI], color ='darkred', label = 'Densità Gruppo I')


# GRUPPO II ==========================================================================================================================================================================================================================================================================================================

# costruzione grafico
contourII = plot_density_contours(m_ini[GrII], MsuH[GrII], color = 'sandybrown', label = 'Densità Gruppo II')


# GRUPPO III =========================================================================================================================================================================================================================================================================================================

# costruzione grafico
contourIII = plot_density_contours(m_ini[GrIII], MsuH[GrIII], color = 'navy', label = 'Densità Gruppo III')


#LEGENDA =========================================================================================================================================================================================================================================================================================================

# inserimento legenda
legend_lines = [Line2D([0], [0], color='darkred', lw=2), Line2D([0], [0], color='sandybrown', lw=2), Line2D([0], [0], color='navy', lw=2)]
plt.legend(legend_lines, ['Curve di densità Gruppo I', 'Curve di densità Gruppo II', 'Curve di densità Gruppo III'], loc='lower right', frameon=True, framealpha=0.5)

# plot del grafico
plt.savefig('Densità Metallicità vs Massa.png')
plt.show()
