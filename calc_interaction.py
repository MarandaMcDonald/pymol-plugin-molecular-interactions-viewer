############################################################
#####################  Core Functions  #####################
############################################################

import math

def pdb_read(pdbfile):
    '''
        This function will read into a PDB file format using the readlines command

        **Parameters**

        PDBlist: *list*
            A list of strings in PDB file format
        **Returns**

            Sorted list by acsending resiue number position
        '''
    pdbfile=input("Enter a PDB file\n")
    rawfile=open(pdbfile,"r",  encoding="utf8")
    pdblist=rawfile.readlines()
    rawfile.close()
    return pdblist

def remove(string=str):
    '''
    This function will remove space characters from a string

    **Parameters**

    string: *str*
        The given string to have removed spaces

    **Returns**

        String containing no space characters
    '''
    return string.replace(" ", "")

def only_pdb_first(string=str):
    '''
    This function will remove 'PDB_Files' from the 'filename' variable

    **Parameters**

    string: *str*
        The given string to have removed characters

    **Returns**

        String containing no 'PDB_Files'
    '''
    return string.replace("PDB_Files/", "")

def only_pdb_last(string=str):
    '''
    This function will remove '.pdb' from the 'filename' variable

    **Parameters**

    string: *str*
        The given string to have removed characters

    **Returns**

        String containing no '.pdb'
    '''
    return string.replace(".pdb", "")

def extractxyz(pdbline=str):
    '''
    This function will extract the x, y and z coordinates of an atom from the line of a PDB file

    **Parameters**

    pdbline: *str*
        

    **Returns**

        x, y and z coordinates as a list of floats
    '''
    return([float(pdbline[29:38]),float(pdbline[38:46]),float(pdbline[46:54])])

def calcdistance(list1=list,list2=list):
    '''
    This function will calculate the distance in angstroms between two atoms

    **Parameters**

    list1: *list*
        First list of floats of xyz coordniates for atoms in a PDB file
    
    list1: *list*
        Second list of floats of xyz coordniates as floats for atoms
        

    **Returns**

        Distance in angstroms between two atoms in a PDB file
    '''
    return(math.sqrt((list1[0]-list2[0])**2 + (list1[1]-list2[1])**2 + (list1[2]-list2[2])**2))

def atom_finder(pdblist=list,base=str, atom=str, mylist=list):
    '''
    This function will find a given a given atom in a nucleotide base and append the whole PDB line to a given list

    **Parameters**

    base: *str*
        The nucleotide base that is to be parsed (e.g. A = adenine, G = guanine, C = cytosine, T = thymine)
    
    atom: *str*
        The atom position in the nucleotide base, where the first character 
        is a letter for the elements (e.g. C=carbon, N=nitrogen, O=oxygen),
        and the second charcter is the carbon atom position in the base 
        (e.g. N7 =  the nitrogen atom on carbon 7)
    
    mylist: *list*
        Any given list to be appended with the pdbline of the atom found

    **Returns**

        Appending the atom to a given a list
    '''
    for line in pdblist:
        if (line[0:4]=="ATOM"):
            if (line[19:20]==base):
                if (line[13:16]==atom):
                    mylist.append(line)

def residue_finder(pdblist=list, resn="CYS", mylist="cys_list_unsorted"):
    '''
    This function will read PDB file and search for a given amino acid resiue, 
    and the atomic element specified. This atom will be appended to a list given

    **Parameters**

    pdbfile: *list*
        A list of strings in PDB file format
    **Returns**

        Sorted list by acsending resiue number position
    '''
    for line in pdblist:
        if (line[0:4]=="ATOM") and (line[17:20]==resn) and (line[77:78]=="S"):
            mylist.append(line)

def sorted_pdb(pdblist=list):
    '''
    This function will read a given list in PDB list, and sort to return a list in acsening residue position order

    **Parameters**

    PDBlist: *list*
        A list of strings in PDB file format
    **Returns**

        Sorted list by acsending resiue number position
    '''
    return(sorted(pdblist, key=lambda s: s[22:29]))

def bond_distance(mylist=list, lower=1.95, upper=2.00):
    '''
    This function will calculate if a bond distance is in a given range, then print out values

    **Parameters**

    mylist: *list*
        A list of distances that correspond to potential residue-residue pairs

    lower: *float*
        The lower potential bond distance in angstroms

    uper: *float*
    The upper potential bond distance in angstroms

    **Returns*
    
        Sorted list by acsending resiue number position
    '''
    for i in mylist:
        if upper >i > lower:
            print("{}, {}".format(i[17:29],i))

def atom_to_atom(mylist=list, new_list=list):
    '''
    This function will go through a PDB lists of lines and calculatr all the potential Cysteine residue pairs

    **Parameters**

    mylist: *list*
        A list of of any amount of PDB lines. Can be specific for just one amino acid residue type, or all amino acids.

    new_list: *list*
        The provided new list that PDB lines will be appended to upon the fucntion

    **Returns*
    
        Sorted list by acsending resiue number position
    '''
    # pylint: disable=consider-using-enumerate
    for i in range(len(mylist)):
        for z in range(i):
            new_list.append((mylist[i]) + (mylist[z]))

