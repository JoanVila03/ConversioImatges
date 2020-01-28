def escriu_capçelera(nom_fitxer):
    with open(nom_fitxer, mode='w') as imatge:
        imatge.write('P1\n')
        imatge.write('3 3\n')
        
if __name__ == '__main__':
    escriu_capçelera('imatge.pbm')