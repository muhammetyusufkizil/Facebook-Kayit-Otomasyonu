# Selenium kütüphanesini içe aktaralım
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Bir web sürücüsü oluşturalım
driver = webdriver.Chrome() # Bu satırı ekledik

# Facebook'un kayıt sayfasına gidelim
driver.get("https://www.facebook.com/r.php")

# Kullanıcıdan hesap bilgilerini girmesini isteyelim
isim = input("İsminizi giriniz: ") # Bu satırı ekledik
soyisim = input("Soyisminizi giriniz: ")
email = input("E-posta adresinizi giriniz: ")
sifre = input("Şifrenizi giriniz: ")
dogum_gunu = input("Doğum gününüzü giriniz (gg/aa/yyyy): ")

# Doğum gününü parçalara ayıralım
gun, ay, yil = dogum_gunu.split("/")

# İsim, soyisim, e-posta ve şifre alanlarını bulalım
isim_alani = driver.find_element(By.NAME, "firstname")
soyisim_alani = driver.find_element(By.NAME, "lastname")
email_alani = driver.find_element(By.NAME, "reg_email__")
sifre_alani = driver.find_element(By.NAME, "reg_passwd__")

# Alanlara girdiğimiz bilgileri yazalım
isim_alani.send_keys(isim)
soyisim_alani.send_keys(soyisim)
email_alani.send_keys(email)
sifre_alani.send_keys(sifre)

# İkinci mail alanını bulalım
ikinci_email_alani = driver.find_element(By.NAME, "reg_email_confirmation__")

# Aynı mail adresini yazalım
ikinci_email_alani.send_keys(email)

# Doğum günü seçeneklerini bulalım
gun_secenekleri = driver.find_element(By.ID, "day")
ay_secenekleri = driver.find_element(By.ID, "month")
yil_secenekleri = driver.find_element(By.ID, "year")

# Seçeneklerden girdiğimiz değerleri seçelim
gun_secenekleri.send_keys(gun)
ay_secenekleri.send_keys(ay)
yil_secenekleri.send_keys(yil)

# Cinsiyet seçeneğini bulalım
cinsiyet_secenegi = driver.find_element(By.XPATH, "//input[@value='2']")

# Cinsiyet seçeneğini işaretleyelim (varsayılan olarak kadın)
cinsiyet_secenegi.click()

# Kaydol butonunu bulalım
kaydol_butonu = driver.find_element(By.NAME, "websubmit")

# Kaydol butonuna tıklayalım
kaydol_butonu.click()