def oxygen_finder(pdblist=list, atom_name="O", new_list=list):
    '''
    This function will find oxygen atoms in a PDB list and append them to a new list

    **Parameters**

    pdblist: *list*
        A list of readlines of a PDB file

    atom_name: *str*
        The given oxygen atom to be searched (e.g. 'O')

    new_list: *list*
        The provided new list that PDB lines will be appended to upon the fucntion

    **Returns*
    
       Appended list containing all the backbone carbonyl oxygen atoms of the polypeptide
    '''
    for line in pdblist:
        if (line[0:4]=="ATOM") and (line[13:16]==atom_name):
            new_list.append(line)

def nitrogen_finder(pdblist=list, atom_name="N", new_list=list):
    '''
    This function will find oxygen atoms in a PDB list and append them to a new list

    **Parameters**

    pdblist: *list*
        A list of readlines of a PDB file

    atom_name: *str*
        The given Nitrogen atom to be searched (e.g. 'N')

    new_list: *list*
        The provided new list that PDB lines will be appended to upon the fucntion

    **Returns*
    
        Appended list containing all the backbone nitrogen atoms of the polypeptide
    '''
    for line in pdblist:
        if (line[0:4]=="ATOM") and (line[13:16]==atom_name):
            new_list.append(line)

############################################################
###################  Output Peptide FASTA  #################
############################################################

def output_fasta(filename=str, fasta_seq_list=list):
    '''
    This function will output a text of FASTA sequence of peptide in single amino acid code

    **Parameters**

    filename: *str*
        A string of the input PDB file

    fasta_seq_list: *list*
        An empty list to be appended to with the single amino acid code of the peptide



    **Returns*
    
        Appended list an fasta sequecne of given peptide in PDB file
    '''
    aminoacid={}
    aminoacid["ALA"]="A"
    aminoacid["CYS"]="C"
    aminoacid["ASP"]="D"
    aminoacid["GLU"]="E"
    aminoacid["PHE"]="F"
    aminoacid["GLY"]="G"
    aminoacid["HIS"]="H"
    aminoacid["ILE"]="I"
    aminoacid["LYS"]="K"
    aminoacid["LEU"]="L"
    aminoacid["MET"]="M"
    aminoacid["MSE"]="M"
    aminoacid["ASN"]="N"
    aminoacid["PRO"]="P"
    aminoacid["GLN"]="Q"
    aminoacid["ARG"]="R"
    aminoacid["SER"]="S"
    aminoacid["THR"]="T"
    aminoacid["VAL"]="V"
    aminoacid["TRP"]="W"
    aminoacid["UNK"]="X"
    aminoacid["TYR"]="Y"

    # read in a pdb file from command line:

    pdbfileraw=open(filename,"r", encoding="utf8")
    pdbfilelist=pdbfileraw.readlines()

    # make a list for storing amino acids
    aalist=[]

    for line in pdbfilelist:
        if line[0:4]=="ATOM":
            # here only look at CA lines
            if line[13:15]=="CA":
            #copy residue type into list
                aalist.append(line[17:20])

    # here output in FASTA format, with first line beginning with ">" and having info about sequence
    counter=0 # for printing out nicely
    fasta_seq_list=[]
    print(">"+filename)
    for letter in aalist:
        if letter in aminoacid:
            fasta_seq_list.append(aminoacid[letter])
            print(aminoacid[letter],end="")
        else:
            fasta_seq_list.append("X")
            print("X",end="")
    if (counter+1)%40==0:
        print()
    counter+=1

############################################################
###################  Detect Sulfide Bonds  #################
############################################################

