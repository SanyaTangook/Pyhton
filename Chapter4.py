#ตัวดำเนินการ Operator
'''
เป็นสัญลักษ์ที่บอกให้อินเตอร์พรีเตอร์ดำเนินการอย่างใดอย่างหนึ่งกับข้อมูลในตัวแปรและส่งค่าคงที่ต่างๆ
เช่นการคำนวณ + - / * และการเปรียบเทียบที่ใข้เครื่องหมายที่ > < >= <= != == เป็นต้น
ส่วนข้อมูลที่นำมากระทำกับตัวดำเนินการนั้น เรียกว่า โอเปอแรนด์
'''
#นิพจน์ Expression 
"""
เป็นการนำตัวแปรและค่าคงที่มากระทำด้วยตัวดำเนินการแล้วได้ออกมาเป็นค่าผลลัพธ์ 
นิพรน์จึงประกอบด้วย โอเปอแรนด์ (ตัวแปร ค่าคงที่) และตัวดำเนินการ
"""
x,y=7,2
a,b=True,False
#ตัวดำเนินการยูนารี (Unary Operator)
print(-5 , ",",--5) # - ใส่ค่า ค่าบวกจะเป็นลบ ค่าลบจะเป็นบวก
print(+5 ,",",+-5) # + ไม่จำเป็นต้องใส่ เพราะจะได้ค่าเดิม
print(~5) #เปลี่ยนบิตข้อมูลเป็นตรงข้าม ~x = -x-1

#ตัวดำเนินการทางคณิตศาสตร์ (Arithmetic operator)
print("X+Y = ", x+y) #การบวก
print("X-Y = ", x-y) #การลบ
print("X*Y = ", x*y) #การคูณ
print("X/Y = ", x/y ) #การหาร
print("X//Y = ", x//y) #หารไม่เอาเศษ ทิ้งเศษ
print("X%Y = ", x%y) #หารเอาแต่เศษ
print("X**Y = ",x**y) #การยกกำลัง

#ตัวดำเนินการเปรียบเทียบ
'''เป็นตัวดำเนินการที่นำข้อมูลมาเปรียบเทียบ ผลลักพธ์จะได้เป็น บูลีน'''
print(x==y) #เท่ากัน
print(x!=y) #ไม่เท่ากับ
print(x>y) #มากกว่า
print(x<y) #น้อยกว่า
print(x>=y) #มากกว่าหรือเท่ากับ
print(x<=y) #น้อยกว่าหรือเท่ากับ

#ตัวดำเนินการทางตรรกะ (Logical operator)
print("a and b is ",a and b) #ต้องเหมือนกันทั้งคู่
print("a or b is " ,a or b) # ตัวใดตัวนึง True
print("a not is ", not a) # ตรงข้ามกับตัวแปร

# ตัวดำเนินการบิตข้อมูล (Bitwise operator)
'''เป็นการดำเนินการกับข้อมูลระดับบิตในรูปแบบเลขฐานสอง โดยมีสัญลักษณ์ของตัวดำเนินการระดับบิต'''
'''
&   หมายถึง  AND p & q ให้ค่าเป็น 1 เมื่อบิตใน p และ q ให้เป็น 1 ทั้งคู่ 
|     ,,    OR  p | q ให้ค่าเป็น 1 เมื่อบิตใน p หรือ q ให้เป็น 1
^     ,,    XOR p ^ q ให้ค่าเป็น 1 เมื่อบิตใน p หรือ q มีค่าต่างกัน
~     ,,    One's Complement    เปลี่ยนบิตเป็นค่าตรงค่า ~X X=2 เหมือนนำ -x -1 = 3
>>    ,,    Left Shift  เลื่อนบิตไปทางซ้ายตามค่าที่กำหนด
<<    ,,    Right Shift เลื่อนบิตไปทางขวาตามค่าที่กำหนก
'''
p=10
q=4 
print('p & q = ',p & q)     #ใช้ตัวดำเนินการ & กับตัวแปร p และ q
print('p | q = ',p | q)     #ใช้ตัวดำเนินการ | กับตัวแปร p และ q
print('p ^ q = ',p ^ q)     #ใช้ตัวดำเนินการ & กับตัวแปร p และ q
print(' ~p = ', ~p)         #ใช้ตัวดำเนินการ ~ กับตัวแปร ~p
print('p >> 1 = ',p>>1)     #ใช้ตัวดำเนินการ >> กับตัวแปร p
print('q << 2 = ',q>>2)     #ใช้ตัวดำเนินการ << กับตัวแปร q

print('5 >> 2 = ',5>>2)     #ใช้ตัวดำเนินการ >> กับเลขฐานสิบ
print('0b1010 | 0101 = ',0b1010|1010)   #ใช้ตัวดำเนินการ | เลขฐานสอง
print('0x5A & 0x3F = ',0x5a&0x3F)       #ใช้ตัวดำเนินการ & เลขฐานสิบหก

#ตัวดำเนินการการกำหนดค่า (Assignment opertator)
'''เป็นตัวดำเนินการที่ใช้กำหนดค่าให้กับตัวแปรโดยใช้เครื่องหมาย = เช่น x=+1 หมายถึง x=x+1 '''

#ตัวดำเนินการพิเศษในภาษาไพธอน
'''ที่เกี่ยวกับการตรวจสอบความเท่ากันในการใช้พื้นที่หน่วยควาามจำ(Identity opertors)ของตัวแปรหรือค่าคงที่ และตัวดำเนินการที่เกี่ยวกับการตรวจสอบสมาชิก0(Membership opera-tors) ในชนิดข้อมูลที่เป็นลักษณะลิสต์'''

#ตัวดำเนินการเอกลักษณ์ (Identity operators) 
'''เป็นตัวดำเนินการที่ใช้เปรียบเทียบ 2 ออบเจ็กต์ ได้แก่ ค่าคงที่หรือตัวแปรที่อยู่ในหน่วยความจำมีค่าเหมือนกันหรือไม่ ดังนี้ is , is not'''
num1=12-6
num2=3*2 
print(num1 is num2) #จะไปผลลัพธ์เป็น True เพราะตัวแปร num1 กับ num2 มีค่า 6 เหมือนกัน
print(13 is not num2)  #จะไปผลลัพธ์เป็น True เพราะตัวแปร num2 มีค่าไม่เท่า่ 13  เหมือนกัน

key= input('Enter a key : ')
print(key is "A") #ตรวจสอบว่าศีย์ที่กด คืออักษร "A" ใช่หรือไม่

#ตัวดำเนินการสมาชิก (Membership operator)
'''เป็นตัวดำเนินการที่ใช้ตรวจสอบค่าว่าเป็นสมาชิกในรายการของตัวแปรหรือไม่ได้แก่ ตัวแปรชนิดข้อมูล string, list, Tuple, SetและDictionary ซึ่งผลลัพธ์จะได้ออกมาเป็น True หรือ False
สามารถนำมาประยุกต์ใช้ค้นหาข้อมูลในฐานข้อมูล เพื่อแจ้งว่าพบข้อมูลหรือไม่พบข้อมูล'''
L=[1,2,3]
S='Hello'
D={1:'m',2:'a',3:'y'}
print("'e' in S =",'e' in S)#ค่า e เป็นข้อมูลอยู่ในรายการของตัวแปร S
print("2 in L =",2 in L)#ค่า 2 ไม่เป็นข้อมูลอยู่ในรายการของตัวแปร L
print("'a' not in D",'a' not in D)#ค่า a ไม่เป็นข้อมูลอยู่ในรายการของตัวแปร D (ตรวจสอบค่าผ่านศีย์)

#ลำดับความสำคัญของตัวดำเนินการ (Operators Precedence)
'''จะเริ่มจากซ้ายไปขวา แต่ถ้ามี()จะทำภายใน()ก่อน หลังจากนั้นจะเรียกลำดับความสำคัญ แต่ถ้าหากลำดับความสำคัญเท่ากันก็จะเริ่มจากซ้ายไปขวา'''
'''============================================================================================================'''
'''
ตัวดำเนินการ                    |ความสำคัญมากไปน้อย
()                                   
**                                  
~ + -                                
* / % //                              
+ -
>> <<
&
^ |
<= < > >=
== !=
= %= /= //= -= += *= **=
is is not
in not in
not or and
'''

#การใช้ การบวกsrting 
'''สามารถใช้ได้ + หรือ * โดย + จะใช้ในการบวกหรือเพิ่มคำ การใข้ * จะใช้ในการคูณเพิ่มจำนวนคำ'''
print("T"+"C") #ใช้การบวกคำ
print("c"*3) #ใช้การคูณคำ
