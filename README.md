TIM HORE - Pengolahan Citra Digital

Topik : Handwritten Signature Verification

Challenges :
- Model yang terdapat dalam paper sulit diperoleh. Karena recognition tanda tangan tidak terlalu populer. Sehingga paper rujukan pun sulit ditemukan.
- Dataset yang sulit diperoleh, karena dataset yang tersebar berupa data real / forge dan milik banyak subjek tertentu. Sehingga mesin perlu melakukan 2 job yaitu menentukan ttd milik siapa dan apakah itu real atau forged. dan menurut kami hal itu terlalu advanced. Jadi project ini berubah menjadi signature verification yaitu hanya untuk 1 subjek saja.
- Saat melakukan data acquisition secara mandiri terdapat kendala karena sulitnya mendapatkan kualitas foto yang konsisten. Sehingga kita merubah foto yang diperoleh menjadi seperti dalam bentuk scan. Sehingga saat ini mesin hanya dapat menerima bentuk foto yang konsisten dan tidak dapat ditangkap secara asal dengan kamera
- Saat melakukan konversi foto dari .HEIC ke .PNG windows tidak dapat melakukan nya dengan lib yang ada karena hanya mensupport macOS dan Linux. Sehingga dilakukan konversi melalui layanan online
#- Saat melakukan deteksi, terjadi false negative. Karena tanda tangan yang Forged kemungkinan besar akan terdeteksi sebagai forge. Tetapi ttd yang real juga sering terdeteksi sebagai forge. Hal ini karena ttd yang dilakukan oleh manusia akan sangat sulit untuk dapat konsisten. Bahkan saat dilihat dengan mata manusia pun juga terlihat berbeda meskipun dilakukan oleh pemilik ttd itu sendiri

Lessons Learned :
- Dapat menggunakan git sebagai version control dan wadah kolaborasi dalam mengerjakan suatu project
- Dapat berfikir kritis atas kendala yang dihadapi pada saat development. Misalnya kita membuat dataset ttd sendiri.
- Lebih memahami lagi apa itu preprocessing dan bagaimana perannya menjadikan seluruh foto menjadi homogen agar dapat diproses oleh machine learning
- Mempelajari kesulitan yang ada saat mengembangkan recognition tanda tangan. Misalnya jika dibandingkan foto hasil scan medis, misalnya CTScan akan sangat sulit.
- Mempelajari proses machine learning dan bagaimana tahap-tahap nya dalam split training and testing dan bagaimana suatu proses diperoleh
- Mempelajari bagaimana mengembangkan GUI dan mengintegrasikannya dengan harapan saat user mengupload foto , akan terdeteksi bahwa foto tersebut berupa Forged atau Real

Further Development : 
- menerapkan ke dalam GUI / web apps. GUI Preferable with TKInter or PyQt5
- mencoba predict dengan ttd yang dilakukan secara langsung (di luar dataset)
- Improve accuracy if possible