def calc_disulfide(filename=str):
    '''
        This function will calculate any disulfide bonds in a PDB file and display in PyMOL 

        **Parameters**

        filename: *string*
            A string with the PDB file name (e.g. 1fdl.pdb)
        **Returns**

            Text of residues with connecting disulfiude bonds
            PyMOL Viewer Structure with disulfiees highlighted and bonds drawn
        '''
    # Initialize reading into PDB file and converting into a list of lines as strings
    
    # To write a pml file
    bondfile=open("disulfide_bonds.pml", "w",  encoding="utf8")
    # pylint: disable=consider-using-f-string
    bondfile.write("load {:}\n".format((filename)))
    bondfile.write("remove resn hoh\n")
    #bondfile.write("color green")

    #pdbfile=input("Enter a PDB file\n")
    rawfile=open(filename,"r",  encoding="utf8")
    pdblist=rawfile.readlines()
    rawfile.close()
    cys_list_unsorted=[]
    
    # To find all the Cysteine residues in the PDB structure
    residue_finder(pdblist,"CYS", cys_list_unsorted)

    # To sort all the Cysteine residues in acsending order
    cys_llist_sorted=sorted_pdb(cys_list_unsorted)

    # To print out the total number of Cysteine residues in the PDB structure
    print("\nThere are",len(cys_llist_sorted), "CYS residues")

    # A dictionary where the keys are the Cys to Cys residue pairs and the values are the bond distances
    cys_distances_list=[]
    cyskeys= []
    cysvalues = []
    cysdict={}

    # To loop through the sorted Cysteine list of residues, and if residues are sequential, then calculate the potential bond distances and
    # store in a new list, cys_distances_list
    for i in range(len(cys_llist_sorted)):
        for z in range(i):
            cys_distances_list.append(calcdistance(extractxyz(cys_llist_sorted[i]), extractxyz(cys_llist_sorted[z])))

    # To provide the the potential S-S bond interactions")
    StoSlist=[]
    atom_to_atom(cys_llist_sorted, StoSlist)

    # To make list of Cysteine-Cysteine distances
    for i in cys_distances_list:
        cysvalues.append(i)

    # To make list of Cysteine-Cysteine combinations
    for i in StoSlist:
        cyskeys.append(i)

    # To make a dictionary matching the residue combination to the bond distance
    for i in range(len(cyskeys)):
        cysdict[cyskeys[i]] = cysvalues[i]

    # To detect if a potential disulfide bond is within the accpetable 2.00 angstroms plus or minus 0.05
    cysValueToKey = {i for i in cysdict if 2.05 >cysdict[i] > 1.95}
    trueCysBondlist = list(cysValueToKey)
    trueDistancelist = list()
    for i in cysdict.values():
            if 2.05 > i> 1.95:
                trueDistancelist.append(i)

    
    # To print out the Cysteine RESN to Cysteine RESN combinations
    # joined_list = "\n".join("{} {}".format(x, y) for x, y in zip(trueCysBondlist, "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"))
    print("There are", len(trueDistancelist), "disulfide bonds\n")
    print("DISULFDE BONDS ( 2 ± 0.05 Å )")

    # To print the joined_list
    for i in trueCysBondlist:
        print(i[17:27], "---", i[97:107],)
    print("\nThanks for using me!")
    
    for line in trueCysBondlist:
        #print("dist disulfide_bond, /{}//{}/{}`{}/{},/{}//{}/{}`{}/{}\n".format(only_pdb_first(only_pdb_last(filename)), line[21:22],line[17:20],remove(line[23:26]),line[13:16], only_pdb_first(only_pdb_last(filename)),line[102:103],remove(line[98:102]),remove(line[103:107]),line[94:96]))
        bondfile.write("dist disulfide_bond, /{}//{}/{}`{}/{},/{}//{}/{}`{}/{}\n".format(only_pdb_first(only_pdb_last(filename)), line[21:22],line[17:20],remove(line[23:26]),line[13:16], only_pdb_first(only_pdb_last(filename)),line[102:103],remove(line[98:102]),remove(line[103:107]),line[94:96]))
        bondfile.write("show sticks, /{}//{}/{}`{}\n".format(only_pdb_first(only_pdb_last(filename)), line[21:22],line[17:20],remove(line[23:26])))
        bondfile.write("show sticks, /{}//{}/{}`{}\n".format(only_pdb_first(only_pdb_last(filename)),line[102:103],remove(line[98:102]),remove(line[103:107])))
        bondfile.write("color atomic, /{}//{}/{}`{}\n".format(only_pdb_first(only_pdb_last(filename)), line[21:22],line[17:20],remove(line[23:26])))
        bondfile.write("color atomic, /{}//{}/{}`{}\n".format(only_pdb_first(only_pdb_last(filename)),line[102:103],remove(line[98:102]),remove(line[103:107])))
 
#Additional changes to alter pymol image
    bondfile.write("\nhide labels, disulfide_bond\n")
    bondfile.write("set dash_length, 0.2500\n")
    bondfile.write("set dash_gap, 0.4\n")
    bondfile.write("set dash_radius, .15\n")                  

############################################################
#############  WC and Non-WC Nucleic Acid Interactions  ####
############################################################

