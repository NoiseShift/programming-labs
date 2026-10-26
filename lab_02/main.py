def simulate_robot_braking(v0, deceleration, time_step, emergency_stop: bool = False):
    v = v0
    total_t = 0
    while v > 0:
        if emergency_stop:
            break
        v = v - deceleration * time_step
        total_t += time_step
    s = v0 * total_t / 2
    return [s, total_t]


v1 = float(input('Начальная скорость: '))
a = float(input('Торможение: '))
t = float(input('Шаг времени: '))

print(simulate_robot_braking(v1, a, t))