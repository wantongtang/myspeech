import csv



with open("test.csv","w") as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(["fname","label"])
	for i in range(1,10):
		writer.writerow([i,i*2])
		

