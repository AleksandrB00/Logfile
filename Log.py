class Log():
  def __init__(self, log_file_name, excel_file_name):
    self.log_file_name = log_file_name
    self.excel_file_name = excel_file_name


  def get_stat(self):
    vocabulary = ['[main] D [a] New route: Route(code=', "2", "[", "г", ", tar"]
    f1 = open(self.log_file_name, 'r', encoding='UTF-8' )
    f2 = open (self.excel_file_name, 'a', encoding='UTF-8')
    k = 0
    for line in f1.readlines():
      k+=1
      if vocabulary[0] in line:
       a = line[line.find(vocabulary[1]):line.find(vocabulary[2])]
       b = line[line.find(vocabulary[3]):line.find(vocabulary[4])]
       f2.writelines(a + b + '\n')
 

Value1 = Log('1.txt', 'test.txt')
Value1.get_stat()

Value2 = Log('2.txt', 'test.txt')
Value2.get_stat()

Value3 = Log('3.txt', 'test.txt')
Value3.get_stat()
