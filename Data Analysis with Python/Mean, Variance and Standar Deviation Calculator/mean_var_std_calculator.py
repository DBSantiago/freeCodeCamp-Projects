import numpy as np

def calculate(my_list):
    if len(my_list) < 9:
        raise ValueError('List must contain nine numbers.')
    else:

        array = np.array(my_list)
        matrix = array.reshape(3,3)

        means = [np.mean(matrix, axis=0).tolist(), np.mean(matrix,axis=1).tolist(), np.mean(matrix).tolist()]
        
        variances = [np.var(matrix, axis=0).tolist(), np.var(matrix,axis=1).tolist(), np.var(matrix).tolist()]
        
        stds = [np.std(matrix, axis=0).tolist(), np.std(matrix,axis=1).tolist(), np.std(matrix).tolist()]

        maxs = [np.max(matrix, axis=0).tolist(), np.max(matrix,axis=1).tolist(), np.max(matrix).tolist()]

        mins = [np.min(matrix, axis=0).tolist(), np.min(matrix,axis=1).tolist(), np.min(matrix).tolist()]

        sums = [np.sum(matrix, axis=0).tolist(), np.sum(matrix,axis=1).tolist(), np.sum(matrix).tolist()]

        calculations = {
            'mean': means,
            'variance': variances,
            'standard deviation': stds,
            'max': maxs,
            'min': mins,
            'sum': sums
        }
        return calculations

