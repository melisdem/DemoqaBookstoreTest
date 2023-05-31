# Demoqa Bookstore Tests
## Açıklamalar

<p>Projede testler için <strong>pytest</strong> kullandım.</p>
<p>ilk önce hızlı olması sebebiyle <em><strong>seleniumIDE</strong></em> eklentisini kullanarak otomatize bir test oluşturdum.
Her iki case için de kodlarımı <strong>seleniumIDE_Tests</strong> dosyasında bulabilirsiniz.

<p>Daha sonra POM'a uygun olarak kendi kodlarımı yazdım. Bu kodlarımı da <strong>seleniumTest</strong> dosyası içinde bulabilirsiniz.
Burada iki case'i de tek bir dosyada ve bir class'ta tanımladım.
</p>

<p>Opsiyonel olarak verdiğiniz API kullanarak otomatize test oluşturma case'inin kodlarını da <strong>pytestsWithAPI</strong> dosyasında bulabilirsiniz.</p>

<p>Son olarak <em><strong>allure reports</strong></em> kullanarak oluşturduğum raporları <strong>Bookstore</strong> klasöründe terminal açarak <code> allure serve allure_reports/</code> command'iyle çalıştırıp, browserda oluşan raporu inceleyebilirsiniz.</p>