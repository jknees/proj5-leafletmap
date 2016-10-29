

def process(raw):

	cooked = []

	for line in raw:
		entry = {}
		entry['name'], entry['lat'], entry['lon'] = line.split(',')
		cooked.append(entry)
		print(line)

	return cooked

print(process(open("poi.txt")))
