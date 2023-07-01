# -*- coding: utf-8 -*-
"""
Last updated on Sat Jul  1 15:58:28 2023
@author: Ye Kyaw Thu, LST Lab., Myanmar

Reference:
https://ogunlao.github.io/2020/05/23/knn-as-a-neural-network.html

How to run:
python dKNN.py --help

    
"""

import argparse
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

class Net(nn.Module):
    def __init__(self, input_dim, n_layers):
        super(Net, self).__init__()
        layers = []
        hidden_dim = 16
        for _ in range(n_layers):
            layers.append(nn.Linear(input_dim, hidden_dim))
            layers.append(nn.ReLU())
            input_dim = hidden_dim
        self.model = nn.Sequential(*layers)

    def forward(self, x):
        return self.model(x)

class DiffKNN(nn.Module):
    def __init__(self, n_neighbors):
        super(DiffKNN, self).__init__()
        self.n_neighbors = n_neighbors

    def forward(self, X_train, X_test):
        dists = torch.cdist(X_test, X_train)
        _, idxs = dists.topk(self.n_neighbors, dim=1, largest=False)
        return idxs

def load_data(dataset_name):
    if dataset_name == "iris":
        data = datasets.load_iris()
    elif dataset_name == "wine":
        data = datasets.load_wine()

    X, y = data.data, data.target
    X = StandardScaler().fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

def main(mode, dataset, epochs, n_layers, n_neighbors):
    if mode in ["knn", "diffknn"] and epochs != 10:
        raise ValueError("The 'epochs' argument should not be specified for 'knn' and 'diffknn' modes.")
    if mode in ["knn", "diffknn"] and n_layers != 2:
        raise ValueError("The 'n_layers' argument should not be specified for 'knn' and 'diffknn' modes.")

    X_train, X_test, y_train, y_test = load_data(dataset)
    X_train = torch.tensor(X_train, dtype=torch.float32)
    X_test = torch.tensor(X_test, dtype=torch.float32)
    y_train = torch.tensor(y_train, dtype=torch.long)

    if mode == "knn":
        knn = KNeighborsClassifier(n_neighbors=n_neighbors)
        knn.fit(X_train, y_train)
        y_pred = knn.predict(X_test)
        print(f"Dataset: {dataset}")
        print(f"Test accuracy (KNN): {accuracy_score(y_test, y_pred)}")
        print(f"Confusion matrix (KNN):\n {confusion_matrix(y_test, y_pred)}")
    elif mode == "deepknn":
        model = Net(X_train.shape[1], n_layers)
        optimizer = optim.Adam(model.parameters())
        criterion = nn.CrossEntropyLoss()
        for epoch in range(epochs):
            optimizer.zero_grad()
            outputs = model(X_train)
            _, preds = torch.max(outputs, 1)
            loss = criterion(outputs, y_train)
            loss.backward()
            optimizer.step()
        train_outputs = model(X_train)
        test_outputs = model(X_test)
        idxs = DiffKNN(n_neighbors)(train_outputs.detach(), test_outputs)
        y_pred = y_train[idxs].mode(dim=1)[0].numpy()
        print(f"Dataset: {dataset}")        
        print(f"Test accuracy (DeepKNN): {accuracy_score(y_test, y_pred)}")
        print(f"Confusion matrix (DeepKNN):\n {confusion_matrix(y_test, y_pred)}")
    elif mode == "diffknn":
        model = DiffKNN(n_neighbors)
        idxs = model(X_train, X_test)
        y_pred = y_train[idxs].mode(dim=1)[0].numpy()
        print(f"Dataset: {dataset}")
        print(f"Test accuracy (DiffKNN): {accuracy_score(y_test, y_pred)}")
        print(f"Confusion matrix (DiffKNN):\n {confusion_matrix(y_test, y_pred)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='This program provides 3 methods for classification: KNN, DeepKNN, and DiffKNN. \
        KNN is the traditional K-Nearest Neighbors. DeepKNN first trains a neural network on the input data, and \
        uses the trained model to transform the input data before applying the KNN algorithm. DiffKNN treats the \
        K-Nearest Neighbors process as a differentiable operation, optimizing the entire process end-to-end.')
    parser.add_argument("--mode", type=str, default="knn", choices=["knn", "deepknn", "diffknn"], help="The mode to run: traditional KNN, DeepKNN, or DiffKNN.")
    parser.add_argument("--dataset", type=str, default="iris", choices=["iris", "wine"], help="The dataset to use: Iris or Wine.")
    parser.add_argument("--epochs", type=int, default=10, help="The number of epochs to train for (DeepKNN only).")
    parser.add_argument("--n_layers", type=int, default=2, help="The number of layers in the neural network (DeepKNN only).")
    parser.add_argument("--n_neighbors", type=int, default=3, help="The number of neighbors to use in KNN.")
    args = parser.parse_args()
    main(args.mode, args.dataset, args.epochs, args.n_layers, args.n_neighbors)
