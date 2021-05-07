from time import sleep, perf_counter
from threading import Thread
#from multiprocessing import shared_memory
global anzahl_kunden
anzahl_kunden = 0
stations_namen = ['Bäcker', 'Wursttheke', 'Käsetheke', 'Kasse']
kunden_pool = []
stations_pool = []
kunden_in_station = [0, 0, 0, 0]
k_tsh = 10
##station über mutex
warteliste1 = []
warteliste2 = []
warteliste3 = []
warteliste4 = []
warteliste = [warteliste1, warteliste2, warteliste3, warteliste4]
#######
bedienliste1 = []
bedienliste2 = []
bedienliste3 = []
bedienliste4 = []
bedienliste = [bedienliste1,bedienliste2,bedienliste3,bedienliste4]
#######
t_echtzeit = [10,60,30,5]
timeouts2= []
timeouts3 = []
timeouts4 = []
t_test = [10,10,10,10]
timeouts = [t_echtzeit, timeouts2, timeouts3, timeouts4, t_test]
#######
pfad1 = []
pfad2 = []
pfade = [pfad1, pfad2]
def station(angebot, position):
    global warteliste
    global bedienliste
    schlange_vor_station = [position]
    #kunden_pool[anzahl_kunden]
    #wache kunden aus threadpool auf
    #eigener pool mit t ids von wartenden kunden get_ident()

    while(True):
        print(f'Station {angebot} bedient im Moment '+
        f'{kunden_in_station[position]} Kunden...'
        + f'\n und {len(bedienliste[position])} warten ')

        sleep(1)
        if(len(warteliste[position]) == 0):
            continue
        xbf = warteliste[position]
        xsf = bedienliste[position]
        xsf.append(xbf[0])
        del xbf[0]
        warteliste[position] = xbf
        sleep(t_echtzeit[position])
        del xsf[0]
        bedienliste[position] = xsf

        #print(f'Station {angebot} hat Kunde {id} fertig bedient ...')

def kunde(id):
    Kundennr = id
    print(f'Kunde {id} betritt Supermarkt ...')
    sleep(t_test[0])
    sp = 0
    sp1 = 3
    for s in stations_pool:
        #xbf
        xsf = any
        if(sp<sp1):
            print(f'Kunde {id} wartet an Station {stations_namen[sp]}')
            warteliste[sp].append(Kundennr)
            print(f'{warteliste[sp]}')
            while(True):
                xsf = bedienliste[sp]

                if id in xsf:
                    break
                else:
                   sleep(t_test[0])
            kunden_in_station[sp] = kunden_in_station[sp] + 1
            
            print(f'Kunde {id} betritt Station {stations_namen[sp]}')
            sleep(t_test[0])  
            #print(f'Kunde {id} geht zu Station {stations_namen[sp+1]}')
            kunden_in_station[sp] = kunden_in_station[sp] - 1
            sp = sp+1

        else:
            kunden_in_station[sp] = kunden_in_station[sp] + 1
            print(f'Kunde {id} betritt Station {stations_namen[sp]}')
            sleep(t_test[0])
            kunden_in_station[sp] = kunden_in_station[sp] - 1
    print(f'Kunde {id} verlässt Supermarkt ...')


def generiere_kunden_pool():
# create and start 10 threads

    for n in range(1, k_tsh):
        t = Thread(target=kunde, args=(n,))
        kunden_pool.append(t)
        t.start()
def generiere_stations_pool():

    for m in range(0,4):
        s = Thread(target=station, args=(stations_namen[m], m))
        stations_pool.append(s)
        s.start()
#thread daraus machen blockt ausgabe
def balanciere_kunden_pool(kunden_pool):
    # wait for the threads to complete
    count = k_tsh
    for t in kunden_pool:
        count = count+1
        t.join()
        sleep(t_test[0])
        z = t
        z = Thread(target=kunde, args=(count,))
        kunden_pool.append(z)
        z.start()
##thread der kunden von station zu station leitet
def main():
    generiere_stations_pool()
    generiere_kunden_pool()
    balanciere_kunden_pool(kunden_pool)

if __name__ == "__main__":
    start_time = perf_counter()
    anzahl_kunden = 0
    main()

    end_time = perf_counter()
