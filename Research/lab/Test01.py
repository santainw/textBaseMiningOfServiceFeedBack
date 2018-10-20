import tensorflow as tf

# Initialize two constants
x1 = tf.constant([1, 2, 3, 5])
x2 = tf.constant([5, 6, 6, 5])

# Multiply
result = tf.multiply(x1, x2)

# Print the result
print(result)
print(x1)