def calc_wc_nwc(filename=str):
    '''
    This function calculate all potential Watson-Crick and Non Watson-Crick noncovlaent bonds in a nucleic acid PDB file

    **Parameters**

    filename: *str*
        A string of the input PDB file

    **Returns*
    
        Appended list an fasta sequecne of given peptide in PDB file
    '''
    # To write a pml file
    bondfile=open("get_bonds.pml", "w")
    bondfile.write("load {:}\n".format((filename)))
    bondfile.write("remove resn hoh\n")
    #bondfile.write("color green")

    rawfile = open(filename, "r")
    pdblist=rawfile.readlines()
    rawfile.close()

    def WC_distance_pymol(list1=list, list2=list):
        '''
        This function will go through a PDB lists of lines and calculatr all the potential Cysteine residue pairs

        **Parameters**

        mylist: *list*
            A list of of any amount of PDB lines. Can be specific for just one amino acid residue type, or all amino acids.

        new_list: *list*
            The provided new list that PDB lines will be appended to upon the fucntion

        **Returns*
        
            Sorted list by acsending resiue number position
        '''
        for line in list1:
            dist1=extractxyz(line)
            for i in list2:
                dist2=extractxyz(i)
                distance = (calcdistance(dist1, dist2))
                if distance < 3.2:
                            bondfile.write("dist WC_hbond, /{}//{}/{}`{}/{},/{}//{}/{}`{}/{}\n".format(only_pdb_first(only_pdb_last(filename)), line[21:22],line[19:20],remove(line[23:26]),line[13:16], only_pdb_first(only_pdb_last(filename)),i[21:22],i[19:20],i[23:26],i[13:15]))
                            # OPTIONAL 'show sticks' in PyMOL structure
                            #bondfile.write("show sticks, /1Z43//{}/{}`{}\n".format(line[21:22],line[19:20],remove(line[23:26]),line[13:16]))
                            #bondfile.write("show sticks, /1Z43//{}/{}`{}\n".format(i[21:22],i[19:20],i[23:26],i[13:15]))

    def Non_WC_distance_pymol(list1=list, list2=list):
        for line in list1:
            dist1=extractxyz(line)
            for i in list2:
                dist2=extractxyz(i)
                distance = (calcdistance(dist1, dist2))
                if 2.5 < distance < 3.2:
                            bondfile.write("dist Non_WC_hbond, /{}//{}/{}`{}/{},/{}//{}/{}`{}/{}\n".format(only_pdb_first(only_pdb_last(filename)),line[21:22],line[19:20],remove(line[23:26]),line[13:16], only_pdb_first(only_pdb_last(filename)),i[21:22],i[19:20],i[23:26],i[13:15]))
                            #print(("dist Non_WC_hbond, /{}//{}/{}`{}/{},/{}//{}/{}`{}/{}\n".format(only_pdb_first(only_pdb_last(filename)),line[21:22],line[19:20],remove(line[23:26]),line[13:16],only_pdb_first(only_pdb_last(filename)),i[21:22],i[19:20],i[23:26],i[13:15])))
                            # OPTIONAL 'show sticks' in PyMOL structure
                            #bondfile.write("show sticks, /1Z43//{}/{}`{}\n".format(line[21:22],line[19:20],remove(line[23:26]),line[13:16]))
                            #bondfile.write("show sticks, /1Z43//{}/{}`{}\n".format(i[21:22],i[19:20],i[23:26],i[13:15]))

    #lists of WC bonding atoms

    #Guanine
    GO6=[]
    GN1=[]
    GN2=[]

    #Cytosine
    CN4=[]
    CN3=[]
    CO2=[]

    #Adenine
    AN6=[]
    AN1=[]

    #Uracil
    UO4=[]
    UN3=[]

    #lists of Non-WC bonding atoms

    #Guanine
    GN3=[]
    GN9=[]
    GN7=[]

    #Adenine
    AN7=[]
    AN9=[]
    AN3=[]

    #Uracil
    UO2=[]

    dist1=[]
    #WC atoms
    (atom_finder(pdblist,"G","O6 ",GO6))
    (atom_finder(pdblist,"G","N1 ",GN1))
    (atom_finder(pdblist,"G","N2 ",GN2))

    (atom_finder(pdblist,"C","N4 ",CN4))
    (atom_finder(pdblist,"C","N3 ",CN3))
    (atom_finder(pdblist,"C","O2 ",CO2))

    (atom_finder(pdblist,"A","N6 ",AN6))
    (atom_finder(pdblist,"A","N1 ",AN1))

    (atom_finder(pdblist,"U","O4 ",UO4))
    (atom_finder(pdblist,"U","N3 ",UN3))   

    #Non-WC atoms
    (atom_finder(pdblist,"G","N3 ",GN3))
    (atom_finder(pdblist,"G","N9 ",GN9))
    (atom_finder(pdblist,"G","N7 ",GN7))


    (atom_finder(pdblist,"A","N7 ",AN7))
    (atom_finder(pdblist,"A","N9 ",AN9))
    (atom_finder(pdblist,"A","N3 ",AN3))

    (atom_finder(pdblist,"U","O2 ",UO2))


    #function to write to a pml file to draw the WC hydrogen bond distance for each WC hydrogen bonding atom pair


    #write to pml file of 
    WC_distance_pymol(GO6, CN4)
    WC_distance_pymol(GN1, CN3)
    WC_distance_pymol(GN2, CO2)

    WC_distance_pymol(AN6, UO4)
    WC_distance_pymol(AN1, UN3)

    bondfile.write("set dash_color, yellow, WC_hbond")

    #Non-WC distances
    #function to write to a pml file to draw the WC hydrogen bond distance for each WC hydrogen bonding atom pair



    atomList=[GO6,GN1,GN2,GN3,GN7,GN9,CN4,CN3,CO2,AN6,AN1,AN7,AN9,AN3,UO4,UN3,]

    #WC BONDING ATOMS LIST
    Gwc=[GO6,GN1,GN2]
    Cwc=[CN4,CN3,CO2]
    Awc=[AN6,AN1]
    Uwc=[UO4,UN3]

    #HOOGSTEIN/NONWC BONDING ATOMS LIST
    Ghoog=[GN3,GN9,GN7]
    Ahoog=[AN7,AN3,AN9]

    #Series of all the atoms tested for hydrogen bond (these are all non-WC)
    #Manually exmained the pymol structure to elimate which distances are not true hydrogen bonds

    #Hoogsteen
    Non_WC_distance_pymol(AN7,UN3)
    Non_WC_distance_pymol(AN6,UO4)

    Non_WC_distance_pymol(GN7,CN3)

    #GO6
    Non_WC_distance_pymol(GO6,CO2)
    Non_WC_distance_pymol(GO6,AN6)
    Non_WC_distance_pymol(GO6,AN1)
    Non_WC_distance_pymol(GO6,AN7)

    Non_WC_distance_pymol(GO6,UN3)

    #GN1
    Non_WC_distance_pymol(GN1,GN3)
    Non_WC_distance_pymol(GN1,GN7)


    Non_WC_distance_pymol(GN1,AN1)
    Non_WC_distance_pymol(GN1,AN3)
    Non_WC_distance_pymol(GN1,AN7)

    Non_WC_distance_pymol(GN1,UO4)
    Non_WC_distance_pymol(GN1,UN3)


    #GN2
    Non_WC_distance_pymol(GN2,GN7)

    Non_WC_distance_pymol(GN2,AN6)
    Non_WC_distance_pymol(GN2,AN1)
    Non_WC_distance_pymol(GN2,AN3)
    Non_WC_distance_pymol(GN2,AN7)

    Non_WC_distance_pymol(GN2,UO4)
    Non_WC_distance_pymol(GN2,UN3)


    #GN3
    Non_WC_distance_pymol(GN3,GO6)

    Non_WC_distance_pymol(GN3,CN3)
    Non_WC_distance_pymol(GN3,CO2)

    Non_WC_distance_pymol(GN3,AN6)
    Non_WC_distance_pymol(GN3,AN1)
    Non_WC_distance_pymol(GN3,AN3)

    Non_WC_distance_pymol(GN3,UO4)
    Non_WC_distance_pymol(GN3,UN3)

    #GN7
    Non_WC_distance_pymol(GN7,GN1)
    Non_WC_distance_pymol(GN7,GN2)
    Non_WC_distance_pymol(GN7,GN7)

    Non_WC_distance_pymol(GN7,CN3)
    Non_WC_distance_pymol(GN7,CO2)

    Non_WC_distance_pymol(GN7,AN6)
    Non_WC_distance_pymol(GN7,AN1)
    Non_WC_distance_pymol(GN7,AN3)
    Non_WC_distance_pymol(GN7,AN7)

    Non_WC_distance_pymol(GN7,UO4)
    Non_WC_distance_pymol(GN7,UN3)


    #AN6
    Non_WC_distance_pymol(AN6,GO6)
    Non_WC_distance_pymol(AN6,GN2)
    Non_WC_distance_pymol(AN6,GN3)
    Non_WC_distance_pymol(AN6,GN7)

    Non_WC_distance_pymol(AN6,CN3)
    Non_WC_distance_pymol(AN6,CO2)

    Non_WC_distance_pymol(AN6,UN3)


    #AN1
    Non_WC_distance_pymol(AN1,GO6)
    Non_WC_distance_pymol(AN1,GN1)
    Non_WC_distance_pymol(AN1,GN2)
    Non_WC_distance_pymol(AN1,GN3)
    Non_WC_distance_pymol(AN1,GN7)

    Non_WC_distance_pymol(AN1,CN3)
    Non_WC_distance_pymol(AN1,CO2)

    Non_WC_distance_pymol(AN1,AN6)
    Non_WC_distance_pymol(AN1,AN1)
    Non_WC_distance_pymol(AN1,AN3)
    Non_WC_distance_pymol(AN1,AN7)

    Non_WC_distance_pymol(AN1,UO4)

    #AN7
    Non_WC_distance_pymol(AN7,GO6)
    Non_WC_distance_pymol(AN7,GN1)
    Non_WC_distance_pymol(AN7,GN2)
    Non_WC_distance_pymol(AN7,GN7)

    Non_WC_distance_pymol(AN7,CN3)
    Non_WC_distance_pymol(AN7,CO2)

    Non_WC_distance_pymol(AN7,AN1)
    Non_WC_distance_pymol(AN7,AN3)

    Non_WC_distance_pymol(AN7,UO4)
    Non_WC_distance_pymol(AN7,UN3)

    #AN3
    Non_WC_distance_pymol(AN3,GO6)
    Non_WC_distance_pymol(AN3,GN1)
    Non_WC_distance_pymol(AN3,GN2)
    Non_WC_distance_pymol(AN3,GN3)
    Non_WC_distance_pymol(AN3,GN7)

    Non_WC_distance_pymol(AN3,CN3)
    Non_WC_distance_pymol(AN3,CO2)

    Non_WC_distance_pymol(AN3,AN6)
    Non_WC_distance_pymol(AN3,AN7)
    Non_WC_distance_pymol(AN3,AN9)

    Non_WC_distance_pymol(AN3,UO4)
    Non_WC_distance_pymol(AN3,UN3)


    #UO4
    Non_WC_distance_pymol(UO4,GN1)
    Non_WC_distance_pymol(UO4,GN2)
    Non_WC_distance_pymol(UO4,GN3)
    Non_WC_distance_pymol(UO4,GN7)

    Non_WC_distance_pymol(UO4,CN3)
    Non_WC_distance_pymol(UO4,CO2)

    Non_WC_distance_pymol(UO4,AN1)
    Non_WC_distance_pymol(UO4,AN3)
    Non_WC_distance_pymol(UO4,AN7)

    #UN3
    Non_WC_distance_pymol(UN3,GO6)
    Non_WC_distance_pymol(UN3,GN1)
    Non_WC_distance_pymol(UN3,GN2)
    Non_WC_distance_pymol(UN3,GN3)
    Non_WC_distance_pymol(UN3,GN7)

    Non_WC_distance_pymol(UN3,CN3)
    Non_WC_distance_pymol(UN3,CO2)

    Non_WC_distance_pymol(UN3,AN6)
    Non_WC_distance_pymol(UN3,AN3)
    Non_WC_distance_pymol(UN3,AN7)

    Non_WC_distance_pymol(UN3,UO4)
    Non_WC_distance_pymol(UO4,UO2)

    #CN4
    Non_WC_distance_pymol(CN4,GN3)
    Non_WC_distance_pymol(CN4,GN7)

    Non_WC_distance_pymol(CN4,AN1)
    Non_WC_distance_pymol(CN4,AN3)
    Non_WC_distance_pymol(CN4,AN7)


    Non_WC_distance_pymol(CN4,UO4)
    Non_WC_distance_pymol(CN4,UN3)

    #CN3
    Non_WC_distance_pymol(CN3,GN3)
    Non_WC_distance_pymol(CN3,GN7)

    Non_WC_distance_pymol(CN3,AN6)
    Non_WC_distance_pymol(CN3,AN1)
    Non_WC_distance_pymol(CN3,AN3)
    Non_WC_distance_pymol(CN3,AN7)

    Non_WC_distance_pymol(CN3,UO4)
    Non_WC_distance_pymol(CN3,UN3)

    #CO2
    Non_WC_distance_pymol(CO2,GO6)
    Non_WC_distance_pymol(CO2,GN3)
    Non_WC_distance_pymol(CO2,GN7)

    Non_WC_distance_pymol(CO2,AN6)
    Non_WC_distance_pymol(CO2,AN1)
    Non_WC_distance_pymol(CO2,AN3)
    Non_WC_distance_pymol(CO2,AN7)


    Non_WC_distance_pymol(CO2,UO4)
    Non_WC_distance_pymol(CO2,UN3)

    #Additional changes to alter pymol image
    bondfile.write("\n")
    bondfile.write("set dash_color, red, Non_WC_hbond")
    bondfile.write("\n")
    bondfile.write("set cartoon_ring_mode,3")
    bondfile.write("\n")
    bondfile.write("hide labels, Non_WC_hbond")
    bondfile.write("\n")
    bondfile.write("hide labels, WC_hbond")
    bondfile.write("\n")
    bondfile.write("show sticks, sidechain extend 1")
    bondfile.write("\n")
    bondfile.write("color grey, sidechain")
    bondfile.write("\n")
    bondfile.write("color atomic, (not elem C)")
    bondfile.write("\n")
    bondfile.write("set dash_length, 0.2500")
    bondfile.write("\n")
    bondfile.write("set dash_gap, 0.4")
    bondfile.write("\n")
    bondfile.write("set dash_radius, .15")

