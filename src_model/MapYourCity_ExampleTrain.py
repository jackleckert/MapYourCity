#!/usr/bin/env python
# coding: utf-8
# # Main Lines: 295 and 816            
import imageio.v2 as io 
import matplotlib.pyplot as plt 
FOLDER = '/Data/ndionelis/StreetDataset/'     
import torchvision            
import random    
import torchvision.transforms as T                       
def get_random_pos(img, window_shape): 
    w, h = window_shape
    W, H = img.shape[-2:]
    x1 = random.randint(0, W - w - 1)
    x2 = x1 + w
    y1 = random.randint(0, H - h - 1)
    y2 = y1 + h 
    return x1, x2, y1, y2
WINDOW_SIZE = (600, 600)          
# image1 = torchvision.io.read_image(FOLDER+'0/0_00_311059203.jpg')         
# plt.imshow(image1.permute(1, 2, 0))   

import os          
import imageio.v2 as io
import shutil
from PIL import Image
from torchvision import transforms, datasets
import numpy as np      
import matplotlib.pyplot as plt    
from torch.utils.data import Dataset
from sklearn.preprocessing import LabelEncoder
import torch
from torchsummary import summary
import random
from tqdm import tqdm
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torchvision 

FOLDER = '/Data/ndionelis/StreetDataset/'             
MAINFOLDER = '/Data/ndionelis/'   
#NUMWORKERS = 6                    
NUMWORKERS = 0 
#BATCH_SIZE = 256        
BATCH_SIZE = 32
#epochs = 200       
epochs = 120
SEED = random.randint(1, 10000)
print('The random seed is: ' + str(SEED) + '.')  
torch.cuda.empty_cache()
random.seed(SEED)
np.random.seed(SEED) 
torch.manual_seed(SEED)   
torch.cuda.manual_seed_all(SEED)

data_transforms = {
    'train': transforms.Compose([
        transforms.Resize((512, 512)),
        transforms.ToTensor(),
    ]),
    'val': transforms.Compose([
        transforms.Resize((512, 512)), 
        transforms.ToTensor(), 
    ]),
    'test': transforms.Compose([ 
        transforms.Resize((512, 512)), 
        transforms.ToTensor(),  
    ]),
}
data_dir = MAINFOLDER + 'TheNewDataset'   
image_datasets = {x: datasets.ImageFolder(os.path.join(data_dir, x),
                                        data_transforms[x])
                for x in ['train', 'val', 'test']}    
train_dataset = image_datasets['train']             
valid_dataset = image_datasets['test']  
print('Length of training set: ' + str(len(image_datasets['train'])))     
print('Length of validation set: ' + str(len(image_datasets['val'])))
print('Length of test set: ' + str(len(image_datasets['test'])))

dataloaders = {x: torch.utils.data.DataLoader(image_datasets[x], batch_size=BATCH_SIZE,
                                            shuffle=True, num_workers=NUMWORKERS) 
            for x in ['train', 'val', 'test']}
train_dataloader = dataloaders['train']      
valid_dataloader = dataloaders['test'] 

labels = np.array(dataloaders['train'].dataset.targets) 
lb = LabelEncoder() 
labels = lb.fit_transform(labels)
print(f"Total Number of Classes: {len(lb.classes_)}") 
device = torch.device("cuda:0")
print('Device: ' + str(device))   

