#!/usr/bin/env python
# coding: utf-8

# In[1]:


import load_dataset_module

#Store the data into the variable
transaction_details = load_dataset_module.loadTranscations()

#Function for calculate the min and max  
def max_min_amount_transaction(user_id):
    try:
        # use max function and use the lambda function for calculating
        max_amount_transaction = max((transaction_details[user_id]), key = lambda value: value['amount'])['amount']
        min_amount_transaction = min((transaction_details[user_id]), key = lambda value: value['amount'])['amount']
        return max_amount_transaction,min_amount_transaction
    except:
        print("Error for retrieving the data! Please enter valid details.")
        return None

    #Function for calculate the centroid  
def calculate_centroid(user_id):
    data = transaction_details[user_id]
    x_cord=0
    y_cord=0
    count = 0
    # for loop for adding each x,y values to get individual sum
    try:
        for info in data:
            x_cord=x_cord+info['x_coordinate']
            y_cord=y_cord+info['y_coordinate']
            count = count + 1
        # calculating sum by taking mean of x and y
        x_cent = round(x_cord/ count, 2)
        y_cent = round(y_cord / count, 2)

        return (x_cent,y_cent)
    except:
        print ("Retreiving data error. Please enter the valid details.")
        
#Function for calculate the distance
def calculate_distance(user_id):
    try:
        transaction_text="Please Enter the Transaction ID: "
        transId=int(input(transaction_text))
        # getting centriod
        centroid=calculate_centroid(user_id)
        for key in transaction_details[user_id]:
            # Check the trsaction id in the data
            if key['transaction_id'] == transId:
                trans_data = key
        trans_location=(trans_data['x_coordinate'],trans_data['y_coordinate'])

        # finding distance
        dist=((centroid[0] - trans_location[0])**2 + (centroid[1] - trans_location[1])**2 )**0.5

        return round(dist,2)
    #Error for enter non integer
    except ValueError:
        print("Please enter the interger value!")
    except:
        print("Please enter the valid transaction id")
        
#Function for calculate the total transactions    
def total_transaction(user_id):
    mean = 0
    cnt = 0
    v =0
    #Exception handling block
    try:
        for info in transaction_details[user_id]:
                mean = mean + float(info['amount'])
                cnt += 1
        #Calculating mean
        mean = mean / cnt
        data_v = 0
        for key in transaction_details[user_id]:
            #Calculate the variance of the amount
                data_v = data_v + ((float(key['amount']) - mean) * (float(key['amount']) - mean))      
        total_amount = data_v / cnt
        return round(total_amount,2)
    except:
        print("!!!! Fetching data error !!!!")

#Function for calculate the variance
def calulate_variance(user_id):
   #Exception handling block
    try:
         # calculating variance
        variance=total_transaction(user_id)
        return round(variance,2)
    except:
        print("!!!! Fetching data error !!!!")

#Function for calculate the standard deviation
def calculate_standarddeviation(user_id):
    # call the variance function
    v_data = calulate_variance(user_id)
    std_variance = float(v_data ** 0.5)
    return round(std_variance,2)

#Function for checking the fraud transactions
def check_fraud_transaction(user_id):
    
    try:
        trans =  int(input("Enter transaction  id : "))
        for key in transaction_details[user_id]:
            #Check the transaction id exist in the data
            if key['transaction_id'] == trans:
                #Check the fraud transaction status in the data
                if key['fraud_status'] == 'true':
                    print("Entered transaction is fraud")
                    print("User id",user_id)
                    print("Transaction id",key['transaction_id'])
                    print("Transaction descreption",key['description'])
                    print("Transaction amount",key['amount'])
                    print("Transaction location X",key['x_coordinate'])
                    print("Transaction location y",key['y_coordinate'])
                if key['fraud_status'] == 'false':
                    print("Entered transaction is Good")
                    print("User id",user_id)
                    print("Transaction id",key['transaction_id'])
                    print("Transaction descreption",key['description'])
                    print("Transaction amount",key['amount'])
                    print("Transaction location X",key['x_coordinate'])
                    print("Transaction location y",key['y_coordinate'])
    except ValueError:
        print("Please enter the interger value!")
    except:
        print("Please enter the valid transaction id")
        
#Function Distance between two transactions        
def distancebetweentwotransactions(user_id):
    try:
        trans1 =  int(input("Enter transaction  id 1: "))
        trans2 =  int(input("Enter transaction  id 2: "))
        trans1x = 0
        trans1y = 0
        trans2x = 0
        trans2y = 0
        for info in transaction_details[user_id]:
            if info['transaction_id'] == trans1:
                trans1x = float(info['x_coordinate'])
                trans1y = float(info['y_coordinate'])
            if info['transaction_id'] == trans2:
                trans2x = float(info['x_coordinate'])
                trans2y = float(info['y_coordinate'])
        if(trans1x != 0 and trans2x !=0):
            print ("Distance of X coordinates", trans2x - trans1x)
            print ("Distance of Y coordinates", trans2y - trans1y)
    except ValueError:
        print("Please enter the interger value!")
    except:
        print("Please enter the valid transaction id")
        
#Function Distance between two users
def distanceusertransactions(user_id):
    try:
        user_id2 =  int(input("Please enter another User ID: "))
        cent1x = 0
        cent1y = 0
        cent2x = 0
        cent2y = 0
        centroid_one = calculate_centroid(user_id)
        centtroid_two = calculate_centroid(user_id2)
        # finding distance
        dist=((centroid_one[0] - centtroid_two[0])**2 + (centroid_one[1] - centtroid_two[1])**2 )**0.5
        print ("Distance of two users",dist)
    except ValueError:
        print("Please enter the interger value!")
    except:
        print("Please enter the valid user id")
    
# In[ ]:




