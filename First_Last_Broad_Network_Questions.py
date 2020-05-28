import math
import random
import cidr_dec_conv

ip_list = []

# This generates a random subnet mask in CIDR and decimal notation.
def FLBN_question_creation_func():
    randCidrGenerator = random.randint(0, 32)
    x = randCidrGenerator
    y = cidr_dec_conv.cidrconvert(x)
    generatedcidrlist = [x, y]
    return generatedcidrlist  # format of list is [[32], [255.255.255.255]]


# This function generates a random private IP address and pulls a subnet mask

def small_private_IP_Subnet_Generator():
    small_range_start = str(192.168)
    selection_priv_IP = random.randint(0, 2)
    final_small_ip_string = ''
    for i in range(0, 2):
        final_small_ip_string += '.'
        ip_octet_gen = random.randint(0, 255)
        final_small_ip_string += str(ip_octet_gen)
    small_range_start += str(final_small_ip_string)
    ip_list.append(small_range_start)

# selection_priv_IP = random.randint(0,2)
# subnetmask_pair_v = FLBN_question_creation_func()
# medium_range_start = str(172.16)
# large_range_start = str(10)


def medium_private_IP_Subnet_Generator():
    medium_range_start = str(172.16)
    final_medium_ip_string = ''
    for i in range(0, 2):
        final_medium_ip_string += '.'
        ip_octet_gen = random.randint(0, 255)
        final_medium_ip_string += str(ip_octet_gen)
    medium_range_start += str(final_medium_ip_string)
    ip_list.append(medium_range_start)


def large_private_IP_Subnet_Generator():
    large_range_start = str(10)
    final_large_ip_string = ''
    for i in range(0, 3):
        final_large_ip_string += '.'
        ip_octet_gen = random.randint(0, 255)
        final_large_ip_string += str(ip_octet_gen)
    large_range_start += str(final_large_ip_string)
    ip_list.append(large_range_start)



def final_IP_Quest_Gen():
    small_private_IP_Subnet_Generator()
    medium_private_IP_Subnet_Generator()
    large_private_IP_Subnet_Generator()
    generated_ip = random.randint(0,2)
    generated_subnet_mask = FLBN_question_creation_func()
    generated_ip = ip_list[generated_ip]
    ip_subnet_list = [generated_ip, generated_subnet_mask]
    print(ip_subnet_list)
    return ip_subnet_list


def text_IP_Quest_Gen():
    ip_info = final_IP_Quest_Gen()
    select_subnet_mask_type = random.randint(0,1)
    # 0 - first available address
    if select_subnet_mask_type == 0:
        question1 = input("Given IP address: " + str(ip_info[0]) + " - subnet mask /" + str(ip_info[1][select_subnet_mask_type])
                         + "\nWhat is the first available IP address on this subnet?\nEnter here: ")
    else:
        question1 = input("Given IP address: " + str(ip_info[0]) + " - subnet mask: " + str(ip_info[1][select_subnet_mask_type])
                         + "\nWhat is the first available IP address on this subnet?\nEnter here: ")
    # 1 - last available address
    if select_subnet_mask_type == 0:
        question2 = input("What is the last available IP address on this subnet?\nEnter here: ")
    else:
        question2 = input("What is the last available IP address on this subnet?\nEnter here: ")
    # 2 - broadcast address
    if select_subnet_mask_type == 0:
        question3 = input("What is the broadcast address of this subnet?\nEnter here: ")
    else:
        question3 = input("What is the broadcast address of this subnet?\nEnter here: ")

    # 3 - network address
    if select_subnet_mask_type == 0:
        question4 = input("What is the network address of this subnet?\nEnter here: ")
    else:
        question4 = input("What is the network address of this subnet?\nEnter here: ")

    listofquestions = []
    listofquestions.append(question1)
    listofquestions.append(question2)
    listofquestions.append(question3)
    listofquestions.append(question4)
    listofquestions.append(ip_info)
    return listofquestions





