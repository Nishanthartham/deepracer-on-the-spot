import math

class PARAMS:
    prev_speed = None
    prev_steering_angle = None 
    prev_steps = None
    prev_direction_diff = None
    prev_normalized_distance_from_route = None

def calculate_track_direction(waypoints, closest_waypoints):
    next_point = waypoints[closest_waypoints[1]]
    prev_point = waypoints[closest_waypoints[0]]
    track_direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0])
    track_direction = math.degrees(track_direction)
    return track_direction

def calculate_normalized_distance_from_route(distance_from_center, track_width):
    return distance_from_center / (track_width / 2)

def is_heading_in_right_direction(heading, track_direction, threshold=10):
    direction_diff = abs(track_direction - heading)
    if direction_diff > 180:
        direction_diff = 360 - direction_diff
    return direction_diff < threshold

def is_turn_upcoming(waypoints, closest_waypoints, turn_threshold=15):
    next_point = waypoints[closest_waypoints[1]]
    future_point = waypoints[min(closest_waypoints[1] + 5, len(waypoints) - 1)]
    future_direction = math.atan2(future_point[1] - next_point[1], future_point[0] - next_point[0])
    future_direction = math.degrees(future_direction)
    track_direction = calculate_track_direction(waypoints, closest_waypoints)
    direction_diff = abs(track_direction - future_direction)
    if direction_diff > 180:
        direction_diff = 360 - direction_diff
    return direction_diff > turn_threshold

def reward_function(params):
    # Read input parameters
    heading = params['heading']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    steps = params['steps']
    steering_angle = params['steering_angle']
    speed = params['speed']
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']

    track_direction = calculate_track_direction(waypoints, closest_waypoints)
    direction_diff = abs(track_direction - heading)
    normalized_distance_from_route = calculate_normalized_distance_from_route(distance_from_center, track_width)
    heading_right_direction = is_heading_in_right_direction(heading, track_direction)
    turn_upcoming = is_turn_upcoming(waypoints, closest_waypoints)

    # Reinitialize previous parameters if it is a new episode
    if PARAMS.prev_steps is None or steps < PARAMS.prev_steps:
        PARAMS.prev_speed = None
        PARAMS.prev_steering_angle = None
        PARAMS.prev_direction_diff = None
        PARAMS.prev_normalized_distance_from_route = None
    
    # Check if the speed has dropped
    has_speed_dropped = False
    if PARAMS.prev_speed is not None and PARAMS.prev_speed > speed:
        has_speed_dropped = True
    
    # Penalize slowing down without good reason on straight portions
    speed_maintain_bonus = 1
    if has_speed_dropped and not turn_upcoming:
        speed_maintain_bonus = min(speed / PARAMS.prev_speed, 1)
    
    # Penalize making the heading direction worse
    heading_decrease_bonus = 0
    if PARAMS.prev_direction_diff is not None and heading_right_direction:
        if abs(PARAMS.prev_direction_diff / direction_diff) > 1:
            heading_decrease_bonus = min(10, abs(PARAMS.prev_direction_diff / direction_diff))
    
    # Check if the steering angle has changed
    has_steering_angle_changed = False
    if PARAMS.prev_steering_angle is not None and not math.isclose(PARAMS.prev_steering_angle, steering_angle):
        has_steering_angle_changed = True
    
    steering_angle_maintain_bonus = 1
    if heading_right_direction and not has_steering_angle_changed:
        if abs(direction_diff) < 10:
            steering_angle_maintain_bonus *= 2
        if abs(direction_diff) < 5:
            steering_angle_maintain_bonus *= 2
        if PARAMS.prev_direction_diff is not None and abs(PARAMS.prev_direction_diff) > abs(direction_diff):
            steering_angle_maintain_bonus *= 2
    
    # Reward reducing distance to the race line
    distance_reduction_bonus = 1
    if PARAMS.prev_normalized_distance_from_route is not None and PARAMS.prev_normalized_distance_from_route > normalized_distance_from_route:
        if abs(normalized_distance_from_route) > 0:
            distance_reduction_bonus = min(abs(PARAMS.prev_normalized_distance_from_route / normalized_distance_from_route), 2)
    
    reward = speed_maintain_bonus + heading_decrease_bonus + steering_angle_maintain_bonus + distance_reduction_bonus
    
    # Before returning reward, update the variables
    PARAMS.prev_speed = speed
    PARAMS.prev_steering_angle = steering_angle
    PARAMS.prev_direction_diff = direction_diff
    PARAMS.prev_steps = steps
    PARAMS.prev_normalized_distance_from_route = normalized_distance_from_route
    
    return reward


# params = {"speed":1,"steering_angle":90,"steps":10,"distance_from_center":90,"heading":8,"waypoints":[[1,2],[1,2],[1,2]],"closest_waypoints":[0,0],"track_width":10}
# print(reward_function(params))
