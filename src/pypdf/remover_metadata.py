from PyPDF2 import PdfFileReader, PdfFileWriter

# 若出现以下报错信息：
# ‘latin-1’ codec can’t encode characters in position 8-11: ordinal not in range(256)
# 通常这情况是出现了中文字符编码问题，解决方案见代码最后

inputfilename = '20210331.pdf'      # 若找不到文件则使用绝对路径
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



# 1、修改pypdf2包中的generic.py文件
# 由于我使用的是anaconda，路径为anaconda\Lib\site-packages\PyPDF2\generic.py
# 由于我使用的是Python37，路径为Python37\Lib\site-packages\PyPDF2\generic.py

# generic.py文件第488行原文

# try:
#    return NameObject(name.decode('utf-8'))
#    except (UnicodeEncodeError, UnicodeDecodeError) as e:
#    # Name objects should represent irregular characters
#    # with a '#' followed by the symbol's hex number
#    if not pdf.strict:
#       warnings.warn("Illegal character in Name Object", utils.PdfReadWarning)
#       return NameObject(name)
#    else:
#       raise utils.PdfReadError("Illegal character in Name Object")

# 改成

# try:
#      return NameObject(name.decode('utf-8'))
#  except (UnicodeEncodeError, UnicodeDecodeError) as e:
#      try:
#          return NameObject(name.decode('gbk'))
#      except (UnicodeEncodeError, UnicodeDecodeError) as e:
#          # Name objects should represent irregular characters
#          # with a '#' followed by the symbol's hex number
#          if not pdf.strict:
#              warnings.warn("Illegal character in Name Object", utils.PdfReadWarning)
#              return NameObject(name)
#          else:
#              raise utils.PdfReadError("Illegal character in Name Object")
            
# 2、修改pypdf2包中的utils.py文件
# utils.py238行原文

#  r = s.encode('latin-1')
#  if len(s) < 2:
#    		bc[s] = r
#  return r

# 修改为

# try:
#     r = s.encode('latin-1')
#     if len(s) < 2:
#         bc[s] = r
#     return r
# except Exception as e:
#     print(s)
#     r = s.encode('utf-8')
#     if len(s) < 2:
#         bc[s] = r
#     return r

# 问题解决
# ————————————————
# 版权声明：本文为CSDN博主「小羊瓜瓜」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/weixin_43116153/article/details/105218309
