kanta_str = input('Anna suorakulmion kannan pituus metreinä:')
korkeus_str = input('Anna suorakulmion korkeus metreinä:')
kanta = float(kanta_str)
korkeus = float(korkeus_str)
piiri = kanta+kanta+korkeus+korkeus
ala = kanta * korkeus
print('Suorakulmion piiri on: ' + str(piiri) + 'm')
print('Suorakulmion pinta-ala on: ' + str(ala) + 'm\u00b2')