kuukaudet = ('talvi', 'talvi', 'kevät', 'kevät', 'kevät', 'kesä', 'kesä', 'kesä', 'syksy', 'syksy', 'syksy', 'talvi')
kknumero = int(input('Anna kuukauden numero (1-12): '))
vuodenaika = kuukaudet[kknumero-1]
print('Kuukauden vuodenaika on ' + vuodenaika + '.')