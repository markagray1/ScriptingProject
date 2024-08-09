#Mark Gray
#Project 1
import os, getpass, shutil, zipfile, random
#os.system('cls')

#Declarations
ZIP_ARCHIVES = os.path.join('Complaints','Zip Archives')
FILE_ARCHIVES = os.path.join('Complaints','File Archives')
PROCESSING = os.path.join('Complaints','Processing')
COMPLAINTS = os.path.join('Complaints')
COMPLAINTS_MASTER = os.path.join('Complaints','Complaints_Master.csv')

#move user
my_desktop = os.path.join('C:\\Users',getpass.getuser(),'Desktop')
os.chdir(my_desktop)

#setup
def setup():
    #delete if it exists
    if os.path.exists(COMPLAINTS):
        shutil.rmtree(COMPLAINTS)
    #make directories
    os.mkdir(COMPLAINTS)
    os.mkdir(ZIP_ARCHIVES)
    os.mkdir(FILE_ARCHIVES)
    os.mkdir(PROCESSING)
    #write in csv file
    with open(COMPLAINTS_MASTER,'w') as f:
        f.write('Complaint ID, Date Received, Company, Product, Issue\n')

#unpacking
def unpacking():
    os.system('cls')
##    shutil.copy('aggregate_complaints_001.zip', 'new1.zip')
##    shutil.copy('aggregate_complaints_002.zip', 'new2.zip')
    try:    
        #put files in zip archives
        desktop_files = os.listdir()
        zipped_list = []
        for i in desktop_files:
            if i.startswith('aggregate_complaints_'):
                zipped_list.append(i)
                shutil.move(i,ZIP_ARCHIVES)

        print('Please wait, processing ' + str(len(zipped_list)) + " zip file(s).")

        zipped_list_2 = []
        for j in zipped_list:
            my_path = os.path.join(ZIP_ARCHIVES,j)
            
            zipped_current = zipfile.ZipFile(my_path)
            zipped_list_2 = zipped_current.namelist()
            zipped_current.close

        files_list = []

        for n in files_list:
            my_path = path.os.join(FILE_ARCHIVES,n)
            active_zip = zipfile.ZipFile(files_current)
            files_list = active_zip.namelist()
            active_zip.close

        for active_file in zipped_list:
            if active_file not in files_list:
                zipped_path_2 = os.path.join(my_desktop,ZIP_ARCHIVES)
                os.chdir(zipped_path_2)
                for json_files in zipped_list_2:
                    files_path = os.path.join(my_desktop,ZIP_ARCHIVES,active_file)
                    processing_path = os.path.join(my_desktop,PROCESSING)

                    active_zip = zipfile.ZipFile(files_path)
                    active_zip.extractall(path = processing_path)
                    active_zip.close

        os.chdir(my_desktop)            
        processing_list = os.listdir(PROCESSING)
        
        #splitting up lines in json files and writing them into complaints master file
        
        for json_file in processing_list:
            json_path_1 = os.path.join(PROCESSING,json_file)
            json_path_2 = os.path.join(FILE_ARCHIVES,json_file)
            with open(json_path_1,'r') as j:
                next(j)
                for line in j:
                    if len(line) < 3:
                        break
                    line_split = line.split(':')
                    date = line_split[1][2:12]
                    complaint_undone = line_split[-1].split('\"')
                    complaint_id = complaint_undone[1]
                    split_1 = line_split[-11]
                    company_undone = split_1.split('\",')
                    company1 = company_undone[0][2:]
                    company2 = company1.replace(',',' ')
                    company3 = company2.replace('  ',' ')
                    split_2 = line_split[2]
                    product_undone = split_2.split('\",')
                    product1 = product_undone[0][2:]
                    product2 = product1.replace(',',' ')
                    product3 = product2.replace('  ',' ')
                    split_3 = line_split[4]
                    issue_undone = split_3.split('\",')
                    issue1 = issue_undone[0][2:]
                    issue2 = issue1.replace(',',' ')
                    issue3 = issue2.replace('  ',' ')
                    with open(COMPLAINTS_MASTER,'a') as a:
                        a.write(complaint_id + ',' + date + ',' + company3 + ',' + product3 + ',' + issue3 + '\n')
            shutil.move(json_path_1,json_path_2)
        os.system('cls')
        print("Complaint file processing is complete.")

    except:
        print("Processing is complete")
        pass
    input("\nPress enter to continue")
    os.system('cls')
    
