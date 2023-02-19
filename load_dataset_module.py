#!/usr/bin/env python
# coding: utf-8
###Load dataset module
# In[ ]:


# Returns a dictionary of Transactions with exception handling
def loadTranscations():
  # Get Transactions
    try:
        dict_data = {}
        # Open the file and encoding
        with open('Transaction.txt', encoding='utf8') as f:           
            transaction_list = []
            index = 0 
            # Read the data line by line
            for line in f.readlines():
                # Split the data using semicolon
                line_data=line.strip().split(':')
                user=int(line_data[0])
                # retreive the remaining data and stored in to the variable
                user_data={"transaction_id":int(line_data[1]),"description":line_data[2],"amount":float(line_data[3]),"x_coordinate":float(line_data[4]),"y_coordinate":float(line_data[5]),"fraud_status":line_data[6]}       
                # Check the user not in the iteration
                if user not in transaction_list:
                    # Append the data in the object of the user
                    transaction_list.append(user)
                    dict_data[user]=[user_data]                    
                else:
                    # Add the new user data and append in to the list
                    inner_data=dict_data[user]
                    inner_data.append(user_data)
                    dict_data[user]=inner_data
            return dict_data
        # Exception handling for filename error
    except IOError as ioerr:
        print('File error: ' + str(ioerr))
        return None


# In[ ]:




