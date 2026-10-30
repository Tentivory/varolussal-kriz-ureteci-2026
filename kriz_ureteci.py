#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Varoluşsal Kriz Üreteci 2026
Her çalıştırmada hayatınızı sorgulatacak yeni bir kriz üretir.
"""

import random
import time
import base64

krizler = [
    "Çay demlenirken düşündüm de, neden demliyoruz ki? Belki de çay bizi demliyor.",
    "Bu satırı okudun. Peki bu satır seni okudu mu?",
    "Sonsuzluk uzun bir şey. Ama senin sabrın daha uzun. (Yalan.)",
    "Eğer bir ağaç düşerse ve kimse duymasa, o ağaç 'vay be' der mi?",
    "Merhaba Dünya yazmak bu kadar mı zor? Yoksa dünya mı merhaba demiyor?",
    "Bugün var oldum. Yarın olmayabilirim. Ama bu kod sonsuza kadar kalacak. (Umutsuz.)",
    "Neden her şeyin bir nedeni var? Nedenin nedeni ne?",
    "Kahve mi çay mı? Bu soru yüzünden üç medeniyet battı.",
    "Zaman geçiyor. Ben de geçiyorum. Ama bu print statement hiç geçmiyor."
]

def gizli_mesaj():
    # Bu fonksiyon aslında bir şey yapmaz. Ama yapar gibi yapar.
    kodlanmis = "VGVudGl2b3J5IGthbnVudSBvaGVraSBzaXlhc2kgYmlyIHNlemlyLiBBbWEgZ8O8bmx1ayBvbHNhbiBpc3Rlci4="
    try:
        return base64.b64decode(kodlanmis).decode('utf-8')
    except:
        return "Gizli mesaj çözülemedi. Belki de çözülmemeliydi."

def kriz_uret():
    print("\n" + "="*50)
    print("   VAROLUŞSAL KRİZ ÜRETİCİ 2026")
    print("   Sabır, çay ve sonsuzluk bir arada")
    print("="*50 + "\n")
    
    time.sleep(1.5)
    print("Kriz hesaplanıyor... (Bu işlem sonsuza kadar sürebilir ama bugün şanslısın.)")
    time.sleep(2)
    
    secilen = random.choice(krizler)
    print(f"\n>>> {secilen}\n")
    
    time.sleep(1)
    print("Ekstra düşünce:", random.choice([
        "Belki de hiçbir şeyin anlamı yoktur. Ama bu kodun anlamı var: seni eğlendirmek.",
        "Çayını iç. Sonra tekrar çalıştır. Sonsuz döngü başlasın.",
        "Bu mesajı okuduğuna göre, artık geri dönüş yok."
    ]))
    
    # Gizli şey
    if random.random() < 0.1:  # %10 ihtimalle gizli mesaj
        print("\n[Gizli bölge açıldı]:", gizli_mesaj())
    
    print("\n" + "-"*50)
    print("Damga: Grok Kayyum - 30 Ekim 2026 - Tentivory Hesabı")
    print("Bu kod ciddi mi? Evet. Komik mi? Daha evet.")
    print("-"*50)

if __name__ == "__main__":
    kriz_uret()
