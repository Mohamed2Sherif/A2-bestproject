from PyPDF2 import PdfFileReader , PdfFileWriter , PdfFileMerger
# open the file path
def pdf_extracter():
    pdf_name = input("Enter the pdf name : ")
    file_loc = open(pdf_name,"rb")
    #get hte base file name just to help add  the -X at the end of the name when x = page number
    base_name = pdf_name.replace(".pdf","")
    # make pypdf2 read the file
    pdf_reader = PdfFileReader(file_loc)
    pdf_writer = PdfFileWriter()
    #make the user input the pages he want in the sub pdf file
    max = pdf_reader.numPages
    while True :
        try :
            num = int(input(f"Enter a page number you want to extract \t Make Sure It's <= {max} : "))
            num = num-1
            if num < max:
                break    
        except BaseException :
                print("pls Enter valid numebr")
            

    pdf_writer.addPage(pdf_reader.getPage(num))
    #create the new file and write the pages using the required subname of the original file
    sub_loc = open(f"{base_name}-{num+1}.pdf","wb")
    pdf_writer.write(sub_loc)
    sub_loc.close()
    file_loc.close()
def merger():
    #The files to Merge 
    files =[]
    #make sure the user inputed  number not letters or weird symbols
    while True :
        try :
            num_files = int(input("How many files Want to Merge : ")) 
            break
        except BaseException :
            print("Make sure you dont have errors")
    #append the file names to the files list 
    for file in range (num_files):
      files.append(input("Enter File Names : "))
    # make the merger function 
    Merger =PdfFileMerger()
    # make the merger function read the file 
    for pdffile in files :
        Merger.append(pdffile)
    # make the user name the final file name 
    MERGED_DOCUMENT = input("Enter the merged file name : ")
    # write the final document and merge the pdf together (it iwll pass the file in wb mode by default )
    Merger.write(f"{MERGED_DOCUMENT}.pdf")
    Merger.close()
def spliter() :
    #-X
    file_name = input("Enter the file name : ")
    base_name = file_name.replace(".pdf","")
    file = open (file_name,"rb")
    reader = PdfFileReader(file)

    max1 = reader.numPages

    for page in range(max1) :
        writer = PdfFileWriter()
        writer.addPage(reader.getPage(page))
        splited_file = (f"{base_name}-{page+1}.pdf") 
        with open (splited_file , "wb") as final :
            writer.write(final)
while True :
    print("1-Merge Two Files. \n2-Extract a page in a separate file.\n3-split file into several pages.\n4-Exit.")
    while True :
        try :
            option = int(input("chose the option : "))
            if option ==1 or option ==2 or option ==3 or option ==4:
             break 
        except BaseException :
            print("Make sure you entered an available option")

    if option == 1:
        merger()
    elif option == 2:
        pdf_extracter()
    elif option == 3 :
        spliter()
    elif option == 4 :
        break
