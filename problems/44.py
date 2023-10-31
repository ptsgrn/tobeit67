import math
# #include<bits/stdc++.h>
# using namespace std;
# int main()
# {
#     float a ,b ,c ,d;
#     cin >> a >> b >> c >> d; // ราคา ซื้อ เเถม ต้องการ
#     float total = floor(d/(c+b));
#     total = (c+b);
#     float rem =  d - total;
#     //cout <<rem;

#     if (rem > b) {total += b+c; cout << total; return 0;}
#     else 
#     {
#         total = total (c+b) ;
#         total += (d - total);
#         cout <<  total;
#         return 0;
#     }
#     // 5 2 4 10
#     // 12 12*5
# }

a, b, c, d = [int(input()) for _ in range(4)]

total = math.floor(d / (c + b))
total = (c + b)
rem = d - total

if rem > b:
  total += b + c
  print(total)
else:
  total = total * (c + b)
  total += (d - total)
  print(total)