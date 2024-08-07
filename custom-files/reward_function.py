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
    left_lane = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,21, 22, 23,24, 25, 26, 27,28,29,30,31,32,33,34, 35, 36, 37, 38, 39,40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93,90, 91, 92, 93, 94, 95, 96, 97, 98, 99,100, 101, 102, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155]

    center_lane = [103,104, 105, 106, 107, 108, 109, 110, 111, 112, 113,114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131]  # Fill in the waypoints
    right_lane = [ 57, 58, 59,60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80]  # Fill in the waypoint4
    right_turn = [63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]

    # Speed

    fast = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,12, 13,14, 15, 16, 17, 18,19,20,21,22, 23, 24, 25, 26, 27,28,29,30,31,32,33,34, 35, 36, 37, 38, 39,40, 41,54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64,65, 66,80, 81, 82, 83,84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116,117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131,132,133,134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154]  # 3

    moderate = [11,42,43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 67, 68, 69,70, 71, 72, 73, 74, 75, 76, 77,78,79,99, 100, 101, 102, 103, 104, 105, 106]  # 2

    # slow = [63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 73]  # 1
    sharp_turns = [65,66,67]
    # rounded_turns = [19, 32, 107]

    reward = 30

    if params["all_wheels_on_track"]:
        print("on track")

        reward += 10

    else:

        reward -= 30

    if params["closest_waypoints"][1] in left_lane and params["is_left_of_center"]:
        print("left lane")
        reward += 10

    elif params["closest_waypoints"][1] in right_lane and not params["is_left_of_center"]:

        reward += 20

    elif params["closest_waypoints"][1] in center_lane and center_variance < 0.4:
        print("center lane")

        reward += 10

    else:

        reward -= 10

##rewarding to prevent zigzag
    # if steering < 10:#( / params["steps"]
    #     print("sterring < 10")
    #     reward += 5
    step = params["steps"]

    if step > 0:
        reward += ((params["progress"]*150)/step)#######
        print(f"((params['progress']*150)/step) = {((params['progress']*150)/step)}")

#####SPEED

    if params["closest_waypoints"][1] in fast:

        if params["speed"] > 2.5:#add reward += speed*2

            print("spped")

            reward += 5

        else:

            reward -= 5

    elif params["closest_waypoints"][1] in moderate:

        if params["speed"] > 1.75 and params["speed"] <= 2.5:
            # print("moderate")
            reward += 5
            
    # elif params["closest_waypoints"][1] in slow:
    #     if params["speed"] <1.2 and params["speed"] >= 1:
    #         # print("slow")
    #         reward += 5

        else:

            reward -= 5

    print(params["closest_waypoints"][1])

    if params["closest_waypoints"][1] in right_turn:
        print("in right turn")
        if params["steering_angle"] < -5:
            reward -= 10
        else:
            reward += 10

        if params["closest_waypoints"][1] in sharp_turns:
            if params["steering_angle"] >= 12:
                reward += 10
            else:
                reward -= 10
    else:
        print("in left turn")

        if params["steering_angle"] > 5:
            reward -= 10
        else:
            reward += 10



# Steering penality threshold, change the number based on your action space setting
    ABS_STEERING_THRESHOLD = 15
    if steering > ABS_STEERING_THRESHOLD:
        print("steering more than 15")
        reward *= 0.8
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
    reward += params["speed"]**2

    return float(reward)


# params = {"speed":2.75,"steering_angle":0,"steps":71,"distance_from_center":90,"heading":8,"waypoints":[[1,2],[1,2],[1,2]],"closest_waypoints":[1,11],"track_width":10,"all_wheels_on_track":True,"is_left_of_center":True,"progress":10.61311464}
# print(reward_function(params))