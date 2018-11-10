def testPairedList():
    correct_paired = 0
    incorrect_paired = 0
    correct_unpaired = 0
    incorrect_unpaired = 0
    for i in range(300):
        person_paired = paired_list[i]
        person_name_paired = person_paired[0]
        person_first_number_paired = person_paired[1]
        person_second_number_paired = person_paired[2].split('\n')[0]
        idx1_paired = person2IndexConverter(person_name_paired,person_first_number_paired)
        idx2_paired = person2IndexConverter(person_name_paired,person_second_number_paired)
        distance_two_image_paired = distance(embedded[idx1_paired], embedded[idx2_paired])

        person_unpaired = unpaired_list[i]
        person_name_1_unpaired = person_unpaired[0]
        person_name_2_unpaired = person_unpaired[2]
        person_first_number_unpaired = person_unpaired[1]
        person_second_number_unpaired = person_unpaired[3].split('\n')[0]
        idx1_unpaired = person2IndexConverter(person_name_1_unpaired,person_first_number_unpaired)
        idx2_unpaired = person2IndexConverter(person_name_2_unpaired,person_second_number_unpaired)
        distance_two_image_unpaired = distance(embedded[idx1_unpaired], embedded[idx2_unpaired])
        
        if(distance_two_image_paired < 0.70):
            correct_paired += 1
        else:
            incorrect_paired += 1

        if(distance_two_image_unpaired >= 0.70):
            correct_unpaired += 1
        else:
            incorrect_unpaired += 1
              
    print("Correct Number: [PairedList]",correct_paired)
    print("Incorrect Number: [PairedList]",incorrect_paired)
    print("Ratio: [PairedList]",correct_paired/(300))
    print("")
    print("Correct Number: [UnPairedList]",correct_unpaired)
    print("Incorrect Number: [UnPairedList]",incorrect_unpaired)
    print("Ratio: [UnPairedList]",correct_unpaired/(300))