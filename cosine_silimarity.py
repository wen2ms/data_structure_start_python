import math


def cosine_similarity(vec_1: list[float], vec_2: list[float]) -> float:
    if len(vec_1) != len(vec_2):
        raise ValueError("Vectors must have the same length.")

    dot_product = sum(x * y for x, y in zip(vec_1, vec_2, strict=False))
    norm_1 = math.sqrt(sum(x * x for x in vec_1))
    norm_2 = math.sqrt(sum(x * x for x in vec_2))
    if norm_1 == 0.0 or norm_2 == 0.0:
        raise ValueError("Zero vectors.")
    return dot_product / (norm_1 * norm_2)


if __name__ == "__main__":
    vec_a = [0.5, 0.5]
    vec_b = [0.7, 0.7]
    vec_c = [0.7, 0.5]
    vec_d = [-0.6, -0.5]

    print(f"ab: {cosine_similarity(vec_a, vec_b)}")
    print(f"ac: {cosine_similarity(vec_a, vec_c)}")
    print(f"ad: {cosine_similarity(vec_a, vec_d)}")
    print(f"aa: {cosine_similarity(vec_a, vec_a)}")
