def main():

    def ingresarPaises():
        paises=(input("Ingrese los paises que desea agergar separados por coma: "))
        listPaises=paises.split(", ")
        return listPaises

    def sinRepetir(lista):
        newPaises=list(set(lista))
        return newPaises

    def ordenar(lista):
        lista.sort()
        print("La lista ordenada y sin repetir es", lista)

    listPaises=ingresarPaises()
    newPaises=sinRepetir(listPaises)
    ordenar(newPaises)



if __name__=="__main__":
    main()