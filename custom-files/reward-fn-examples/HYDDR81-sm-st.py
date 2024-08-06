def reward_function(params):
    right_turn = [63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]
    steering = params['steering_angle']
    if params["all_wheels_on_track"] and params["steps"] > 0:
        if params["closest_waypoints"][1] not in right_turn:
            if steering > 0:
                reward = 0.001
            else:
                reward += 20
        # else:

        reward = ((params["progress"] / params["steps"]) * 100) + (params["speed"]**2)
    else:
        reward = 0.01
        
    return float(reward)

