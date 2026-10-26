def validate_coordinates(point_tuple, limits_dict):
    x, y, z = point_tuple
    x_min, x_max = limits_dict['x']
    y_min, y_max = limits_dict['y']
    z_min, z_max = limits_dict['z']

    return (x_min <= x <= x_max) and (y_min <= y <= y_max) and (z_min <= z <= z_max)


def smooth_trajectory(points_list):
    if len(points_list) < 3:
        return list(points_list)

    smoothed = [points_list[0]]

    for i in range(1, len(points_list) - 1):
        prev_p = points_list[i - 1]
        curr_p = points_list[i]
        next_p = points_list[i + 1]
        new_point = tuple((prev_p[j] + curr_p[j] + next_p[j]) // 3 for j in range(3))
        smoothed.append(new_point)
    smoothed.append(points_list[-1])
    return smoothed

def get_reversed_path(points_list):
    return points_list[::-1]
