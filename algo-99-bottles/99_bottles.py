def bottle_song():
	starting_count = 99

	for n in range(starting_count, -1, -1):
		if n == 2:
			print(f"{n} bottles of beer on the wall, {n} bottles of beer. ")
			print(f"Take one down and pass it around, {n-1} bottle of beer on the wall.")
		elif n == 1:
			print(f"{n} bottle of beer on the wall, {n} bottle of beer. ")
			print(f"Take one down and pass it around, No more bottles of beer on the wall.")
		elif n == 0:
			print("No more bottles of beer on the wall, no more bottles of beer.")
			print(f"Go to the store and buy some more, {starting_count} bottles of beer on the wall.")
			break
		else:
			print(f"{n} bottles of beer on the wall, {n} bottles of beer. ")
			print(f"Take one down and pass it around, {n-1} bottles of beer on the wall.")

bottle_song()