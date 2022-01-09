import math

def vector_add(v, w):
    """벡터의 각 성분끼리 더한다"""
    return [v_i + w_i for v_i, w_i in zip(v, w)]

def vector_subtract(v, w):
    """벡터의 각 성분끼리 뺀다"""
    return [v_i - w_i for v_i, w_i in zip(v, w)]

def vector_sum(vectors):
    """모든 벡터의 각 성분들끼리 더한다"""
    result = vectors[0]
    for vector in vectors[1:]:
        result = vector_add(result, vector)
    return result
    #return reduce(vector_add, vectors) -> reduce로 해서 바꿀수


def scalar_multiply(c, v):
    """벡터 v에 스칼라 c를 곱한다(스칼라곱)"""
    return [c*v_i for v_i in v]

def vector_mean(vectors):
    """i번째 성분이 입력된 벡터의 i번째 성분의 평균을 의미하는 벡터를 계산해준다"""
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

def dot(v, w):
    """내적 : v_1*w_1 + ... + v_n*w_n"""
    #result = 0
    #for v_i, w_i in zip(v, w):
    #    result = result + (v_i * w_i)
    #return result
    
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

def sum_of_squares(v):
    """각 성분의 제곱 값의 합"""
    return dot(v, v)


def magnitude(v):
    """벡터의 크기_각성분의제곱의 합의 제곱근"""
    return math.sqrt(sum_of_squares(v))


def distance(v, w):
    """두 벡터의 거리를 계산"""
    return magnitude(vector_subtract(v,w))



v1 = [1,2]
v2 = [3,4]
v1s = [[1,2],[3,4],[2,5]]

m1 = [[1,2,3,],[4,5,6]]
m2 = [[4,1,3],[7,4,4]]
m3 = [[6,3,4],[4,1,2],[8,9,4]]
m4 = [[1,2],[3,4],[5,6]]

def matrix_shape(a):
    """행렬의 행,열크기를 구함"""
    num_rows = len(a)
    num_columns = len(a[0])
    return num_rows, num_columns

def get_matrix_row(a, i):
    """행렬 a의 i번째 행을 구함"""
    return a[i]

def get_matrix_column(a, i):
    """행렬 a의 i번째 열을 구함"""
    return [v_i[i] for v_i in a]

def make_matrix(num_rows, num_columns, entry_fn):
    """i, j번째 원소가 함수 entry_fn(i,j)인 num_row x num_columns의 List반환"""
    return [[entry_fn(i,j) for j in range(num_columns)] for i in range(num_rows)]

def is_diagonal(i, j):
    """i==j 일때 1, 아니면 0을 반환"""
    return 1 if i==j else 0


num_friends = [100,49,41,40,25,21,21,19,19,18,18,16,15,15,15,15,14,14,13,13,13,13,12,12,11,
10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,8,8,8,
8,8,8,8,8,8,8,8,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,5,
5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,
3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

def mean(x):
    """list x의 각 요소의 평균을 구함"""
    return sum(x) / len(x)

print(mean(num_friends))

