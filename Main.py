def main():

    def ingresarPaises():
        paises=(input("Ingrese los paises que desea agergar separados por coma: "))
        listPaises=paises.split(", ")
        print("La lista con los paises ingresados es:",listPaises)
        return listPaises

    def sinRepetir(lista):
        newPaises=list(set(lista))
        print("la lista con los paises ingresados sin repetir es:",newPaises)

    listPaises=ingresarPaises()
    sinRepetir(listPaises)


if __name__=="__main__":
    main()