############################################################
###################  Detect Alpha Helice  ##################
############################################################

def alpha_helice(filename=str):
    '''
        This function will detect any potential alpha helical seconday structure in polypeptides

        **Parameters**

        filename: *string*
            A string with the PDB file name (e.g. 1fdl.pdb)
        **Returns**

            Text of residues with alpha helical structure
            PyMOL Viewer Structure with alpha helices highlighted and bonds drawn
        '''

    aminoacid={}
    aminoacid["ALA"]="A"
    aminoacid["CYS"]="C"
    aminoacid["ASP"]="D"
    aminoacid["GLU"]="E"
    aminoacid["PHE"]="F"
    aminoacid["GLY"]="G"
    aminoacid["HIS"]="H"
    aminoacid["ILE"]="I"
    aminoacid["LYS"]="K"
    aminoacid["LEU"]="L"
    aminoacid["MET"]="M"
    aminoacid["MSE"]="M"
    aminoacid["ASN"]="N"
    aminoacid["PRO"]="P"
    aminoacid["GLN"]="Q"
    aminoacid["ARG"]="R"
    aminoacid["SER"]="S"
    aminoacid["THR"]="T"
    aminoacid["VAL"]="V"
    aminoacid["TRP"]="W"
    aminoacid["UNK"]="X"
    aminoacid["TYR"]="Y"

    #to put all the carbonly oxygen ATOM lines in a list
    oxygenAtomList=[]
    nitrogenAtomList=[]

    # To read into PDB file
    print("Alpha-helical structure detector\n")
    rawfile=open(filename,"r", encoding="utf8")
    pdblist=rawfile.readlines()
    rawfile.close()


    oxygen_finder(pdblist,"O  ", oxygenAtomList)
    #print(oxygenAtomList)

    nitrogen_finder(pdblist,"N  ", nitrogenAtomList)
    #print(nitrogenAtomList)

    # To remove the extraneous last 4 nitrogens that cannot participate in alpha helix
    nitrogenAtomList.pop(0)
    nitrogenAtomList.pop(0)
    nitrogenAtomList.pop(0)
    nitrogenAtomList.pop(0)


    distancelist=[]
    for i in range(len(nitrogenAtomList)):
        distancelist.append(calcdistance(extractxyz(oxygenAtomList[i]), extractxyz(nitrogenAtomList[i])))
    aalist=[]
    for line in oxygenAtomList:
        aalist.append(line[17:20])

    # Top output the protein in FASTA format, with first line beginning with ">" and having info about sequence
    singleaalist=[]

    #Make a list of the single letter amino acid FASTA sequence
    for letter in aalist:
        if letter in aminoacid:
            singleaalist.append(aminoacid[letter])
        else:
            singleaalist.append("x")

    #Make a list of the "-" and "H" for the single amino acid FASTA seqeuence
    Hbondlist=[]
    for i in range(len(distancelist)):
        if 0.5 < distancelist[i] < 4.7:
            Hbondlist.append("H")
        else:
            Hbondlist.append("-")
        
    # To account for the 4 i+4 Hydorgen bonding between carbonyl oxygen and amine
    Hbondlist.append("-")
    Hbondlist.append("-")
    Hbondlist.append("-")
    Hbondlist.append("-")

    
    print("\n\n'H' = alpha helical structure")
    print("'-' = non-alpha helical structure")
    print("\n>"+filename)

    #Here is a method to print the fasta sequence and alpha helical structure
    #in an alinged manner, coded up to 531 characters, so this method works for aa < 531, and
    #can be coded for higher MW proteins if necessary
    print(*singleaalist[0:40], sep = "")
    print(*Hbondlist[0:40], sep = "")

    print(*singleaalist[41:81], sep = "")
    print(*Hbondlist[41:81], sep = "")

    print(*singleaalist[82:122], sep = "")
    print(*Hbondlist[82:122], sep = "")

    print(*singleaalist[163:203], sep = "")
    print(*Hbondlist[163:203], sep = "")

    print(*singleaalist[204:244], sep = "")
    print(*Hbondlist[204:244], sep = "")

    print(*singleaalist[245:285], sep = "")
    print(*Hbondlist[245:285], sep = "")

    print(*singleaalist[286:326], sep = "")
    print(*Hbondlist[286:326], sep = "")

    print(*singleaalist[327:367], sep = "")
    print(*Hbondlist[327:367], sep = "")

    print(*singleaalist[368:408], sep = "")
    print(*Hbondlist[368:408], sep = "")

    print(*singleaalist[409:449], sep = "")
    print(*Hbondlist[409:449], sep = "")

    print(*singleaalist[450:490], sep = "")
    print(*Hbondlist[450:490], sep = "")

    print(*singleaalist[491:531], sep = "")
    print(*Hbondlist[491:531], sep = "")

    print(*singleaalist[532:572], sep = "")
    print(*Hbondlist[532:572], sep = "")

