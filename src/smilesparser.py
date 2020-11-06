def main() :
    ## do not remove the following 9 lines !!
    smilesstr = input("Write a SMILES string: ")
    smiles = list(smilesstr)

    atoms = ['C', 'H', 'N', 'O', 'F', 'S']
    numatoms=[0,0,0,0,0,0]
    valatoms=[4,1,3,2,1,2]
    numeros=['1','2','3','4','5','6','7','8','9']

    ## your code should start here


    ## your code should end here, do not remove any line below this one!!

    outstr = "Molecular formula: "
    nindex = 0
    while (nindex < len(atoms)) :
        if (numatoms[nindex] > 0) :
            outstr = outstr + "%s%d" %(atoms[nindex], numatoms[nindex])
        nindex=nindex+1
    
    return outstr

if __name__ == "__main__" :
    print(main())