import torchvision.transforms.functional as fn 
import paths_config
def a9g9a9e9a9t9alaoader_CIFAR10(train, batch_size, augmentation, dataloader_kwargs):
    transform = transforms.Compose(
        []
        + [transforms.ToTensor(), ]
    ) 
    dset = datasets.CIFAR10(paths_config.location_dict['CIFAR10'], train, download=True, transform=transform)
    # i = 0
    # ppaath = '/Data/ndionelis/StreetDataset/5/'
    # for file in [f for f in
    #              os.listdir(ppaath)
    #              if
    #              f.endswith('.jpg')]:
    #     img = Image.open(
    #         ppaath + str(
    #             file))
    #     resize = fn.resize(img, size=(512, 512))
    #     for file2 in [f2 for f2 in os.listdir(path2) if f2.endswith(file[5:-4]+'.tif')]:
    #         img2 = Image.open(
    #         path2 + str(
    #             file2))
    #         resize2 = fn.resize(img2, size=(512, 512))
    #         resize = np.concatenate((resize, resize2))
    #         # plt.imshow(resize)
    dset.targets = torch.load('/Data/ndionelis/dtsettargets0.pt') 
    dset.data = torch.load('/Data/ndionelis/dtsetdata0a.pt')
    dset.data = np.concatenate((dset.data, torch.load('/Data/ndionelis/dtsetdata0b.pt')), axis=0)
    dset.targets = np.concatenate((dset.targets, torch.load('/Data/ndionelis/dtsettargets1.pt')), axis=0)
    dset.data = np.concatenate((dset.data, torch.load('/Data/ndionelis/dtsetdata1.pt')), axis=0)
    dset.targets = np.concatenate((dset.targets, torch.load('/Data/ndionelis/dtsettargets2.pt')), axis=0)
    dset.data = np.concatenate((dset.data, torch.load('/Data/ndionelis/dtsetdata2.pt')), axis=0)
    dset.targets = np.concatenate((dset.targets, torch.load('/Data/ndionelis/dtsettargets3.pt')), axis=0)
    dset.data = np.concatenate((dset.data, torch.load('/Data/ndionelis/dtsetdata3.pt')), axis=0)
    dset.targets = np.concatenate((dset.targets, torch.load('/Data/ndionelis/dtsettargets4.pt')), axis=0)
    dset.data = np.concatenate((dset.data, torch.load('/Data/ndionelis/dtsetdata4.pt')), axis=0)
    dset.targets = np.concatenate((dset.targets, torch.load('/Data/ndionelis/dtsettargets5.pt')), axis=0)
    dset.data = np.concatenate((dset.data, torch.load('/Data/ndionelis/dtsetdata5.pt')), axis=0)
    dset.targets = np.concatenate((dset.targets, torch.load('/Data/ndionelis/dtsettargets6.pt')), axis=0).tolist()  
    dset.data = np.concatenate((dset.data, torch.load('/Data/ndionelis/dtsetdata6.pt')), axis=0)   
    length_names = len(dset)
    perm = torch.load('/Data/ndionelis/chaClassiTopVperm.pt')
    idx = perm[:round(0.7*length_names)] # draw round(0.7*length_names) samples
    #names_data = np.array(names_data)
    idx = idx.numpy()
    #training_data = names_data[idx]     
    from torch.utils.data import Subset
    training_data = Subset(dset, idx)
    idx2 = perm[round(0.7*length_names):round(0.85*length_names)]
    idx2 = idx2.numpy()
    #forVa_data = names_data[idx2]    
    forVa_data = Subset(dset, idx2)
    idx3 = perm[round(0.85*length_names):]
    idx3 = idx3.numpy()
    #test_data = names_data[idx3]        
    test_data = Subset(dset, idx3)
    print('Length of training set: ' + str(len(training_data)))   
    print('Length of validation set: ' + str(len(forVa_data)))
    print('Length of test set: ' + str(len(test_data)))
    loadertrain = torch.utils.data.DataLoader(
        training_data,
        batch_size=batch_size,
        shuffle=True,
        **dataloader_kwargs, drop_last=True)
    loaderval = torch.utils.data.DataLoader(
        forVa_data,
        batch_size=batch_size,
        shuffle=True,
        **dataloader_kwargs, drop_last=True)
    loadertest = torch.utils.data.DataLoader(
        test_data,
        batch_size=batch_size,
        shuffle=False,
        **dataloader_kwargs, drop_last=False) 
    return loadertrain, loaderval, loadertest, training_data, forVa_data, test_data 

