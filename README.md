# llamaindex_typhoon

### install  
```sh
pip install git+https://github.com/WATCHARAPHON6912/llamaindex_typhoon.git
```
### example
```python
from Modbus_Film69 import Modbus_Film69
ser=Modbus_Film69(port="COM3", slaveaddress=1, baudrate=9600)
while 1:
    rec,len_Bytes=ser.send("01 03 20 00 00 04")
    print(rec,len_Bytes)
```
