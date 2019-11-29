# -*- coding: utf-8 -*-

# numbers in Python
a = [1, 2, 3, 4, 5, 6, 7]

print(a[0])

a[2] = 3

a

a[3:7]


# torch
import torch
a = torch.ones(3)
a

a[1]

float(a[1])

a[2] = 2.0
a


# shape and size
points = torch.tensor([[1.0, 4.0], [2.0, 1.0], [3.0, 5.0]])
points.shape

# storage
points = torch.tensor([[1.0, 4.0], [2.0, 1.0], [3.0, 5.0]])
points.storage()

points_storage = points.storage()
points_storage[0]
points.storage()[1]


points = torch.tensor([[1.0, 4.0], [2.0, 1.0], [3.0, 5.0]])
points_storage = points.storage()
points_storage[0] = 2.0
points

# size, offset and stride
points = torch.tensor([[1.0, 4.0], [2.0, 1.0], [3.0, 5.0]])
second_point = points[1]
second_point.storage_offset()
second_point.size()
torch.Size([2])
second_point.shape
torch.Size([2])
points.stride()
points = torch.tensor([[1.0, 4.0], [2.0, 1.0], [3.0, 5.0]])
second_point = points[1]
second_point.size()
torch.Size([2])
second_point.storage_offset()
second_point.stride()
points = torch.tensor([[1.0, 4.0], [2.0, 1.0], [3.0, 5.0]])
second_point = points[1]
second_point[0] = 10.0
points
points = torch.tensor([[1.0, 4.0], [2.0, 1.0], [3.0, 5.0]])
second_point = points[1].clone()
second_point[0] = 10.0
points

points = torch.tensor([[1.0, 4.0], [2.0, 1.0], [3.0, 5.0]])
points

points_t = points.t()
points_t

id(points.storage()) == id(points_t.storage())

points.stride()

points_t.stride()

# transpose
some_tensor = torch.ones(3, 4, 5)
some_tensor_t = some_tensor.transpose(0, 2)
some_tensor.shape

some_tensor_t.shape

torch.Size([5, 4, 3])

some_tensor.stride()

some_tensor_t.stride()


points.is_contiguous()

points_t.is_contiguous()

points = torch.tensor([[1.0, 4.0], [2.0, 1.0], [3.0, 5.0]])
points_t = points.t()
points_t

points_t.storage()

points_t.stride()

points_t_cont = points_t.contiguous()
points_t_cont

points_t_cont.stride()

points_t_cont.storage()

# types
double_points = torch.ones(10, 2, dtype=torch.double)
short_points = torch.tensor([[1, 2], [3, 4]], dtype=torch.short)


# indexing
some_list = list(range(6))
some_list[:]
some_list[1:4]
some_list[1:]
some_list[:4]
some_list[:-1]
some_list[1:4:2]

points[1:]
points[1:, :]
points[1:, 0]

# numpy interopabiity

points = torch.ones(3, 4)
points_np = points.numpy()
points_np