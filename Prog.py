
uniq_vals = lambda cols: df[cols].unique()
desc_col = lambda cols: df[cols].describe()
col_info = lambda cols: df[cols].info()


#Find Frequency of unique values
def find_freq(cols):
    outDF = pd.DataFrame(data = {cols: df[cols].value_counts().index, 
                                       'Freq': list(round(df[cols].value_counts())), 
                                       "Freq_%": list(round(df[cols].value_counts(normalize=True)*100, 2))})
    outDF.index = outDF.index+1
    return outDF


#Find Quartiles information
def QuartileFind(cols):
    q25 = round(df[cols].quantile(.25), 2)
    q75 = round(df[cols].quantile(.75), 2)
    
    print(f'25th quartile = {q25}')
    print(f'75th quartile = {q75}')
    print(f'IQR is {q75-q25}')
    
    return desc_col(cols)


### -----------------------