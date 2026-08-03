import numpy as np


def cosine_similarity(vec_1: list[float], vec_2: list[float]) -> float:
    return np.dot(vec_1, vec_2) / (np.linalg.norm(vec_1) * np.linalg.norm(vec_2))


if __name__ == "__main__":
    vec_a = [0.5, 0.5]
    vec_b = [0.7, 0.7]
    vec_c = [0.7, 0.5]
    vec_d = [-0.6, -0.5]

    print("ab: ", cosine_similarity(vec_a, vec_b))
    print("ac: ", cosine_similarity(vec_a, vec_c))
    print("ad: ", cosine_similarity(vec_a, vec_d))
    print("aa: ", cosine_similarity(vec_a, vec_a))
