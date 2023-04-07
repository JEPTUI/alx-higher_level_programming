#!/usr/bin/python3
""" Module - 101-lazy_matrix_mul
Defines a function that multiplies 2 matrices by using Numpy module """

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices

    Args: m_a - first mtrix
        m_b - second matrix
    """
    return (np.matmul(m_a, m_b))
