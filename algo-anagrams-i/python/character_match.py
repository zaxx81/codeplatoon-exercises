import re

def is_character_match(string1, string2):
	
	str_arr1 = re.findall("[a-z0-9]", string1.lower())
	str_arr2 = re.findall("[a-z0-9]", string2.lower())
  
	compare_str1 = "".join(sorted(str_arr1))
	compare_str2 = "".join(sorted(str_arr2))

	return compare_str1 == compare_str2
