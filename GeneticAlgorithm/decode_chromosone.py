def decode_binary_chromosone(chrom, intrevall = [0,1], varLength = 25):
    '''
    Pre: Binary Chromosone, numpy array of ones and zeros
         varLength = 25, the length of each variables in the chromsone
    Ret: Variabels Enconded in the chromsone, Doubles
    '''
    
    diff = intrevall[1]-intrevall[0]
    # TODO should be calculated from number of variables and length of chromsone
    
    numVar = int(len(chrom)/varLength)
    #TODO Assert numVar int

    decode_variable = []
    for i in range(numVar):
        pow = -1
        sum = 0
        for j in range(varLength):
            sum += chrom[i*varLength + j]*2**(pow)
            pow += -1
        decode_variable.append(intrevall[0]+diff/(1-2**(-varLength))*sum)

    return(decode_variable)
