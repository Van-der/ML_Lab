'''import numpy as np

def entropy(col):
    counts=col.value_counts()
    prob=counts/len(col)

    if len(counts)<=1:
        return 0
    
    return -np.sum(prob*np.log2(prob))

def info_gain(df,x,y,):
    
    org_ent=entropy(df[y])

    unique_vals=df[x].unique()

    weighted_ent=0

    for val in unique_vals:
        sub=df[df[x]==val]
        sub_ent=entropy(sub[y])
        weighted_ent+=len(sub)/len(df)*sub_ent #weighted average entropy 
    
    return org_ent-weighted_ent

#def find_best_'''