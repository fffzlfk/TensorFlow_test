import tensorflow as tf

a = tf.constant(3.0, dtype=tf.float32)
b = tf.constant(4.0)
c = tf.add(a, b)

sess = tf.Session()

print(sess.run(a))
print(sess.run(b))
print(sess.run(c))