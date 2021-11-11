header = 'sf_100_dt_hvac_cfd_r1_09_'

for hour in range(1, 49):
	h = hour % 24
	d = 1 + hour // 24
	if h == 0:
		h = 24
		d -= 1

	with open(header + str(d).zfill(2) + '_' + str(h).zfill(2) + '_00.json', 'w') as out:
		with open (str(hour) + '.json', 'r') as f:
			content = f.readlines()
			for line in content:
				if 'inf' in line:
					# print('inf')
					line = line.replace('inf', '999')
				if 'wind_d' in line:
					# print(line)
					line = line.replace('nan', '0')
				out.write(line + '')