############################################################
#####################  End to End Distance  ################
############################################################

def end_to_end_dist(filename=str):
    '''
        This function will calculate the molecular weight of a peptide

        **Parameters**

        filename: *string*
            A string with the PDB file name (e.g. 1fdl.pdb)
        **Returns**

            Text of molecular weight of a peptide 
        '''
    while (True): 
    #will read into file if ".pdb"
        try:
            rawfile=open(filename,"r", encoding="utf8")
            pdblist=rawfile.readlines()
            rawfile.close()
            rawfile=open(filename,"r", encoding="utf8")
            pdblist=rawfile.readlines()
            rawfile.close()

            #Generate a file name to store CA atoms
            outputfile=("outputMWFile")
            CAatoms=open(outputfile,"w", encoding="utf8")

            def stripoutCAatoms(pdb):
                ### goal of function is to take PDB list and return only CA atoms
                returnedlist=[]
                for line in pdb:
                    if line[0:4]=="ATOM" and line[13:15]=="CA":
                        CAatoms.write(line)
                        returnedlist.append(line)
                return(returnedlist)
            CAonly=stripoutCAatoms(pdblist)
            CAatoms.close()

            #extract the first and last atoms from CA atoms file
            with open(outputfile, "r",  encoding="utf8") as file:
                first_line = file.readline()
                for last_line in file:
                    pass

            CAonly= [first_line, last_line]
            
            #time to print!
            print("First Residue:",first_line[17:20])
            print("Last Residue:", last_line[17:20])
            
            print("Distance between Cα atoms of first and last residue: {:.2f} Å".format((calcdistance(extractxyz(first_line), extractxyz(last_line)))))

            print()

            break
        except:
            break

