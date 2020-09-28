strings = ['Samsung j5',
           'samsung galaxy',
           'iphone 10',
           'iphone 5S',
           'samsung a9',
           'ASUS-Roc',
           'Acer HyperX',
           'Macbook Air 18',
           'Macbook Pro 18',
           'geforce gtx460',
           'HDD 1TB',
           'SSD Adata 3100/1400mbs',
           'HDD 2TB',
           'Mac 19',
           'amd Ryzen 490',
           'GeForce TI 2020',
           'SSD Kingston 512 gb',
           'SSD Adata 1TB',
           'Acer zenbook',
           'Asus razer']
def write_to(strings):
       with open('message2.txt', 'w') as file1:
            for sentence in strings:
                file1.write(sentence.lower() + '\n')
write_to(strings)
def red_lines():
    with open('message2.txt', 'r') as file2:
        var = file2.readlines()
        for i in var:
            if i.startswith('iphone') or i.startswith('samsung'):
                with open('telephone.txt','a')as file3:
                    file3.write(i)
            elif i.startswith('asus') or i.startswith('acer') or i.startswith('mac') or i.startswith('macbook'):
                with open('computers.txt', 'a')as file4:
                    file4.write(i)
            elif i.startswith('ssd') or i.startswith('hdd'):
                with open('hard_disk.txt', 'a') as file5:
                    file5.write(i)
            elif i.startswith('geforce') or i.startswith('amd'):
                with open('processor.txt','a') as file6:
                    file6.write(i)
red_lines()
def open_files(file_name):
    with open(file_name,'r') as read1:
        phones = read1.read()
file_name = 'telephone.txt'
open_files(file_name='telephone.txt')












