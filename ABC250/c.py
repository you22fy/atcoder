n, q = map(int, input().split())
balls = [i + 1 for i in range(n)]
balls_position = {ball: idx for idx, ball in enumerate(balls)}

for _ in range(q):
    x = int(input())
    target_id = balls_position[x]
    if target_id == n - 1:
        balls_position[balls[target_id]] = target_id - 1
        balls_position[balls[target_id - 1]] = target_id

        balls[target_id], balls[target_id - 1] = balls[target_id - 1], balls[target_id]
    else:
        balls_position[balls[target_id + 1]] = target_id
        balls_position[balls[target_id]] = target_id + 1

        balls[target_id], balls[target_id + 1] = balls[target_id + 1], balls[target_id]

print(*balls)
