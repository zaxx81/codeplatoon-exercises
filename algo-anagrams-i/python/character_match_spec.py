from character_match import is_character_match

print(is_character_match('charm', 'march') == True)
print(is_character_match('zach', 'attack') == False)
print(is_character_match('CharM', 'mARcH') == True)
print(is_character_match('abcde2', 'c2abed') == True)
print(is_character_match('Anna Madrigal', 'A man and a girl') == True)
