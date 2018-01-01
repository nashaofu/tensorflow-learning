import tensorflow as tf

a = tf.constant(2, name = "input_a")
b = tf.constant(5, name = "input_b")
c = tf.add(a, b, name = "c")
d = tf.constant(8, name = "input_d")
e = tf.multiply(c, d, name = "e")

sess = tf.Session()

out = sess.run(e)

writer = tf.summary.FileWriter('C:\\Users\\nashaofu\\Documents\\Github\\tensorflow-learning\\logs', sess.graph)
