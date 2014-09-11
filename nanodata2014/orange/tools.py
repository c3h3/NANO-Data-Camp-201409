
import numpy as np
import Orange


ContinuousTypes = [np.int_,  np.int8, np.int16, np.int16, np.int32, np.int64, 
                   np.float_, np.float16, np.float32, np.float64, np.float128]

DiscreteTypes = [np.str_, np.str, np.unicode_, np.unicode]

def auto_convert_to_orange_domains(column_type):
    if column_type in DiscreteTypes:
        return Orange.feature.Discrete
    elif column_type in ContinuousTypes:
        return Orange.feature.Continuous
    else:
        return Orange.feature.Python
    
def convert_string_to_orange_column_type(type_string):
    assert type_string in ["Continuous", "Discrete", "Python"]
    if type_string == "Discrete":
        return Orange.feature.Discrete
    elif type_string == "Continuous":
        return Orange.feature.Continuous
    else:
        return Orange.feature.Python


def df_to_orange_table(df, output_column = None, skip_columns = [], column_types = {}, 
                       problem_type = "classification", discrete2string = 50):
    
    assert problem_type in ["classification", "regression"]
    assert isinstance(discrete2string, int)
    
    cols_list = [ one_col for one_col in df.columns if (one_col != output_column) and (not one_col in skip_columns)] 
    
    if output_column != None:
        cols_list =  cols_list + [output_column]
        
    domains_list = []
    data_list = []
    
    for one_col in cols_list:
        one_col_arr = np.array(df[one_col].values.tolist())
        one_col_arr_type = one_col_arr.dtype.type
        
        if one_col == output_column:
            if (problem_type == "classification") and (not one_col_arr_type in DiscreteTypes):
                one_col_arr = one_col_arr.astype(DiscreteTypes[0])
                one_col_arr_type = one_col_arr.dtype.type
        
        one_col_domain_type = auto_convert_to_orange_domains(one_col_arr_type)
        
        if one_col_domain_type == Orange.feature.Discrete:
            
            unique_values = np.unique(one_col_arr)
            
            if discrete2string > 0:
#                 print one_col
#                 print len(unique_values)
                
                if len(unique_values) > discrete2string:
                    one_col_domain = Orange.feature.String
                    
        if one_col_domain_type == Orange.feature.Discrete:
            one_col_values = unique_values.tolist()
            one_col_domain = one_col_domain_type(one_col,values=one_col_values)
        
        else:
            one_col_domain = one_col_domain_type(one_col)
        
        domains_list.append(one_col_domain)
        data_list.append(one_col_arr.tolist())
    
        
    table_domains = Orange.data.Domain(domains_list)
    orange_table = Orange.data.Table(table_domains,map(list,zip(*data_list)))
    
    return orange_table
        