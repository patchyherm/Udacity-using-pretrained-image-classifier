#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#
# PROGRAMMER: Patch
# DATE CREATED: 07/06/20
# REVISED DATE: 14/06/20
# PURPOSE: Create the function get_pet_labels that creates the pet labels from
#          the image's filename. This function inputs:
#           - The Image Folder as image_dir within get_pet_labels function and
#             as in_arg.dir for the function call within the main function.
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main.
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir


def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames
    of the image files. These pet image labels are used to check the accuracy
    of the labels that are returned by the classifier function, since the
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    filename_list = listdir(image_dir)
    results_dic = dict()
    pet_names_split = list()
    pet_names_list = list()

    for i in range(len(filename_list)):
        pet_names_split.append(filename_list[i].lower().split("_"))

    for i in pet_names_split:
        pet_name = ""
        for j in i:
            if j.isalpha():
                pet_name += j + " "
        pet_names_list.append(pet_name.strip())

    pet_labels = pet_names_list

    for idx in range(0, len(filename_list), 1):
        if (filename_list[idx] not in results_dic) and (not filename_list[idx].startswith(".")):
            results_dic[filename_list[idx]] = [pet_labels[idx]]
        elif (filename_list[idx] not in results_dic) and (filename_list[idx].startswith(".")):
            continue
        else:
            print("** Warning: Key=", filename_list[idx],
               "already exists in results_dic with value =",
               results_dic[filename_list[idx]])

    # Replace None with the results_dic dictionary that you created with this
    # function

    return results_dic
