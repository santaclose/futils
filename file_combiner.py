import os
import sys

output_file_path = "output"
if len(sys.argv) < 2:
	print("Usage: python file_combiner c folder_path [output_file_path]\nor     python file_combiner s input_file_path")
	exit()


def read_in_chunks(file, total_size, chunk_size=1024):
	currently_read = 0
	while currently_read < total_size:
		left_to_read = total_size - currently_read
		current_read_size = left_to_read if left_to_read < chunk_size else chunk_size
		current_read_bytes = file.read(current_read_size)
		yield current_read_bytes
		currently_read += current_read_size


def combine(input_folder_path, output_file_path):
	files_in_folder = [os.path.join(dp, f).replace('\\', '/') for dp, dn, filenames in os.walk(input_folder_path) for f in filenames]

	for i, file_path in enumerate(files_in_folder):
		file_open_mode = 'w' if i == 0 else 'a'
		with open(output_file_path, file_open_mode) as output_file:
			output_file.write(file_path + ', ')
		# with open(file_path, 'rb') as file:
		# 	file_bytes = file.read()
		# with open(output_file_path, 'ab') as output_file:
		# 	output_file.write(f"{len(file_bytes)}\n".encode('utf-8'))
		# 	output_file.write(file_bytes)
		# 	output_file.write("\n".encode('utf-8'))
		with open(file_path, 'rb') as file:
			file.seek(0, os.SEEK_END)
			file_size = file.tell()
			file.seek(0, os.SEEK_SET)
			with open(output_file_path, 'ab') as output_file:
				output_file.write(f"{file_size}\n".encode('utf-8'))
				for piece in read_in_chunks(file, file_size):
					output_file.write(piece)
				output_file.write("\n".encode('utf-8'))


def separate(input_file_path):
	with open(input_file_path, 'rb') as input_file:
		while True:
			line_bytes = input_file.readline()
			if len(line_bytes) == 0:
				break
			file_path, file_length = line_bytes.decode('utf-8')[:-1].split(', ')
			file_length = int(file_length)

			# file_bytes = input_file.read(file_length)
			# os.makedirs(os.path.dirname(file_path), exist_ok=True)
			# with open(file_path, 'wb') as file:
			# 	file.write(file_bytes)
			os.makedirs(os.path.dirname(file_path), exist_ok=True)
			with open(file_path, 'wb') as file:
				for piece in read_in_chunks(input_file, file_length):
					file.write(piece)


			extra_line = input_file.read(1)


if sys.argv[1] == 'c':
	input_folder_path = sys.argv[2]
	if len(sys.argv) > 3:
		output_file_path = sys.argv[3]
	combine(input_folder_path, output_file_path)
else:
	input_file_path = sys.argv[2]
	separate(input_file_path)
