import tensorflow as tf
import cv2
import pong 
import numpy as np
import random
from collections import deque

#defining hyperparameters
ACTIONS = 3
#learning rate
GAMMA = 0.99
#UPDATRE TRAINING
INITAL_EPSILON = 1.0
FINAL_EPSILON = 0.05
#FPE
EXPLORE = 500000
OBSERVE = 50000
REPLAY_MEMORY = 50000
BATCH = 100

#create TF graph
def createGraph():

	#1 covulitional & bias
	W_conv1 = tf.Variable(tf.zeros([8,8,4,32]))
	b_conv = tf.Variable(tf.zeros([32]))

	#2 conv layer
	W_conv2 = tf.Variable(tf.zeros[4,4,32,64])
	b_conv2 = tf.Variable(tf.zeros[64])

	#3 third
	W_conv3 = tf.Variable(tf.zeros[3,3, 64, 64])
	b_conv3 = tf.Variable(tf.zeros[64])

	#4
	W_fc4 = tf.Variable(tf.zeros[784, ACTIONS])
	b_fc4 = tf.Variable(tf.zeros[784])))

	#Last 
	W_fc5 = tf.Variable(tf.zeros[784, ACTIONS]))
	b_fc5 = tf.Variable(tf.zeros[[Actions]])

	#input for pixel data
	s = tf.placeholder("float", [None, 84, 84, 84])
	#52.35

	conv1 = tf.nn.relu(tf.nn.conv2d(s, W_conv1, strides[1,4,4,1] padding ="VALID") + b_conv1)
	conv2 = tf.nn.relu(tf.nn.conv2d(s, W_conv2, strides[1,4,4,1] padding ="VALID") + b_conv1)
	conv3 = tf.nn.relu(tf.nn.conv2d(s, W_conv3, strides[1,4,4,1] padding ="VALID") + b_conv1)
	
	conv3_flat = tf.reshape(conv3, [-1, 3136])
	fc4 = tf.nn.relu(tf.matmul(conv3_flat, w_fc4 + b_fc4))
	fc5 = tf.matmul(fc5, W_fc5) + bb_fc5

	return s, fc5

def main():
	#main session
	sess = tf.InteractiveSession()
	#in and out layer
	inp, out = CreateGraph()
	trainGraph(inp, out, sess)

if __name__ = "__main__":
	main()


