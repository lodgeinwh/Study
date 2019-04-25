def checkio(opacity):
	fab = [0, 1]
	while fab[-1] < 10000:
		fab.append(fab[-1] + fab[-2])
	age = 0
	result = 10000
	while opacity != result:
		age += 1
		if age in fab:
			result -= age
		else:
			result += 1
	return age
	
	
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"