def nnewa9g9a9e9a9t9alaoader_CIFAR10(train, batch_size, augmentation, dataloader_kwargs): 
    transform = transforms.Compose(
        []
        + [transforms.ToTensor(), ]
    ) 
    dset = datasets.CIFAR10(paths_config.location_dict['CIFAR10'], train, download=True, transform=transform)
    # i = 0  
    # ppaath = '/Data/ndionelis/StreetDataset/2/'      
    # for file in [f for f in
    #              os.listdir(ppaath)
    #              if
    #              f.endswith('.jpg')]:
    #     #print(file) 
    # i = 0    
    # ppaath = '/Data/ndionelis/StreetDataset/4/'
    # for file in [f for f in
    #              os.listdir(ppaath)
    #              if
    #              f.endswith('.jpg')]:
    #     if file[0] != '6' and not file.startswith('3_13_w136228316'):     
    #         img = Image.open(
    #             ppaath + str(
    #                 file))
    #         resize = fn.resize(img, size=(32, 32))
    #         for file2 in [f2 for f2 in os.listdir(path2) if f2.endswith(file[5:-4]+'.tif')]:
    #             try:
    #                 img2 = Image.open(
    #                 path2 + str(
    #                     file2))
    #             except:
    #                 # os.system('gdal_translate -of PNG ' + path2 + str(
    #                 #     file2) + ' ' + path2 + str(
    #                 #     file2[:-4]) + '.png')    
    #                 try:
    #                     img2 = Image.open(
    #                         path2 + str(
    #                         file2[:-4]) + '.png') 
    #                 except:
    #                     os.system('gdal_translate -of PNG ' + path2 + str(
    #                         file2) + ' ' + path2 + str(
    #                         file2[:-4]) + '.png')     
    #                     img2 = Image.open(
    #                         path2 + str(
    #                         file2[:-4]) + '.png')                          
    #                 #continue  
    #             resize2 = fn.resize(img2, size=(32, 32))
    #             resize = np.concatenate((resize, resize2))
    #             # plt.imshow(resize)
    dset.targets = torch.load('/Data/ndionelis/alltargets0.pt') 
    # #torch.save(total_pil_to_tensor2, '/Data/ndionelis/alldata6.pt')  
    dset.data = torch.load('/Data/ndionelis/alldata0.pt') 
    dset.targets = torch.cat((dset.targets, torch.load('/Data/ndionelis/alltargets1.pt')), 0)      
    dset.data = np.concatenate((dset.data, torch.load('/Data/ndionelis/alldata1.pt')), axis=0)     
    dset.targets = torch.cat((dset.targets, torch.load('/Data/ndionelis/alltargets2.pt')), 0)   
    dset.data = np.concatenate((dset.data, torch.load('/Data/ndionelis/alldata2.pt')), axis=0)   
    dset.targets = torch.cat((dset.targets, torch.load('/Data/ndionelis/alltargets3.pt')), 0)   
    dset.data = np.concatenate((dset.data, torch.load('/Data/ndionelis/alldata3.pt')), axis=0)   
    dset.targets = torch.cat((dset.targets, torch.load('/Data/ndionelis/alltargets4.pt')), 0)   
    dset.data = np.concatenate((dset.data, torch.load('/Data/ndionelis/alldata4.pt')), axis=0)   
    dset.targets = torch.cat((dset.targets, torch.load('/Data/ndionelis/alltargets5.pt')), 0)   
    dset.data = np.concatenate((dset.data, torch.load('/Data/ndionelis/alldata5.pt')), axis=0)   
    dset.targets = torch.cat((dset.targets, torch.load('/Data/ndionelis/alltargets6.pt')), 0).tolist()     
    dset.data = np.concatenate((dset.data, torch.load('/Data/ndionelis/alldata6.pt')), axis=0)   
    # print(len(dset))                          
    #length_names = len(names_data)
    length_names = len(dset)
    #print(length_names)   
    #perm = torch.randperm(length_names)       
    # #torch.save(perm, '/Data/ndionelis/alldatachaClassiTopVperm.pt')  
    perm = torch.load('/Data/ndionelis/alldatachaClassiTopVperm.pt') 
    # #torch.save(perm, '/Data/ndionelis/newchaClassiTopVperm.pt')      
    #perm = torch.load('/Data/ndionelis/newchaClassiTopVperm.pt')
    # # torch.save(perm, '/Data/ndionelis/chaClassiTopVperm.pt') 
    #perm = torch.load('/Data/ndionelis/chaClassiTopVperm.pt')
    #idx = perm[:round(0.8*length_names)] # draw round(0.8*length_names) samples    
    idx = perm[:round(0.7*length_names)] # draw round(0.7*length_names) samples
    #names_data = np.array(names_data)
    idx = idx.numpy()
    #training_data = names_data[idx]      
    from torch.utils.data import Subset
    training_data = Subset(dset, idx)
    idx2 = perm[round(0.7*length_names):round(0.85*length_names)]
    idx2 = idx2.numpy()
    #forVa_data = names_data[idx2]    
    forVa_data = Subset(dset, idx2)
    idx3 = perm[round(0.85*length_names):]
    idx3 = idx3.numpy()
    #test_data = names_data[idx3]         
    test_data = Subset(dset, idx3)
    print('Length of training set: ' + str(len(training_data)))   
    print('Length of validation set: ' + str(len(forVa_data)))
    print('Length of test set: ' + str(len(test_data)))
    loadertrain = torch.utils.data.DataLoader(
        training_data,
        batch_size=batch_size,
        shuffle=True,
        **dataloader_kwargs, drop_last=True) 
    loaderval = torch.utils.data.DataLoader(
        forVa_data,
        batch_size=batch_size,
        shuffle=True,
        **dataloader_kwargs, drop_last=True)
    loadertest = torch.utils.data.DataLoader(
        test_data,
        batch_size=batch_size,
        shuffle=False,
        **dataloader_kwargs, drop_last=False) 
    return loadertrain, loaderval, loadertest, training_data, forVa_data, test_data