def cleanup():
    os.system('cls')
    csv_data = []
    unique = []
    os.chdir(my_desktop)
    
    with open(COMPLAINTS_MASTER,'r') as r:
        next(r)
        print("Removing duplicate records please wait \n")
        for line in r:
            csv_data.append(line)
            if line not in unique:
                unique.append(line)

    print("\t\t\tNumber of current records: " + str(len(csv_data)))

    
    print("Number of records after removing duplicates: " + str(len(unique)))

    duplicates = str(len(csv_data) - len(unique))

    print("\n\t\t\tDuplicates removed: " + str(duplicates))


    #Delete csv file
    os.chdir(my_desktop)
    delete = os.path.join(COMPLAINTS)
    os.chdir(delete)
    os.remove('Complaints_Master.csv')

    #open a new one
    with open('Complaints_Master.csv','a') as new:
        new.write('Complaint ID, Date Received, Company, Product, Issue\n')
        for line in unique:
            new.write(line)
    input("\nPress enter to continue")
    os.system('cls')


    

def report():
    os.chdir(my_desktop)
    os.system('cls')
    #make lists and counter
    products_list = []
    all_products = []
    counter = 0

    #open file and read lines into a new list
    with open(COMPLAINTS_MASTER,'r') as o:
        for line in o:
            products_list.append(line)
            #print(products_list)
    for line in products_list:
        line_split = line.split(',')
        if line_split[3] not in all_products:
            all_products.append(line_split[3])
    #delete "product"
    del all_products[0]
##    print(len(all_products))
##    print(all_products)

    #Products menu
    while True:
        print("Avaliable Products\n------------------\n")
        try:
            all_products.sort()
            for i in range(1,18):
                print("\t\t" + str(i) + ". " + all_products[i-1])

        except:
            pass

        
        user_input = input("\nEnter the product number (zero to exit): ")
        
        try:
            #Check if input is in the range 
            if (int(user_input) > 0 and int(user_input) < 18):
                user_choice = all_products[int(user_input) - 1]
                unique_iss = []
                unique_comp = []
                count = 0
                
                for item in products_list:
                    split = item.split(',')

                    if split[3] == user_choice:
                        count = count + 1

                        #append companies to company list and issues to issue list
                        if split[2] not in unique_comp:
                            unique_comp.append(split[2])
                        if split[4] not in unique_iss:
                                 unique_iss.append(split[4])

                #Matching records
                os.system('cls')
                print('PRODUCT: ' + str(user_choice.upper()))

                print('Number of Companies Involved: ' + str(len(unique_comp)))

                print('   Number of matching records: ' + str(count))

                #issues
                print('\n\t\t\tISSUES\n\t\t\t------\n')
                unique_iss.sort()

                for issue in unique_iss:
                    print(issue[:-1])

                input('\nPress enter to continue: ')
                os.system('cls')
                continue

            elif (user_input == '0'):
                break
            else:
                os.system('cls')
                print("That is not a valid product number\n")
                input("\nPress enter to continue: ")
                os.system('cls')
                continue

        except:
            os.system('cls')
            print("That is not a valid product number\n")
            input("\nPress enter to continue: ")
            os.system('cls')
            pass
            
    
    os.system('cls')
        
#call setup      
setup()

#menu
while True:
    print('''----- MAIN MENU -----\n
Please select from the following options: \n
1. Process Complaint Files
2. Remove Duplicate Complaint Records
3. Report by Product
4. Exit''')

    user_choice = input("\nOption#: ")

    if user_choice == '1':
        os.system('cls')
        unpacking()
    elif user_choice == '2':
        os.system('cls')
        cleanup()
    elif user_choice == '3':
        os.system('cls')
        report()
    elif user_choice == '4':
        break
    else:
        os.system('cls')
        continue



        

