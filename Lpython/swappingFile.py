def swapFileData(file1, file2):
    try:
        
        with open(file1, 'r') as f1:
            data_a = f1.read()

       
        with open(file2, 'r') as f2:
            data_b = f2.read()

        
        with open(file1, 'w') as f1:
            f1.write(data_b)

        
        with open(file2, 'w') as f2:
            f2.write(data_a)

        print(f"Data swapped successfully between {file1} and {file2}")
    except Exception as e:
        print(f"An error occurred: {e}")


file1_name = input("Enter the name of the first file (e.g., sample1.txt): ")
file2_name = input("Enter the name of the second file (e.g., sample2.txt): ")


swapFileData(file1_name, file2_name)