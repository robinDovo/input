def read_file(filename):

	lines = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			lines.append(line.strip())
	return lines 

def convert(lines):

	person = None
	hu_word_count = 0
	hu_k_count = 0
	s_word_count = 0
	s_k_count = 0
	for line in lines:
		s = line.split(' ')
		print(s)
		time = s[0]
		name = s[1] 
		if name == '丫頭仔':
			if s[2] == '貼圖':
				 s_k_count += 1
			else:
				for m in s[2]:
					s_word_count += len(m)
		elif name == '洪小清':
			if s[2] == '貼圖':
				hu_k_count += 1
			else:
				for m in s[2]:
					hu_word_count += len(m)
	print('丫頭仔說了', s_word_count, '個字', '共有', s_k_count, '張貼圖')
	print('洪小清說了', hu_word_count, '個字', '共有', hu_k_count, '張貼圖')



def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('[LINE]丫頭仔.txt')
	lines = convert(lines)
	# write_file('output.txt', lines)


main()

 