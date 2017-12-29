

from __future__ import absolute_import

import tensorflow as tf

def load_graph(filename):
	with tf.gfile.FastGFile(filename,'rb') as f:
		graph_def = tf.GraphDef()
		graph_def.ParseFromString(f.read())


#load_graph('/tmp/my_frozen_graph.pb')


def restore_graph():
	with tf.Session() as sess:
		new_saver = tf.train.import_meta_graph('/tmp/speech_commands_train/conv.ckpt-18000.meta')
#		new_saver.restore(sess,'/tmp/speech_commands_train/conv.ckpt-18000')


restore_graph()
