print("Ovo je moj python projekt, dobrodosli! ")

ime = input("Koje je tvoje ime? ")
print("Bok,", ime )
dob = int(input("Koliko imas godina? "))

if dob >= 15: 
   print("Super, dovoljno ste stari! ")

   zeli_igrati = input("Zelite li zaigrati igru? ")
   if zeli_igrati == "da":
       print("Zaigrajmo")

       lijevo_ili_desno = input("Prvi odabir, zelite li ici lijevo ili desno? (lijevo/desno) ")
       if lijevo_ili_desno == "desno":
           ans = input("Nalazis se pored jezera, zelite li plivati kroz njega ili ga zaobici? (plivati/zaobici) ")
           
           if ans ==  "plivati":  
              ans = input("Naisao si na sjajnu kovanicu na dnu jezera, zelis li ju pokupiti? (da/ne) ") 
              if ans == "da":
                print("Utopio si se i izgubio!")
              elif ans == "ne":
                   ans = input("Dosao si na drugu stranu, vidis poznanika, zelis li ga pozdraviti? (da/ne)"  )
                   if ans == "da":
                     ans = input("On te pozdravlja natrag... Pronasli ste kraj igre... Bravo!")
                   else:
                       print("Poznanik se naljutio jer ga nisi pozdravio i izgubio si! ")
           elif ans == "zaobici":
               ans = input("Naisao si na stand sa  limunadom, zelis li kupiti limunadu? (da/ne)  ")
               if ans == "da":
                 ans = input("Ocijeni limunadu od 1 - 10.  ")
                 print("Krivo, izgubili ste!")
               elif ans == "ne":
                   ans = input("Jos uvijek ste zedni, sto bi htijeli popiti?  ")
                   print("Krivi odabir, izgubili ste!")

       else:
           print("Izgubili ste se...")
   else:
       print("U redu, bok! ")

else:
    print("Nazalost niste dovoljno stari za igranje! ")
