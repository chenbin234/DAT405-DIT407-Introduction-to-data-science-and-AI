import numpy as np


def check_possibilities(x, y, dim):
    # the function takes the indices of a point and the dimension of a grid and returns possible moves at a point (x,y) in the grid
    (m, n) = dim
    possib = []
    # if the if-statements were not true, we would move outside the grid
    if y < m-1:
        possib.append((x, y+1, 'N'))
    if y > 0:
        possib.append((x, y-1, 'S'))
    if x < n-1:
        possib.append((x+1, y, 'E'))
    if x > 0:
        possib.append((x-1, y, 'W'))
    return possib


def get_V(x, y, V_last, reward, p_mov=0.8, gamma=0.9):

    # the function calculates the total reward V for a state s=(x,y) given the last V, V_last
    # initialize v with minus infinity and policy with empty string
    # p_mov is the probability for a move on the grid
    # the function returns V and pi

    v = float('-inf')
    pi = ''
    p = check_possibilities(x, y, reward.shape)
    for x1, y1, m in p:
        # move to next field + stay in the same field
        v_ = p_mov * (reward[y1, x1]+gamma*V_last[y1, x1]) + \
            (1-p_mov)*(reward[y, x]+gamma*V_last[y, x])
        if (v_ > v):
            # if new total reward is bigger than old one, replace it and save policy
            v = v_
            pi = m
    return pi, v


def value_iteration(V_0, reward, epsilon=0.0001, gamma=0.9):

    # The function finds the optimal policy pi by iterating over all states and calling the get_V function
    # It returns the final states of the last iteration and the underlying policy

    (m, n) = reward.shape
    V_last = V_0
    # initialize V and pi with dimension of reward matrix
    V = np.zeros((m, n))
    pi = np.zeros((m, n), dtype=str)
    iteration_times = 1

    while True:
        for i in range(m):
            for j in range(n):
                # call get_V function:
                pi[i, j], V[i, j] = get_V(j, i, V_last, reward, gamma=gamma)
        # If abs(V_k-V_{k-1})<epsilon -> convergence
        if (np.abs(V-V_last) < epsilon).all():
            return pi, V, iteration_times
        V_last = V.copy()
        iteration_times += 1


# initialize what is given in exercise:
rewards = np.array([(0, 0, 0), (0, 10, 0), (0, 0, 0)])
V_init = 0*np.ones(rewards.shape)

# call function with initialized parameters and epsilon=0.0001
pi, V, iteration_times= value_iteration(V_init, rewards, epsilon=0.0001)


# The arrays need to be flipped to show the grid correctly:

print('V:')
print(np.flipud(V))

print('Policy:')
print(np.flipud(pi))


print('iteration time:', iteration_times)
