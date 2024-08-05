def reward_function(params):
    center_variance = params["distance_from_center"] / params["track_width"]
    steering = abs(params['steering_angle'])
    # racing line 84 points
# #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 
# 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59,
#  60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79,80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 
#   100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115,
#    116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 
#    132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155]
    left_lane = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,21, 22, 23,24, 25, 26, 27,28,29,30,31,32,33,34, 35, 36, 37, 38, 39,40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59,60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79,80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93,90, 91, 92, 93, 94, 95, 96, 97, 98, 99,100, 101, 102, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155]

    center_lane = [103,104, 105, 106, 107, 108, 109, 110, 111, 112, 113,114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131]  # Fill in the waypoints
    # right_lane = [ 41, 42, 43, 44, 45, 46, 47,66, 67, 68, 69, 70,76, 77, 78, 79,80, 81, 82, 83]  # Fill in the waypoint4

    # Speed

    # fast = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 22, 23, 24, 25, 26, 27,34, 35, 36, 37, 38, 39,40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53,59, 60, 61, 62, 63, 64,70, 71, 72, 73, 74, 75, 76, 77,99,100, 101, 102, 103, 104, 105, 106, 107, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131,132,133,134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154]  # 3

    # moderate = [19,20,21,31,32,33,84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98,108, 109, 110, 111, 112, 113, 114, 115,116,117]  # 2

    # slow = [14, 15, 16, 17, 18,28,29,30,54, 55, 56, 57, 58, 59,65, 66, 67, 68, 69,78, 79,80, 81, 82, 83]  # 1
    # sharp_turns = [57, 69,80]
    # rounded_turns = [19, 32, 107]

    reward = 30

    if params["all_wheels_on_track"]:

        reward += 5

    else:

        reward -= 5

    if params["closest_waypoints"][1] in left_lane and params["is_left_of_center"]:

        reward += 10

    # elif params["closest_waypoints"][1] in right_lane and not params["is_left_of_center"]:

    #     reward += 10

    elif params["closest_waypoints"][1] in center_lane and center_variance < 0.4:

        reward += 10

    else:

        reward -= 10

###rewarding to prevent zigzag
    if abs(params["steering_angle"]) < 10:
        reward += 1
    if step > 0:
        reward = ((progress*150)/step)**2
    else:
        reward = 1
# # Steering penality threshold, change the number based on your action space setting
#     ABS_STEERING_THRESHOLD = 15
#     if steering > ABS_STEERING_THRESHOLD:
#         reward *= 0.8

    # if params["closest_waypoints"][1] in fast:

    #     if params["speed"] > 3.3:

    #         reward += 20

    #     else:

    #         reward -= 20

    # elif params["closest_waypoints"][1] in moderate:

    #     if params["speed"] > 1 and params["speed"] <= 3.3:

    #         reward += 10

    #     else:

    #         reward -= 10

    # elif params["closest_waypoints"][1] in slow:

    #     if params["speed"] <= 1:

    #         reward += 10

    #     else:

    #         reward -= 10

    # if params["closest_waypoints"][1] in sharp_turns:
    #     if params['steering_angle'] > 20 and params['steering_angle'] < 50:
    #         reward += 25
    #     else:
    #         reward -= 25
    #
    # if params["closest_waypoints"][1] in rounded_turns:
    #     if params['steering_angle'] > 10 and params['steering_angle'] < 20:
    #         reward += 25
    #     else:
    #         reward -= 25

    # print("Next point", params["closest_waypoints"][1])
    # print("Speed", params["speed"])
    # print("Is left", params["is_left_of_center"])

    return float(reward)