augmentation_train_in = {
    transforms.Compose([
        transforms.ToTensor(),
    ]),
}  
dataloader_kwargs = {'num_workers': 0} 
dataloaders['train'], dataloaders['val'], dataloaders['test'], image_datasets['train'], image_datasets['val'], image_datasets['test'] = nnewa9g9a9e9a9t9alaoader_CIFAR10(train=True, batch_size=BATCH_SIZE,
                                           augmentation=augmentation_train_in,
                                           dataloader_kwargs=dataloader_kwargs)
train_dataloader = dataloaders['train']         
valid_dataloader = dataloaders['test']

# use train_loader and test_loader  
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import rasterio 
input_path = "/Data/ndionelis/building-age-dataset/"
train_path = input_path + "train/data/"
test_path = input_path + "test/data/"
# Load csv files
test_df = pd.read_csv(input_path + "test/test-set.csv")
train_df = pd.read_csv(input_path + "train/train-set.csv")
# Check csv files
train_df.head()
test_df.head() 
names_data = os.listdir(train_path) # # to not load all data in a single tensor, load only the names                    
length_names = len(names_data)
perm = torch.randperm(length_names)
#idx = perm[:round(0.8*length_names)] # # # draw round(0.8*length_names) samples     
#torch.save(idx, 'indexForTrainVal.pt')       
idx = torch.load('indexForTrainVal.pt')  
names_data = np.array(names_data)
idx = idx.numpy() 
training_data = names_data[idx]
#test_data = names_data[~idx]         
mask = np.ones(names_data.size, dtype=bool) 
mask[idx] = False
test_data = names_data[mask]

# we use train_loader and test_loader    
#from PIL import Image    
import cv2 
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
train_set = Dataset(training_data.tolist()) 
train_loader = torch.utils.data.DataLoader(train_set, batch_size=BATCH_SIZE, shuffle=True)  

test_set = Dataset(test_data)  
test_loader = torch.utils.data.DataLoader(test_set, batch_size=BATCH_SIZE)   
# use train_loader and test_loader              

# after test_loader      
names_data2 = os.listdir(test_path) # to not load all data in a single tensor, load only the names                         
test_data2 = np.array(names_data2) 
test_set2 = Dataset(test_data2.tolist())
test_loader2 = torch.utils.data.DataLoader(test_set2, batch_size=BATCH_SIZE) 

train_dataloader = train_loader          
valid_dataloader = test_loader

def cutout(data) :
    min_k, max_k = 90, 170
    data = data.clone()
    h, w = data.size(2), data.size(3)
    b_size = data.size(0)
    for i in range(b_size): 
        k = (min_k + (max_k - min_k) * torch.rand(1)).long().item() 
        #k = 40 
        h_pos = ((h - k) * torch.rand(1)).long().item()
        w_pos = ((w - k) * torch.rand(1)).long().item()
        patch = data[i,:,h_pos:h_pos+k,w_pos:w_pos+k]
        #patch_mean = torch.mean(patch, axis = (1,2), keepdim = True)  
        patch_mean = 0.
        data[i,:,h_pos:h_pos+k,w_pos:w_pos+k] = torch.ones_like(patch) * patch_mean
    return data

