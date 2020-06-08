import First_Last_Broad_Network_Questions



imported_data = First_Last_Broad_Network_Questions.text_IP_Quest_Gen()



def first_convert_IP_func():
    submask_chart_dict = {128: 128,
                           192: 64,
                           224: 32,
                           240: 16,
                           248: 8,
                           252: 4,
                           254: 2,
                           255: 1}



    answer0 = imported_data[0]
    solve_for_this_ip = imported_data[5][0]
    solve_for_mask = imported_data[5][1][1]
    wild_card = 32 - imported_data[5][1][0]
    print('this is unfinished wild card ' + str(wild_card))
    wild_card_done = (2**wild_card) - 2
    print(wild_card_done)
    print('this is solve for masks ' + str(solve_for_mask))
    ipaddress_split = solve_for_this_ip.split(".")
    subnet_mask_split = solve_for_mask.split(".")
    skips = (subnet_mask_split.count("255"))
    print(ipaddress_split)
    if skips == 4:
       skips -=1
    first_non_max_subnet = subnet_mask_split[skips]
    permanent_start = ipaddress_split[0:skips]
    skipped_portion_ip = ipaddress_split[skips::]
    print(permanent_start,skipped_portion_ip)
    broadcast_range = 0
    while broadcast_range <= int(skipped_portion_ip[0]):
        broadcast_range += submask_chart_dict[int(first_non_max_subnet)]
    broadcast_range -= 1
    network_range = broadcast_range - submask_chart_dict[int(first_non_max_subnet)]
    if network_range != 0:
        network_range += 1

    if network_range < 0:
        network_range += 1

    maximum_host_ip = broadcast_range - 1
    minimum_host_ip = network_range + 1
    print(broadcast_range,network_range,maximum_host_ip,minimum_host_ip)

    print(permanent_start)
    #final broadcast_range IP
    broadcast_start_final = permanent_start.copy()
    broadcast_start_final.append(broadcast_range)
    while len(broadcast_start_final) < 4:
        broadcast_start_final.append(255)
    print('final broadcast address answer: ' + str(broadcast_start_final))
    if len(permanent_start) == 0:
        pass
    print(permanent_start)

    #final network_range IP
    network_start_final = permanent_start.copy()
    network_start_final.append(network_range)
    while len(network_start_final) < 4:
        network_start_final.append(0)
    print('final network address answer: ' + str(network_start_final))

    #final max usable IP
    for x in range(-4, 0):
        if 0
    max_usable_ip = permanent_start.copy()
    max_usable_ip.append(broadcast_range - 1)
    while len(max_usable_ip) < 4:
        max_usable_ip.append(255)
    print('final max usable ip address answer: ' + str(max_usable_ip))





first_convert_IP_func()


# Create functions to convert IP into proper subnet answers then combine them with imported questions.

# Must figure out how to handle when you get a 0 for a dictionary key value








