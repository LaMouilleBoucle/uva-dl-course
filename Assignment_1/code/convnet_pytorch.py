"""
This module implements a Convolutional Neural Network in PyTorch.
You should fill in code into indicated sections.
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import torch
import torch.nn as nn
import torch.nn.functional as F

class ConvNet(nn.Module):
  """
  This class implements a Convolutional Neural Network in PyTorch.
  It handles the different layers and parameters of the model.
  Once initialized an ConvNet object can perform forward.
  """

  def __init__(self, n_channels, n_classes):
    """
    Initializes ConvNet object.

    Args:
      n_channels: number of input channels
      n_classes: number of classes of the classification problem


    TODO:
    Implement initialization of the network.
    """

    ########################
    # PUT YOUR CODE HERE  #
    #######################
    super(ConvNet, self).__init__()
    self.hidden_layers = nn.Sequential(
                            nn.Conv2d(n_channels,64,3,padding=1),\
                            nn.BatchNorm2d(64),\
                            nn.ReLU(),\
                            nn.MaxPool2d(3,stride=2,padding=1),\
                            nn.Conv2d(64,128,3,padding=1),\
                            nn.BatchNorm2d(128),\
                            nn.ReLU(),\
                            nn.MaxPool2d(3,stride=2,padding=1),\
                            nn.Conv2d(128,256,3,padding=1),\
                            nn.BatchNorm2d(256),\
                            nn.ReLU(),\
                            nn.Conv2d(256,256,3,padding=1),\
                            nn.BatchNorm2d(256),\
                            nn.ReLU(),\
                            nn.MaxPool2d(3,stride=2,padding=1),\

                            nn.Conv2d(256,512,3,padding=1),\
                            nn.BatchNorm2d(512),\
                            nn.ReLU(),\
                            nn.Conv2d(512,512,3,padding=1),\
                            nn.BatchNorm2d(512),\
                            nn.ReLU(),\
                            nn.MaxPool2d(3,stride=2,padding=1),\

                            nn.Conv2d(512,512,3,padding=1),\
                            nn.BatchNorm2d(512),\
                            nn.ReLU(),\
                            nn.Conv2d(512,512,3,padding=1),\
                            nn.BatchNorm2d(512),\
                            nn.ReLU(),\
                            nn.MaxPool2d(3,stride=2,padding=1))
    self.output_layer = nn.Linear(512,n_classes)
    #######################
    # END OF YOUR CODE    #
    #######################

  def forward(self, x):
    """
    Performs forward pass of the input. Here an input tensor x is transformed through
    several layer transformations.

    Args:
      x: input to the network
    Returns:
      out: outputs of the network

    TODO:
    Implement forward pass of the network.
    """

    ########################
    # PUT YOUR CODE HERE  #
    ######################
    x_3D = self.hidden_layers(x)
    x_flat = x_3D.view(x_3D.size(0),-1)
    out = self.output_layer(x_flat)
    ########################
    # END OF YOUR CODE    #
    #######################

    return out
