import pandas as pd
import numpy as np
from scipy import stats  
import sys
import warnings

warnings.filterwarnings("ignore")


#print(arg_dic)

#exit()

print("\n\n*************************************************************************\n\n\
 	\t\tWelcome to \n\n\
   \tDEXA: Differential Expression Analysis\n\n\
*************************************************************************\n\n\
    Documentation Link: https://github.com/ICAR-BIOINFORMATICS/DEXA \n\n\
*************************************************************************\n\n\
    Institute: ICAR-NIPB & ICAR-IASRI, New Delhi, India\n\n\
    Developed by: \n\
    \tDr. Shbana Begam, ICAR-NIPB, New Delhi, India \n\
    \tDr. Samarth Godara, ICAR-IASRI, New Delhi, India\n\n\
*************************************************************************\n\n")

#first argument - adapter library
path = sys.argv[1]

#second argument - chloroplast reference genome
#rep = int(sys.argv[arg_dic['rep']+1])

print("Opening file: ",path)

#path = '/home/samarth/Downloads/L2FC script/Sample Data.xlsx'

data = pd.read_excel(io = path)

rep = int((len(data.columns)-1)/2)
print("Number of replications: ",rep)

print("1. Calculating Log 2 Fold Change Values...")

#print(data.columns[1:rep+1])
a = np.mean(data[data.columns[1:rep+1]], axis=1)
#print(a)

#print(data.columns[rep+1:rep+rep+1])
b = np.mean(data[data.columns[rep+1:rep+rep+1]], axis=1)
#print(b)

data['L2FC'] = np.log2(np.nan_to_num(np.divide(b, a), nan=1))

#print(data.iloc[0])

def cal_p(rec):
    c = rec[data.columns[1:rep+1]].values
    d = rec[data.columns[rep+1:rep+rep+1]].values
    #print(c)
    #print(d)
    t_stat, p_val = stats.ttest_ind(c.tolist(), d.tolist()) 
    return p_val

print("2. Calculating p-values...")

p_vals = data.apply(cal_p, axis=1) 

#print(p_vals)

data['p_vals'] = p_vals

def test_exp(rec):
    e = rec[data.columns[1:rep+1]].values
    f = rec[data.columns[rep+1:rep+rep+1]].values
    
    g = False
    
    for i in e:
        if i>0.0:
            g=True
            break

    h = False

    for i in f:
        if i>0.0:
            h=True
            break

    if (g and not(h)):
        if np.mean(e)>1:
            return '--'
        else:
            return '-'
    elif (h and not(g)):
        if np.mean(f)>1:
            return '++'
        else:
            return '+'
    else:
        return ' '

print("3. Calculating expressions...")

data['exp'] = data.apply(test_exp, axis=1)

#print(data)

print("4. Saving the output file 1...")

new_path = path[:-5]+"_results.xlsx"

data.to_excel(new_path, index=False)  

print("File saved: ", new_path)

print("5. Filtering the results...")

p_data = data[(data.p_vals<=0.05) & (data.p_vals>=0.0)]

def exp_type(rec):
    if rec['exp']=='--':
        return "Deactivator"
    elif rec['exp']=='++':
        return "Activator"
    elif rec['L2FC']>0:
        return "Significantly High Expression"
    elif rec['L2FC']<0:
        return "Significantly Low Expression"
    else:
        return "No Significance"

p_data['Description'] = p_data.apply(exp_type, axis=1)

p_data = p_data[(p_data.exp!='+') & (p_data.exp!='-')]

print("6. Saving the gene list...")

new_path = path[:-5]+"_gene_list.xlsx"

p_data = p_data.sort_values(['Description'])

p_data = p_data[p_data.columns[:-2].tolist() + p_data.columns[-1:].tolist()]

p_data.to_excel(new_path, index=False)

print("File saved: ", new_path)

print("Execution finished...\n\n")