import torch.nn as nn
#from utils import get_activation, get_normalization, SE_Block 
class SE_Block(nn.Module): 
    def __init__(self, channels, reduction=16, activation="relu"):
        super().__init__()
        self.reduction = reduction
        self.squeeze = nn.AdaptiveAvgPool2d(1)
        self.excitation = nn.Sequential(
            nn.Linear(channels, channels // self.reduction, bias=False),
            nn.ReLU(inplace=True),
            nn.Linear(channels // self.reduction, channels, bias=False),
            nn.Sigmoid()
        )

    def forward(self, x):
        bs, c, _, _ = x.shape
        y = self.squeeze(x).view(bs, c)
        y = self.excitation(y).view(bs, c, 1, 1)
        return x * y.expand_as(x)

def get_activation(activation_name):
    if activation_name == "relu":
        return nn.ReLU6(inplace=True)
    elif isinstance(activation_name, torch.nn.modules.activation.ReLU6):
        return activation_name

    elif activation_name == "gelu":
        return nn.GELU()
    elif isinstance(activation_name, torch.nn.modules.activation.GELU):
        return activation_name

    elif activation_name == "leaky_relu":
        return nn.LeakyReLU(inplace=True)
    elif isinstance(activation_name, torch.nn.modules.activation.LeakyReLU):
        return activation_name

    elif activation_name == "prelu":
        return nn.PReLU()
    elif isinstance(activation_name, torch.nn.modules.activation.PReLU):
        return activation_name

    elif activation_name == "selu":
        return nn.SELU(inplace=True)
    elif isinstance(activation_name, torch.nn.modules.activation.SELU):
        return activation_name

    elif activation_name == "sigmoid":
        return nn.Sigmoid()
    elif isinstance(activation_name, torch.nn.modules.activation.Sigmoid):
        return activation_name

    elif activation_name == "tanh":
        return nn.Tanh()
    elif isinstance(activation_name, torch.nn.modules.activation.Tanh):
        return activation_name

    elif activation_name == "mish":
        return nn.Mish()
    elif isinstance(activation_name, torch.nn.modules.activation.Mish):
        return activation_name
    else:
        raise ValueError(f"activation must be one of leaky_relu, prelu, selu, gelu, sigmoid, tanh, relu. Got: {activation_name}")

def get_normalization(normalization_name, num_channels, num_groups=32, dims=2):
    if normalization_name == "batch":
        if dims == 1:
            return nn.BatchNorm1d(num_channels)
        elif dims == 2:
            return nn.BatchNorm2d(num_channels)
        elif dims == 3:
            return nn.BatchNorm3d(num_channels)
    elif normalization_name == "instance":
        if dims == 1:
            return nn.InstanceNorm1d(num_channels)
        elif dims == 2:
            return nn.InstanceNorm2d(num_channels)
        elif dims == 3:
            return nn.InstanceNorm3d(num_channels)
    elif normalization_name == "layer":
        # return LayerNorm(num_channels)
        return nn.LayerNorm(num_channels)
    elif normalization_name == "group":
        return nn.GroupNorm(num_groups=num_groups, num_channels=num_channels)
    elif normalization_name == "bcn":
        if dims == 1:
            return nn.Sequential(
                nn.BatchNorm1d(num_channels),
                nn.GroupNorm(1, num_channels)
            )
        elif dims == 2:
            return nn.Sequential(
                nn.BatchNorm2d(num_channels),
                nn.GroupNorm(1, num_channels)
            )
        elif dims == 3:
            return nn.Sequential(
                nn.BatchNorm3d(num_channels),
                nn.GroupNorm(1, num_channels)
            )    
    elif normalization_name == "none":
        return nn.Identity()
    else:
        raise ValueError(f"normalization must be one of batch, instance, layer, group, none. Got: {normalization_name}") 

class CoreCNNBlock(nn.Module):
    def __init__(self, in_channels, out_channels, *, norm="batch", activation="relu", padding="same", residual=True):
        super(CoreCNNBlock, self).__init__()

        self.activation = get_activation(activation)
        self.residual = residual
        self.padding = padding
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.squeeze = SE_Block(self.out_channels)

        self.match_channels = nn.Identity()
        if in_channels != out_channels:
            self.match_channels = nn.Sequential(
                nn.Conv2d(in_channels, out_channels, kernel_size=1, padding=0, bias=False),
                get_normalization(norm, out_channels),
            )

        self.conv1 = nn.Conv2d(self.in_channels, self.out_channels, 1, padding=0)
        self.norm1 = get_normalization(norm, self.out_channels)

        self.conv2 = nn.Conv2d(self.out_channels, self.out_channels, 3, padding=self.padding, groups=self.out_channels)
        self.norm2 = get_normalization(norm, self.out_channels)
        
        self.conv3 = nn.Conv2d(self.out_channels, self.out_channels, 3, padding=self.padding, groups=1)
        self.norm3 = get_normalization(norm, self.out_channels)

    def forward(self, x):
        identity = x
        x = self.activation(self.norm1(self.conv1(x)))
        x = self.activation(self.norm2(self.conv2(x)))
        x = self.norm3(self.conv3(x))
        x = x * self.squeeze(x)
        if self.residual:
            x = x + self.match_channels(identity)
        x = self.activation(x) 
        return x

class CoreEncoderBlock(nn.Module): 
    def __init__(self, depth, in_channels, out_channels, norm="batch", activation="relu", padding="same"):
        super(CoreEncoderBlock, self).__init__() 
        self.depth = depth
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.activation = activation
        self.norm = norm
        self.padding = padding
        self.blocks = []
        for i in range(self.depth): 
            _in_channels = self.in_channels if i == 0 else self.out_channels
            block = CoreCNNBlock(_in_channels, self.out_channels, norm=self.norm, activation=self.activation, padding=self.padding)

            self.blocks.append(block)
        self.blocks = nn.Sequential(*self.blocks)
        self.downsample = nn.MaxPool2d(kernel_size=2, stride=2)
    
    def forward(self, x):
        for i in range(self.depth):
            x = self.blocks[i](x)
        before_downsample = x
        x = self.downsample(x)
        return x, before_downsample

class CoreAttentionBlock(nn.Module):
    def __init__(self,
        lower_channels,
        higher_channels, *,
        norm="batch",
        activation="relu",
        padding="same",
    ):
        super(CoreAttentionBlock, self).__init__()
        self.lower_channels = lower_channels
        self.higher_channels = higher_channels
        self.activation = get_activation(activation)
        self.norm = norm
        self.padding = padding
        self.expansion = 4
        self.reduction = 4
        if self.lower_channels != self.higher_channels:
            self.match = nn.Sequential(
                nn.Conv2d(self.higher_channels, self.lower_channels, kernel_size=1, padding=0, bias=False),
                get_normalization(self.norm, self.lower_channels),
            )
        self.compress = nn.Conv2d(self.lower_channels, 1, kernel_size=1, padding=0)
        self.sigmoid = nn.Sigmoid()
        self.attn_c_pool = nn.AdaptiveAvgPool2d(self.reduction)
        self.attn_c_reduction = nn.Linear(self.lower_channels * (self.reduction ** 2), self.lower_channels * self.expansion)
        self.attn_c_extention = nn.Linear(self.lower_channels * self.expansion, self.lower_channels)

    def forward(self, x, skip):
        if x.size(1) != skip.size(1):
            x = self.match(x)
        x = x + skip
        x = self.activation(x)
        attn_spatial = self.compress(x)
        attn_spatial = self.sigmoid(attn_spatial)
        attn_channel = self.attn_c_pool(x)
        attn_channel = attn_channel.reshape(attn_channel.size(0), -1)
        attn_channel = self.attn_c_reduction(attn_channel)
        attn_channel = self.activation(attn_channel)
        attn_channel = self.attn_c_extention(attn_channel)
        attn_channel = attn_channel.reshape(x.size(0), x.size(1), 1, 1)
        attn_channel = self.sigmoid(attn_channel)
        return attn_spatial, attn_channel

class CoreDecoderBlock(nn.Module):
    def __init__(self, depth, in_channels, out_channels, *, norm="batch", activation="relu", padding="same"):
        super(CoreDecoderBlock, self).__init__()
        self.depth = depth
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.activation_blocks = activation
        self.activation = get_activation(activation)
        self.norm = norm
        self.padding = padding
        self.upsample = nn.UpsamplingBilinear2d(scale_factor=2)
        self.match_channels = CoreCNNBlock(self.in_channels * 2, self.out_channels, norm=self.norm, activation=self.activation_blocks, padding=self.padding)
        self.attention = CoreAttentionBlock(self.in_channels, self.in_channels, norm=self.norm, activation=self.activation_blocks, padding=self.padding)
        self.blocks = []
        for _ in range(self.depth):
            block = CoreCNNBlock(self.out_channels, self.out_channels, norm=self.norm, activation=self.activation_blocks, padding=self.padding)
            self.blocks.append(block)
        self.blocks = nn.Sequential(*self.blocks)
    
    def forward(self, x, skip):
        x = self.upsample(x)
        attn_s, attn_c = self.attention(x, skip)
        x = torch.cat([x, (skip * attn_s) + (skip + attn_c)], dim=1)
        x = self.match_channels(x)
        for i in range(self.depth):
            x = self.blocks[i](x)
        return x

class CoreUnet(nn.Module):  
    def __init__(self, *,
        input_dim=10,
        output_dim=1,
        depths=None,
        dims=None,
        activation="relu",
        norm="batch",
        padding="same",
    ): 
        super(CoreUnet, self).__init__() 
        self.depths = [3, 3, 9, 3] if depths is None else depths 
        self.dims = [96, 192, 384, 768] if dims is None else dims
        #self.depths = [3, 3, 9] if depths is None else depths
        #self.dims = [96, 192, 384] if dims is None else dims
        self.output_dim = output_dim
        self.input_dim = input_dim
        self.activation = activation
        self.norm = norm
        self.padding = padding
        self.dims = [v // 2 for v in self.dims] 
        assert len(self.depths) == len(self.dims), "depths and dims must have the same length. "   
        self.stem = nn.Sequential(
            CoreCNNBlock(self.input_dim, self.dims[0], norm=self.norm, activation=self.activation, padding=self.padding),
        )  
        self.encoder_blocks = []  
        for i in range(len(self.depths)):
            encoder_block = CoreEncoderBlock(
                self.depths[i],
                self.dims[i - 1] if i > 0 else self.dims[0],
                self.dims[i],
                norm=self.norm,
                activation=self.activation,
                padding=self.padding,
            )
            self.encoder_blocks.append(encoder_block)
        self.encoder_blocks = nn.ModuleList(self.encoder_blocks)
        self.decoder_blocks = [] 
        for i in reversed(range(len(self.encoder_blocks))):
            decoder_block = CoreDecoderBlock(
                self.depths[i],
                self.dims[i],
                self.dims[i - 1] if i > 0 else self.dims[0],
                norm=self.norm,
                activation=self.activation,
                padding=self.padding,
            )
            self.decoder_blocks.append(decoder_block)
        self.decoder_blocks = nn.ModuleList(self.decoder_blocks)
        self.bridge = nn.Sequential(
            CoreCNNBlock(self.dims[-1], self.dims[-1], norm=self.norm, activation=self.activation, padding=self.padding),
        )
        self.head = nn.Sequential(
            CoreCNNBlock(self.dims[0], self.dims[0], norm=self.norm, activation=self.activation, padding=self.padding),
            nn.Conv2d(self.dims[0], self.output_dim, kernel_size=1, padding=0),
        )

    def forward(self, x):
        skip_connections = []    
        x = self.stem(x)
        for block in self.encoder_blocks:
            x, skip = block(x)
            skip_connections.append(skip)
        x = self.bridge(x)
        return x

class CoreEncoder(nn.Module):
    def __init__(self, *,
        input_dim=10,
        output_dim=1,
        depths=None,
        dims=None,
        activation="relu",
        norm="batch",
        padding="same",
    ):
        super(CoreEncoder, self).__init__()
        self.depths = [3, 3, 9, 3] if depths is None else depths
        self.dims = [96, 192, 384, 768] if dims is None else dims
        self.output_dim = output_dim
        self.input_dim = input_dim
        self.activation = activation
        self.norm = norm
        self.padding = padding
        assert len(self.depths) == len(self.dims), "depths and dims must have the same length."
        self.stem = CoreCNNBlock(self.input_dim, self.dims[0], norm=self.norm, activation=self.activation, padding=self.padding)
        self.encoder_blocks = []  
        for i in range(len(self.depths)): 
            encoder_block = CoreEncoderBlock(
                self.depths[i],
                self.dims[i - 1] if i > 0 else self.dims[0],
                self.dims[i],
                norm=self.norm,
                activation=self.activation,
                padding=self.padding,
            )
            self.encoder_blocks.append(encoder_block)
        self.encoder_blocks = nn.ModuleList(self.encoder_blocks)
        self.head = nn.Sequential(
            nn.AdaptiveAvgPool2d((1, 1)),
            nn.Flatten(),
            nn.Linear(self.dims[-1], self.output_dim),
        )

    def forward(self, x):
        x = self.stem(x)
        for block in self.encoder_blocks:
            x, _ = block(x)
        x = self.head(x)
        return x

class ResNet152(nn.Module):
    def __init__(self, pretrained):
        super(ResNet152, self).__init__() 
        #self.model = pretrainedmodels.__dict__['resnet152'](pretrained='imagenet')                         
        #self.model = torchvision.models.resnet152(pretrained=True)                          
        class MyResNet18(nn.Module):
            def __init__(self, resnet, resnet2):
                super().__init__()
                self.features = nn.Sequential(
                    resnet.conv1,
                    resnet.bn1,
                    resnet.relu,
                    resnet.maxpool,
                    resnet.layer1,
                    resnet.layer2,
                    resnet.layer3,
                    resnet.layer4
                ) 
                self.avgpool = resnet.avgpool
                self.fc = resnet.fc

                self.features2 = nn.Sequential(
                    resnet2.conv1,
                    resnet2.bn1,
                    resnet2.relu,
                    resnet2.maxpool,
                    resnet2.layer1,
                    resnet2.layer2,
                    resnet2.layer3,
                    resnet2.layer4
                )
                self.avgpool2 = resnet2.avgpool
                self.fc2 = resnet2.fc

            def _forward_impl(self, x: torch.Tensor, x2: torch.Tensor) -> torch.Tensor:
                x = self.features(x)
                x = self.avgpool(x)
                x = torch.flatten(x, 1)
                x = self.fc(x)
                x2 = self.features2(x2)
                x2 = self.avgpool2(x2)
                x2 = torch.flatten(x2, 1)
                x2 = self.fc2(x2) 
                return x, x2

            def forward(self, x: torch.Tensor, x2: torch.Tensor) -> torch.Tensor:
                return self._forward_impl(x, x2) 

        model = torchvision.models.resnet152(pretrained=True)
        model2 = torchvision.models.resnet152(pretrained=True)
        self.model = MyResNet18(model, model2)
        self.l0 = nn.Linear(4480, len(lb.classes_))

    def forward(self, x, x2, x3):
        batch, _, _, _ = x.shape
        x = self.model.features(x)
        x2 = self.model.features2(x2)
        
        BATCH_SIZE = 32 
        CHANNELS = 12
        HEIGHT = 64
        WIDTH = 64
        model = CoreUnet(
            input_dim=CHANNELS,
            output_dim=1,
        ).to(device)   

        x3 = model(x3) 
        x = F.adaptive_avg_pool2d(x, 1).reshape(batch, -1)    
        x2 = F.adaptive_avg_pool2d(x2, 1).reshape(batch, -1) 
        x3 = F.adaptive_avg_pool2d(x3, 1).reshape(batch, -1) 
        x = torch.cat((x, x2, x3), 1)   
        l0 = self.l0(x)
        return l0 

model = ResNet152(pretrained=True).to(device) 
model.train()
criterion = nn.CrossEntropyLoss() 
optimizer = optim.Adam(model.parameters(), lr=1e-5, weight_decay=0.5e-3)   

def validate(model):    
  print('Now validating')                     
  model.eval()    
  running_loss = 0.0  
  running_correct = 0
  with torch.no_grad():
      for idx, batch in enumerate(tqdm(valid_dataloader)):
          pixel_values, pixel_values2, pixel_values3, labels = batch[0].to(device, dtype=torch.float32), batch[1].to(device, dtype=torch.float32), batch[2].to(device, dtype=torch.float32), batch[3].to(device)
          pixel_values = pixel_values.permute(0, 3, 1, 2)         
          pixel_values2 = pixel_values2.permute(0, 3, 1, 2)   
          pixel_values3 = pixel_values3.permute(0, 3, 1, 2)
          outputs = model(pixel_values, pixel_values2, pixel_values3)
          _, preds = torch.max(outputs, 1)
          running_correct += (preds == labels).sum().item() 
      accuracy = 100. * running_correct / len(valid_dataloader.dataset)
      print(f'Val Acc: {accuracy:.2f}')
      return accuracy

best_test_bpd = 0    
for epoch in range(120):  # loop over the dataset multiple times                       
   print("Epoch:", epoch) 
   for idx, batch in enumerate(tqdm(train_dataloader)): 
        model.train()
        pixel_values, pixel_values2, pixel_values3, labels = batch[0].to(device, dtype=torch.float32), batch[1].to(device, dtype=torch.float32), batch[2].to(device, dtype=torch.float32), batch[3].to(device) 
        pixel_values = pixel_values.permute(0, 3, 1, 2)        
        pixel_values2 = pixel_values2.permute(0, 3, 1, 2) 
        pixel_values3 = pixel_values3.permute(0, 3, 1, 2)
        optimizer.zero_grad() 
        outputs = model(pixel_values, pixel_values2, pixel_values3) 
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        print("Loss:", loss.item())  

        if (epoch % 5 == 0) and (idx == 0): 
          accToCheck = validate(model)   
          if accToCheck > best_test_bpd:     
              best_test_bpd = accToCheck  
              torch.save(model.state_dict(), './modelB.pt')   

torch.save(model.state_dict(), './model.pt')   