import tensorflow as tf

hello = tf.constant('Hello World! Tensorflow was properly installed :)')
sess = tf.Session()

print(sess.run(hello))