############################################################
###################  Calculate Peptide MW  #################
############################################################

def calc_peptide_mw(filename):
    '''
        This function will calculate the molecular weight of a peptide

        **Parameters**

        filename: *string*
            A string with the PDB file name (e.g. 1fdl.pdb)
        **Returns**

            Text of molecular weight of a peptide 
        '''
# To read into a PDB file and then outputs the protein sequence in FASTA format

    aminoacid={}
    aminoacid["ALA"]="A"
    aminoacid["CYS"]="C"
    aminoacid["ASP"]="D"
    aminoacid["GLU"]="E"
    aminoacid["PHE"]="F"
    aminoacid["GLY"]="G"
    aminoacid["HIS"]="H"
    aminoacid["ILE"]="I"
    aminoacid["LYS"]="K"
    aminoacid["LEU"]="L"
    aminoacid["MET"]="M"
    aminoacid["MSE"]="M"
    aminoacid["ASN"]="N"
    aminoacid["PRO"]="P"
    aminoacid["GLN"]="Q"
    aminoacid["ARG"]="R"
    aminoacid["SER"]="S"
    aminoacid["THR"]="T"
    aminoacid["VAL"]="V"
    aminoacid["TRP"]="W"
    aminoacid["UNK"]="X"
    aminoacid["TYR"]="Y"

    # read in a pdb file from command line:

    pdbfileraw=open(filename,"r",  encoding="utf8")
    pdbfilelist=pdbfileraw.readlines()

    # make a list for storing amino acids
    aalist=[]

    for line in pdbfilelist:
        if line[0:4]=="ATOM":
            # here only look at CA lines
            if line[13:15]=="CA":
            #copy residue type into list
                aalist.append(line[17:20])

    # here output in FASTA format, with first line beginning with ">" and having info about sequence
    counter=0 # for printing out nicely
    fasta_seq_list=[]
    print(">"+filename)
    for letter in aalist:
        if letter in aminoacid:
            fasta_seq_list.append(aminoacid[letter])
        else:
            fasta_seq_list.append("X")
    if (counter+1)%40==0:
        print()
    counter+=1

    #Amino Acid Molecular Weight dictionary
    aaMW={}
    aaMW["A"]=89.09
    aaMW["C"]=121.16
    aaMW["D"]=133.10
    aaMW["E"]=147.13
    aaMW["F"]=165.19
    aaMW["G"]=75.07
    aaMW["H"]=155.16
    aaMW["I"]=131.18
    aaMW["K"]=146.19
    aaMW["L"]=131.18
    aaMW["M"]=149.21
    aaMW["N"]=132.12
    aaMW["P"]=115.13
    aaMW["Q"]=146.15
    aaMW["R"]=174.20
    aaMW["S"]=105.09
    aaMW["T"]=119.12
    aaMW["V"]=117.15
    aaMW["W"]=204.23
    aaMW["Y"]=181.19
    aaMW["["]=0
    aaMW["]"]=0
    aaMW["\n"]=0
    aaMW[","]=0
    aaMW[" "]=0
    aaMW["'"]=0
    aaMW["_"]=0
    aaMW["X"]=0

    #water molecular weight
    aaMW["HOH"]=18.02

    # To print the amino acid sequence from fasta file

    total=0
    for char in fasta_seq_list:
        letter_to_number = aaMW[char]
        total += letter_to_number

    loss_of_water = (int(len(fasta_seq_list))-1) * 18.02
    peptide_mass=total - loss_of_water
    print("Peptide Mass: {:.2f} Daltons".format(peptide_mass))
