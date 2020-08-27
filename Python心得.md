1. os.startfile(r'D:\pyqtStudy\Qevent.xmind')

2. 路径不能用单引号，比如QPixmap

3. 读取excel

   ```python
   import xlrd
   
   
   data = xlrd.open_workbook("01.xls") #打开当前目录下名为01.xls的文档
   #此时data相当于指向该文件的指针
   table = data.sheet_by_index(0) #通过索引获取，例如打开第一个sheet表格
   table = data.sheet_by_name("sheet1") #通过名称获取，如读取sheet1表单
   table = data.sheets()[0] #通过索引顺序获取
   # 以上三个函数都会返回一个xlrd.sheet.Sheet()对象
    
   names = data.sheet_names()    #返回book中所有工作表的名字
   data.sheet_loaded(sheet_name or indx)   # 检查某个sheet是否导入完毕
   
   nrows = table.nrows  #获取该sheet中的有效行数
   table.row(rowx)  #返回由该行中所有的单元格对象组成的列表
   table.row_slice(rowx)  #返回由该列中所有的单元格对象组成的列表
   table.row_types(rowx, start_colx=0, end_colx=None)    #返回由该行中所有单元格的数据类型组成的列表
   table.row_values(rowx, start_colx=0, end_colx=None)   #返回由该行中所有单元格的数据组成的列表
   table.row_len(rowx) #返回该列的有效单元格长度
   
   ncols = table.ncols #获取列表的有效列数
   table.col(colx, start_rowx=0, end_rowx=None) #返回由该列中所有的单元格对象组成的列表
   table.col_slice(colx, start_rowx=0, end_rowx=None) #返回由该列中所有的单元格对象组成的列表
   table.col_types(colx, start_rowx=0, end_rowx=None) #返回由该列中所有单元格的数据类型组成的列表
   table.col_values(colx, start_rowx=0, end_rowx=None) #返回由该列中所有单元格的数据组成的列表
   
   table.cell(rowx, colx)  # 返回单元格对象
   table.cell_type(rowx, colx)  # 返回单元格中的数据类型
   table.cell_value(rowx,colx)   #返回单元格中的数据
   ```

   

4. 123
