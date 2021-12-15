def DatafromTexT1(nazwa):

    file = open(nazwa)

    content = file.readlines()

    numerFaktury = content[1].split(None, 1)[1]

    miasto = content[45].split(None, 2)[2]

    dataWystawienia = content[46].split(None, 2)[2]

    dataSprzedazy = content[47].split(None, 2)[2]

    sprzedawcaImie = content[49].split()[1]
    sprzedawcaNazwisko = content[49].split()[2]

    nabywcaImie = content[49].split()[3]
    nabywcaNazwisko = content[49].split()[4]

    sprzedawcaKodPocztowy = content[51].split(None, 3)[0]
    sprzedawcaMiasto = content[51].split(None, 3)[1]

    nabywcaKodPocztowy = content[51].split(None, 3)[2]
    nabywcaMiasto = content[51].split(None, 3)[3]

    NIP = content[52].split(None, 1)[1]

    nazwaTowaru1 = content[54].split()[1]
    ilosc1 = content[54].split()[3]
    cenaNetto1 = content[54].split()[4]
    VAT1 = content[54].split()[5]
    VAT1 = float(VAT1[:-1])/100

    nazwaTowaru2 = content[55].split()[1]
    ilosc2 = content[55].split()[3]
    cenaNetto2 = content[55].split()[4]
    VAT2 = content[55].split()[6]
    VAT2 = float(VAT2[:-1])/100

    nazwaTowaru3 = content[56].split()[1]
    ilosc3 = content[56].split()[3]
    cenaNetto3 = content[56].split()[4]
    VAT3 = content[56].split()[6]
    VAT3 = float(VAT3[:-1])/100

    slownie = content[61].split(None, 5)[5]

    formaPlatnosci = content[63].split(None, 2)[2]

    terminZaplaty = content[64].split(None, 2)[2]

    numerKonta = content[69]

    bank = content[70]

    return [numerFaktury, miasto, dataWystawienia, dataSprzedazy,
            sprzedawcaImie, sprzedawcaNazwisko, sprzedawcaKodPocztowy, sprzedawcaMiasto,
            nabywcaImie, nabywcaNazwisko, nabywcaKodPocztowy, nabywcaMiasto, NIP,
            nazwaTowaru1, ilosc1, cenaNetto1, VAT1,
            nazwaTowaru2, ilosc2, cenaNetto2, VAT2,
            nazwaTowaru3, ilosc3, cenaNetto3, VAT3,
            slownie, formaPlatnosci, terminZaplaty, numerKonta, bank]
