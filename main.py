import random
tur=1
aletler=['taş','kağıt','makas']
KullanıcıSkor=0
BilgisayarSkor=0
while True :
 print('Tur:',tur,'----------')
 print('Oyuncunun Skoru',KullanıcıSkor)
 print('Bilgisayarın Skoru',BilgisayarSkor)
 alet=random.choice(aletler)
 kullanıcınınaleti=input()
 print('kullanıcı:', kullanıcınınaleti,'-','bilgisayar:', alet)
 if(alet==kullanıcınınaleti):
  print('berabere')
 elif(kullanıcınınaleti=='taş' and alet=='kağıt') :
  print('kaybettin')
  BilgisayarSkor=BilgisayarSkor+1
 elif(kullanıcınınaleti=='makas' and alet=='taş') :
  print('kaybettin')
  BilgisayarSkor = BilgisayarSkor + 1
 elif(kullanıcınınaleti=='kağıt' and alet=='makas') :
  print('kaybettin')
  BilgisayarSkor = BilgisayarSkor + 1
 elif(kullanıcınınaleti not in aletler):
  print('Geçersiz Girdi Lütfen Tekrar Deneyiniz')
  continue
 else:
  print('kazandın')
  KullanıcıSkor=KullanıcıSkor+1
 tur=tur+1
 if(KullanıcıSkor==3) :
  print('Oyunu kazandın')
  break
 if (BilgisayarSkor==3) :
  print('Oyunu kaybettin')
  break
