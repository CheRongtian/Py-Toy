alien_0 = {'colour':'green','point':5}

print(alien_0['colour'])
print(alien_0['point'])
print(alien_0)

ori_points=alien_0['point']
print(f"You could get {ori_points} points!")

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0['point'] = 10
new_points=alien_0['point']
print(f"You could get {new_points} points now!")

