#!/usr/bin/env python
# coding: utf-8

# Example DataLoader for the MapYourCity dataset   
# Use train_loader and test_loader    

# Library imports  
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import rasterio 
import os  
import cv2
# Use PyTorch
import torch

# Define the paths to the data   
# input_path = "directory with MapYourCity image files" 
input_path = "/Data/ndionelis/building-age-dataset/"
train_path = input_path + "train/data/"
test_path = input_path + "test/data/"

# Load the csv files
test_df = pd.read_csv(input_path + "test/test-set.csv")
train_df = pd.read_csv(input_path + "train/train-set.csv")
train_df.head()
test_df.head() 

names_data = os.listdir(train_path) # to not load all data in a single tensor, load only the names                    
length_names = len(names_data) 
perm = torch.randperm(length_names)
#idx = perm[:round(0.8*length_names)] # draw round(0.8*length_names) samples     
#torch.save(idx, 'indexForTrainVal.pt')      
idx = torch.load('indexForTrainVal.pt')  

# For the training data
names_data = np.array(names_data) 
idx = idx.numpy() 
training_data = names_data[idx]

# For the test data
#test_data = names_data[~idx]         
mask = np.ones(names_data.size, dtype=bool)  
mask[idx] = False
test_data = names_data[mask]

class Dataset(torch.utils.data.Dataset):  
    def __init__(self, list_IDs):
        self.list_IDs = list_IDs 

    def __len__(self):
        return len(self.list_IDs) 

    def __getitem__(self, index): 
        ID = self.list_IDs[index] 
        X = cv2.imread(train_path + ID + '/street.jpg')
        X = cv2.resize(X, (256, 256)) 
        X2 = cv2.imread(train_path + ID + '/orthophoto.tif') 
        X2 = cv2.resize(X2, (256, 256)) 
        X3 = rasterio.open(train_path + ID + '/s2_l2a.tif').read() 
        X3 = np.transpose(X3, [1, 2, 0]) 
        y = int(open(train_path + ID + '/label.txt', "r").read())
        return X, X2, X3, y 

#BATCH_SIZE = 256
BATCH_SIZE = 32 

# For the training set
train_set = Dataset(training_data.tolist()) 
train_loader = torch.utils.data.DataLoader(train_set, batch_size=BATCH_SIZE, shuffle=True)  
#train_loader_iter = iter(train_loader)
#train_loader_iter_next = next(train_loader_iter) 

# Example for the test set
test_set = Dataset(test_data.tolist())  
test_loader = torch.utils.data.DataLoader(test_set, batch_size=BATCH_SIZE)   
#test_loader_iter = iter(test_loader) 
#test_loader_iter_next = next(test_loader_iter)   

# For the DataLoaders
# use train_loader and test_loader      
train_dataloader = train_loader          
valid_dataloader = test_loader 

# The sizes depend on the BATCH_SIZE  
print(next(iter(train_dataloader))[0].shape) 
print(next(iter(train_dataloader))[1].shape)
print(next(iter(train_dataloader))[2].shape)
print(next(iter(train_dataloader))[3].shape)
