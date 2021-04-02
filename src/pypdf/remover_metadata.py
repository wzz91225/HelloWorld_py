from PyPDF2 import PdfFileReader, PdfFileWriter

inputfilename = '20210331.pdf'
outputfilename = '20210331new.pdf'

fin = open(inputfilename, 'rb')
reader = PdfFileReader(fin)
writer = PdfFileWriter()

writer.appendPagesFromReader(reader)


# read origin metadata
# metadata = reader.getDocumentInfo()
# writer.addMetadata(metadata)

# remove origin metadata
writer.addMetadata({'/Producer': 'Adobe'})


# Write your custom metadata here:
# writer.addMetadata({
#     # '/Title': 'this'
#     '/CreateDate': '2021-03-31T21:21:35+08:00',
#     '/CreatorTool': 'RICOH MP 3554',
#     '/ModifyDate': '2021-03-31T21:21:35+08:00',
#     '/Producer': 'RICOH MP 3554'
# })


fout = open(outputfilename, 'wb') #ab is append binary; if you do wb, the file will append blank pages
writer.write(fout)

fin.close()
fout.close()
