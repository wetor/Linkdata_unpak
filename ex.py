import io,os,struct,glob,codecs,math,re,zlib

src = 'LINKDATA_A.BIN'

fl = open(src,'rb')
filename = os.path.basename(src)
if os.path.isdir(filename+'_unpacked') == False:
    os.makedirs(filename+'_unpacked')
fl.seek(4)
file_num, = struct.unpack('<I',fl.read(4))
print(file_num)
for i in range(file_num):
    fl.seek(15+i*16)
    file_pos, = struct.unpack('<I',fl.read(4))
    fl.seek(5,1)
    data_size,=struct.unpack('<I',fl.read(4))
    file_size,=struct.unpack('<I',fl.read(4))
    print(file_pos,data_size,file_size)
    fl.seek(file_pos)
    file = open(filename+'_unpacked\\'+str(i)+'.bin','wb')
    if file_size==0 :#无压缩
        data=fl.read(data_size)
        file.write(data)
    else:
        fl.seek(4,1)
        if(file_pos==155001858):
            fl.seek(-2,1)
        temp_size,=struct.unpack('<I',fl.read(4))
        while temp_size!=0 :
            data=zlib.decompress(fl.read(temp_size))
            file.write(data)
            temp_size,=struct.unpack('<I',fl.read(4))
    file.close()
fl.close()
