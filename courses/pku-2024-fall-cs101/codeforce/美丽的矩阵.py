a11,a12,a13,a14,a15=input().split()
a21,a22,a23,a24,a25=input().split()
a31,a32,a33,a34,a35=input().split()
a41,a42,a43,a44,a45=input().split()
a51,a52,a53,a54,a55=input().split()
if a33=='1':
    print(0)
if a23=='1' or a32=='1' or a43=='1' or a34=='1':
    print(1)
if a31=='1' or a53=='1' or a35=='1' or a13=='1' or a22=='1' or a42=='1' or a44=='1' or a24=='1':
    print(2)
if a12=='1' or a21=='1' or a41=='1' or a52=='1' or a54=='1' or a45=='1' or a25=='1' or a14=='1':
    print(3)
if a11=='1' or a51=='1' or a15=='1' or a55=='1':
    print(4)