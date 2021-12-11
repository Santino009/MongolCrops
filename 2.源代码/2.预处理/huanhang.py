def delblankline(infile, outfile):    #读取文件, 将文件内的空白行删除
    infopen = open(infile, 'r', encoding="utf-8")
    outfopen = open(outfile, 'w', encoding="utf-8")
    db = infopen.read()

    outfopen.write(db.replace('/n', ''))
    infopen.close()
    outfopen.close()
delblankline(r'C:\Users\DELL\Desktop\put.txt', r'C:\Users\DELL\Desktop\put.txt_out.txt')