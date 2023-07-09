# NOTE: at the moment I do not take advantage of GPU acceleration
import tensorflow as tf

def minimize_function(f, initial_vector, learning_rate=0.1, num_iterations=100):
    vector = tf.Variable(initial_vector, dtype=tf.float32)
    optimizer = tf.optimizers.SGD(learning_rate)

    for _ in range(num_iterations):
        with tf.GradientTape() as tape:
            value = f(vector)
        gradients = tape.gradient(value, vector)
        optimizer.apply_gradients([(gradients, vector)])

    return value.numpy(), vector.numpy()

# Example usage:
def example_function(x):
    return tf.reduce_sum(tf.square(x))  # Example function: sum of squares

def offset_parabola(x):
    return tf.reduce_sum(tf.square(x - 3.0))

# initial_vector = [1.0, 2.0, 3.0]
N = 100
initial_vector = tf.zeros(N)
minimum_value, minimum_vector = minimize_function(offset_parabola, initial_vector)

print("Minimum value:", minimum_value)
print("Minimum vector:", minimum_vector)
