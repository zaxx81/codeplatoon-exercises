import re

def anagrams_for(word, list_of_words):
	results = []
	str_arr1 = re.findall("[a-z0-9]", str(word).lower())
	compare_str1 = "".join(sorted(str_arr1))

	for elem in list_of_words:			
		str_arr2 = re.findall("[a-z0-9]", elem.lower())
		compare_str2 = "".join(sorted(str_arr2))
		if (compare_str1 == compare_str2):
			results.append(elem)

	return results
	