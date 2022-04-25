
import pandas as pd
import numpy as np

def add_sum(path, sheet, output_path, output_sheet):
    df = pd.read_excel(path, sheet_name='Sheet1')
    #x = df.iloc[:, [0,1,2,3,4,5,6,7]].values
    x = df.iloc[:,:].values
    labels = df.iloc[:, 8].values
    np_array = np.zeros(len(x))
    for i in range(len(x)):
        # org, edu, com ending
        np_array[i] += x[i,3]
        np_array[i] += x[i,4]
        np_array[i] += x[i,5]
        
        # keyword in entry
        np_array[i] += x[i,7]
        
        # tutorial, wiki, introduction, course, class, lecture, video, graph, diagram, book
        #index = 8
        #np_array[i] += x[i,index] + x[i,index+1] + x[i,index+2] + x[i,index+3] + x[i,index+4] + x[i,index+5] + x[i,index+6] + x[i,index+7] + x[i,index+8] + x[i,index+9]
        
        # keyword_count
        np_array[i] += x[i,19]
        
        # content diagram, example, formula, graph, code, video, book
        j = 21
        np_array[i] += x[i,j] + x[i,j+1] + x[i,j+2] + x[i,j+3] + x[i,j+4] + x[i,j+5] + x[i,j+6]
        

    df['sum'] = np_array.tolist()
    # statistics of np_array
    print(df)
    print(np.mean(np_array))
    print(np.std(np_array))
    print(np.percentile(np_array, [25, 50, 75]))
    
    
    # if path == output_path:
    #     print("writing file to " + output_path)
    #     with pd.ExcelWriter(output_path,
    #                     mode='a') as writer:  
    #         df.to_excel(writer, sheet_name=output_sheet)
    # else:
    df.to_excel(output_path,
         sheet_name=output_sheet) 
    
    
